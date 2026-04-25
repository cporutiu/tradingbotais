# Cloud Routines

Paste each prompt verbatim into its Claude Code cloud routine. Do not paraphrase.

## Cron Schedules (America/Chicago)

| Routine | File | Cron |
|---------|------|------|
| Pre-market research | pre-market.md | `0 6 * * 1-5` |
| Market-open execution | market-open.md | `30 8 * * 1-5` |
| Midday scan | midday.md | `0 12 * * 1-5` |
| Daily summary | daily-summary.md | `0 15 * * 1-5` |
| Weekly review | weekly-review.md | `0 16 * * 5` |

## Required Environment Variables (set on routine, NOT in .env)

- ALPACA_API_KEY
- ALPACA_SECRET_KEY
- ALPACA_ENDPOINT (optional; defaults to live URL)
- ALPACA_DATA_ENDPOINT (optional; defaults to data URL)
- PERPLEXITY_API_KEY
- PERPLEXITY_MODEL (optional; defaults to sonar)
- CLICKUP_API_KEY
- CLICKUP_WORKSPACE_ID
- CLICKUP_CHANNEL_ID

## Critical Setup Steps

1. Install Claude GitHub App on this repo
2. Enable "Allow unrestricted branch pushes" on every routine's environment
3. Set env vars on the routine — never in a committed .env file
