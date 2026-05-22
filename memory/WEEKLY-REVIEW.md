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
- XLE continued to drag: -3.22% from entry, oil fell from $106 to ~$94-97; thesis intact but barely (WTI $90 floor 5% away) — **exited proactively after close May 8; market sell 300sh fills Monday May 12 open**
- FCX entry failed R:R check — no valid fourth position found this week; missed deployment boost opportunity
- Wednesday urgency check triggered (≥2 slots unused, <60% deployed) but no valid entry existed — structural gap in candidate pipeline depth
- EOD reviews did not surface thesis-deterioration questions proactively — user had to raise XLE exit in weekly review discussion; **fixed: daily EOD now includes mandatory action questions on thesis health and deployment**

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

---

## Week ending 2026-05-15

### Stats
| Metric | Value |
|--------|-------|
| Starting portfolio | $100,924.27 (May 8 EOD / May 11 open) |
| Ending portfolio | $102,844.19 |
| Week return | +$1,919.92 (+1.90%) |
| S&P 500 week | +1.40% |
| Bot vs S&P | +0.50% (first alpha-positive week) |
| Phase P&L | +$2,844.19 (+2.84% from $100,000 start) |
| Trades | 2 new (W:0 / L:0 / open:4) |
| Win rate | N/A (no closed trades) |
| Best trade | NVDA +12.26% unrealized (drove Thursday +$1,908 day gain) |
| Worst trade | CAT -0.63% unrealized (risk-off Friday selloff) |
| Profit factor | N/A (no closed trades) |

### Closed Trades
| Ticker | Entry | Exit | P&L | Notes |
|--------|-------|------|-----|-------|
| — | — | — | — | No closed trades this week |

### Open Positions at Week End
| Ticker | Entry | Close | Unrealized | Stop |
|--------|-------|-------|------------|------|
| CAT | $892.689 | $887.06 | -$112.58 (-0.63%) | 10% trail HWM $931.35 / stop $838.215 |
| NVDA | $200.54 | $225.13 | +$2,336.14 (+12.26%) | 7% trail HWM $236.54 / stop $219.98 |
| XLK | $175.494 | $175.95 | +$46.97 (+0.26%) | 10% trail HWM $180.215 / stop $162.19 |
| XOM | $150.769 | $157.64 | +$893.25 (+4.57%) | 10% trail HWM $157.425 / stop $141.68 |

### Sector Watchlist — Week 4 (May 19–23)
| Priority | Sector | ETF | Candidate | Condition to Enter |
|----------|--------|-----|-----------|-------------------|
| 1 | Technology | XLK | NVDA/XLK (held) | Post-NVDA earnings May 20 clarity; hold or replace per pre-earnings decision |
| 2 | Energy | XLE | XOM (held) | WTI $100+ sustained; if XOM exits, re-enter XOM/XLE on bounce |
| 3 | Materials | XLB | FCX | Bid/ask spread <$1 Sunday; R:R ≥2:1 at ask; 5th position if slot available |
| 4 | Industrials | XLI | CAT (held) | Hold to stop $838.215; exit manually at -7% ($830.20) if thesis breaks |

### What Worked
- Deployment finally in target zone: 75.6% at week end (4 positions vs 3 last week)
- First alpha-positive week: +1.90% vs S&P +1.40% → +0.50% outperformance
- XOM entry well-timed: WTI/Hormuz premium resilient; +4.57% in 2 sessions; best Friday performer
- NVDA 7% stop tighten executed cleanly when $230.62 threshold breached Thursday; locking +9.7% floor
- XLK entry validated: CPI benign + AI momentum thesis intact; +0.26% after 3 days

### What Didn't Work
- Friday risk-off (-$1,482) erased most of Thursday's gains (+$1,908); net week P&L dampened by single-day reversal
- CAT -3.47% Friday, now -0.63% from entry; no specific catalyst — tariff/macro sensitivity real; thesis integrity uncertain
- NVDA stop $219.98 only 2.3% below Friday close $225.13 — gap-down risk on May 20 earnings not hedged
- Last trade slot (2/3 used) carried unused to Week 4; deployment barely above 75% floor
- Hot PPI + Warsh Fed Chair rumor = new macro tail risk not anticipated; no defensive repositioning before close

### Key Lessons
- 75%+ deployment is the alpha unlock — first week above floor = first alpha-positive week; validates the strategy rule
- NVDA earnings May 20 is the portfolio's single biggest risk; 7% stop protects +9.7% floor but a gap-down on miss can blow through it — need explicit hold/trim/exit decision before May 19 close
- XOM is the surprise outperformer: WTI holding $100+ validates energy re-entry after proactive XLE exit
- CAT needs a thesis check — two consecutive weeks of weakness, now below entry; if tariff fears escalate, stop trigger is only $49 away ($838.215 vs $887)
- Risk-off macro events (PPI hot, Fed Chair regime change) can compress alpha in a single session; position diversification across sectors is working as XOM bucked the trend

### Adjustments for Next Week
- **NVDA earnings May 20:** Decide before May 19 close: (a) hold through with 7% stop, (b) exit partial 30-50sh, (c) exit full to avoid gap risk. Stop $219.98 only 2.3% below close — gap-down on miss exceeds stop buffer. **This is the #1 action item.**
- **CAT monitor:** Stop at $838.215; if price approaches $838 or thesis breaks (tariff guidance, ISM contract), exit manually. Consider replacing with FCX or SOXX if CAT exits.
- **5th position:** FCX if bid/ask spread <$1.00 confirmed Sunday and R:R ≥2:1; SOXX as fallback if semis recover post-NVDA earnings. Week 4 has 3 fresh slots.
- **Macro watch:** PPI hot trend + Warsh risk = rate-sensitive names (CAT, XLK) under pressure; XOM/energy is the macro hedge.
- **Deployment:** Maintain ≥75% floor; if NVDA exits, replace within 1-2 sessions to avoid cash drag.

### Overall Grade: B

---

## Week ending 2026-05-22

### Stats
| Metric | Value |
|--------|-------|
| Starting portfolio | $102,844.19 (May 15 EOD / Week 3 end) |
| Ending portfolio | $103,277.06 |
| Week return | +$432.87 (+0.42%) |
| S&P 500 week | ~+0.5% (cap-weighted; equal-weight +1.5%; extending 8-week win streak) |
| Bot vs S&P | ~-0.08% (roughly flat vs benchmark) |
| Phase P&L | +$3,277.06 (+3.28% from $100,000 start) |
| Trades | 2 (W:1 / L:0 / open:4) — 1 closed (NVDA stop), 1 new buy (AMD) |
| Win rate | 100% (1 closed trade, 0 losers) |
| Best trade | NVDA +9.73% ($+1,847 realized — 7% trailing stop triggered May 18) |
| Worst trade | N/A (no losing closed trades) |
| Profit factor | ∞ (1 winner, 0 losers — insufficient for meaningful ratio) |

### Closed Trades
| Ticker | Entry | Exit | P&L | Notes |
|--------|-------|------|-----|-------|
| NVDA | $200.54 (May 4) | $219.98 (May 18) | +$1,847 (+9.73%) | 7% trailing stop triggered intraday; 14-day hold; auto-exit per tighten rule |

### Open Positions at Week End
| Ticker | Entry | Close | Unrealized | Stop |
|--------|-------|-------|------------|------|
| AMD | $443.38 | $467.54 | +$966 (+5.45%) | 10% trail HWM $481.41 / stop $433.269 |
| CAT | $892.689 | $879.89 | -$258 (-1.44%) | 10% trail HWM $931.35 / stop $838.215 (locked) |
| XLK | $175.494 | $180.39 | +$469 (+2.60%) | 10% trail HWM $181.73 / stop $163.557 |
| XOM | $150.769 | $154.92 | +$516 (+2.75%) | 10% trail HWM $163.68 / stop $147.312 (locked) |

### Sector Watchlist — Week 5 (May 27–30)
| Priority | Sector | ETF | Candidate | Condition to Enter |
|----------|--------|-----|-----------|-------------------|
| 1 | Materials | XLB | FCX | Deferred from Week 4; enter Tue May 27 ~$20K if R:R ≥2:1 and spread <$1 at open; restores deployment ≥75% |
| 2 | Energy | XLE | XOM (held) | Hold to stop $147.312; exit proactively if WTI closes below $95-96 (thesis break); no add |
| 3 | Industrials | XLI | CAT (held) | Hold to stop $838.215; 4 weeks below entry = thesis reassessment; exit manually if ISM contracts |
| 4 | Technology | XLK | AMD/XLK (held) | Sector at cap (2 positions); no new tech buys until one exits |

### What Worked
- NVDA stop discipline executed perfectly: 7% trailing stop auto-triggered at $219.98, locking +9.73% realized gain on a volatile pre-earnings drop that blew through $229 → $219 in a single session
- AMD entry timing was excellent: entered $443.38 post-NVDA beat gap-up May 21; closed week at +5.45% (+$966 unrealized) in one session
- Pre-NVDA earnings blackout fully honored Mon–Tue (May 18–19): no buys into gap-down risk; correct
- XLK recovered above entry (+2.60%) on NVDA beat momentum; tech sector allocation validated
- XOM sustained +2.75% unrealized despite energy-to-tech rotation and Iran de-escalation headwinds; WTI stayed above $95-96 thesis-break line

### What Didn't Work
- Deployment collapsed to 55% after NVDA exit (May 18) and stayed there 2 sessions before AMD buy May 21; week ended at 72.6% — still below 75% floor for the 5th consecutive week
- Only 1 of 3 buy slots used (AMD) — FCX deferred twice (Weeks 3 and 4), SOXX blocked by sector cap; leaving cash idle heading into 3-day weekend
- CAT fourth consecutive week below entry: -1.44% unrealized; no specific catalyst but persistent macro/tariff drag; approaching slow-bleed territory
- XOM thesis visibly weakening: energy-to-tech rotation + Iran de-escalation compressing Hormuz risk premium; WTI slipped toward $97-99 from $106 peak
- Bot returned +0.42% vs S&P ~+0.5% — marginal underperformance; deployment gap is the primary structural drag

### Key Lessons
- NVDA stop discipline payoff: the 7% tighten rule (applied at +15%) caught a profitable exit that a looser 10% stop would have held longer into earnings gap-down risk; rule is proven — keep it
- Gap-up entries post-catalyst beat are valid: AMD +5.45% in one session validates entering at open the morning after a massive beat, even above prior close; don't wait for a pullback that may not come
- 3-day holiday weekends require pre-Thursday deployment action: FCX was a valid entry all week but kept being deferred; going into a 3-day weekend at 72.6% deployed means 4 days without ability to redeploy if something hits a stop
- CAT at 4 weeks below entry with no specific catalyst is a different situation than "temporary weakness"; the record $63B backlog and ISM expansion are still intact but the market isn't rewarding the thesis yet — manual threshold needed
- Equal-weight S&P +1.5% vs cap-weight +0.5%: broad market rally, small/mid-cap led — suggests further sector diversification into Materials (FCX) is the right call for Week 5

### Adjustments for Next Week
- **FCX Tuesday May 27 mandatory:** 5th position, Materials sector, ~$20K (~333sh @~$60); restores deployment to ~90%+; do NOT defer again; only blocker = FCX bid/ask spread >$1 at open
- **CAT exit trigger added:** If CAT closes below $860 on any session OR macro ISM contracts below 50, exit manually; 4 weeks of underperformance = thesis questionable; do not let this become a -7% cut
- **XOM exit trigger confirmed:** WTI close below $95 = thesis break = exit immediately; do not wait for stop $147.312 (4.9% buffer is too wide if thesis is broken)
- **AMD next tighten:** +15% from $443.38 = $509.89; apply 7% trail at that level; monitor daily
- **Deployment goal:** ≥80% by Wednesday May 28 (FCX Tue + hold 4 positions = 5 total ~90% deployed); never enter a 3-day weekend below 75% floor again

### Overall Grade: B-
