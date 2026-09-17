param(
    [switch]$Embed
)

$ErrorActionPreference = "Stop"

# =========================
# 可修改参数
# =========================
$VaultRoot = "E:\5-newplanet\new planet"
$RefreshScript = Join-Path -Path $VaultRoot -ChildPath "scripts\02_refresh_llm_wikid.ps1"
$ResultRoot = Join-Path -Path $VaultRoot -ChildPath "result"
$RunTag = Get-Date -Format "yyyy-MM-dd_HHmmss"
$DayTag = Get-Date -Format "yyyy-MM-dd"
$LogPath = Join-Path -Path $ResultRoot -ChildPath "${RunTag}_wechat_auto_route_run.log"
$DailyManifestPath = Join-Path -Path $ResultRoot -ChildPath "${DayTag}_wechat_raw_auto_route_manifest.csv"
$RunManifestPath = Join-Path -Path $ResultRoot -ChildPath "${RunTag}_wechat_raw_auto_route_manifest.csv"

# =========================
# 线性执行流程
# =========================
New-Item -ItemType Directory -Force -Path $ResultRoot | Out-Null
Set-Location -LiteralPath $VaultRoot

Start-Transcript -LiteralPath $LogPath -Append

Write-Host ("[{0}] WeChat auto route started" -f (Get-Date -Format "yyyy-MM-dd HH:mm:ss"))
Write-Host ("Log: {0}" -f $LogPath)

if ($Embed) {
    & $RefreshScript -Embed
} else {
    & $RefreshScript
}

Copy-Item -LiteralPath $DailyManifestPath -Destination $RunManifestPath -Force
Write-Host ("Run manifest: {0}" -f $RunManifestPath)

Write-Host ("[{0}] WeChat auto route completed" -f (Get-Date -Format "yyyy-MM-dd HH:mm:ss"))

Stop-Transcript
