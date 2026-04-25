#Requires -Version 5.1
<#
.SYNOPSIS
    Launches a TradingBotAIS routine via Claude Code non-interactively.

.PARAMETER Routine
    Name of the routine to run: pre-market, market-open, midday, daily-summary, weekly-review

.EXAMPLE
    powershell -File scripts\run_routine.ps1 -Routine pre-market
#>
param(
    [Parameter(Mandatory=$true)]
    [ValidateSet('pre-market','market-open','midday','daily-summary','weekly-review')]
    [string]$Routine
)

$ProjectRoot = "c:\Users\Cipru\OneDrive - Picksur LLC\Documents\AIPROJECTS\TradingBotAIS"
Set-Location $ProjectRoot

# Resolve claude.exe from the versioned package install directory (picks latest version automatically)
$ClaudeBase = "$env:LOCALAPPDATA\Packages\Claude_pzs8sxrjxfjjc\LocalCache\Roaming\Claude\claude-code"
$ClaudePath = Get-ChildItem $ClaudeBase -Directory -ErrorAction SilentlyContinue |
    Sort-Object Name -Descending |
    Select-Object -First 1 |
    ForEach-Object { Join-Path $_.FullName "claude.exe" }
if (-not $ClaudePath -or -not (Test-Path $ClaudePath)) {
    Write-Error "claude.exe not found under $ClaudeBase - is Claude desktop installed?"
    exit 1
}

# Load .env into process environment so Claude and all bash subprocesses inherit the vars
$EnvFile = Join-Path $ProjectRoot ".env"
if (Test-Path $EnvFile) {
    Get-Content $EnvFile | Where-Object { ($_ -notmatch '^\s*#') -and ($_ -match '=') -and ($_ -match '\S') } | ForEach-Object {
        $parts = $_ -split '=', 2
        $key   = $parts[0].Trim()
        $val   = $parts[1].Trim().Trim('"').Trim("'")
        if ($key) {
            [System.Environment]::SetEnvironmentVariable($key, $val, 'Process')
        }
    }
} else {
    Write-Error ".env not found at $EnvFile - aborting."
    exit 1
}

# Ensure .tmp exists for logs
$TmpDir = Join-Path $ProjectRoot ".tmp"
if (-not (Test-Path $TmpDir)) { New-Item -ItemType Directory -Path $TmpDir | Out-Null }

$Timestamp  = Get-Date -Format 'yyyy-MM-dd_HH-mm'
$LogFile    = Join-Path $TmpDir "routine_${Routine}_${Timestamp}.txt"
$StartTime  = Get-Date -Format 'HH:mm:ss'

Write-Host "[$StartTime] Starting $Routine routine..."

# Feed the routine file to claude -p (non-interactive print mode)
$RoutineFile = Join-Path $ProjectRoot "routines\$Routine.md"
$Prompt = Get-Content -Raw $RoutineFile
$Prompt | & $ClaudePath -p --dangerously-skip-permissions - | Tee-Object -FilePath $LogFile

$EndTime = Get-Date -Format 'HH:mm:ss'
Write-Host "[$EndTime] $Routine complete. Log: $LogFile"
