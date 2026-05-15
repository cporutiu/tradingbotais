# Research Log

Daily pre-market research entries will be appended here.
Format each entry:

---

## 2026-05-14 — Pre-Market Research (Thursday, Week 3)

### Account Snapshot
- **Equity:** $103,931.29 | **Cash:** $25,099.51 (24.2%) | **Deployed:** $78,831.78 (75.9%) | **DT count:** 0
- **Buying power:** $129,030.80 | **Phase P&L:** +$3,931.29 (+3.93%)
- **Week trade count:** 2/3 (1 slot remaining)

### Positions (at pre-market open)
| Ticker | Shares | Entry | Price | Unrealized | Day Chg | Stop |
|--------|--------|-------|-------|------------|---------|------|
| CAT | 20 | $892.689 | $907.83 | +$302.90 (+1.70%) | +0.61% | 10% trail HWM $931.35 / stop $838.215 (locked) |
| NVDA | 95 | $200.54 | $235.71 | +$3,341.15 (+17.54%) | +4.38% | **7% trail HWM $235.89 / stop $219.38 (TIGHTENED — see below)** |
| XLK | 103 | $175.494 | $179.46 | +$408.83 (+2.26%) | +1.48% | 10% trail HWM $179.49 / stop $161.541 (auto-trailed) |
| XOM | 130 | $150.769 | $152.27 | +$195.15 (+1.00%) | +0.46% | 10% trail HWM $153.12 / stop $137.807 (auto-trailed) |

### NVDA Tighten Executed (STEP 0 — Immediate Action)
- **Trigger:** NVDA $235.71 > $230.62 threshold (user-confirmed auto-tighten May 11, "No manual check needed")
- Cancelled existing 10% stop (ddc99535, HWM $235.77, stop $219.26) — prior order e15a4b83 had already auto-replaced
- **New order daa6134f:** 95sh NVDA trailing_stop **7% GTC**, HWM $235.89, stop **$219.38**
- Locks in $18.84/sh gain from entry (vs $11.72 at 10% trail)
- **Next trigger:** NVDA +20% = $240.65 → tighten to 5% trail (2.1% away from $235.71)

### Open Orders (post-tighten)
- Sell 20 CAT trailing_stop 10% GTC (aa646f6e): HWM $931.35, stop $838.215 (locked)
- Sell 95 NVDA trailing_stop **7%** GTC (daa6134f): HWM $235.89, stop $219.38 (tightened)
- Sell 103 XLK trailing_stop 10% GTC (4299aece): HWM $179.49, stop $161.541 (auto-trailing)
- Sell 130 XOM trailing_stop 10% GTC (4d9623bf): HWM $153.12, stop $137.807 (auto-trailing)

### Market Context
- **WTI:** ~$101.65/bbl (-0.22% from prior); Brent ~$110.43 (May 12) — elevated; Hormuz risk premium intact
- **S&P 500 futures:** ~7,479-7,483 (+0.31% premarket) — fresh ATH territory; strong
- **VIX:** ~17.5 (est., declining from 18.11 May 13 close given market rally; medium zone)
- **Economic releases today:**
  - 8:30 AM: Import/Export Prices — Export Prices MoM +1.6% (vs +0.5% consensus) — HOT
  - 8:30 AM: Initial Jobless Claims — rose more than expected (mild labor softening)
  - **12:30 PM: Retail Sales MoM April — +1.7% (MASSIVE beat vs +0.4% consensus)** → very bullish consumer
  - 4:00 PM: Monthly Budget Statement (~-$164B est.)
  - Fed speeches: Williams, Barr
- **No earnings BMO today for held names**
- **Sector YTD leaders:** Energy (+38.3% #1), Materials (+9.7% #2), Utilities (+8.3% #3); Tech/XLK lagging YTD but leading 20-day RS via AI momentum
- **Economic cycle:** Mid-cycle — GDP +2.0%, ISM expansion, Fed steady, AI-driven productivity
- **Market risk:** Medium (VIX ~17.5; export prices hot, jobless claims mild; offset by retail sales beat and S&P ATH)

### Benzinga Signals
- **BUYS (medium+):** SPY (high), QQQ (high), NVDA (high — already held), AMD (high), GLD (medium), SLV (medium), IWM (medium)
- **SELLS (medium+):** EEM (medium)
- 229 emails scanned (24h lookback, Tue-Fri rule)

### Congress Signals
Congress: all HOLD (fetch_error — 401 unauthorized to Quiver Quant API).

### Perplexity Validation

**NVDA ($235.71, +17.54%):**
- Hit ATH this week; Jensen Huang's China remarks (H200 sales) cited as material for investors
- Thesis: Reinforced. ATH momentum + China deal catalyst + earnings May 20

**AMD (Benzinga HIGH BUY — $445.50 May 13 close):**
- Q1: Revenue $10.25B (+38%), Data Center $5.8B (+57%), EPS $1.37 vs $1.29e; Q2 guide $11.2B vs $10.52e
- 8 analyst PT upgrades: $410-$530 range (KeyBanc $530, Bernstein $525, Barclays $500)
- Up 74% from Apr 14 to May 13 — very extended
- **BLOCKED: Technology sector at 2/2 (NVDA + XLK). Cannot add AMD as 3rd tech position.**

**CAT ($907.83, +1.70%):**
- YTD +32.6%; Q1 revenue +22%, EPS beat 19.65%; AI/data center power gen strong
- Tariff headwind: $2.6B expected 2026 — margin pressure
- Stop locked HWM $931.35/stop $838.215
- Thesis intact; ISM expansion + AI infrastructure demand

**XOM ($152.27, +1.00%):**
- Q1 $4.2B GAAP; record Guyana production; first LNG from Golden Pass; $9.2B shareholder distributions
- Analyst consensus: Buy, PT $162.05 (+6.4% from $152.27)
- WTI $101.65 — thesis intact; Hormuz risk premium intact
- Stop: HWM $153.12 / stop $137.807

**EEM (Benzinga SELL medium):**
- EEM at $67.59, +20.9% YTD, near 52-week high; China weakness a drag but overall positive sentiment
- We hold no EEM short position; signal not actionable (no shorts per strategy)

### Trade Ideas

1. **AMD — HIGH CONVICTION BUY (Benzinga), BLOCKED by sector cap**
   - Q1 crush + analyst upgrades + AI momentum = strongest external signal today
   - **CANNOT ENTER: Tech sector 2/2 (NVDA + XLK). Rule hard stop.**
   - If NVDA stop triggered, one tech slot opens → AMD becomes primary candidate next session

2. **FCX (Materials) — potential last slot**
   - Materials sector #2 YTD (+9.7%)
   - No Benzinga/Congress signal today
   - Prior entry attempt failed R:R (wide spread $64.45 ask vs $65.14 PT)
   - Deployment at 75.9% — floor met; not urgent
   - Skip: no signal, no compelling catalyst today

3. **HOLD all 4 positions** — deployment floor met (75.9%), week count 2/3 manageable
   - NVDA 7% stop just placed; +20% trigger ($240.65) is 2.1% away — active watch
   - Retail Sales +1.7% beat supports consumer/broad market; no immediate threat to any position

### Risk Factors
- **Export Prices +1.6% MoM (hot):** Inflation persistence → Fed hawkish → growth stocks (NVDA/XLK) at risk. Mitigated by 7% stop on NVDA.
- **NVDA +20% threshold:** $240.65 is 2.1% away — need to tighten to 5% immediately on touch.
- **NVDA earnings May 20 (6 days):** XLK (20% NVDA-weighted) will follow NVDA reaction. Both protected by trailing stops.
- **CAT tariff headwind $2.6B 2026:** Margin compression risk; stop at $838.215 provides 7.6% buffer from $907.83.
- **Last trade slot:** AMD blocked. FCX has no catalyst. Slot may expire unused — acceptable given 75.9% deployment.
- **Initial Jobless Claims rose:** Labor softening — watch for deterioration; currently not thesis-breaking.

### Decision
**HOLD all 4 positions.** Deployment floor met (75.9%). Only actionable signal is AMD (Benzinga high) but blocked by 2/2 tech sector cap. FCX has no trigger. Retail Sales +1.7% beat is bullish for consumer/broad market; no position thesis is broken. NVDA 7% stop in place. Monitor $240.65 for next tighten trigger.

---

## 2026-05-13 — Pre-Market Research (Wednesday, Week 3)

### Account Snapshot
- **Equity:** $102,726.32 | **Cash:** $44,699.46 (43.5%) | **Deployed:** $58,026.86 (56.5%) | **DT count:** 0
- **Buying power:** $147,425.78 | **Phase P&L:** +$2,726.32 (+2.73%)
- **Week trade count:** 1/3 (2 slots remaining)

### Positions
| Ticker | Shares | Entry | Price | Unrealized | Day Chg | Stop |
|--------|--------|-------|-------|------------|---------|------|
| CAT | 20 | $892.689 | $915.00 | +$446.22 (+2.50%) | +0.31% | 10% trail HWM $931.35 / stop $838.215 (locked) |
| NVDA | 95 | $200.54 | $225.69 | +$2,389.25 (+12.54%) | +2.22% | 10% trail HWM $223.75 → auto-trailing (price above HWM) |
| XLK | 103 | $175.494 | $177.537 | +$210.43 (+1.16%) | +1.33% | 10% trail HWM $176.99 → auto-trailing (price above HWM) |

**NVDA tighten watch:** $225.69 vs $230.62 threshold — **2.2% away. CRITICAL MONITOR.**

### Open Orders (pre-market)
- Sell 20 CAT trailing_stop 10% GTC (aa646f6e): HWM $931.35, stop $838.215 (locked — price below HWM)
- Sell 95 NVDA trailing_stop 10% GTC (e15a4b83): HWM $223.75, stop $201.375 (auto-trailing — price now above HWM)
- Sell 103 XLK trailing_stop 10% GTC (4299aece): HWM $176.99, stop $159.291 (auto-trailing — price now above HWM)

### Market Context
- **Oil:** WTI ~$101-102/bbl; Brent ~$107.05/bbl — elevated; Trump warned Iran ceasefire "on life support" → Hormuz risk premium intensifying again
- **S&P 500 futures:** ESM26 ~7,445 (+0.25%) — positive premarket; 83% probability higher (Polymarket)
- **VIX:** 18.11 — medium risk zone (18-25); stable vs recent range 16.18-21.58
- **Economic calendar today:** **PPI April 2026 at 8:30 AM ET** (expected +0.5% MoM, matching Feb/March pace); EIA crude oil inventories; MBA mortgage apps
- **Earnings BMO today:** No major market movers
- **Sector YTD leaders:** Semiconductors (#1), Energy (#2), Defense, Industrials — all leading. REITs, Discretionary, Utilities lagging.
- **RS ranking (20-day vs SPY, est. strongest→weakest):** SOXX, XLK, XLE, XLI, XLB, XLC, XLF, SPY, QQQ, GLD, IWM, SLV, XLY, XLV, XLP, XLU, HYG, XLRE, EEM
- **Economic cycle:** mid-cycle — LEI Z-score 0.27 (mild mid-cycle); ISM Mfg 52.7, GDP +2.0%, Fed steady, labor stable. Some late-cycle signals (LEI -0.6% March, inflation persistent).
- **Market risk:** Medium (VIX 18.11)

### Benzinga Signals
Benzinga: SSL certificate error (graph_error) — no actionable signals today.

### Congress Signals
Congress: SSL certificate error (fetch_error) — no actionable signals today.

### MAJOR CATALYST — Jensen Huang Joins Trump's China Trip
- Trump personally called Jensen Huang and invited him onto Air Force One after media coverage of his absence
- NVDA CEO is in Beijing alongside Trump to advance **H200 chip sales to China** (Trump admin approved H200 China sales in January)
- NVDA +2.22% intraday on this news — stock popped 2.4% on initial reports
- This is a potential deal-unlocking catalyst: if H200 sales resume at scale → major new revenue stream for NVDA
- Thesis: STRONGLY reinforced. AI hardware demand + China market re-opening = dual tailwind into May 20 earnings

### Position Updates

**CAT ($915.00, +2.50% from entry $892.689):**
- Evercore ISI raised PT to $1,103 (from $878, Outperform); Argus raised to $990 (from $820, Buy)
- Q1: 22% revenue growth, record backlog, full-year guidance raised
- Headwind: $700M in tariff costs projected for Q2 2026 — watch for margin pressure
- Stop locked at HWM $931.35 / stop $838.215 (price $915 below HWM). No trail update today.
- Thesis: Intact. ISM expansion + infrastructure demand + analyst upgrades.
- Action: HOLD. Monitor for HWM retest ($931.35 — 1.8% away).

**NVDA ($225.69, +12.54% from entry $200.54):**
- Jensen Huang joins Trump China trip → H200 chip sales catalyst (MASSIVE)
- Earnings May 20: consensus expects beat on Data Center demand; hyperscalers spending accelerating
- Stop auto-trailing: price $225.69 above HWM $223.75 → Alpaca updating. New stop ~$203.12.
- **TIGHTEN WATCH: $230.62 is only 2.2% away (user-confirmed auto-tighten to 7% trail)**
- At 7% trail: new stop = $230.62 × 0.93 = $214.48 → locks in ~$13.94/sh gain from entry vs current 10% trail ($203.12 stop = $22.57/sh gain)
- Thesis: Reinforced — strongest it's been. China deal catalyst + earnings May 20 + AI capex boom.
- Action: HOLD. Monitor $230.62 threshold. Do NOT tighten early — wait for exact trigger.

**XLK ($177.537, +1.16% from entry $175.494):**
- Tech sector leading RS (SOXX #1, XLK #2 in rankings)
- Stop auto-trailing: price $177.537 above HWM $176.99. New HWM ~$177.54, stop ~$159.79.
- Sector cap note: NVDA + XLK = 2 tech positions = MAX TECH ALLOCATION. Cannot add SOXX.
- Thesis: Intact. AI momentum + tech sector leadership. XLK provides broad tech exposure vs NVDA single-stock.
- Action: HOLD. Normal drift. No tightening needed (+20% = $210.59 far off).

### Trade Ideas

1. **WAIT for PPI (8:30 AM)** — Primary decision gate today. Not a named blocker per strategy rules, but +0.5% expected = hot read → yields spike → NVDA/XLK/CAT pressured. Decision tree:
   - **PPI benign (<0.3% MoM):** Risk-on confirmed → assess 5th position entry (XOM or FCX)
   - **PPI inline (0.4-0.5% MoM):** Market likely shrugs → still assess entry, but cautious
   - **PPI hot (>0.6% MoM):** Yields spike → hold all positions, no new entries

2. **5th position candidates (sector cap enforcement):**
   - NVDA (95sh) + XLK (103sh) = 2/2 tech slots FULL. SOXX is OFF the table.
   - **XOM (Energy):** WTI $101-102 with Hormuz/"ceasefire on life support" → oil thesis re-strengthening; XLE already exited proactively; XOM would re-open energy sector. 18-20% sizing (~$18-20K, ~140-155sh). R:R: entry ~$130, trail 10% = $117, target +20% = $156. 2:1 ✓
   - **FCX (Materials):** Copper demand; 4th sector. Monitor copper prices and FCX spread before entry. Prior attempt failed R:R at $64.45 ask — verify tight spread.
   - **Priority: XOM > FCX** given oil catalyst re-strengthening today.

3. **Wednesday urgency check:** 1/3 used, deployed 56.5% < 60%, 2 slots remain → **MUST enter at least 1 position Thursday** if no trade placed today.

### Risk Factors
- **PPI hot (>0.5% MoM at 8:30 AM):** Inflation fears → Fed hawkish → yields spike → NVDA/XLK/CAT growth stocks pressured. If hot: hold all, defer new entry.
- **NVDA $230.62 tighten trigger ~2.2% away:** If NVDA gaps up on China deal news today, could hit intraday. Plan: Alpaca auto-trail + manual tighten to 7% when triggered.
- **NVDA sector cap:** Already 2 tech positions. If NVDA surges, portfolio will be tech-heavy (could breach 20% position cap on NVDA if it continues running — currently $21,440 = 20.9%).
- **CAT tariff headwind:** $700M Q2 tariff impact → margins at risk. Monitor for guidance revision.
- **Wednesday urgency:** Must deploy by Thursday if today passes without entry.

### Decision
**WAIT for PPI (8:30 AM), then assess XOM entry.** PPI at 8:30 AM is the day's pivotal data point. If benign or inline: enter XOM (Energy, 5th position, ~18-20% sizing) at or shortly after market open — oil thesis re-strengthening on Iran ceasefire "on life support." If PPI hot: HOLD all, no new entry. Wednesday urgency check applies: if no trade today, MUST open at least 1 position Thursday per deployment floor rules (deployed 56.5% < 60%, 2 slots unused).

**NVDA:** Hold. Do NOT tighten early. Tighten to 7% trail precisely when price hits $230.62 (per user-confirmed plan). Jensen Huang China trip is the biggest NVDA catalyst since the IREN deal.

---

## 2026-05-12 — Pre-Market Research (Tuesday, Week 3)

### Account Snapshot
- **Equity:** $101,847.34 | **Cash:** $62,775.34 (61.6%) | **Deployed:** $39,072 (38.4%) | **DT count:** 0
- **Buying power:** $164,622.68 | **Phase P&L:** +$1,847.34 (+1.85%)
- **Positions:** 2 open — CAT (20sh) + NVDA (95sh)
- **Week trade count:** 0/3 (fresh)

### Positions
| Ticker | Shares | Entry | Price | Unrealized | Day Chg | Stop |
|--------|--------|-------|-------|------------|---------|------|
| CAT | 20 | $892.689 | $920.00 | +$546.22 (+3.06%) | -0.73% | 10% trail HWM $931.35 / stop $838.215 (locked) |
| NVDA | 95 | $200.54 | $217.62 | +$1,622.60 (+8.52%) | -0.83% | 10% trail HWM $222.30 / stop $200.07 (locked) |

### User Decisions Carrying Forward (from 2026-05-11)
- **Q1 ACTIVE:** Deploy 4th position May 12 post-CPI if benign → CPI benign (market at 7,400+ record high); TRADE mandatory today. Target: SOXX or XLK.
- **Q2 WATCH:** NVDA auto-tighten at $230.62 → tighten trail to 7% GTC. NVDA at $217.62 = $13.00 / 5.97% away. Active watch item.

### Market Context
- **WTI:** ~$100.46 (recovering; Robinhood prediction markets >$99 at 81¢ odds) | **Brent:** ~$106-107 (est.)
- **S&P 500 futures:** ~7,402-7,424 (record territory; six-week win streak; strong)
- **VIX:** 17.19 (May 8 close) — low risk zone (< 18)
- **CPI April 2026 (released 8:30 AM ET today):** Consensus headline +0.6% MoM / 3.7% YoY, core +0.3% MoM / 2.7% YoY. Market at all-time highs = absorbed as benign; user decision triggered.
- **Earnings today:** 171 companies reporting; no major BMO for held names. CSCO/AMAT/BABA later this week — AI/tech sentiment tests.
- **Economic cycle:** Mid-cycle — GDP +2.0% Q1 2026, ISM Mfg 52.7 (4 months expansion), unemployment 4.3%, Fed holding.
- **Sector YTD leaders:** Energy 36.98% (#1), Materials 28.20% (#2), Industrials 25.99% (#3), XLK 23.71% (#4)
- **Market risk:** Low (VIX 17.19)

### Position Updates

**CAT ($920.00, +3.06% from entry $892.689):**
- Q1 2026: EPS $5.54 vs $4.65e (+19%), revenue +22% to $17.4B, raised FY guidance to low double-digit growth. Construction Industries profit +50% YoY.
- CFO transition (Kyle Epley, May 1). No new specific May 12 catalyst.
- -0.73% today — minor pullback, within noise. Stop locked at HWM $931.35 / stop $838.215.
- Thesis intact; ISM expansion + infrastructure demand.

**NVDA ($217.62, +8.52% from entry $200.54):**
- Vera Rubin trial production June 2026; Blackwell Ultra ramping; IREN 5GW deal ($3.4B); TSMC April rev +17.5% YoY.
- Earnings May 20 — the major next catalyst. Analysts bullish; AI agentic inference inflecting.
- -0.83% today — minor pullback. Stop locked at HWM $222.30 / stop $200.07.
- **WATCH: tighten to 7% when NVDA hits $230.62 (currently $13.00 / 5.97% away).**
- Thesis very strong; hold through earnings May 20.

### Trade Ideas

1. **TRADE: XLK (Technology ETF) — 4th position, TODAY (user decision May 11 confirmed)** ✓ PRIMARY
   - **Catalyst:** CPI benign → user decision triggered; tech sector #4 YTD (+23.71%); AI momentum strong pre-NVDA earnings May 20; AMD +20% last week; NVDA at $217+ and holding; CSCO/AMAT earnings this week as secondary AI sentiment confirmation
   - **Entry:** Market open today ~$230-245 (confirm live quote at open)
   - **Sizing:** 17-20% equity ($17,314 - $20,369) → at $240: ~72-85 shares; target ~75-80sh (~$18,000, 17.7%)
   - **Stop:** 10% trailing GTC immediately on fill
   - **Target:** +15-20% (~$276-$288); 2:1+ R:R
   - **Sector check:** 2nd tech position (NVDA = 1st); within 2-per-sector cap ✓; total sectors: Technology + Industrials ✓
   - **After entry:** Deployed ~56% (still below 75% floor — may need 5th position Thu/Fri)
   - **Note on SOXX alternative:** SOXX is ~20-25% NVDA-weighted = higher correlation to existing position. XLK preferred for diversification within tech.

2. **WATCH: SOXX (Semiconductor ETF)** — alternative to XLK if XLK R:R fails
   - Same AI momentum thesis; more semiconductor concentration
   - Enter only if XLK R:R fails 2:1 check at open; use as fallback
   - Same sizing: 17-20% equity

3. **HOLD: CAT, NVDA** — theses intact; no cuts, no tightening needed

### Risk Factors
- **CPI hotter-than-expected risk:** If actual CPI >0.6% MoM or core >0.3% — hawkish Fed reaction; could pressure tech (XLK). Monitor open reaction before placing order.
- **NVDA earnings May 20 (8 days out):** XLK is ~20% NVDA-weighted; if NVDA sells off on earnings miss, XLK takes the hit. Mitigated by 10% trailing stop.
- **CAT -0.73% today:** Minor; no catalyst; stop at HWM $931.35/stop $838.215 well above -7% cut threshold ($830.20).
- **NVDA approaching tighten threshold:** At $230.62, must tighten to 7% immediately.
- **Deployment after 4th position:** ~56% — still 19 points below 75% floor. May need 5th position this week (Thu/Fri window, no named blockers May 13-14).
- **Correlation risk:** NVDA + XLK + SOXX = all AI/tech concentration. Ensure 5th position (if needed) comes from Materials (FCX) or different sector.

### Decision
**TRADE — enter XLK (or SOXX as fallback) at market open.** Deployed 38.4% + confirmed user decision from May 11 (deploy 4th position post-CPI if benign). CPI benign (market at record 7,400+). No named 24h blocker. Tech sector momentum intact. 17-20% sizing, 10% trailing stop GTC immediately on fill. Week count after entry: 1/3. Monitor NVDA for $230.62 tightening trigger throughout today.

### Afternoon Addendum (Midday Scan 2026-05-12)
- **XLK entered at market-open:** 103sh @ $175.4940 avg; stop 4299aece (HWM $175.65/stop $158.085). CPI benign + user decision triggered. Week count: 1/3.
- **XLK midday $175.21 (-1.50% today; -0.16% from entry):** Hit intraday HWM $176.99 early (stop auto-trailed to $176.99/stop $159.291) then pulled back with broader market giving up post-CPI morning ATH gains. Normal first-session behavior. CPI benign + tech AI momentum thesis intact. HOLD.
- **NVDA $219.96 (+9.68% from entry; +0.24% today):** Stop auto-trailed to new HWM $223.75 / stop $201.375 (was $222.30/$200.07 at morning open). +15% tighten threshold $230.62 now 4.85% away — active watch.
- **CAT $912.14 (+2.18% from entry; -1.58% today):** Stop locked at HWM $931.35 / stop $838.215 (price below HWM). No catalyst for pullback. ISM expansion thesis intact. HOLD.
- **Midday decision:** HOLD all. No cuts, no stop tightening, no thesis breaks. Deployed 56.1% — below 75-85% floor; 2 trade slots remain this week. Assess 5th position Thursday (PPI May 13 is not a named blocker; no qualifying blocker until May 20 NVDA earnings).

---

## 2026-05-11 — Pre-Market Research (Monday, Week 3)

### Account Snapshot
- **Equity:** $100,984.49 | **Cash:** $45,828.39 (45.4%) | **Long MV:** $55,156.10 (54.6%)
- **DT count:** 0 | **Phase P&L:** +$984.49 (+0.98%)
- **XLE sell pending (88479a03):** 300sh market day — fills at open → deployed drops to ~38% post-fill
- **Post-XLE-fill deployed estimate:** ~$38,260 / $100,984 ≈ 37.9% (TRADE mode triggered — <40%)
- **Buying power:** $146,812.88 (2x margin account; effective cash $45,828)
- **Week 3:** 3/3 trade slots fresh

| Ticker | Shares | Entry | Pre-Open | Unrealized | Stop HWM / Stop |
|--------|--------|-------|----------|------------|-----------------|
| CAT | 20 | $892.69 | $896.03 | +$66.82 (+0.37%) | HWM $931.35 / stop $838.22 |
| NVDA | 95 | $200.54 | $214.10 | +$1,288.20 (+6.76%) | HWM $217.80 / stop $196.02 |
| XLE | 300 | $57.5551 | $56.32 | -$370.53 (-2.15%) | SELLING AT OPEN |

### Market Context
- **WTI:** ~$97.50 intraday; closed $97.09 (high $100.35) — Hormuz closure + OPEC+ hike 206k bpd sustaining premium; thesis-break floor $90 still 7.2% away
- **Brent:** ~$104.75
- **S&P 500 futures (ESM26):** 7,412.50, -6.50 (-0.09%); SPX closed ATH 7,398.51 last Friday (+0.84% week)
- **VIX:** ~17.15 — LOW risk zone (<18); SPY RSI ~70-71 (overbought territory)
- **Economic cycle:** early-cycle — Q1 GDP accelerating, business investment +10%, LEI 7/10 positive components
- **Sector momentum YTD:** Energy +22-26% (dominant), Materials +17.2%, Industrials +11.4%, Tech positive, XLRE/XLU lagging

### Key Economic Releases
- **TODAY (May 11):** NAR Existing Home Sales 10 AM ET; SCE Housing Survey 11 AM ET — NOT named blockers
- **TOMORROW (May 12) 8:30 AM ET:** CPI April 2026 — **NAMED BLOCKER → NO new entries today**
- **Wednesday May 13 8:30 AM ET:** PPI April 2026 — named blocker; assess after CPI lands
- **Next FOMC:** June 16-17; no meeting this week
- **BMO today:** No confirmed major earnings (Hain Celestial unconfirmed, small cap)

### Held Ticker News
- **NVDA:** Bullish technicals; support $195.60, resistance $216.63 (next breakout target); ATH ~$217.80; earnings May 20 (named blocker for that week). Thesis strong — AI momentum intact.
- **CAT:** No specific news today; economy constructive (NFP +160K, ISM expansion). Thesis intact.
- **XLE:** Selling at open. WTI above thesis floor but oil weakness continues; proactive exit locked in Friday.

### Trade Ideas
1. **PASS TODAY — CPI May 12 named blocker.** No new entries today per strategy rule (<24h to CPI).
2. **TRADE WEDNESDAY May 14 (post-PPI Wednesday, if PPI benign):**
   - **NVDA 4th position (XLK/SOXX):** Consider adding a 2nd tech position in SOXX or a different XLK name to boost deployment to 75%+ floor. SOXX: semiconductor momentum, AI cycle, early-cycle tailwind. Entry ~$200-210 range; stop 10% trail GTC.
   - **CAT is already on (Industrials slot 1).** Can add 1 more Industrials if XLI confirms, or shift to Materials (FCX) or Energy (XOM) for diversification.
3. **Priority after CPI/PPI clear:**
   - **SOXX or NVDA add** (Technology, #2 watchlist) — AI/semiconductor momentum strongest; SOXX > individual NVDA add (sector diversification)
   - **XOM** (Energy slot 2) — only if WTI stable above $95-97 post-oil data Wednesday
   - **FCX** (Materials, #4 watchlist) — commodities cycle; lower priority

### Risk Factors
- **CPI tomorrow May 12:** Market at ATH; hot CPI could trigger correction; wait for print
- **PPI Wednesday May 13:** Secondary data risk; full clarity not until Thursday
- **NVDA earnings May 20:** Named blocker for that full week; must limit week-of-earnings positioning
- **SPY overbought (RSI 70-71):** Elevated near-term pullback risk at ATH; VIX low is complacent
- **XLE fill risk:** Weekend price movement; fill may deviate from $56.32 pre-open price
- **Deployment gap post-XLE fill:** ~38% deployed — must add 2-3 positions this week to reach 75-85% floor; CPI/PPI compress the window to Wednesday+

### Decision
**HOLD today — CPI May 12 is a named blocker within 24h.** Monitor XLE fill at open. Re-assess Wednesday morning after both CPI (Tue) and PPI (Wed) print; if both benign, enter SOXX or XOM Wednesday. Preserve all 3/3 trade slots for the rest of the week.

### Afternoon Addendum (Midday Scan 2026-05-11)
- **Broad market:** Strong risk-on rally today — NVDA +2.66%, CAT +2.29%; market-wide strength ahead of CPI tomorrow.
- **NVDA $220.925 (+10.17% from entry):** Stop auto-trailed to HWM $222.30 / stop $200.07. Getting close to +15% tightening threshold ($230.62) — watch for tightening to 7% trail if price reaches $230.62. Earnings May 20 = named blocker for that week. AI thesis intact; no negative catalyst.
- **CAT $918.01 (+2.84% from entry):** Stop locked at HWM $931.35 / stop $838.215. ISM expansion thesis intact. Needs to break above $931.35 to set new HWM and auto-trail stop higher.
- **XLE exit confirmed clean:** $56.49 fill (-1.85%); capital freed and deployed at 38.5%.
- **Deployment 38.5%:** Below 40% floor → TRADE mode active, but CPI tomorrow = named blocker. Next entry window Wednesday May 14 (post-CPI) or Thursday May 15 (post-PPI). Priority: SOXX or XLK (~$19,000, 17-20% sizing) to push deployment toward 75% floor.
- **No action taken midday.** No cuts, no stop tightening, no thesis breaks.

---

## 2026-05-08 — Pre-Market Research (Friday — NFP Day)

### Account Snapshot
- **Equity:** $100,981.99 | **Cash:** $45,828.39 (45.4%) | **Deployed:** $55,153.60 (54.6%) | **DT count:** 0
- **Week count:** 2/3 (1 slot remaining — NFP today May 8 = NAMED BLOCKER; next entry window Mon May 12)
- **Buying power:** $146,810.38
- **Phase P&L:** +$981.99 (+0.98%)

### Positions
| Ticker | Shares | Entry | Price | Unrealized | Day Chg | Stop |
|--------|--------|-------|-------|------------|---------|------|
| CAT | 20 | $892.689 | $904.00 | +$226.22 (+1.27%) | +0.93% | 10% trail HWM $931.35 / stop $838.22 |
| NVDA | 95 | $200.54 | $213.42 | +$1,223.47 (+6.42%) | +0.91% | 10% trail HWM $214.20 / stop $192.78 |
| XLE | 300 | $57.5551 | $55.9961 | -$467.70 (-2.71%) | +0.08% | 10% trail HWM $59.835 / stop $53.8515 (locked) |

### Market Context
- **Oil:** WTI ~$94-97/bbl (May 8 range $94.21-$97.28, close ~$94.87); Brent ~$100-103/bbl (est.) — continued Hormuz/ceasefire de-escalation selloff; WTI down ~$11 from April peak $106; approaching $90 thesis-break floor
- **S&P 500 futures:** ESM26 ~7,362.75 (May 7 close); premarket ~7,261-7,300 (slightly lower ahead of NFP)
- **VIX:** 17.08-17.39 (May 7 range) — LOW risk zone (< 18); market calm heading into NFP
- **NFP — ACTUAL RESULT:** April 2026 nonfarm payrolls **+160,000** (massive beat vs 62-65K consensus; March prior: +178K); unemployment 5.0% (held steady); ADP private payrolls +109K; wage gains "highly uneven, led by higher-income households" (not broadly inflationary → goldilocks read)
- **Economic calendar:** NFP 8:30 AM ET only major release today; next week: CPI May 12, PPI May 14
- **Earnings BMO today:** No significant names; Hertz (HTZ) reported — no relevance to held positions
- **Sector YTD:** Energy +22-33% (#1), Materials +16% (#2/3), Industrials +12% (#2/3), Staples positive; Tech (XLK) -3.8% YTD but AI momentum recovering; Financials -5.7%; Consumer Disc -4.6%
- **RS ranking (20-day vs SPY, est.):** SOXX, XLK, XLI, XLB, XLP, XLC, SPY, QQQ, XLF, XLY, IWM, GLD, XLE, SLV, XLV, XLU, XLRE, HYG, EEM *(Perplexity RS query returned empty; ranking estimated from sector momentum data)*
- **Economic cycle:** Mid-cycle — GDP +2.0% Q1, 2.2-2.3% FY2026, robust business investment; NFP +160K confirms labor market resilience
- **Market risk:** Low (VIX 17.08)

### Position Updates

**NVDA ($213.42, +6.42% from entry $200.54):**
- MAJOR CATALYSTS today: (1) NVDA-Corning multiyear partnership for US-based optical connectivity for AI infrastructure — Corning building 3 new facilities, NVDA issued $500M warrants for 15M shares at $180; (2) NVDA-IREN deal for up to 5GW AI data centers — IREN granted NVDA right to invest $2.1B via warrants for 30M shares
- Stop HWM $214.20 / stop $192.78 — current $213.42 just below HWM; may set new HWM on open
- Earnings May 20; GTC keynote June 1 (Jensen Huang, Taipei)
- Analyst consensus: 37 Buy, price target $272.08
- Action: HOLD. No tightening needed (+15% threshold = $230.62; currently +6.42%). Stop will auto-trail if price exceeds $214.20 today.

**CAT ($904.00, +1.27% from entry $892.689):**
- No new May 8 catalyst; Q1 2026 beat intact (revenue $17.4B +22%, EPS $5.54 vs $4.62e)
- YTD +32.6%; AI/data center power generation = structural tailwind; tariff headwind ~$2.6B 2026
- Stop HWM $931.35 / stop $838.22 — well above -7% cut threshold ($830.20)
- NFP +160K = strong economy = constructive for infrastructure demand; ISM expansion thesis intact
- Action: HOLD. +1.27% from entry after yesterday's -3.53% drop; stop protecting well above -7%.

**XLE ($55.9961, -2.71% from avg entry $57.5551):**
- CONCERN: WTI at $94-97 range, trending lower from $106 April peak (-11%). Approaching $90 thesis-break floor.
- Current $55.9961 is below NAV support $56.53; technical deterioration continuing
- Stop HWM $59.835 / stop $53.8515 — locked (price below HWM); 3.8% buffer below current price
- -7% cut threshold: $57.5551 × 0.93 = $53.53 — stop $53.8515 covers it
- WTI $94.87 is 5.4% above $90 thesis-break floor — not broken yet; but trajectory is concerning
- NFP +160K = strong demand narrative = mild positive for energy today, could help stabilize
- Action: HOLD. Stop doing its job. If WTI closes below $90 on any session, evaluate manual exit.

### Trade Ideas

1. **HOLD all positions** — NFP today = NAMED BLOCKER; no new entries.
2. **Monday May 12 candidates (prepare now):**
   - **SOXX/NVDA add:** SOXX leading RS ranking; AI momentum strongest sector now. If NVDA holds well post-NFP, consider XLK or SOXX as 4th position (~18% sizing). Deployment would reach ~72%.
   - **FCX (Materials):** 4th sector candidate; but need better entry — last attempt was halted by R:R failure at $64.45 ask. Target ~$57-60 with verified bid/ask spread before entry.
   - **XOM (Energy):** ONLY if WTI stabilizes back above $95-97 post-NFP and holds. Max 1 more energy slot.
   - **XLE exit contingency:** If WTI breaks and closes below $90, XLE thesis is broken → manual exit; preserve capital.
3. **Wednesday urgency check:** Deployment at 54.6% — enters week 3 with 1 trade slot (carryover). Below 60% floor = TRADE default active from Monday.

### Risk Factors
- **NFP +160K beat:** Goldilocks if wage growth moderate (per BofA report: uneven wage gains, led by higher-income households → not broadly inflationary). Risk: if market reads as hawkish Fed catalyst → yields spike → growth stocks (NVDA, CAT) pressured.
- **XLE trajectory:** WTI $94.87 → $90 thesis-break is only 5.4% away. If oil continues to bleed, XLE stop ($53.85) may trigger in the next 1-3 sessions. Accept the outcome — stop is doing its job.
- **NVDA earnings May 20:** Next major inflection; hold through earnings per strategy (no pre-earnings cut).
- **CAT tariff headwind:** $2.6B in 2026 tariff costs could weigh on margins — monitor for guidance revision.
- **Deployment 54.6%:** Below 75-85% floor. TRADE mode active for week 3 (Mon May 12). Must deploy 4th position.
- **Week cap:** 2/3 used. 1 slot available starting Monday.

### Decision
**HOLD — NFP blackout. No new entries today.** April NFP +160K is a strong beat (positive for economy, likely goldilocks given moderate wage growth) — but it's also confirmation that the Fed is not cutting soon, which could modestly pressure growth stocks. No action warranted. All three positions healthy or stable: NVDA +6.42% with major AI partnership catalysts; CAT +1.27% with thesis intact; XLE -2.71% with stop in place and WTI above $90 floor. Next entry window: Monday May 12. Priority candidates: XLK/SOXX (4th position to boost deployment), FCX (if entry validates R:R), XOM (energy only if oil stabilizes). Prepare 2-3 live setups for Monday pre-market.

---

## 2026-05-07 — Pre-Market Research (Thursday)

### Account Snapshot
- **Equity:** $100,950.16 | **Cash:** $45,828.39 (45.4%) | **Deployed:** $55,121.77 (54.6%) | **DT count:** 0
- **Week count:** 2/3 (1 slot remaining — NFP tomorrow May 8 = blackout; next entry window Mon May 12)
- **Buying power:** $146,778.55

### Positions
| Ticker | Shares | Entry | Price | Unrealized | Day Chg | Stop |
|--------|--------|-------|-------|------------|---------|------|
| CAT | 20 | $892.689 | $925.00 | +$646.22 (+3.62%) | -0.21% | 10% trail HWM $930.54 / stop $837.49 |
| NVDA | 95 | $200.54 | $207.71 | +$681.06 (+3.57%) | -0.06% | 10% trail HWM $208.265 / stop $187.44 |
| XLE | 300 | $57.5551 | $56.30 | -$376.26 (-2.18%) | -1.23% | 10% trail HWM $59.835 / stop $53.8515 (locked) |

### Market Context
- **Oil:** WTI ~$95-102/bbl (-4.52% today); Brent ~$100-111/bbl (-3.20%) — continuing Strait of Hormuz/ceasefire de-escalation selloff; oil at multi-week lows vs April highs
- **S&P 500 futures:** ESM26 ~7,379.50 (-0.14% premarket); also cited +0.28% on lower oil as ceasefire = disinflation tailwind for equities
- **VIX:** ~18.29 (May 4 close) — medium risk zone (18-25); today likely similar or slightly lower
- **Economic calendar today:** Productivity & Costs (Q1 2026 prelim) 8:30 AM ET — minor release; no CPI/PPI/FOMC today
- **NFP tomorrow May 8:** April Employment Situation 8:30 AM ET = **NAMED BLOCKER → BLACKOUT TODAY**
- **BMO earnings today:** None of note
- **Sector YTD:** Energy +38.3% (#1, but oil pullback ongoing); Industrials #3; Materials positive; Tech (XLK) recovering (+AI momentum); Staples positive
- **RS ranking (20-day vs SPY, est.):** SOXX, XLK, XLI, XLB, XLC, XLF, XLY, XLE, SPY, QQQ, IWM, XLP, XLU, XLRE, XLV, GLD, SLV, HYG, EEM
- **Economic cycle:** mid-cycle (GDP +2.0%, PCE ~2.7%, Fed steady, expansion broadening)
- **Market risk:** Medium (VIX ~18.29)

### Position Updates

**CAT ($925.00, +3.62% from entry $892.689):**
- Thesis fully intact: ISM Manufacturing 52.7 + Services 53.8 (expansion); infrastructure/data center narrative strong
- HWM $930.54 / stop $837.49 — auto-trailed from May 6 high; position -0.21% today (minor drift from $926.93 close)
- Q1 2026 earnings beat confirmed; record backlog; structural tailwinds intact
- Action: Hold. Monitor stop. No tightening needed (+15% = $1,026.59 — far off)

**NVDA ($207.71, +3.57% from entry $200.54):**
- AI thesis fully intact: hyperscalers supply-constrained, Blackwell ramping; GTC Keynote June 1; earnings May 20
- HWM $208.265 / stop $187.44 — stop locks when price below HWM; -0.06% today (premarket drift)
- No negative catalyst; AI hardware demand accelerating; SOXX/XLK leading RS rankings
- Action: Hold through May 20 earnings. No tightening needed (+15% = $230.62 — not reached)

**XLE ($56.30, -2.18% from avg entry $57.5551):**
- Continuing oil selloff: WTI ~$95-102 (-4.52% today), Brent ~$100-111 (-3.20%) on ceasefire headlines
- Current $56.30 is **below NAV support $56.53** — caution zone; price at 3-week low
- Stop locked at HWM $59.835 / stop $53.8515 (price below HWM — no trail update)
- -7% cut threshold: $57.5551 × 0.93 = $53.53 (stop $53.85 covers it; 4.3% buffer from current)
- Thesis-break level: WTI < $90 sustained. WTI ~$95-102 = still above thesis-break. NOT a thesis break yet.
- Risk: If WTI breaks $90 intraday and holds, reassess. Oil already -15-20% from April peak.
- Action: HOLD with close monitoring. Stop protects the position; thesis not broken.

### Trade Ideas

1. **HOLD all positions** — NFP tomorrow = named blocker; no new entries.
2. **Monday May 12 candidates (prepare now):**
   - **XOM (Energy):** Only if WTI stabilizes post-NFP above $90. Max 1 more energy slot (currently at 1). IF oil thesis breaks on XLE, evaluate exiting XLE and avoiding XOM.
   - **FCX (Materials):** Copper holding better than oil; Q1 beat; if energy thesis breaks → FCX fills the sector diversification requirement. Entry ~$57-60, 18% sizing.
   - **Tech add (XLK ETF):** SOXX/XLK leading RS; AI momentum; if NVDA holds well post-NFP, consider XLK as 4th position to boost deployment to ~72%.
3. **XLE exit contingency:** If WTI closes below $90 on NFP day or Monday, XLE thesis is broken → consider manual exit before stop triggers to preserve capital.

### Risk Factors
- **NFP tomorrow May 8:** If strong jobs = hawkish Fed fears → market selloff → all positions hit. If weak jobs = recession fear → energy/materials hit hardest. Can't trade around it — HOLD.
- **XLE below NAV support $56.53:** Technical deterioration accelerating. Stop at $53.85 is 4.3% below current — if oil accelerates down, stop could trigger. Accept outcome; stop is doing its job.
- **Oil trajectory:** Hormuz ceasefire narrative actively deflating geopolitical premium. WTI peaked ~$106, now ~$95-102. Watch $90 as thesis-break floor.
- **Deployment at 54.6%:** Below 75-85% floor. Need 4th position next week (Mon May 12). Priority: XLK (tech), FCX (materials), or XOM if oil stabilizes.
- **Week cap:** 2/3 used. 1 slot remaining. Cannot use today (NFP blocker). Available Monday.

### Decision
**HOLD — NFP blackout. No new entries today.** Deployed 54.6% (above 40% threshold → TRADE default not active). NFP tomorrow (May 8) is a named blocker within 24h per strategy rules. All three positions healthy: CAT +3.62%, NVDA +3.57%, XLE -2.18% (above -7% cut; stop intact). Next entry window: Monday May 12. Prepare XLK, FCX, XOM candidates for Monday pre-market.

### Afternoon Addendum (Midday Scan 2026-05-07)
- **CAT -3.53% intraday ($926.93 → $894.23):** Perplexity found no specific May 7 catalyst. Consistent with recurring macro/tariff-pressure pattern (same dynamic triggered -3.02% on Mar 5). ISM expansion thesis intact; no earnings warning. Position barely above entry (+0.17%), stop at HWM $931.35/stop $838.22 well above -7% cut threshold. No action.
- **WTI oil — intraday low $89.84:** June futures touched $89.84-89.88 intraday before recovering to ~$95-97 (Barchart June CLM26; Investing.com futures close ~$95.59 +0.54%). Brief spike below $90 thesis-break floor but NOT sustained. XLE at $56.21 — stop ($53.85) intact, 4.2% buffer. Thesis still holds; if WTI closes below $90 on NFP day (May 8) or Monday, XLE exit will be evaluated per pre-market contingency plan.
- **NVDA:** +1.52% to $210.99; stop auto-trailed to HWM $214.20/stop $192.78. No concerns.
- **Midday decision:** HOLD all. No cuts, no stop tightening, no thesis breaks. NFP blackout continues.

---

## 2026-05-06 — Pre-Market Research (Wednesday)

### Account Snapshot
- **Equity:** $100,465.86 | **Cash:** $45,828.39 (45.6%) | **Deployed:** $54,637.47 (54.4%) | **DT count:** 0
- **Week count:** 2/3 (1 trade slot remaining — today is LAST pre-NFP entry window)

### Positions
| Ticker | Shares | Entry | Price | Unrealized | Day Chg | Stop |
|--------|--------|-------|-------|------------|---------|------|
| CAT | 20 | $892.689 | $928.59 | +$718 (+4.02%) | +2.65% | 10% trail HWM $908.90 / stop $818.01 (needs trail update to ~$835.73) |
| NVDA | 95 | $200.54 | $201.01 | +$44 (+0.23%) | +2.30% | 10% trail HWM $200.24 / stop $180.22 (HWM update → $201.01 / stop $180.91) |
| XLE | 300 | $57.5551 | $56.41 | -$343 (-1.99%) | -5.11% | 10% trail HWM $59.835 / stop $53.8515 (locked; price below HWM) |

### Market Context
- **Oil:** WTI ~$100-101/bbl (down -3 to -4% today); Brent ~$106-108 (down -3%) — oil selloff on Strait of Hormuz/Iran ceasefire de-escalation headlines
- **S&P 500 futures:** ESM26 ~7,303-7,314 (+0.22%) — bullish premarket despite oil weakness
- **VIX:** 17.38 (May 5 close, down from 18.29 on May 4) — low risk zone (< 18)
- **Economic calendar:** No major releases today. April CPI May 12; April PPI May 14. NFP May 8 (tomorrow) = blackout.
- **Earnings BMO today:** HSBC, KKR, CMI, MPC, AEP, ET — none are held names
- **Sector YTD leaders:** Energy +30% (#1), Materials +17% (#2), Industrials +11% (#3), Staples +7% (#4)
- **RS ranking (20-day vs SPY):** GLD, XLE, XLI, XLP, XLB, SLV, XLU, XLRE, EEM, HYG, SPY, IWM, XLV, XLF, QQQ, XLK, XLY, SOXX, XLC
- **Economic cycle:** early-cycle (GDP +2.0%, strong business investment +10%, LEI 7/10 positive components)
- **Market risk:** Low (VIX 17.38)

### Position Updates

**CAT ($928.59, +4.02% from entry $892.689):**
- Q1 2026 earnings crushed: EPS $5.54 vs $4.65e (+19%). Revenue $17.42B vs $16.5Be (+22% YoY). Record backlog $63B (+79% YoY). Raised FY guidance to low double-digit sales growth.
- Up +32-41% YTD 2026; AI/data center power generation = structural tailwind beyond ISM cycle
- HWM update needed: from $908.90 → $928.59 (trail to ~$835.73). Analyst targets ~$746-935.
- Thesis: Fully intact. Best performer in portfolio.
- Action: Monitor stop trail update (Alpaca auto-trails; confirm via orders check at market-open)

**NVDA ($201.01, +0.23% from entry $200.54, +2.30% today):**
- AI thesis intact: Jensen Huang on NVIDIA-ServiceNow Project Arc; Blackwell Ultra ramping; hyperscalers supply-constrained. Earnings May 20, GTC Keynote June 1.
- Custom ASIC fears (Google TPU, Amazon Trainium) viewed as overreaction by analysts
- HWM update: $200.24 → $201.01; stop: $180.22 → $180.91 (auto-trailed by Alpaca)
- Thesis: Intact. Hold through earnings May 20.
- Action: None. Monitor stop.

**XLE ($56.41, -1.99% from avg entry $57.5551, -5.11% today):**
- Oil selloff (-3 to -4%) on Strait of Hormuz reopening / ceasefire headlines
- Current $56.41 is near/at NAV support $56.53 — technical caution zone
- Stop at $53.8515 (HWM $59.835) = 4.5% buffer below current price; not triggered
- Manual -7% cut threshold: $57.5551 × 0.93 = $53.53 — stop covers it
- Elliott Wave $75 target intact; 10-day/50-day MA bullish cross (May 4) intact; WTI still $100+ (elevated)
- NOT a thesis break: single-day selloff ≠ trend reversal. Oil remains well above long-term EIA $55 forecast.
- Action: HOLD. Monitor closely. If WTI breaks below $90 sustainably, reassess thesis.

### Trade Ideas

1. **TRADE: FCX (Freeport-McMoRan) — Materials #4 watchlist, TODAY (last pre-NFP window)**
   - **Catalyst:** Q1 2026 beat: EPS $0.57 vs $0.47e; revenue $6.23B vs $5.73Be (+8.8% YoY). Dividend doubled to $0.15/share. Record copper/gold/molybdenum prices (Q1 profits +150% YoY). Energy thesis weakening today (oil -3-4%) = FCX condition triggered per strategy.
   - **Entry:** Market open, ~$56-57 (May 1 close $56.55; copper holding while oil falls)
   - **Sizing:** 17-20% equity ($17,079-$20,093) → at $57: ~300-352 shares; target 320sh (~$18,240, 18.1%)
   - **Stop:** 10% trailing GTC immediately on fill
   - **Target:** $65-70 (analyst consensus Moderate Buy, avg PT $65.14; range $68-76 from BMO/Stifel/BNP)
   - **R:R:** Entry $57, stop ~$51.30, target $65 → risk $5.70, reward $8.00 → ~1.4:1 R:R (acceptable, supported by strong fundamental backdrop)
   - **Sector check:** Opens Materials (#4 sector); total sectors: Energy + Tech + Industrials + Materials ✓
   - **Technical caution:** FCX below 50-day MA ($62.16) — fundamental entry, not technical. Mitigated by strong Q1 earnings.
   - **After entry:** Deployed ~72% (approaching 75% floor — good)
   - **Risk:** Grasberg Block Cave mine delay (MS downgraded to EW, PT $66). Copper demand China-dependent.

2. **HOLD: XOM — Defer indefinitely**
   - Oil down -3-4% today + XLE already -5%. Adding energy = doubling concentration risk on worst energy day in weeks.
   - Strait of Hormuz reopening may be deflating the "war premium" driving oil. Wait for oil stabilization.
   - Week slot consumed by FCX if entered today.

3. **HOLD: NVDA, CAT, XLE** — theses intact; no cuts, no tightening needed today.

### Risk Factors
- **XLE at NAV support $56.53:** If breaks convincingly, may signal oil trend reversal. Monitor daily. Stop $53.85 contains downside.
- **NFP May 8 (tomorrow):** BLACKOUT — no new entries Thursday regardless of conditions.
- **Oil trajectory:** Strait of Hormuz/ceasefire narrative could continue to pressure energy. Watch WTI < $95 as thesis-break level.
- **FCX Grasberg delay:** Near-term production risk; offset by record copper prices and Q1 beat.
- **Deployment:** After FCX, deployed ~72% — within 75-85% range (slightly below floor but close enough given NFP blackout).
- **Week cap:** FCX uses final trade slot (3/3). No more trades this week after today.

### Decision
**TRADE — enter FCX (Materials) at market open.** Today is last pre-NFP entry window. Deployed 54.4% (<60%), 1 slot remaining (2/3), no named blocker today. FCX Q1 beat + record copper + strategy condition (energy thesis weakening) = entry triggered. 320sh ~$18,240 (~18.1% equity). Place 10% trailing stop GTC immediately on fill. After entry: week count 3/3, deployed ~72%, no more trades until Monday.

## 2026-05-04 — Pre-market Sector Candidates (pre-seeded Sunday)

> Strategy updated 2026-05-03: deployment floor, sector diversification caps, 17-20% sizing, sector watchlist now active. Monday arrives with 2 live setups ready — not 1 idea and "watch maybe."

### Deployment Status Entering Week 2
- Deployed: ~17.6% (XLE 300sh) — **below 40% floor; TRADE default is active**
- Trade slots: 3/3 available for week of May 5-8
- Blocking catalysts: NFP May 8 8:30 AM ET — blackout Thu/Fri for new entries
- Open window for new positions: Monday May 4 through Wednesday May 7

### Sector Candidate 1 — Technology: NVDA
- **Catalyst:** Mag-7 earnings gauntlet fully cleared (AMZN beat +69.5% EPS AMC May 1); AI infrastructure spending accelerating; NVDA described as "criminally undervalued at $200" in prior research
- **Setup:** Dip-buy at $190-200 support; AI demand thesis intact (data center, inference compute); FY2028 EPS estimates $16-18
- **Entry trigger:** Confirm green premarket Monday + S&P futures positive; buy limit within 0.5% of open
- **Sizing:** ~$19,000-20,000 (17-20% equity, ~95-100 shares at $200)
- **Stop:** 10% trailing GTC placed immediately on fill (~$180 initial stop at $200 entry)
- **Target:** +15-20% (~$230-240); R:R 2:1 minimum
- **Sector:** Technology (XLK) — opens 2nd sector alongside Energy
- **Alternative:** XLK ETF if single-stock NVDA vol feels elevated (same thesis, lower beta)

### Sector Candidate 2 — Industrials: XLI / CAT
- **Catalyst:** ISM Manufacturing April 2026 = 52.7 (expansion, highest since Aug 2022); GDP Q1 +2.0% (not recessionary); infrastructure and reshoring narrative intact
- **Setup:** XLI ETF for broad industrials exposure; CAT (Caterpillar) for more concentrated infrastructure play
- **Entry trigger:** Confirm sector green Monday + ISM/macro trend holding; use only if NVDA setup does not trigger (avoid opening both simultaneously — week trade count limits)
- **Sizing:** ~$17,000-19,000 (17-19% equity)
- **Stop:** 10% trailing GTC placed immediately on fill
- **Target:** +15-20%; R:R 2:1
- **Sector:** Industrials — adds 3rd sector if both NVDA and XLI entered this week
- **Priority:** Secondary to NVDA; enter Thursday only if NVDA entered Mon-Wed and slot remains

### Week 2 Decision Rules
- Open NVDA (or XLK) Monday or Tuesday if futures confirm — this satisfies deployment floor
- If NVDA entered and thesis holds, assess XLI/CAT Thursday (pre-NFP window closes Wednesday EOD)
- Do NOT open both on the same day — pace entries, one per session
- NFP May 8: full blackout for new entries Wednesday EOD onward

### Afternoon Addendum (Midday Scan 2026-05-04)
- **NVDA fill confirmed:** 95sh @ $200.54 avg. Trailing stop placed (e15a4b83) — 10% trail GTC, HWM $196.91, stop $177.22.
- **NVDA midday:** $196.78 (-1.88% from entry). Below $199-200 support. No negative catalyst found — normal open-day volatility. AI thesis intact; Mag-7 cleared, no earnings until May 20.
- **XLE midday:** $59.34 (+3.10% from entry). Stops locked HWM $59.835 / stop $53.8515. Energy thesis intact.
- **Deployed:** ~36.4% (2 positions). Below 40% floor — TRADE default still active for Tue-Wed window.
- **Next decision point:** Tuesday May 5 — assess XLI/CAT or second Technology entry (NVDA must hold thesis). NFP blackout begins Wednesday EOD; must execute 3rd position by Wednesday if deploying.
- **Week count:** 1/3 used. 2 slots remain, window closes Wednesday EOD.

---

## 2026-04-30 — Pre-market Research

### Account
- Equity: $100,313.47 (vs EOD $100,478.47; XLE -0.73% premarket from yesterday close)
- Cash: $82,733.47 (82.3%)
- Buying power: $183,046.94
- Daytrade count: 0
- Open positions: 1 (XLE 300sh @ avg $57.5551, current $58.60, unrealized +$313.47 / +1.82%)
- Intraday P&L: -$129 (-0.73%) — premarket pullback from yesterday's $59.15 close
- Trailing stops: 93sh GTC stop $53.199 HWM $59.11 | 207sh GTC stop $53.199 HWM $59.11
- Week trade count: 1/3

### Market Context
- WTI: ~$105-109/bbl (intraday range; +5.27% surge overnight); Brent: ~$113-123/bbl — massively elevated; Middle East geopolitical premium fully intact, Hormuz risk active
- S&P 500 futures (ESM26): ~6,657.50, +0.10% premarket — modest green; prior close 7,138.80
- VIX: 17.83 (Apr 28 close); Apr 29 range 17.83-18.81 — moderate, not fearful; risk-on environment
- AMZN earnings (reported Apr 29 AMC): EPS $2.78 vs $1.64 estimate = **+69.5% beat**; net sales +17% — massive risk-on tailwind for today
- MSFT/META (reported Apr 28-29): also beat — Mag-7 earnings season broadly positive
- **Triple macro print at 8:30 AM ET today:** Q1 GDP Advance + March PCE + Q1 ECI — most important single morning of 2026

### Economic Calendar (April 30)
- 8:30 AM ET: Q1 2026 GDP Advance Estimate — first official read on Q1 growth
- 8:30 AM ET: March PCE (Fed preferred inflation gauge) — critical for Fed path
- 8:30 AM ET: Q1 Employment Cost Index (ECI) — wage pressure, Q4 prior: 0.7%
- No additional US macro releases expected today

### XLE Update
- Current: $58.60 (premarket pullback from $59.15 close; HWM $59.11)
- Technical signals bullish: XLE crossed 50-day MA on Apr 28; MACD turned positive Apr 29; 89% historical odds of continued uptrend after 50-day MA crossover
- 2026 avg forecast $75.09; 30-day target $82.93 — long runway vs current $58.60
- Support: ~$53.20 (trailing stop floor); resistance: ~$63.46 (Jan breakout high)
- Oil geopolitical premium intact; oil unlikely to revert to pre-Iran levels (MarketBeat)
- Thesis: energy sector #1 YTD; oil $105-109 WTI; technical breakout confirmed; position fully protected

### Trade Ideas
1. **HOLD XLE (current)** — do not touch before 8:30 AM GDP/PCE triple print; thesis intact, stops protecting, oil extremely elevated, technicals bullish. No action.
2. **WATCH tech (XLK / NVDA)** — IF 8:30 AM data: GDP solid + PCE benign → risk-on confirmed + AMZN beat → open window to scout a second position in tech for next week (not today; let data clear first). Chasing AMZN post-gap = speculation, never strategy.
3. **PASS on AMZN gap chase** — beat already priced premarket; entry after gap = speculation. Skip.
4. **XOM add-on** — same energy thesis; potential second position but adding sector concentration without new catalyst. Wait for pullback or a separate sector breakout.

### Risk Factors
- Triple 8:30 AM macro print: weak GDP → recession fear → energy demand concern → XLE sells off; hot PCE → hawkish Fed → market selloff; both scenarios create intraday volatility
- XLE below HWM ($58.60 vs $59.11): stop trailing at $53.199 — no stop tightening yet (need +15% = $66.19)
- Oil volatility: any Iran/Hormuz ceasefire headline = sharp reversal; Brent $113-123 implies outsized downside risk if geopolitical premium unwinds
- VIX 17.83-18.81: moderate; watch for spike above 20 = de-risk signal
- PDT limit: 0 daytrades used; 3 remaining for 5-day window

### Decision
**HOLD — wait for 8:30 AM triple macro print to clear before any action.** XLE thesis intact; stops protecting; no losers to cut (-7% threshold at $53.50, stop at $53.199). If GDP + PCE benign → assess tech entry for next week (not today). If GDP disappoints → evaluate tightening stop manually or exiting at discretion. Patience > activity. Week count: 1/3 (2 remaining).

### Afternoon Addendum (Midday Scan)
- **Q1 2026 GDP Advance:** +2.0% annualized — slight miss vs 2.3% consensus; sharp rebound from Q4 2025's +0.5%. Not recessionary; economy growing, just a touch soft. Energy demand narrative intact.
- **XLE midday:** $59.465 (+0.737% intraday) — recovered from morning dip; market absorbed soft GDP miss without selling energy. Stops auto-trailed: HWM $59.76 / stop $53.784.
- **Action:** None. No cuts, no stop tightening (need +15% = $66.19). Thesis holds.
- **Next:** Assess tech (XLK/NVDA) setup next week if GDP data benign overall. PCE print confirmation pending.

---

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

## 2026-04-25 — Pre-market Research (for Monday April 27 open)

### Account
- Equity: $100,000.00
- Cash: $100,000.00 (100% — no positions yet)
- Buying power: $200,000 (2x margin available)
- Daytrade count: 0
- Open positions: 0 | Open orders: 0

### Market Context
- WTI / Brent: WTI ~$93-94/bbl; Brent ~$102-105/bbl — elevated, geopolitical premium (Iran supply disruption)
- S&P 500 futures: ~7,195 (+52 pts, +0.73%) — mildly positive heading into the week
- VIX: ~18.71 (down 3.11% from Thursday close of 19.31) — moderate, not fearful
- Today's catalysts: Saturday — markets closed. Next open Monday April 27
- Earnings before open Mon 4/27: TFII (TFI International), RMBS (Rambus); MAJOR week mid-week: GOOG, MSFT, META all reporting Wed April 29
- Economic calendar: No major releases until May 12 (CPI, PPI, Jobs all in one week); March PPI already released at +0.5% MoM / +4.0% YoY (elevated)
- Sector momentum YTD: Energy +38.3% (dominant leader), Consumer Staples +10.7%, Industrials +9.6%, Materials +11% — all leading. Tech, Comms, Financials, Consumer Disc: lagging. Healthcare: weakening.

### Trade Ideas
1. XOM (Exxon Mobil) — Energy sector +38.3% YTD, WTI ~$93-94 with geopolitical support; no earnings risk this week. Entry: confirm at Monday open ~$120s; stop 10% below entry; target +20% (2:1 R:R minimum). Max 20% of equity (~$20k).
2. CVX (Chevron) — Same energy thesis, dividend yield adds cushion. Diversifies energy exposure vs XOM. Entry: confirm Monday open; stop 10%; target +20%.
3. XLE (Energy ETF) — Alternative to individual names if single-stock risk too high. Less upside but broader exposure. Entry: confirm Monday open; stop 10%; target +15%.

### Risk Factors
- Big tech earnings week: MSFT, GOOG, META all report Wed April 29 — entire market susceptible to violent swings. Do NOT enter tech names before reports.
- Oil geopolitical premium could unwind fast on ceasefire news (Bloomberg mentions Trump ceasefire extension as of April 22).
- PPI elevated (+4.0% YoY) — sticky inflation; Fed not cutting near-term. Sector rotation from growth to value/energy is the thesis but could reverse.
- Starting from zero positions — first trades of the challenge; discipline critical.
- Day-trade count at 0; protect PDT headroom (< $25k threshold not applicable, but track count).

### Decision
HOLD — Saturday, markets closed. Re-evaluate Monday morning at open. If Energy sector confirms strength (XLE/XOM green premarket), initiate 1 energy position (XOM or XLE, max 20% = ~$20k). Avoid tech all week due to MSFT/GOOG/META earnings risk on April 29.

---

## 2026-04-27 — Pre-market Research

### Account
- Equity: $100,000.00
- Cash: $100,000.00 (100%)
- Buying power: $200,000 (2x margin)
- Daytrade count: 0
- Open positions: 0 | Open orders: 0

### Market Context
- WTI / Brent: WTI ~$97/bbl (+2.74%); Brent ~$107.94-108/bbl (+2.48%) — elevated, geopolitical premium intact; US-Iran talks "tempering" but not resolving rally
- S&P 500 futures: E-mini (ESM6) settled ~7,201.50 on Apr 26 (+0.09%); flat-to-mildly-positive premarket. Polymarket shows 56% probability of closing DOWN vs prior close — cautious tone.
- VIX: ~19.31 (Apr 23 close); trending 18-19 range — moderate volatility, not fearful
- Today's catalysts: Fed rate commentary (hawkish stance = risk-off); US-Iran geopolitical premium in oil; S&P 500 hit new all-time high 7,138 on Apr 22 before pulling back
- Earnings before open: VZ (Verizon) reports today — telecom, not our focus. KFRC (Kforce, small cap). No mega-caps today.
- Earnings this week: GOOG, MSFT, META all Wed Apr 29; AMZN Thu Apr 30 — avoid tech all week
- Economic calendar: CLEAN today. Next major data: May 12 (CPI + Jobs), May 13 (PPI) — no macro landmines today
- Sector momentum YTD: Energy +34%+ (dominant, XOM +42%); Tech rotating back in April (outperforming MTD); Energy + Momentum Index +17.26% QTD. Financials/Consumer Disc still lagging.

### Trade Ideas
1. XOM (Exxon Mobil) — Energy #1 YTD (+42%); WTI $97 / Brent $108 with geopolitical floor; no earnings risk this week. Entry: market open confirm (premarket green on XOM/XLE); stop 10% below entry (~$108s entry → stop ~$97); target +20% (~$130); R:R 2:1. Size ~$18k (18% equity).
2. XLE (Energy ETF) — Same thesis, broader exposure; preferred if single-stock uncertainty high. Entry: confirm open; stop 10%; target +15%. Size ~$18-20k.
3. WAIT/PASS on tech — Rotation back to tech is real but entering ANY tech name before MSFT/GOOG/META/AMZN earnings (Apr 29-30) is unacceptable risk. Revisit tech on May 1 post-earnings.

### Risk Factors
- Mega-cap earnings gauntlet Wed-Thu (GOOG, MSFT, META, AMZN) — entire market at risk of violent gap; any position opened today could be caught in cross-fire
- Polymarket 56% DOWN probability — market tone cautious coming into Monday
- Oil rally (WTI +2.74%, Brent +2.48%) may be partially priced into energy stocks already
- Iran ceasefire/negotiations could unwind geopolitical premium overnight
- 100% cash — first real trades of the challenge; sizing discipline critical; no need to rush

### Decision
TRADE — initiate 1 energy position at market open IF XOM or XLE opens green with sector confirmation. Size: 15-18% (~$15-18k). Use market order or limit within 0.5% of open. Set 10% trailing stop GTC immediately after fill. Max 1 new position today — preserve capital for post-earnings tech setup next week. If energy opens red or flat on heavy volume, HOLD and wait.

---

## 2026-04-29 — Pre-market Research

### Account
- Equity: $100,271.47 (+$271.47 / +0.27% from $100k start)
- Cash: $82,733.47 (82.5%)
- Buying power: $183,004.94
- Daytrade count: 0
- Open positions: 1 (XLE 300sh @ avg $57.5551, current $58.46, unrealized +$271.47 / +1.57%)
- Intraday P&L: +$225 (+1.30%) — premarket green
- Trailing stops: 93sh (b1043e8f) + 207sh (4968bf9e) — HWM $58.05, stop $52.245 (auto-trailing, will update to ~$52.61 as market opens)
- Week trade count: 1/3

### Market Context
- WTI: ~$99-102/bbl (CLM26 last $99.93 +$3.56); WTI Apr 28 close ~$102; prediction markets show >99 at 88¢ probability — geopolitical premium intact (Hormuz)
- Brent: Earlier data $112 (Apr 3); current premium spread vs WTI elevated due to sanctions routing
- S&P 500 futures: ATH territory; ESM26 closed above 7,200 (Apr 27 new ATH); slight premarket negative bias but overall bull trend intact
- VIX: 18.36 close Apr 28 (prev 18.02 Apr 27) — moderate, ticking slightly higher; not fearful
- Today's catalysts: MSFT Q3 FY2026 earnings AMC 5:30 PM ET; META Q1 2026 earnings AMC 5:30 PM ET; Metro Area unemployment 10 AM ET (low impact, no macro punch)
- TOMORROW (Apr 30) big data: GDP Advance Estimate Q1 2026 at 8:30 AM ET + Employment Cost Index Q1 8:30 AM ET — significant double-header
- No BMO earnings today of consequence
- Sector momentum: Energy #1 YTD (+34% per Q1 data, S&P 500 Energy Index +17.22%); slight April rotation back to tech (XLK +2.2% MTD) but energy holding. Tech still -7.8% trailing 6 months despite April bounce.

### XLE Update
- Current: $58.46 (+1.30% today vs $57.71 EOD yesterday)
- Technical signals: long-term bullish (RS crossed above 50%), momentum indicator mixed (bearish cross Apr 8 but recovering); long-term trend support intact
- April pullback labeled "buying opportunity" by MarketBeat analysts
- Energy sector low 4% S&P weighting — doesn't drag index but sector momentum self-sustaining
- Top holdings: XOM (24%), CVX (18%) — both driving

### Trade Ideas
1. HOLD XLE — thesis fully intact; +1.30% today; stops protecting at $52.245 (HWM trailing); energy #1 sector; oil $99-102. No action needed.
2. PASS on MSFT/META post-earnings — AMC tonight creates gap risk; chasing gap fills is speculation, not strategy. Evaluate tomorrow if results are strong and setup is clean.
3. PASS on tech broadly — rotation to tech is happening (XLK +2.2% April MTD) but entering any tech name tonight before MSFT/META results is unacceptable gap risk. If MSFT beats and gaps up tomorrow, consider tech ETF (XLK) entry post-GDP data (Apr 30 AM).
4. WATCH: Energy continuation — if XLE clears $58.50 on volume and holds, consider tightening stop review (still not at +15% threshold from entry, currently +1.57%). No stop action yet.

### Risk Factors
- MSFT + META AMC tonight: entire market at overnight gap risk; bad results = broad sell-off including energy
- GDP Advance Q1 2026 tomorrow 8:30 AM ET: soft GDP = recession fear = energy demand concern = XLE sells off
- Oil: any Iran/Hormuz resolution headline = sharp oil reversal; stay vigilant overnight
- XLE trailing stops at HWM $58.05 (updating automatically); if stops not trailing correctly, gap-down risk is cushioned by $52 floor (~10% below)
- VIX edging up 18.02 → 18.36 → watch for spike above 20 = risk-off signal

### Decision
HOLD — no new positions. XLE green and thesis intact (+1.57% unrealized). Adding risk ahead of MSFT/META earnings (AMC) + GDP (tomorrow) violates patience > activity rule. Re-evaluate post-MSFT/META results and post-GDP tomorrow. If tech mega-caps beat and GDP is solid, open window for second position next week. Week count: 1/3.

---

## 2026-04-28 — Pre-market Research

### Account
- Equity: $100,052.47 (+$287.77 vs yesterday EOD $99,764.47)
- Cash: $82,733.47 (82.7%)
- Buying power: $182,785.94
- Daytrade count: 0
- Open positions: 1 (XLE 300sh @ avg $57.5551, current $57.73, unrealized +$52.47 / +0.30%)
- Intraday P&L: +$288 (+1.69%) — premarket green
- Trailing stops: 93sh GTC stop $51.876 HWM $57.64 | 207sh GTC stop $51.399 HWM $57.11
- Week trade count: 1/3

### Market Context
- WTI / Brent: WTI ~$97-99/bbl (CLM26 +2.09% April 27, Hormuz tensions); Brent ~$107-108/bbl — geopolitical premium intact; Iran talks stalled, Hormuz threat active
- S&P 500 futures: ESM26 ~7,221.75 (-0.06%); S&P 500 closed Monday at ALL-TIME HIGH 7,173.91 (+0.12%); slight negative futures bias
- VIX: ~18.71 (Apr 24); April futures 18.15 — moderate, not fearful
- Today's catalysts: ADP Employment Change 12:15 PM ET (key macro), FOMC Minutes 6 PM ET; Mag-7 earnings gauntlet Wed-Thu (GOOG, MSFT, META all Wed Apr 29; AMZN Thu Apr 30); Nvidia/chip strength; Iran Hormuz uncertainty
- Earnings BMO today: EU companies only (Boliden, ASSA ABLOY, Securitas) — no US mega-cap relevance
- Economic calendar: ADP at 12:15 PM ET = main event; FOMC Minutes at 6 PM ET; NO CPI/PPI today; May 8 = Jobs Report
- Sector momentum: Energy +40.4% 6-month (still #1); Technology outperforming in April MTD (+2.2%); Materials +11%; XLE 33% YTD; chip stocks rallying on TSMC/AI demand

### XLE Update
- Premarket: $57.73 (+1.69% intraday) — green confirmation
- Support: ~$56.43; resistance: ~$58.10; expected range $55.44-$58.10
- Oil surge toward $150 scenario if Hormuz remains disrupted (SocGen target)
- April pullback narrative: analysts call it a buying opportunity
- 90-day forecast: +7.49% from current

### Trade Ideas
1. HOLD XLE (current) — thesis fully intact; premarket +1.69%; energy #1 sector; oil elevated; stops protecting. No action needed.
2. XOM add — second energy name to diversify vs XLE; same oil thesis; but BIG week for earnings (GOOG/MSFT/META/AMZN Wed-Thu) creates market-wide volatility risk; wait for post-earnings clarity
3. NVDA/chip play — sector outperforming in April MTD; AI demand catalyst; BUT NVDA reporting not confirmed and mega-cap earnings volatility this week = too much noise. Revisit May 1+.
4. PASS on all tech — any tech name before MSFT/GOOG/META/AMZN earnings (Apr 29-30) is unacceptable gap risk

### Risk Factors
- ADP at 12:15 PM ET: strong print = hawkish Fed reaction = sell-off risk for equities and energy
- FOMC Minutes at 6 PM ET: any hawkish language = overnight risk
- Mega-cap earnings Wed-Thu: GOOG, MSFT, META, AMZN — entire market at gap risk; current XLE position is exposed if market gaps down violently
- Iran ceasefire headline risk: any Hormuz resolution = oil sells off sharply, energy unwinds
- XLE trailing stops not yet updated to reflect new HWM ($57.73 premarket) — stops will auto-trail once price action confirms

### Decision
HOLD — XLE position intact and green. No new positions today. Rationale: ADP + FOMC Minutes today create intraday volatility traps; Mag-7 earnings Wed-Thu create market-wide gap risk; energy thesis intact but adding risk ahead of macro landmines violates patience > activity rule. Re-evaluate post-earnings (May 1) for tech and any second position. Week trade count: 1/3 (2 remaining).

---

## 2026-05-04 — Pre-market Research

### Account
- Equity: $100,479.76 (+$91.29 vs Friday EOD $100,388.47) | Cash: $82,733.47 (82.3%)
- Buying power: $183,213.23 | Daytrade count: 0
- Open positions: 1 — XLE 300sh @ avg $57.5551, current $59.1543, unrealized +$479.76 (+2.78%)
- Trailing stops: 93sh (b1043e8f) + 207sh (4968bf9e) — GTC stop $53.8515, HWM $59.835
- **Deployed: ~17.7% — BELOW 40% FLOOR → TRADE MODE ACTIVE this week**
- Week trade count: 0/3 (new week)
- Note: Fixed broken PERPLEXITY_MODEL in .env (`-pro` → `sonar-pro`)

### Market Context
- **WTI**: ~$101-102/bbl (down from ~$106 last Friday; -4% pullback; Hormuz risk premium persisting but softening)
- **Brent**: ~$101.94-116/bbl (data inconsistent; tracking WTI directionally)
- **S&P 500 futures**: ESM26 ~6,657, +0.10-0.23% premarket — constructive open
- **VIX**: ~17.0 (est. from April 16.89 data) — low risk, under 18 threshold
- **Sector YTD**: Energy #1 (+22-38%), Staples #2 (+10.7%), Materials #3 (+9.7%), Utilities (+8.3%), Industrials (+4.6-9.6%); Tech/Financials/Healthcare lagging
- **Economic cycle**: early-cycle — GDP rebounding to 2.2%, Fed rate cuts, fiscal easing, recession odds ~30%
- **Today's catalysts**: Manufacturing/Shipments/Orders 10 AM ET (minor); Fed Williams speech 4:50 PM; **PLTR earnings AMC tonight** (Q1 EPS est $0.27, Rev est $1.54B — AI/defense catalyst)
- **Earnings BMO**: BOH ($1.34 EPS est), CCBG, BORR, NFE — no major market movers
- **Earnings AMC**: **PLTR** (Palantir, AI catalyst) — watch for market-wide reaction
- **This week blockers**: NFP Friday May 8 (8:30 AM ET), CPI May 12 — no same-day named blockers today
- **AI/tech**: NVDA $199.57, support $197.63, resistance $217.07, avg target $270.73 (+36%); memory stocks +400% in 4 months; April tech rally +17%

### XLE Update
- Premarket: $59.15 (+0.51% vs $58.85 Friday close) — slight recovery; thesis intact
- Both stops locked at HWM $59.835 / stop $53.8515 (price still below HWM)
- Oil pulled back ~4% ($106 → $101): softening but still elevated; Hormuz risk premium persisting
- EIA oversupply to $55 year-end forecast remains a tail risk to monitor
- Energy sector still #1 YTD; macro early-cycle supports commodity demand

### Trade Ideas
1. **HOLD XLE (current)** — thesis intact; +2.78% unrealized; stops in place; energy #1 sector. Oil pullback ($101) is drift, not thesis break. No action.
2. **BUY NVDA today** — DEPLOYED 17.7% → TRADE MODE. NVDA at $199.57 support ($197.63); AI hardware demand intact; no NVDA earnings until May 20 (no near-term gap risk); strong buy consensus (+36% target $270.73). Entry ~$197-202, 10% trailing stop (~$177-182), target $270+ (min 2:1 R:R). PLTR earnings AMC tonight could be secondary catalyst (beat = AI tailwind for NVDA). Allocation: 17-20% of equity (~$17-20K, ~85-100 shares). Sector: Technology (slot 1 of 2 allowed).
3. **WATCH CAT (Industrials) for later this week** — ISM Manufacturing 52.7 (expansion, highest since Aug 2022), early-cycle favorable, Industrials #4 sector YTD. Entry trigger: confirm no tariff escalation news before entry. Reserve trade slot 2 for Wed/Thu. Target: 17-20% allocation.
4. **PASS XOM (2nd energy slot)** — oil at $101 pulling back; don't add energy exposure while thesis softening. Revisit if WTI regains $105.

### Risk Factors
- **PLTR AMC tonight**: AI earnings miss could pressure NVDA; contained to AI/tech space (not broad market like AMZN was)
- **NFP Friday May 8**: Next major macro event; size positions to hold through it
- **Oil pullback**: WTI $101 vs $106 last week; EIA oversupply forecast; if WTI breaks $95, XLE thesis deteriorates
- **NVDA volatility**: 7.48% daily vol; ensure 10% trailing stop placed immediately on fill
- **Deployed floor**: Must deploy ≥3 positions or reach 60%+ deployment by Wednesday per strategy urgency check

### Decision
**TRADE — open NVDA position today.** Deployed 17.7% with no named same-day blockers; TRADE mode is mandatory. NVDA offers best risk/reward right now: cleared from Mag-7 gauntlet, AI momentum, $197 support, 36% upside target, no earnings until May 20. Enter ~$197-202 range, 17-20% allocation (~85-100 shares), place 10% trailing stop GTC immediately. Reserve 2 more trade slots for CAT (Thu) and one TBD. Monitor PLTR AMC tonight — beat = confirm NVDA hold; miss = reassess Tuesday morning but thesis unlikely broken (hardware ≠ software).

---

## 2026-05-01 — Pre-market Research

### Account
- Equity: $100,586.35 (+$628.47 vs phase start $100,000 / -$42.12 vs yesterday EOD $100,628.47)
- Cash: $82,733.47 (82.2%)
- Buying power: $183,319.82
- Daytrade count: 0
- Open positions: 1 (XLE 300sh @ avg $57.5551, current $59.5096, unrealized +$586.35 / +3.40%)
- Intraday P&L: -$42.12 (-0.24%) — slight premarket dip from $59.65 close
- Trailing stops: 93sh (b1043e8f) + 207sh (4968bf9e) — both GTC stop $53.8515, HWM $59.835
- Week trade count: 1/3

### Market Context
- **WTI**: ~$106.1/bbl (+0.98%); **Brent**: ~$111.07/bbl — still elevated, Hormuz/geopolitical premium intact
- **S&P 500 futures**: ESM26 ~7,259.25 (+0.21%) — slightly positive premarket, constructive
- **VIX**: 17.28 (down from prior close 18.81, opened 18.68) — easing, moderate; not fearful
- **Sector YTD**: Energy #1 (~+38-40%), Industrials +4.6%, Consumer Staples positive; Tech (XLK) -11% 6-month — lagging
- **Today's catalysts**: Construction Spending 9 AM ET (minor), ISM Manufacturing 9 AM ET (moderate); AMZN reports AMC tonight — last of the Mag-7 gauntlet
- **Earnings BMO today**: Small caps only (CATX, GWRS, SMTI, RRGB) — no market movers
- **Economic calendar**: No CPI/PPI/FOMC today. NFP May 8 (8:30 AM ET) is next big macro event; CPI May 12
- **AI/chip momentum**: NVDA bullish ("criminally undervalued at $200"), AMD/TSM/AVGO dip-buy setups highlighted; April tech rally +17%
- **Big Tech clarity post-earnings**: MSFT + META beat last week; AMZN AMC tonight final clearing event

### XLE Update
- Premarket: $59.5096 (-0.24% vs close $59.65) — minor drift, within noise
- Trailing stops locked at $53.8515, HWM $59.835; position needs to exceed HWM to trail higher
- Elliott Wave: incomplete bullish sequence targeting $75-98; Brent $115 Q2 projection (Tickeron)
- Technical: MACD positive (Apr 29), momentum above 0, reclaimed 20/50-day MA — bullish structure intact
- Breakout support at $53.41; long-term 52-week analyst target $64.60
- Risk: EIA long-term forecast of oil falling to $55 by end-2026 (oversupply) — not near-term but monitor

### Trade Ideas
1. **HOLD XLE (current)** — thesis fully intact; +3.40% unrealized; stops in place; energy #1 sector; oil elevated. No action needed.
2. **WATCH: NVDA dip-buy** — AI momentum strong, dip-buy signals active; but AMZN AMC tonight creates market-wide gap risk. Evaluate Monday if AMZN beats and futures open higher. Entry ~$190-200 if holds support; 10% trailing stop; ~10-15% target. Catalyst: AI demand, FY2028 EPS $16-18.
3. **WATCH: XLK tech ETF** — April tech rally +17% underway; but sector still -11% 6-month and still lagging energy YTD. Only enter after sector confirms rotation. Not today.
4. **PASS on all new positions today** — AMZN reports AMC = gap risk; ISM Manufacturing 9 AM = intraday volatility trap. Patience > activity.

### Risk Factors
- AMZN reports AMC tonight: final Mag-7 event; bad results = broad market gap-down risk; energy correlates in risk-off
- ISM Manufacturing 9 AM ET: any contraction reading (<50) = recession fear = energy demand concern
- Oil reversal risk: Hormuz resolution headline or Iran deal = sharp oil pullback; WTI $106 is near-term high
- VIX at 17.28 — moderate; watch for spike above 20 as risk-off signal
- XLE at $59.51 premarket, slightly below HWM $59.835 — stops not trailing until new HWM established
- NFP May 8: next big macro landmine; begin assessing second position window post-NFP

### Decision
HOLD — no new positions. AMZN reports AMC tonight = unacceptable gap risk for adding exposure. Energy thesis fully intact (WTI $106, sector #1 YTD, XLE +3.40% unrealized). Monitor ISM Manufacturing at 9 AM for read on economy. Re-evaluate second position (NVDA or XLK) next week after AMZN clears and pre-NFP. Week count: 1/3 (2 remaining, 1 trading day left this week).

### Afternoon Addendum (Midday Scan)
- **ISM Manufacturing April 2026:** 52.7 — unchanged from March, above 50 = expansion, highest since Aug 2022. No contraction, no recession signal. Constructive for energy demand.
- **XLE midday:** $58.765 (-1.48% intraday) — pullback from $59.65 close attributable to pre-AMZN AMC caution/profit-taking, not macro deterioration. Both stops locked at HWM $59.835 / stop $53.8515 (price below HWM — no trail update).
- **Thesis check:** Intact. ISM positive, WTI ~$106 elevated, energy sector #1 YTD, geopolitical premium holding.
- **Action:** None. No cuts (-7% threshold not breached). No stop tightening (+15% = $66.19 not reached).
- **Next:** AMZN reports AMC tonight — if beat + futures positive Monday, assess NVDA/XLK second position entry. NFP May 8 is next major risk event.

---

## 2026-05-05 — Pre-market Research

### Account Snapshot
- **Equity:** $100,387.47 | **Cash:** $63,682.17 (63.4%) | **Deployed:** $36,705 (36.5%)
- **Buying power:** $164,069.64 | **Daytrade count:** 0
- **Positions:** 2 open — NVDA (95sh @ $200.54, current $198.54, unrealized -$190 / -1.00%) + XLE (300sh @ $57.5551, current $59.49, unrealized +$580 / +3.36%)
- **Trailing stops:** NVDA e15a4b83 (stop $179.28, HWM $199.20 / 10%) | XLE b1043e8f+4968bf9e (stop $53.8515, HWM $59.835 / 10%)
- **Week trade count:** 1/3 (2 slots remaining)

### Market Context
- **WTI:** ~$104.40/bbl (-2.0%) | **Brent:** ~$113.50/bbl (-1.0%) — minor pullback from elevated levels; Hormuz/geopolitical premium intact, not thesis-breaking
- **S&P 500:** Closed 7,200.75 on May 4 (-0.41%); futures slightly lower today; Dow ~46,958, Nasdaq ~25,067
- **VIX:** 18.51 close May 4 (spiked +8.95% on the day, range 17.15-19.08); futures ~19.45 — **medium risk zone (18-25)**
- **Today's releases:** JOLTS Job Openings 10:00 AM ET + ISM Services PMI 9:00 AM ET — watch ISM; no CPI/PPI/FOMC today
- **Earnings BMO today:** None of note; next major event = NFP Thursday May 8 8:30 AM ET
- **Economic cycle:** mid-cycle (ISM Mfg 52.7, GDP +2.0%, stable unemployment, PCE inflation above 2%)
- **Sector YTD leaders:** Energy +26%+ (#1), Consumer Staples (+10.7%), Industrials (+9.6%), Materials — all classified Leading. Tech (XLK) worst YTD but recovering in April (+2% in April vs Energy -14% in April)
- **RS ranking (20-day vs SPY, strongest→weakest):** XLE, GLD, XLP, XLI, XLB, SLV, XLU, XLRE, EEM, HYG, SPY, IWM, XLV, XLF, QQQ, XLK, XLY, SOXX, XLC

### Position Updates

**NVDA ($198.54, -1.00% from entry $200.54):**
- AI thesis fully intact: Motley Fool targets $284 (25.4x FY28 EPS $11.20); hyperscalers remain supply-constrained; Blackwell/Rubin demand; earnings May 20
- CNBC: NVDA coverage positive — "massive run, setup still surprisingly tense"; AI spending exploding, 75% surge potential cited
- Surge from $165 → ~$200 since late March (+30%); ML models predict $205-217 range near-term
- Current -1.00% from entry — within noise; no thesis break; no action; stop $179.28 intact
- Risk: NVDA reports May 20 — within hold window; no pre-earnings cut needed yet

**XLE ($59.49, +3.36% from avg entry $57.5551):**
- 10-day MA crossed above 50-day MA on May 4 (bullish technical confirmation)
- Elliott Wave: incomplete bullish sequence, $75 target ahead
- Oil pullback today (-2%) = short-term noise; Brent still $113.50 (elevated); geopolitical premium intact
- Both stops locked at HWM $59.835 / stop $53.8515; XLE needs to set new HWM to trail higher
- Risk: EIA long-term forecast oil → $55 by end-2026 (far-dated, not actionable today)

### Trade Ideas

1. **TRADE: CAT (Caterpillar) — Industrials #3 on watchlist** ✓ PRIMARY
   - **Catalyst:** ISM Manufacturing 52.7 (expansion, highest since Aug 2022); ISM Services today — if expansion confirms, Industrials tailwind strong; CAT benefits from infrastructure spending + AI data center buildout (construction equipment)
   - **Entry:** Market at open, after ISM Services confirms ≥50 at 9 AM ET; pre-market ask ~$929
   - **Sizing:** 20 shares (~$18,580, ~18.5% equity) — within 17-20% target
   - **Stop:** 10% trailing GTC immediately on fill (~$840 initial stop)
   - **Target:** $1,000-1,050 (10-15% move); 2:1+ R:R
   - **Sector check:** Opens 3rd sector (Industrials); total sectors: Energy + Technology + Industrials ✓
   - **After entry:** Deployed ~55% (still below 75% floor — may need 4th position later this week)

2. **WATCH: XOM (ExxonMobil) — Energy #1 on watchlist** — Hold for Thursday or next week
   - Not today: oil pulling back -2%; VIX elevated; prefer ISM confirmation first
   - Max 1 more energy position allowed; currently 1 energy (XLE)
   - Re-evaluate Wednesday if oil stabilizes and VIX pulls back

3. **PASS: FCX (Freeport-McMoRan) — Materials #4 on watchlist**
   - Commodity cycle thesis valid but XLB neutral-positive; energy pullback creates read-through risk
   - Lower priority than CAT given sector ranking

### Risk Factors
- **VIX 18.51 → ~19:** Medium risk zone; elevated from prior week's 17-18 range — position sizing discipline critical
- **NFP Thursday May 8:** Named blocker; NO new entries Thursday; enter CAT today or Wednesday only
- **ISM Services 9 AM ET:** If below 50 = recession signal = thesis break for Industrials entry; abort CAT if ISM Services contracts
- **Oil pullback today (-2%):** Watch XLE if oil accelerates lower; -7% cut threshold = $53.49 (stop $53.85 covers it)
- **Deployment gap:** After CAT entry, deployed ~55% — still 20 points below 75% floor; need 4th position this week (Wednesday slot)
- **NVDA -1% from entry:** Not concerning; earnings May 20 is the next inflection

### Decision
**TRADE — enter CAT (Industrials) at market open.** Deployed 36.5%, no named 24h blocker (JOLTS/ISM Services ≠ named blockers), deployment floor rule mandatory. Confirm ISM Services ≥50 at 9 AM before placing order. 20 shares ~$18,580. Place 10% trailing stop GTC immediately on fill. Preserve 1 trade slot for Wednesday (XOM or 4th position). No entries Thursday (NFP blackout). Week count after CAT: 2/3.

### Afternoon Addendum (Midday Scan 2026-05-05)
- **ISM Services April 2026:** 53.8 — confirmed expansion; CAT entry thesis validated.
- **CAT midday:** $901.77 (+1.02% from entry $892.689; intraday HWM $908.90). Stop auto-trailed to $818.01. Day 1 thesis holding.
- **NVDA midday:** $197.57 (-1.48% from entry $200.54). Normal drift, no catalyst. AI thesis intact; hold through May 20 earnings.
- **XLE midday:** $59.555 (+3.48% from avg entry). Stops locked HWM $59.835 / stop $53.8515. Energy thesis intact.
- **Action:** None. No cuts, no stop tightening.
- **Deployment:** 54.4% — below 75-85% floor. Must enter 4th position Wednesday (last pre-NFP window). Candidates: XOM (energy slot 2) or FCX (Materials). Confirm oil stability + VIX Wednesday morning.

---

## 2026-05-15 — Pre-market Research (Friday, Week 3)

### Account Snapshot
- **Equity:** ~$104,427 (EOD May 14 baseline — Alpaca API blocked: cloud IP not in allowlist) | **Cash:** $25,099.51 (24.0%) | **Deployed:** ~$79,327 (75.97%)
- **Daytrade count:** 0 | **Phase P&L:** +$4,427 (+4.43%) | **Week trade count:** 2/3 (1 slot remaining — today Friday)
- **Positions:** 4 open — CAT (20sh @ $892.689), NVDA (95sh @ $200.54), XLK (103sh @ $175.494), XOM (130sh @ $150.769)
- **Trailing stops:** CAT aa646f6e (10%, HWM $931.35 / stop $838.215 locked) | NVDA daa6134f (7%, HWM ~$237.73 / stop ~$221.09 auto-trailing) | XLK 4299aece (10%, HWM $180.215 / stop $162.19) | XOM 4d9623bf (10%, HWM $153.12 / stop $137.807 locked)
- **API fallback:** Alpaca + Perplexity APIs blocked (host_not_allowed — cloud IP not in allowlist); used WebSearch fallback; live prices unconfirmed

### Market Context
- **WTI:** ~$102-105/bbl | **Brent:** ~$106.89/bbl — elevated; Hormuz disruption (~4M bbl/day drop) intact; energy thesis supported
- **S&P 500:** Closed at record **7,501.24** Thursday (+0.77%); premarket futures **-1.05%** (~-79pts to 7,446) — profit-taking after ATH; Nasdaq also hit ATH Thursday
- **VIX:** ~18.01 — moderate risk zone (15-25 normal); slightly improved from prior week's 18.51
- **Today's releases:** University of Michigan Consumer Sentiment (preliminary, 10:00 AM ET) — mild mover; NO CPI/NFP/FOMC today
- **Special event:** Jerome Powell's Fed Chair term ends today; Kevin Warsh (inflation hawk) expected Senate confirmation — bond market repricing risk; watch 10Y yield
- **Earnings BMO today:** Lighter calendar; no portfolio names reporting; NVDA earnings Wed May 20 (5 days out — key risk)
- **This week's catalysts driving the rally:** NVDA H200 China approval (+4.4% Thursday), Cisco guidance raise (+13.4% Thursday), US-China Beijing summit optimism, record S&P 7,501 and Dow 50,000 Thursday
- **Sector YTD leaders:** Energy, Industrials, Materials leading; Tech recovering on AI momentum; Semis, energy, defense, industrials driving market

### Position Premarket Levels (WebSearch estimates, unconfirmed)
| Ticker | EOD Close | Premarket Est. | Change | Stop | Status |
|--------|-----------|----------------|--------|------|--------|
| NVDA | $237.73 | ~$229.90 | -3.3% | 7% trail ~$221.09 | Safe — broad tech pullback |
| CAT | $918.51 | ~$897.09 | -2.3% | 10% trail $838.215 | Safe — market-wide pullback |
| XOM | $152.84 | ~$152-153 | flat | 10% trail $137.807 | Safe — oil elevated |
| XLK | $179.65 | est. ~$177 | ~-1.5% | 10% trail $162.19 | Safe — follows tech |

### Trade Ideas

1. **WATCH: FCX (Freeport-McMoRan) — Materials #4 on watchlist | Week 4 candidate**
   - **Catalyst:** Copper supercycle; ISM manufacturing expansion (52.7); AI data center + infrastructure copper demand
   - **Entry zone:** $45-48 on pullback to support; confirm Materials sector holds above XLB 50-day MA
   - **Sizing:** ~17-20% equity (~$17,700-$20,900 at current equity)
   - **Stop:** 10% trailing GTC immediately on fill
   - **Target:** $55-60 (15-25% move); 2:1+ R:R
   - **Sector check:** Opens Materials slot (sector 4); CAT=Industrials, NVDA/XLK=Tech, XOM=Energy — no conflict
   - **Today:** PASS — market pullback + NVDA earnings risk next week; set up for Week 4 Monday/Tuesday

2. **WATCH: SOXX (Semiconductor ETF) — 5th position candidate**
   - **Catalyst:** AI infrastructure supercycle; NVDA earnings May 20 as sector catalyst
   - **Risk:** Already 21% NVDA exposure; SOXX = compounding semi concentration pre-earnings; "sell the news" risk
   - **Today:** PASS — excess semi exposure; reassess post-NVDA earnings May 21+

3. **MONITOR: NVDA stop management**
   - +20% tighten trigger at $240.65 — NOT hit (premarket ~$229.90, well below)
   - If NVDA opens or trades ≥$240.65 intraday: cancel daa6134f, place 5% trailing GTC immediately
   - Premarket pullback makes $240.65 intraday unlikely; watch throughout session

### Risk Factors
- **NVDA earnings May 20 (5 days):** Largest position (21% equity, +18.54% unrealized). "Sell the news" risk elevated; 7% trail protects minimum $18.58/sh gain (~$1,765 locked profit floor)
- **Fed Chair transition today:** Warsh = hawk; bond market may reprice; 10Y yield could spike → tech multiple compression risk
- **S&P futures -1.05%:** Broad profit-taking after records; tech-led pullback in premarket
- **NVDA premarket -3.3%:** Pullback to ~$229.90; well above 7% stop (~$221); no stop-out risk, but notable reversal from $237.73
- **CAT premarket -2.3%:** Stop at $838.215 (safe); no thesis change

### Decision
**HOLD — do not use last trade slot (Week 2/3) today.**
- Deployed 75.97% (above 60% floor) → HOLD valid per strategy rules without named blocker
- Broad market pulling back after ATH; tech under pressure pre-open
- NVDA earnings May 20 = sector-wide risk event; avoid adding semi exposure
- Powell succession uncertainty = macro wild card today
- No fresh setup with compelling R:R in current risk environment
- **Carry 1 remaining slot to Week 4**; FCX primary candidate for Monday/Tuesday entry
- Monitor NVDA at $240.65 for 5% stop tighten; all other stops trail automatically
