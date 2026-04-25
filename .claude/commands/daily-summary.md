---
description: Run the daily summary workflow locally using .env credentials
---

Run the daily summary workflow. Uses local .env for credentials.

DATE=$(date +%Y-%m-%d)

STEP 1 — Read memory for continuity:
- tail of memory/TRADE-LOG.md (most recent EOD snapshot -> yesterday's equity)
- Count TRADE-LOG entries dated today
- Count trades Mon-today this week

STEP 2 — Pull final state of the day:
  bash scripts/alpaca.sh account
  bash scripts/alpaca.sh positions
  bash scripts/alpaca.sh orders

STEP 3 — Compute metrics:
- Day P&L ($ and %) = today_equity - yesterday_equity
- Phase cumulative P&L = today_equity - starting_equity
- Trades today (list or "none")
- Trades this week (running total)

STEP 4 — Append EOD snapshot to memory/TRADE-LOG.md (matching existing format).

STEP 5 — Send ONE ClickUp message (always, even on no-trade days, <= 15 lines):
  bash scripts/clickup.sh "EOD MMM DD ..."
