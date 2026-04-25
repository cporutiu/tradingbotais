#Requires -Version 5.1
#Requires -RunAsAdministrator
<#
.SYNOPSIS
    Registers all TradingBotAIS routines as Windows Task Scheduler tasks.
    Run once from an elevated PowerShell prompt.

.NOTES
    All times are Eastern Time (ET). The tasks run Monday-Friday.
    To remove all tasks: Get-ScheduledTask -TaskName "TradingBot-*" | Unregister-ScheduledTask -Confirm:$false
#>

$ProjectRoot = "c:\Users\Cipru\OneDrive - Picksur LLC\Documents\AIPROJECTS\TradingBotAIS"
$LauncherScript = Join-Path $ProjectRoot "scripts\run_routine.ps1"
$PS = "powershell.exe"

$tasks = @(
    @{ Name = "TradingBot-PreMarket";    Routine = "pre-market";    Time = "07:00"; Days = "Monday","Tuesday","Wednesday","Thursday","Friday" },
    @{ Name = "TradingBot-MarketOpen";   Routine = "market-open";   Time = "09:30"; Days = "Monday","Tuesday","Wednesday","Thursday","Friday" },
    @{ Name = "TradingBot-Midday";       Routine = "midday";        Time = "13:00"; Days = "Monday","Tuesday","Wednesday","Thursday","Friday" },
    @{ Name = "TradingBot-DailySummary"; Routine = "daily-summary"; Time = "16:00"; Days = "Monday","Tuesday","Wednesday","Thursday","Friday" },
    @{ Name = "TradingBot-WeeklyReview"; Routine = "weekly-review"; Time = "17:00"; Days = "Friday" }
)

foreach ($t in $tasks) {
    $args = "-NonInteractive -ExecutionPolicy Bypass -File `"$LauncherScript`" -Routine $($t.Routine)"
    $action   = New-ScheduledTaskAction -Execute $PS -Argument $args -WorkingDirectory $ProjectRoot
    $trigger  = New-ScheduledTaskTrigger -Weekly -WeeksInterval 1 -DaysOfWeek $t.Days -At $t.Time
    $settings = New-ScheduledTaskSettingsSet `
        -ExecutionTimeLimit (New-TimeSpan -Hours 1) `
        -StartWhenAvailable `
        -WakeToRun:$false `
        -MultipleInstances IgnoreNew
    $principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive -RunLevel Limited

    Register-ScheduledTask `
        -TaskName  $t.Name `
        -Action    $action `
        -Trigger   $trigger `
        -Settings  $settings `
        -Principal $principal `
        -Force | Out-Null

    Write-Host "Registered: $($t.Name)  ->  $($t.Time) ET on $($t.Days -join ', ')"
}

Write-Host ""
Write-Host "All tasks registered. Verify with:"
Write-Host "  Get-ScheduledTask -TaskName 'TradingBot-*' | Select TaskName,State"
Write-Host ""
Write-Host "To run a task immediately for testing:"
Write-Host "  Start-ScheduledTask -TaskName 'TradingBot-PreMarket'"
Write-Host ""
Write-Host "To remove all tasks:"
Write-Host "  Get-ScheduledTask -TaskName 'TradingBot-*' | Unregister-ScheduledTask -Confirm:`$false"
