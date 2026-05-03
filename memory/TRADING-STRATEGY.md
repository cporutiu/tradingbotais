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
11. Patience > activity — **valid only when deployed ≥60% OR a named blocker exists**

## Deployment Floor — Enforced

Default is **TRADE** when all of the following are true:
- Deployed capital < 40%, AND
- No named blocking catalyst within 24h (qualifying blockers: earnings BMO/AMC for a held name, NFP, CPI, GDP Advance, FOMC decision)

"General uncertainty," "earnings next week," and "oil could reverse" do NOT qualify as blockers.

**Wednesday urgency check:** If ≥2 trade slots unused at Wednesday close AND deployed < 60%, open at least 1 position Thursday — NFP/same-day earnings caveat still applies.

## Sector Diversification Rules
- Max 2 positions in any single sector
- When ≥3 positions open, must span ≥2 sectors
- Each weekly review assigns a ranked sector watchlist + 1 candidate ticker per sector for the upcoming week; Monday pre-market must arrive with 2-3 live setups, not 1 idea and vague "watch X"

## Sector Watchlist (update each Friday in WEEKLY-REVIEW.md)
| Priority | Sector | ETF | Candidate | Condition to Enter |
|----------|--------|-----|-----------|-------------------|
| 1 | Energy | XLE | XOM | Hold until oil thesis breaks; max 1 more energy position |
| 2 | Technology | XLK | NVDA | Post-Mag-7 cleared; AI momentum; entry on dip to support |
| 3 | Industrials | XLI | CAT | ISM expansion confirmed; macro tailwind |
| 4 | Materials | XLB | FCX | Commodity cycle; enter only if energy thesis weakens |

## Entry Checklist
- Specific catalyst?
- Sector in momentum AND on ranked watchlist?
- Deployment check: is deployed < 40% with no named blocker? → TRADE default
- Position sizing: 17-20% of current equity
- Stop level: 10% trailing GTC, placed immediately on fill
- Target: min 2:1 R:R
- Sector cap: does this keep me at ≤2 positions in this sector?
