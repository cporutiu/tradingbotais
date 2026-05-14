#!/usr/bin/env python3
"""
Fetch congressional stock trading signals from Quiver Quantitative
(STOCK Act / Periodic Transaction Report disclosures — no API key required).
Outputs .tmp/congress_signals_{date}.json with BUY/SELL/HOLD per ticker.

Strategy: track ALL Congress members for trades in the bot's UNIVERSE tickers.
Trades by the 10 named "priority" politicians (committee overlap, high frequency)
are flagged separately and raise confidence.
"""
import os, json, sys, requests
from datetime import datetime, timedelta

_API_URL      = "https://api.quiverquant.com/beta/live/congresstrading"
LOOKBACK_DAYS = int(os.environ.get("CONGRESS_LOOKBACK_DAYS", "45"))

# Priority politicians — committee assignments overlap with bot's sector watchlist.
# Their trades are flagged and raise signal confidence.
# See memory/RESEARCH-LOG.md 2026-05-12 for full selection rationale.
PRIORITY_FRAGMENTS = {
    "Gottheimer", "Pelosi", "Crenshaw", "Tuberville",
    "Hoeven", "DelBene", "Khanna", "McMorris", "McCaul",
}
# Disambiguate "Mark Kelly" from other Kellys in the dataset
_MARK_KELLY = "Mark Kelly"

UNIVERSE = [
    # Broad market / sector ETFs
    "SPY", "QQQ", "GLD", "SLV", "XLE", "XLF", "XLK", "XLV", "XLU",
    "XLI", "XLB", "XLP", "XLY", "XLC", "XLRE", "IWM", "HYG", "EEM", "SOXX",
    # Active positions
    "NVDA", "CAT",
    # Watchlist candidates
    "XOM", "FCX", "CVX",
    # AI/chip research refs
    "AMD", "AVGO",
]

_BUY_LABELS  = {"purchase", "exchange"}
_SELL_LABELS = {"sale", "sale (partial)", "sale (full)"}


def _is_priority(name: str) -> bool:
    name_lower = name.lower()
    if "mark kelly" in name_lower:
        return True
    return any(f.lower() in name_lower for f in PRIORITY_FRAGMENTS)


def _fetch_trades() -> list:
    r = requests.get(
        _API_URL,
        headers={"Accept": "application/json", "User-Agent": "TradingBotAIS/1.0"},
        timeout=30,
    )
    r.raise_for_status()
    return r.json()


def _aggregate_signals(trades: list, cutoff: datetime) -> dict:
    ticker_data = {t: {"buys": [], "sells": []} for t in UNIVERSE}

    for record in trades:
        ticker      = str(record.get("Ticker", "")).upper().strip()
        rep         = str(record.get("Representative", "")).strip()
        transaction = str(record.get("Transaction", "")).strip().lower()
        report_date_str = str(record.get("ReportDate", ""))
        tx_date_str     = str(record.get("TransactionDate", ""))
        amount          = str(record.get("Range", "")).strip()

        if ticker not in UNIVERSE:
            continue

        try:
            report_date = datetime.strptime(report_date_str, "%Y-%m-%d")
        except ValueError:
            continue
        if report_date < cutoff:
            continue

        priority = _is_priority(rep)
        label = (
            f"{'[PRIORITY] ' if priority else ''}"
            f"{rep} {transaction.upper()} {tx_date_str} "
            f"filed {report_date_str} {amount}"
        )

        tx_key = transaction.split("(")[0].strip()
        entry = {"politician": rep, "label": label, "priority": priority}

        if tx_key in _BUY_LABELS:
            ticker_data[ticker]["buys"].append(entry)
        elif tx_key in _SELL_LABELS or "sale" in tx_key:
            ticker_data[ticker]["sells"].append(entry)

    result = {}
    for ticker in UNIVERSE:
        buys  = ticker_data[ticker]["buys"]
        sells = ticker_data[ticker]["sells"]
        net   = len(buys) - len(sells)
        total = len(buys) + len(sells)

        if total == 0:
            result[ticker] = {"action": "HOLD", "confidence": None, "reason": "no_activity"}
            continue

        if net > 0:
            action = "BUY"
        elif net < 0:
            action = "SELL"
        else:
            action = "HOLD"

        priority_count = sum(1 for e in (buys + sells) if e["priority"])

        # Confidence: boosted when priority politicians are involved
        if total >= 3 and abs(net) >= 2:
            confidence = "high"
        elif total >= 2 or abs(net) >= 1:
            confidence = "medium"
        else:
            confidence = "low"

        if priority_count >= 1 and confidence == "medium":
            confidence = "high"

        politicians = sorted({e["politician"] for e in (buys + sells)})
        summaries   = [e["label"] for e in (buys + sells)[:4]]

        result[ticker] = {
            "action":         action,
            "confidence":     confidence,
            "source":         "quiverquant_stockact",
            "politicians":    politicians,
            "priority_count": priority_count,
            "summary":        "; ".join(summaries),
            "buy_count":      len(buys),
            "sell_count":     len(sells),
        }

    return result


def main():
    today    = datetime.now().strftime("%Y-%m-%d")
    cutoff   = datetime.now() - timedelta(days=LOOKBACK_DAYS)
    out_path = os.path.join(".tmp", f"congress_signals_{today}.json")
    os.makedirs(".tmp", exist_ok=True)

    if os.path.exists(out_path):
        with open(out_path) as f:
            cached = json.load(f)
        active = sum(1 for v in cached.values() if v.get("action") != "HOLD")
        print(f"[congress] CACHED — {active} active signals", file=sys.stderr)
        print(json.dumps(cached, indent=2))
        return

    print(
        f"[congress] Fetching STOCK Act disclosures from Quiver Quant "
        f"(lookback {LOOKBACK_DAYS}d since {cutoff.strftime('%Y-%m-%d')})...",
        file=sys.stderr,
    )

    try:
        raw_trades = _fetch_trades()
        print(f"[congress] {len(raw_trades)} total records received", file=sys.stderr)
    except Exception as e:
        print(f"[congress] ERROR fetching data: {e} — all HOLD", file=sys.stderr)
        result = {t: {"action": "HOLD", "confidence": None, "reason": "fetch_error"} for t in UNIVERSE}
        print(json.dumps(result, indent=2))
        return

    result = _aggregate_signals(raw_trades, cutoff)

    # Suppress low-confidence signals (same policy as fetch_benzinga.py)
    for ticker in UNIVERSE:
        if result[ticker].get("confidence") == "low":
            result[ticker] = {"action": "HOLD", "confidence": "low", "reason": "low_confidence"}

    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)

    buys  = sum(1 for v in result.values() if v["action"] == "BUY")
    sells = sum(1 for v in result.values() if v["action"] == "SELL")
    print(
        f"[congress] BUY={buys} SELL={sells} HOLD={len(result)-buys-sells} -> {out_path}",
        file=sys.stderr,
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
