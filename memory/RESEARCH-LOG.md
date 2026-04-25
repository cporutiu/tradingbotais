# Research Log

Daily pre-market research entries will be appended here.
Format each entry:

## YYYY-MM-DD — Pre-market Research

### Account
- Equity: $X
- Cash: $X
- Buying power: $X
- Daytrade count: N

### Market Context
- WTI / Brent:
- S&P 500 futures:
- VIX:
- Today's catalysts:
- Earnings before open:
- Economic calendar:
- Sector momentum:

### Trade Ideas
1. TICKER — catalyst, entry $X, stop $X, target $X, R:R X:1
2. ...

### Risk Factors
- ...

### Decision
TRADE or HOLD (default HOLD if no edge)

---

## 2026-04-25 — Pre-market Research

> Note: April 25 is Saturday. Markets open Monday April 27. This entry prepares for Monday open.
> Alpaca API unreachable from sandbox (host not in egress allowlist) — account snapshot from trade log baseline.
> Perplexity API blocked — all market data via WebSearch (fallback noted).

### Account
- Equity: ~$100,000 (Day 0 baseline, no live API confirmation)
- Cash: ~$100,000 (100% cash, no positions)
- Buying power: ~$100,000
- Daytrade count: 0
- Status: Launch week — need to deploy 75-85% across 5-6 positions per strategy

### Market Context
- WTI: $94.40/bbl (weekly +13%; oil surging on geopolitical risk)
- Brent: $105.33/bbl (weekly +16%; U.S.-Iran talks restart, Strait of Hormuz concerns)
- S&P 500 futures: ~7,196 (range 7,135–7,200; signal: Strong Buy on technicals)
- VIX: 18.71 (April 24 close, down 3.1%; fear subsiding but event risk ahead)
- Earnings before open Monday: Nucor (NUE), Verizon (VZ), Universal Health Services (UHS), AvalonBay (AVB)
- Key week ahead:
  - Wed Apr 29: FOMC rate decision + MSFT/AMZN/GOOGL/META earnings after close
  - Thu Apr 30: Q1 GDP (first estimate), March PCE/core PCE, AAPL/LLY earnings, ECB decision
  - Fri May 1: European/Asian markets closed (Labor Day) — thin liquidity
- INTC: Massive Q1 beat Thursday after close — EPS 29¢ vs 1¢ est, Rev $13.58B vs $12.42B est; +24% Friday; stock +105% YTD; data center/AI rev $5.1B (+22%)
- Sector momentum YTD:
  - Leading: Materials +22%, Energy strong, Industrials/Healthcare outperforming
  - Cooling: Technology (AI run, now consolidating), Consumer Discretionary
  - Improving: Real Estate, Utilities (flight-to-safety bid)
  - Tech sector up 11% this month despite rotation

### Trade Ideas
1. **FCX** (Freeport-McMoRan) — Materials #1 YTD sector (+22%), copper benefits from AI data center buildout + infrastructure; entry ~$45.00, stop $40.50 (-10%), target $55.00 (+22%), R:R ~2.2:1. Wait for Monday open confirmation above Friday close.
2. **XOM** (ExxonMobil) — Energy sector momentum, Brent $105 with geopolitical premium intact, Iran talks could resolve OR escalate; entry ~$112.00, stop $101.00 (-9.8%), target $135.00 (+20.5%), R:R ~2.1:1. Catalyst: sustained Brent >$100 + OPEC+ discipline.
3. **NVDA** — AI capex cycle accelerating; hyperscaler 2026-2030 capex estimates up 25%+ since Oct; MSFT/AMZN/GOOGL/META all report Wed — wait for guidance confirmation before entry; entry ~$780 post-earnings clarity, stop $703 (-9.9%), target $940 (+20.5%), R:R ~2:1. DO NOT enter before FOMC/earnings.

### Risk Factors
- FOMC Wednesday — any hawkish surprise on rates or inflation triggers broad sell-off
- Q1 GDP + PCE Thursday — stagflation signal (weak GDP + hot PCE) is worst-case for risk assets
- Oil at $105 Brent — if Iran talks collapse, spike to $115+ would hit consumer/transport sectors
- Mega-cap tech (MSFT/AMZN/GOOGL/META/AAPL) all report this week — wrong-way earnings = sector collapse
- Market at highs (SPX ~7,196) entering a historically risky week — limited cushion
- VIX at 18.71 could spike sharply if FOMC or GDP disappoints
- Thin Friday liquidity (May 1 = European/Asian Labor Day)

### Decision
**HOLD** — Do NOT deploy capital Monday/Tuesday. Too much binary event risk (FOMC Wed + mega-tech Wed/Thu + GDP/PCE Thu). Wait for Thursday morning after FOMC decision, Powell presser, and MSFT/AMZN/GOOGL/META results are absorbed. If macro + earnings favorable, initiate 2-3 positions Thursday open (FCX, XOM, NVDA candidates). Max 3 new trades this week per strategy rules.
