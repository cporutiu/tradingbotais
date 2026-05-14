#!/usr/bin/env python3
"""
Fetch Benzinga email alerts from Outlook 365 via Microsoft Graph API.
Outputs .tmp/benzinga_signals_{date}.json with BUY/SELL/HOLD per ticker.
Uses OUTLOOK_* env vars (loaded by run_routine.ps1 from .env before this runs).
"""
import os, json, re, sys, msal, requests
from datetime import datetime, timedelta

OUTLOOK_CLIENT_ID     = os.environ.get("OUTLOOK_CLIENT_ID", "")
OUTLOOK_CLIENT_SECRET = os.environ.get("OUTLOOK_CLIENT_SECRET", "")
OUTLOOK_TENANT_ID     = os.environ.get("OUTLOOK_TENANT_ID", "")
OUTLOOK_USER_EMAIL    = os.environ.get("OUTLOOK_USER_EMAIL", "")
OUTLOOK_FOLDER_NAME   = os.environ.get("OUTLOOK_FOLDER_NAME", "Benzinga")
_GRAPH_BASE           = "https://graph.microsoft.com/v1.0"

UNIVERSE = [
    # Broad market / sector ETFs
    "SPY","QQQ","GLD","SLV","XLE","XLF","XLK","XLV","XLU",
    "XLI","XLB","XLP","XLY","XLC","XLRE","IWM","HYG","EEM","SOXX",
    # Active positions
    "NVDA","CAT",
    # Watchlist candidates
    "XOM","FCX","CVX",
    # AI/chip research refs
    "AMD","AVGO",
]
_default_hours = "72" if datetime.now().weekday() == 0 else "24"  # Mon=72h (covers weekend), Tue-Fri=24h
LOOKBACK_HOURS = int(os.environ.get("NEWS_LOOKBACK_HOURS", _default_hours))

_BULLISH = [
    "upgrade","outperform","strong buy","overweight","breakout","beats","beat",
    "rally","rallies","surges","surge","inflow","inflows","bullish","rises",
    "gains","record high","exceeds","positive","buy","upside","raised",
    "raise price target","strong demand",
]
_BEARISH = [
    "downgrade","underperform","underweight","breakdown","misses","miss",
    "drops","drop","falls","fall","outflow","outflows","bearish","decline",
    "warning","cuts","lowers","below expectations","sell","downside","lowered",
    "lower price target","weak demand","recession","downturn",
]
_CONTEXT_WINDOW = 400


def _get_graph_token():
    if not all([OUTLOOK_CLIENT_ID, OUTLOOK_CLIENT_SECRET, OUTLOOK_TENANT_ID]):
        raise ValueError("OUTLOOK_CLIENT_ID / OUTLOOK_CLIENT_SECRET / OUTLOOK_TENANT_ID not set")
    app = msal.ConfidentialClientApplication(
        OUTLOOK_CLIENT_ID,
        authority=f"https://login.microsoftonline.com/{OUTLOOK_TENANT_ID}",
        client_credential=OUTLOOK_CLIENT_SECRET,
    )
    result = app.acquire_token_for_client(scopes=["https://graph.microsoft.com/.default"])
    if "access_token" not in result:
        raise RuntimeError(f"MSAL token error: {result.get('error_description', result)}")
    return result["access_token"]


def _get_folder_id(token, folder_name):
    r = requests.get(
        f"{_GRAPH_BASE}/users/{OUTLOOK_USER_EMAIL}/mailFolders",
        headers={"Authorization": f"Bearer {token}"},
        params={"$top": 50},
        timeout=15,
    )
    r.raise_for_status()
    for folder in r.json().get("value", []):
        if folder["displayName"].lower() == folder_name.lower():
            return folder["id"]
    return None


_BENZINGA_SENDERS = [
    "alerts@benzinga.com",
    "hello@investor.benzinga.com",
]


def _fetch_one_sender(token, endpoint, sender, cutoff):
    headers = {"Authorization": f"Bearer {token}"}
    url     = f"{_GRAPH_BASE}/users/{OUTLOOK_USER_EMAIL}/{endpoint}"
    params  = {
        "$filter": f"from/emailAddress/address eq '{sender}' and receivedDateTime ge {cutoff}",
        "$select": "subject,body,receivedDateTime",
        "$top": 500,
    }
    emails = []
    while url:
        r = requests.get(url, headers=headers, params=params, timeout=30)
        r.raise_for_status()
        data = r.json()
        for msg in data.get("value", []):
            subject  = msg.get("subject", "")
            body_obj = msg.get("body", {})
            raw_body = body_obj.get("content", "")
            if body_obj.get("contentType", "").lower() == "html":
                raw_body = re.sub(r"<[^>]+>", " ", raw_body)
            emails.append({"subject": subject, "body": raw_body})
        url    = data.get("@odata.nextLink")
        params = None  # nextLink already includes all params
    return emails


def _fetch_emails(token):
    cutoff    = (datetime.now() - timedelta(hours=LOOKBACK_HOURS)).strftime("%Y-%m-%dT%H:%M:%SZ")
    folder_id = _get_folder_id(token, OUTLOOK_FOLDER_NAME)
    endpoint  = f"mailFolders/{folder_id}/messages" if folder_id else "messages"

    emails = []
    for sender in _BENZINGA_SENDERS:
        try:
            batch = _fetch_one_sender(token, endpoint, sender, cutoff)
            emails.extend(batch)
        except Exception as e:
            print(f"[benzinga] Fetch failed for {sender}: {e}", file=sys.stderr)
    return emails


def _score_text(text):
    lower = text.lower()
    return sum(lower.count(kw) for kw in _BULLISH) - sum(lower.count(kw) for kw in _BEARISH)


def _extract_signals(emails):
    tickers_sorted = sorted(UNIVERSE, key=len, reverse=True)
    pattern = re.compile(
        r"(?<![A-Z\$])(\b(?:" + "|".join(re.escape(t) for t in tickers_sorted) + r")\b)(?![A-Z])"
    )

    scores   = {t: [] for t in UNIVERSE}
    snippets = {t: [] for t in UNIVERSE}

    for email in emails:
        text = email["subject"] + " " + email["body"]
        for match in pattern.finditer(text):
            ticker = match.group(1)
            if ticker not in UNIVERSE:
                continue
            start = max(0, match.start() - _CONTEXT_WINDOW)
            end   = min(len(text), match.end() + _CONTEXT_WINDOW)
            scores[ticker].append(_score_text(text[start:end]))
            if email["subject"] and ticker in (email["subject"] + " "):
                snippets[ticker].append(email["subject"][:120])

    result = {}
    for ticker in UNIVERSE:
        s = scores[ticker]
        if not s:
            result[ticker] = {"action": "HOLD", "confidence": None, "reason": "no_mention"}
            continue
        total    = sum(s)
        mentions = len(s)
        if total == 0:
            result[ticker] = {"action": "HOLD", "confidence": "low", "reason": "neutral_score"}
            continue
        action = "BUY" if total > 0 else "SELL"
        if abs(total) >= 3 and mentions >= 2:
            confidence = "high"
        elif abs(total) >= 2:
            confidence = "medium"
        else:
            confidence = "low"
        summary = snippets[ticker][0] if snippets[ticker] else f"{ticker} {mentions}x score={total:+d}"
        result[ticker] = {
            "action": action, "confidence": confidence,
            "source": "benzinga_outlook", "summary": summary,
            "score": total, "mentions": mentions,
        }
    return result


def main():
    today    = datetime.now().strftime("%Y-%m-%d")
    out_path = os.path.join(".tmp", f"benzinga_signals_{today}.json")
    os.makedirs(".tmp", exist_ok=True)

    if os.path.exists(out_path):
        with open(out_path) as f:
            cached = json.load(f)
        active = sum(1 for v in cached.values() if v.get("action") != "HOLD")
        print(f"[benzinga] CACHED — {active} active signals")
        print(json.dumps(cached, indent=2))
        return

    try:
        token  = _get_graph_token()
        emails = _fetch_emails(token)
        print(f"[benzinga] {len(emails)} emails found in last {LOOKBACK_HOURS}h", file=sys.stderr)
    except Exception as e:
        print(f"[benzinga] ERROR: {e} — all HOLD", file=sys.stderr)
        result = {t: {"action": "HOLD", "confidence": None, "reason": "graph_error"} for t in UNIVERSE}
        print(json.dumps(result, indent=2))
        return

    if not emails:
        print("[benzinga] No emails found — all HOLD", file=sys.stderr)
        result = {t: {"action": "HOLD", "confidence": None, "reason": "no_emails"} for t in UNIVERSE}
        print(json.dumps(result, indent=2))
        return

    raw    = _extract_signals(emails)
    result = {}
    for t in UNIVERSE:
        entry = raw.get(t, {"action": "HOLD", "confidence": None, "reason": "no_mention"})
        if entry.get("confidence") == "low":
            result[t] = {"action": "HOLD", "confidence": "low", "reason": "low_confidence"}
        else:
            result[t] = entry

    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)

    buys  = sum(1 for v in result.values() if v["action"] == "BUY")
    sells = sum(1 for v in result.values() if v["action"] == "SELL")
    print(f"[benzinga] BUY={buys} SELL={sells} HOLD={len(result)-buys-sells} -> {out_path}", file=sys.stderr)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
