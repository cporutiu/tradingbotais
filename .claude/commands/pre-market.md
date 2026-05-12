---
description: Run the pre-market research workflow locally using .env credentials
---

Run the pre-market research workflow. Uses local .env for credentials.

DATE=$(date +%Y-%m-%d)

STEP 1 — Read memory for context:
- memory/TRADING-STRATEGY.md
- tail of memory/TRADE-LOG.md
- tail of memory/RESEARCH-LOG.md

STEP 1B — Check for pending user decisions:
- Scan the tail of memory/TRADE-LOG.md for any "User decisions" block
  (lines starting with "**User decisions**") in the most recent EOD entry.
- For each decision found, treat it as a confirmed instruction and carry it
  forward into today's plan (entry timing, stop tightening, etc.).
- If a decision references a specific trigger that hasn't fired yet
  (e.g. "tighten NVDA at $230.62"), note it as an active watch item in
  STEP 4's RESEARCH-LOG entry.

STEP 2 — Pull live account state:
  bash scripts/alpaca.sh account
  bash scripts/alpaca.sh positions
  bash scripts/alpaca.sh orders

STEP 3 — Research market context via Perplexity. Run
bash scripts/perplexity.sh "<query>" for each:
- "WTI and Brent oil price right now"
- "S&P 500 futures premarket today"
- "VIX level today"
- "Top stock market catalysts today $DATE"
- "Earnings reports today before market open"
- "Economic calendar today CPI PPI FOMC jobs data"
- "S&P 500 sector momentum YTD"
- News on any currently-held ticker

If Perplexity exits 3, fall back to native WebSearch and note the fallback.

STEP 4 — Write a dated entry to memory/RESEARCH-LOG.md:
- Account snapshot (equity, cash, buying power, daytrade count)
- Market context (oil, indices, VIX, today's releases)
- 2-3 actionable trade ideas WITH catalyst + entry/stop/target
- Risk factors for the day
- Decision: trade or HOLD (default HOLD — patience > activity)

STEP 5 — Notification: silent unless urgent.
