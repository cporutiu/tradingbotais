# Weekly Review

Friday reviews appended here.
Template for each entry:

## Week ending YYYY-MM-DD

### Stats
| Metric | Value |
|--------|-------|
| Starting portfolio | $X |
| Ending portfolio | $X |
| Week return | ±$X (±X%) |
| S&P 500 week | ±X% |
| Bot vs S&P | ±X% |
| Trades | N (W:X / L:Y / open:Z) |
| Win rate | X% |
| Best trade | SYM +X% |
| Worst trade | SYM -X% |
| Profit factor | X.XX |

### Closed Trades
| Ticker | Entry | Exit | P&L | Notes |

### Open Positions at Week End
| Ticker | Entry | Close | Unrealized | Stop |

### What Worked
- ...

### What Didn't Work
- ...

### Key Lessons
- ...

### Adjustments for Next Week
- ...

### Overall Grade: X

---

## Week ending 2026-04-25

### Stats
| Metric | Value |
|--------|-------|
| Starting portfolio | $100,000.00 |
| Ending portfolio | $100,000.00 |
| Week return | $0.00 (0.00%) |
| S&P 500 week | ~+1.5% est. (SPX closed ~7,165 Apr 24) |
| Bot vs S&P | -1.5% (not deployed — launch week) |
| Trades | 0 (W:0 / L:0 / open:0) |
| Win rate | N/A |
| Best trade | N/A |
| Worst trade | N/A |
| Profit factor | N/A |

### Closed Trades
| Ticker | Entry | Exit | P&L | Notes |
|--------|-------|------|-----|-------|
| — | — | — | — | No trades — launch week |

### Open Positions at Week End
| Ticker | Entry | Close | Unrealized | Stop |
|--------|-------|-------|------------|------|
| — | — | — | — | 100% cash |

### What Worked
- Pre-market research completed Saturday for Monday open; energy thesis built
- Account setup fully verified: API keys, scripts, env vars all operational
- Identified primary sector: Energy (XLE/XOM/CVX) — +38.3% YTD, WTI ~$93
- Correctly avoided tech ahead of MSFT/GOOG/META earnings Wed Apr 29
- Infrastructure (Task Scheduler, alpaca.sh, perplexity.sh, clickup.sh) confirmed working

### What Didn't Work
- Zero capital deployed — bot launched Saturday, first market session is Monday Apr 27
- Missed ~+1.5% S&P gain this week while sitting 100% cash (unavoidable — launch timing)
- Big tech earnings week (Wed Apr 29) limits sector selection to energy/staples/materials only

### Key Lessons
- Launch timing: bot went live on a non-trading day; first real P&L begins Apr 27
- Energy sector is the highest-conviction setup entering next week; confirm premarket before entry
- Max 1-2 new positions this week (earnings vol risk from mega-cap tech Wed/Thu)
- PDT count at 0; protect headroom — account > $25k so PDT rules not binding, but track count

### Adjustments for Next Week
- Execute first energy position Monday if XLE/XOM confirm strength at open (buy limit vs market)
- Keep total exposure ≤ 2 positions until Apr 29 earnings clear; add 3rd position Thu/Fri if safe
- Set 10% trailing stop immediately on every fill — no exceptions
- Review again Thursday EOD after MSFT/GOOG/META report

### Overall Grade: N/A (launch week — no trading activity; infrastructure verified, research complete)

---

## Week ending 2026-05-01

### Stats
| Metric | Value |
|--------|-------|
| Starting portfolio | $100,000.00 (Mon Apr 27 AM — first live trading day) |
| Ending portfolio | $100,382.47 |
| Week return | +$382.47 (+0.38%) |
| S&P 500 week | +0.60% |
| Bot vs S&P | -0.22% |
| Trades | 1 (W:0 / L:0 / open:1) |
| Win rate | N/A (no closed trades) |
| Best trade | XLE +2.22% unrealized |
| Worst trade | N/A |
| Profit factor | N/A (no closed trades) |

### Closed Trades
| Ticker | Entry | Exit | P&L | Notes |
|--------|-------|------|-----|-------|
| — | — | — | — | No closed trades this week |

### Open Positions at Week End
| Ticker | Entry | Close | Unrealized | Stop |
|--------|-------|-------|------------|------|
| XLE | $57.5551 | $58.83 | +$382.47 (+2.22%) | 10% trail HWM $59.835 / stop $53.8515 GTC |

### What Worked
- Energy sector selection validated: XLE +2.22% from avg entry, oil WTI surged $97→$106 on Hormuz/geopolitical premium
- 10% trailing stop discipline held all week — both GTC orders active, stops auto-trailed correctly
- Avoided all tech ahead of mega-cap earnings gauntlet (MSFT, META, GOOG, AMZN) — correct call; no gap risk taken
- Patient execution: 1/3 trade slots used, no chasing; AMZN gap risk correctly blocked Friday new position
- Macro reads accurate: GDP Q1 +2.0% not recessionary, ISM Manufacturing 52.7 expansion — energy demand narrative intact

### What Didn't Work
- 75-85% deployment target badly missed: only 17.6% deployed (1 position, 82% cash idle all week)
- Underperformed S&P 500 by 0.22% (+0.38% vs +0.60%) — excess cash drag
- No second position opened despite 2 remaining trade slots and clear thesis window post-Apr 29 earnings
- XLE pulled back Friday (-1.34% day) due to pre-AMZN AMC profit-taking; stops locked, missed trail update opportunity
- Week trade count: 1/3 — left firepower unused; could have added a 2nd position mid-week post-MSFT/META beats

### Key Lessons
- One concentrated position with 82% cash is too conservative vs 75-85% deployment target — need 2nd position faster
- Mega-cap earnings week is an identifiable constraint; plan the 2nd entry window explicitly (Thu/Fri after results clear, not next week)
- XLE trailing stop auto-trailed correctly through Wednesday peak ($59.835 HWM) — stop discipline is working mechanically
- S&P surged +0.60% primarily on tech/risk-on from mega-cap beats; energy-only exposure limits upside capture in risk-on weeks

### Adjustments for Next Week
- AMZN results cleared AMC May 1 — assess NVDA or XLK tech entry Monday May 4 if futures positive
- Target 2nd position by Wednesday May 7 at latest (before NFP May 8 risk window)
- NFP May 8 8:30 AM ET: treat as blackout window for new entries Thu/Fri May 7-8
- If XLE recovers above HWM $59.835, stop will auto-trail; watch for +15% tightening trigger ($66.19 = ~+15% from entry)
- Deployment goal: reach at least 35-40% by end of next week (2 open positions)

### Overall Grade: B-
