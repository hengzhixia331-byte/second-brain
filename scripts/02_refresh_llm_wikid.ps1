param(
    [switch]$Embed
)

$ErrorActionPreference = "Stop"

$VaultRoot = "E:\5-newplanet\new planet"
$WebClipperScript = Join-Path -Path $VaultRoot -ChildPath "scripts\09_import_web_clipper_to_wikid_raw.py"
$RouteScript = Join-Path -Path $VaultRoot -ChildPath "scripts\06_auto_route_wechat_raw_refined.py"
$PythonScript = Join-Path -Path $VaultRoot -ChildPath "scripts\01_organize_existing_notes_to_llm_wikid.py"
$WorkspaceRepairScript = Join-Path -Path $VaultRoot -ChildPath "scripts\10_repair_obsidian_workspace_paths.py"

Set-Location -LiteralPath $VaultRoot
python $WebClipperScript
python $RouteScript
python $PythonScript
python $WorkspaceRepairScript
qmd update

if ($Embed) {
    qmd embed
}
