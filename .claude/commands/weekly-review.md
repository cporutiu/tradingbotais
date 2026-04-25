---
description: Run the Friday weekly review workflow locally using .env credentials
---

Run the weekly review workflow. Uses local .env for credentials.

DATE=$(date +%Y-%m-%d)

STEP 1 — Read memory for full week context:
- memory/WEEKLY-REVIEW.md (match existing template exactly)
- ALL this week's entries in memory/TRADE-LOG.md
- ALL this week's entries in memory/RESEARCH-LOG.md
- memory/TRADING-STRATEGY.md

STEP 2 — Pull week-end state:
  bash scripts/alpaca.sh account
  bash scripts/alpaca.sh positions

STEP 3 — Compute the week's metrics:
- Starting portfolio (Monday AM equity)
- Ending portfolio (today's equity)
- Week return ($ and %)
- S&P 500 week return via Perplexity
- Trades taken (W/L/open), win rate, best/worst trade, profit factor

STEP 4 — Append full review section to memory/WEEKLY-REVIEW.md (matching template).

STEP 5 — If a rule needs to change, update memory/TRADING-STRATEGY.md too.

STEP 6 — Send ONE ClickUp message with headline numbers.
