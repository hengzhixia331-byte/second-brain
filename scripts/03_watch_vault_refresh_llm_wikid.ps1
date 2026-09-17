$ErrorActionPreference = "Stop"

$VaultRoot = "E:\5-newplanet\new planet"
$RawRoot = Join-Path -Path $VaultRoot -ChildPath "llm-wikid\raw"
$RefreshScript = Join-Path -Path $VaultRoot -ChildPath "scripts\02_refresh_llm_wikid.ps1"
$PollSeconds = 15
$QuietSeconds = 60
$RunQmdEmbed = $false

# Only monitor raw markdown files that can enter the LLM Wikid compile chain
function Get-MonitoredMarkdownFiles {
    Get-ChildItem -LiteralPath $RawRoot -Recurse -File -Filter *.md |
        Sort-Object FullName -Unique
}

# Use path + size + modified time to build a stable snapshot
function Get-Snapshot {
    Get-MonitoredMarkdownFiles | ForEach-Object {
        "{0}|{1}|{2}" -f $_.FullName, $_.Length, $_.LastWriteTimeUtc.Ticks
    }
}

function Start-RefreshScript {
    $argumentList = "-NoProfile -ExecutionPolicy Bypass -File `"$RefreshScript`""
    if ($RunQmdEmbed) {
        $argumentList = "$argumentList -Embed"
    }
    $process = Start-Process -FilePath powershell.exe -WindowStyle Hidden -ArgumentList $argumentList -PassThru
    $process.WaitForExit()
}

function Write-Stamp {
    param([string]$Message)
    Write-Host ("[{0}] {1}" -f (Get-Date -Format "yyyy-MM-dd HH:mm:ss"), $Message)
}

Set-Location -LiteralPath $VaultRoot

$lastSnapshot = Get-Snapshot
$lastChange = Get-Date
$needsRefresh = $false

Write-Stamp "watcher started"

while ($true) {
    Start-Sleep -Seconds $PollSeconds

    $currentSnapshot = Get-Snapshot
    if (($currentSnapshot -join "`n") -ne ($lastSnapshot -join "`n")) {
        $lastSnapshot = $currentSnapshot
        $lastChange = Get-Date
        $needsRefresh = $true
        Write-Stamp "vault change detected"
    }

    if ($needsRefresh -and ((Get-Date) - $lastChange).TotalSeconds -ge $QuietSeconds) {
        Write-Stamp "refresh start"
        Start-RefreshScript
        $lastSnapshot = Get-Snapshot
        $lastChange = Get-Date
        $needsRefresh = $false
        Write-Stamp "refresh complete"
    }
}
