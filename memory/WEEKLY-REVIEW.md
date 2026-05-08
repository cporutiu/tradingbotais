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

---

## Week ending 2026-05-08

### Stats
| Metric | Value |
|--------|-------|
| Starting portfolio | $100,388.47 (May 1 EOD / May 4 open) |
| Ending portfolio | $100,924.27 |
| Week return | +$535.80 (+0.53%) |
| S&P 500 week | +1.78% |
| Bot vs S&P | -1.25% |
| Phase P&L | +$924.27 (+0.92% from $100,000 start) |
| Trades | 2 (W:0 / L:0 / open:3) |
| Win rate | N/A (no closed trades) |
| Best trade | NVDA +7.28% unrealized |
| Worst trade | XLE -3.22% unrealized |
| Profit factor | N/A (no closed trades) |

### Closed Trades
| Ticker | Entry | Exit | P&L | Notes |
|--------|-------|------|-----|-------|
| — | — | — | — | No closed trades this week |

### Open Positions at Week End
| Ticker | Entry | Close | Unrealized | Stop |
|--------|-------|-------|------------|------|
| CAT | $892.689 | $897.45 | +$95.22 (+0.53%) | 10% trail HWM $931.35 / stop $838.22 |
| NVDA | $200.54 | $215.13 | +$1,386.05 (+7.28%) | 10% trail HWM $217.80 / stop $196.02 |
| XLE | $57.5551 | $55.70 | -$556.53 (-3.22%) | 10% trail HWM $59.835 / stop $53.8515 |

### Sector Watchlist — Week 4 (May 12–16)
| Priority | Sector | ETF | Candidate | Condition to Enter |
|----------|--------|-----|-----------|-------------------|
| 1 | Technology | XLK | SOXX | NVDA holding above $210; AI momentum intact; CPI clears May 12; 4th position to reach ~72% deployed |
| 2 | Industrials | XLI | CAT (held) | ISM expansion intact; add XLI ETF only if 5th slot opens |
| 3 | Materials | XLB | FCX | Re-validate bid/ask spread and R:R before entry (~$57-60 target); verify 2:1 minimum |
| 4 | Energy | XLE | XOM | HOLD existing XLE; add XOM only if WTI reclaims and holds $97+; max 1 more energy slot |

### What Worked
- NVDA selection excellent: entered $200.54, hit +7.28% unrealized by week end on NVDA-Corning + IREN 5GW partnership catalysts
- CAT entry validated by ISM Services 53.8 confirmation pre-trade; clean +0.53% unrealized with thesis intact
- FCX correctly rejected Wednesday on R:R failure ($64.45 ask → 0.1-0.86:1 vs 2:1 minimum) — rule saved a bad trade
- NFP blackout respected Thu/Fri; no trade placed into the +160K print (goldilocks beat; correct not to rush)
- Stop discipline held all week: all 4 GTC stops active, auto-trailing working correctly on CAT and NVDA

### What Didn't Work
- Underperformed S&P 500 by 1.25% (+0.53% vs +1.78%); deployment gap the primary driver
- Deployment ended week at 54.7% — fourth consecutive week below 75% floor (target 75-85%)
- XLE continued to drag: -3.22% from entry, oil fell from $106 to ~$94-97; thesis intact but barely (WTI $90 floor 5% away)
- FCX entry failed R:R check — no valid fourth position found this week; missed deployment boost opportunity
- Wednesday urgency check triggered (≥2 slots unused, <60% deployed) but no valid entry existed — structural gap in candidate pipeline depth

### Key Lessons
- R:R pre-validation before the entry window is critical: FCX bid/ask spread was $6.50 at open; need to check spread and ask price Sunday/premarket, not at 9:30 AM
- XLE carrying a -3.22% unrealized loss on an oil de-escalation trend; if WTI can't reclaim $95 sustainably, this becomes a slow bleed. Watch $90 thesis-break level daily.
- NVDA and CAT are the right positions: both theses firing; strong unrealized gains offset XLE drag
- S&P +1.78% this week was broad, risk-on (NFP beat, AI momentum, tech leadership); energy-heavy portfolio structurally underperforms in tech-led weeks
- Deployment target (75-85%) requires at least 4 positions; 3 positions at 17-20% each = max 60%; must reach 4th position to close the gap

### Adjustments for Next Week
- **CPI May 12 8:30 AM ET** = named blocker Monday; no new entries Mon AM; assess entries Mon PM or Tuesday
- **4th position priority:** SOXX or XLK — tech sector leading RS; NVDA AI momentum; after CPI clears, enter ~18% sizing to push deployed to ~72%
- **FCX re-entry attempt:** Pull bid/ask spread Sunday evening; only enter if spread <$1.00 and R:R confirms 2:1 minimum at ask price
- **XLE watch:** If WTI closes any session below $90, exit XLE manually (thesis break); do not wait for $53.85 stop if thesis is clearly broken
- **NVDA earnings May 20:** Hold through; tighten stop to 7% if +15% threshold ($230.62) reached before May 20
- **Deployment goal:** Reach ≥65-70% by Wednesday May 14 (4 positions); Wednesday urgency check will apply again

### Overall Grade: C+
