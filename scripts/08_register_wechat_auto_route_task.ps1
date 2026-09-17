param(
    [int]$IntervalMinutes = 15,
    [switch]$Embed,
    [switch]$Remove,
    [string]$TaskName = "NewPlanet WeChat Auto Route"
)

$ErrorActionPreference = "Stop"

# =========================
# 可修改参数
# =========================
$VaultRoot = "E:\5-newplanet\new planet"
$RunScript = Join-Path -Path $VaultRoot -ChildPath "scripts\07_run_wechat_auto_route_refined.ps1"

# =========================
# 线性执行流程
# =========================
if ($Remove) {
    $service = New-Object -ComObject Schedule.Service
    $service.Connect()
    $rootFolder = $service.GetFolder("\")
    $rootFolder.DeleteTask($TaskName, 0)
    Write-Host ("Removed scheduled task: {0}" -f $TaskName)
    return
}

$taskArguments = "-NoProfile -ExecutionPolicy Bypass -File `"$RunScript`""
if ($Embed) {
    $taskArguments = "$taskArguments -Embed"
}

$service = New-Object -ComObject Schedule.Service
$service.Connect()
$rootFolder = $service.GetFolder("\")
$taskDefinition = $service.NewTask(0)

$taskDefinition.RegistrationInfo.Description = "Run WeChat raw auto routing and refresh LLM Wikid."
$taskDefinition.Settings.Enabled = $true
$taskDefinition.Settings.StartWhenAvailable = $true
$taskDefinition.Settings.MultipleInstances = 2
$taskDefinition.Settings.DisallowStartIfOnBatteries = $false
$taskDefinition.Settings.StopIfGoingOnBatteries = $false

$trigger = $taskDefinition.Triggers.Create(1)
$trigger.StartBoundary = (Get-Date).AddMinutes(1).ToString("yyyy-MM-ddTHH:mm:ss")
$trigger.Enabled = $true
$trigger.Repetition.Interval = "PT${IntervalMinutes}M"
$trigger.Repetition.Duration = "P3650D"
$trigger.Repetition.StopAtDurationEnd = $false

$action = $taskDefinition.Actions.Create(0)
$action.Path = "powershell.exe"
$action.Arguments = $taskArguments
$action.WorkingDirectory = $VaultRoot

$rootFolder.RegisterTaskDefinition($TaskName, $taskDefinition, 6, $null, $null, 3) | Out-Null

Write-Host ("Registered scheduled task: {0}" -f $TaskName)
Write-Host ("Interval minutes: {0}" -f $IntervalMinutes)
Write-Host ("Embed enabled: {0}" -f [bool]$Embed)
