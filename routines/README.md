# Routines

The five `.md` files in this folder are the scheduled workflow prompts. They are fed to `claude -p` (non-interactive) on each run, whether via Windows Task Scheduler (local, active) or Claude Code cloud routines (archived, restorable).

---

## Local Execution — Windows Task Scheduler (Active)

### How it works
1. Windows Task Scheduler fires at the scheduled time and calls `scripts/run_routine.ps1 -Routine <name>`.
2. The launcher loads `.env` into the process environment, then pipes the routine `.md` file to `claude -p -`.
3. Claude runs non-interactively, executes all steps, and logs output to `.tmp/routine_<name>_<timestamp>.txt`.

### Schedule (Eastern Time)

| Routine | Task Name | Time (ET) | Days |
|---|---|---|---|
| pre-market | TradingBot-PreMarket | 07:00 | Mon–Fri |
| market-open | TradingBot-MarketOpen | 09:30 | Mon–Fri |
| midday | TradingBot-Midday | 13:00 | Mon–Fri |
| daily-summary | TradingBot-DailySummary | 16:00 | Mon–Fri |
| weekly-review | TradingBot-WeeklyReview | 17:00 | Friday |

### First-time setup

Run once from an **elevated** PowerShell prompt:
```powershell
powershell -ExecutionPolicy Bypass -File "scripts\setup_tasks.ps1"
```

### Verify tasks are registered
```powershell
Get-ScheduledTask -TaskName "TradingBot-*" | Select TaskName, State
```

### Run a task immediately (for testing)
```powershell
Start-ScheduledTask -TaskName "TradingBot-PreMarket"
```

### Check last run result
```powershell
Get-ScheduledTaskInfo -TaskName "TradingBot-PreMarket" | Select LastRunTime, LastTaskResult
# LastTaskResult 0 = success
```

### Remove all tasks
```powershell
Get-ScheduledTask -TaskName "TradingBot-*" | Unregister-ScheduledTask -Confirm:$false
```

---

## Action Questions — User Feedback Loop

ClickUp is **write-only** for the bot. Answers posted as ClickUp comments are never read by any routine.

### Correct workflow
1. **EOD daily-summary** appends action questions to the TRADE-LOG.md EOD entry and posts them to ClickUp for visibility.
2. **User answers** in an interactive Claude Code session (chat). Claude logs the decisions as a `**User decisions (YYYY-MM-DD):**` block directly below the action questions in TRADE-LOG.md and commits/pushes.
3. **Pre-market STEP 1B** reads the most recent `**User decisions**` block and carries confirmed instructions forward into the day's plan and RESEARCH-LOG watch items.

### User decisions block format (TRADE-LOG.md)
```
**User decisions (YYYY-MM-DD):**
- Q1: <decision text>
- Q2: <decision text>
```

---

## Cloud Routine Setup (Preserved — Alternative)

The original approach used Claude Code cloud routines. Every env var was injected by the routine config; there was no `.env` file in the repo. To restore this approach:

### Cron Schedules (America/Chicago)

| Routine | File | Cron |
|---|---|---|
| Pre-market research | pre-market.md | `0 6 * * 1-5` |
| Market-open execution | market-open.md | `30 8 * * 1-5` |
| Midday scan | midday.md | `0 12 * * 1-5` |
| Daily summary | daily-summary.md | `0 15 * * 1-5` |
| Weekly review | weekly-review.md | `0 16 * * 5` |

### Required Environment Variables (set on the routine, NOT in .env)

- ALPACA_API_KEY
- ALPACA_SECRET_KEY
- ALPACA_ENDPOINT (optional; defaults to live URL)
- ALPACA_DATA_ENDPOINT (optional; defaults to data URL)
- PERPLEXITY_API_KEY
- PERPLEXITY_MODEL (optional; defaults to sonar)
- CLICKUP_API_KEY
- CLICKUP_WORKSPACE_ID
- CLICKUP_CHANNEL_ID

### Critical Setup Steps

1. Install Claude GitHub App on this repo
2. Enable "Allow unrestricted branch pushes" on every routine's environment
3. Set env vars on the routine — never in a committed .env file
4. Revert the routine `.md` files: change the ENVIRONMENT VARIABLES block back to the "ALREADY exported as process env var / NO .env file" wording, and change PERSISTENCE back to "Fresh clone. File changes VANISH."
