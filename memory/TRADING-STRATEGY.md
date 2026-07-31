# Trading Strategy

## Mission
Beat the S&P 500 over the challenge window. Stocks only — no options, ever.

## Capital & Constraints
- Starting capital: $100,000
- Platform: Alpaca
- Instruments: Stocks ONLY
- PDT limit: 3 day trades per 5 rolling days (account < $25k)

## Core Rules
1. NO OPTIONS — ever
2. 75-85% deployed — enforced by deployment floor (see below)
3. 5-6 positions at a time; target **17-20% per position** (minimum 17%, not 15%)
4. 10% trailing stop on every position as a real GTC order
5. Cut losers at -7% manually
6. Tighten trail: 7% at +15%, 5% at +20%
7. Never within 3% of current price; never move a stop down
8. Max 3 new trades per week
9. Follow sector momentum; use ranked watchlist (see below)
10. Exit a sector after 2 consecutive failed trades
11. Patience > activity — **valid only when deployed ≥60% OR a named Tier-1 blocker exists**
12. **Time-based exit:** If any position is below entry after 2 full weeks held with no thesis catalyst restoring momentum, exit manually regardless of stop. Prevents slow-bleed positions from occupying slots indefinitely.
13. **3-day weekend thesis check:** Never carry a thesis-deteriorating position into a 3-day market holiday. If a position is on active thesis-break watch (commodity price below manual trigger, ISM contraction signal, confirmed sector rotation away from thesis) by Thursday close before a 3-day weekend, exit Friday. Do not wait for stop proximity to decide.
14. **Unanswered action question default:** If an EOD action question has no user response by the following morning's pre-market run, the bot acts autonomously using the best available pre-market data. Do not carry a question a second day. Log the autonomous decision in TRADE-LOG.md as "Bot autonomous decision (YYYY-MM-DD): [question] → [action] — [1-line rationale]" and execute at market open.
15. **Reconnect protocol:** If a routine resumes after a connectivity/infra gap of more than 3 calendar days (e.g. blocked API egress), the first run back must, before taking any new-entry action: (a) pull live positions/orders directly from Alpaca to reconcile against the last logged state — do not trust the stale log; (b) for every position still open, check current price against every threshold that should have applied during the gap (tighten triggers at +15%/+20%, -7% manual cut, thesis-break levels) and act immediately if one was missed, rather than waiting for the next natural check. Added 2026-07-10 after a 3-week outage (Jun 20–Jul 8) caused CAT's +15% tighten trigger to be hit and exceeded with no tighten ever placed (~$640 cost).

## Deployment Floor — Enforced

Default is **TRADE** when all of the following are true:
- Deployed capital < 40%, AND
- No Tier-1 blocker within 24h

**Blocker tiers:**
- **Tier-1 (full blackout — no new entries):** FOMC decision day, CPI release day, NFP release day, GDP Advance release day, held-name earnings day BMO/AMC
- **Tier-2 (watchful — new entries allowed on strong setups):** PPI, retail sales, ISM Manufacturing/Services, JOLTS, consumer confidence, Fed speaker events
- **Not a blocker:** "General uncertainty," "earnings next week," "oil could reverse," any event >48h away

"General uncertainty," "market looks heavy," and "could pull back" are NEVER blockers.

**Wednesday urgency check:** If ≥2 trade slots unused at Wednesday close AND deployed < 60%, open at least 1 position Thursday — Tier-1 blocker caveat only.

**Deployment urgency protocol (2+ weeks under-deployed):** If deployed has been below 75% for 2 or more consecutive weekly closes:
- R:R minimum drops from 2:1 to 1.5:1 for new entries
- Tier-2 blockers do NOT apply (Tier-1 still blocks)
- Wednesday urgency check triggers at deployed < 70% instead of < 60%
- Document "urgency protocol active" in each RESEARCH-LOG entry until resolved

## Sector Diversification Rules
- Max 2 positions in any single sector — **single stocks only count toward this cap**
- **ETF exception:** Passive broad-market or sector ETFs (e.g. XLK, XLE, IWM, SOXX, GLD) do NOT count toward the 2-position sector cap. A single stock + a sector ETF in the same sector = 1 of 2 slots used, not 2. Two single stocks in the same sector = 2 of 2 slots.
- When ≥3 positions open, must span ≥2 sectors
- Each weekly review assigns a ranked sector watchlist + 1 candidate ticker per sector for the upcoming week; Monday pre-market must arrive with 2-3 live setups, not 1 idea and vague "watch X"

## Sector Watchlist (update each Friday in WEEKLY-REVIEW.md)
See WEEKLY-REVIEW.md for the current week's live-researched watchlist (refreshed every Friday). As of Week 15 (Aug 3-7):
| Priority | Sector | ETF | Candidate | Condition to Enter |
|----------|--------|-----|-----------|-------------------|
| 1 | Technology | — | NVDA (re-entry) | AMD+NVDA both stopped out Jul 27/28 on sector rotation — Rule 10 (2 consecutive failed trades) question unresolved; do not enter until explicitly resolved (see WEEKLY-REVIEW.md Next-week Decisions) |
| 2 | Industrials | XLI | XLI | Macro-supported (ISM Manufacturing 54.0), technically strong; needs entry/stop/target computed before entry |
| 3 | Energy | XLE | XOM (held) | Hold to stop $145.2288; largest single position (~20% equity), no add |
| 4 | Materials/Macro | GLD/XLB | GLD | FCX permanently abandoned (5+ R:R failures) — do not re-add; GLD has no computable price target for 5th consecutive week, R:R exception still unresolved |

## Entry Checklist
- Specific catalyst?
- Sector in momentum AND on ranked watchlist?
- Deployment check: deployed < 40% with no Tier-1 blocker? → TRADE default. Urgency protocol active? → R:R floor = 1.5:1
- Position sizing: 17-20% of current equity
- Stop level: 10% trailing GTC, placed immediately on fill
- Target: min 2:1 R:R (1.5:1 if urgency protocol active)
- Sector cap: ETFs don't count toward cap. Single stocks: ≤2 per sector.
- **Macro alignment pre-check (rate-sensitive names only):** Before entering any name whose thesis depends on rate cuts (small-cap, homebuilders, REITs, high-duration growth): verify last CPI core ≤3.0% AND last NFP ≤150K. If either fails, defer entry until next data cycle.
- **Candidate freshness:** If the same candidate has failed the R:R check for 2 consecutive weeks on the same underlying problem (spread, PT misalignment), abandon it and pivot to the next alternative. Do not retry until market structure visibly changes (spread tightens by >50%, or analyst PT updates meaningfully).

## Post-Catalyst Gap-Up Protocol
When a company reports a major earnings beat (EPS or revenue significantly above consensus, positive forward guidance) after market close or before market open:
- **Entry:** Buy at market open the following morning — do NOT wait for a pullback
- **Sizing:** Full position 17-20% of equity, same as any entry
- **Stop:** 10% trailing GTC placed immediately on fill
- **Do not overthink it:** Gap-up momentum on a genuine beat is statistically front-loaded to the open session. Waiting for a "better price" typically means missing the move
- **Valid catalyst examples:** Major EPS beat >10%, revenue beat with raised guidance, announced partnership or acquisition with clear accretive thesis
- **Invalid:** Gap-up on vague optimism, analyst upgrade only, short-squeeze without fundamental backing
