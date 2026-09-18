from pathlib import Path
from datetime import datetime
import csv
import json
import os
import shutil
import tempfile


# =========================
# 可修改参数
# =========================
VAULT_ROOT = Path(r"E:\5-newplanet\new planet")
RAW_ROOT = VAULT_ROOT / "llm-wikid" / "raw"
RESULT_ROOT = VAULT_ROOT / "result"
WORKSPACE_PATH = VAULT_ROOT / ".obsidian" / "workspace.json"

RUN_TAG = datetime.now().strftime("%Y-%m-%d_%H%M%S")


# =========================
# Obsidian 最近文件路径修复流程
# =========================
def normalized(relative_path):
    return str(relative_path).replace("\\", "/")


def vault_path(relative_path):
    return VAULT_ROOT / normalized(relative_path)


direct_path_map = {}

for manifest_path in sorted(RESULT_ROOT.glob("*wechat_raw_auto_route_manifest.csv")):
    with manifest_path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            target_path = normalized(row["target_path"])
            if target_path and vault_path(target_path).exists():
                direct_path_map[normalized(row["source_path"])] = target_path

for manifest_path in sorted(RESULT_ROOT.glob("*web_clipper_import_manifest.csv")):
    with manifest_path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            target_path = normalized(row["target_path"])
            if target_path and vault_path(target_path).exists():
                direct_path_map[normalized(row["source_path"])] = target_path
                direct_path_map[normalized(row["original_path"])] = target_path

raw_candidates_by_stem = {}
for raw_path in sorted(RAW_ROOT.rglob("*.md")):
    if not raw_path.name.endswith(".excalidraw.md"):
        raw_candidates_by_stem.setdefault(raw_path.stem, []).append(normalized(raw_path.relative_to(VAULT_ROOT)))

workspace = json.loads(WORKSPACE_PATH.read_text(encoding="utf-8"))
original_last_open_files = workspace["lastOpenFiles"]
repaired_last_open_files = []
seen_paths = set()
manifest_rows = []

for old_value in original_last_open_files:
    action = "kept"
    new_value = old_value
    candidate_count = ""

    if old_value.endswith(".md") and not vault_path(old_value).exists():
        normalized_old_value = normalized(old_value)

        if normalized_old_value in direct_path_map:
            new_value = direct_path_map[normalized_old_value]
            action = "replaced_by_manifest"
            candidate_count = 1
        else:
            candidates = raw_candidates_by_stem.get(Path(old_value).stem, [])
            candidate_count = len(candidates)
            if len(candidates) == 1:
                new_value = candidates[0]
                action = "replaced_by_unique_stem"
            else:
                new_value = ""
                action = "removed_missing_path"

    if new_value:
        if new_value not in seen_paths:
            repaired_last_open_files.append(new_value)
            seen_paths.add(new_value)
        else:
            action = "removed_duplicate"

    manifest_rows.append({
        "old_path": old_value,
        "new_path": new_value,
        "action": action,
        "candidate_count": candidate_count,
    })

workspace["lastOpenFiles"] = repaired_last_open_files
workspace_backup_path = WORKSPACE_PATH.with_suffix(".json.before-refresh")
shutil.copy2(WORKSPACE_PATH, workspace_backup_path)
with tempfile.NamedTemporaryFile(
    mode="w",
    encoding="utf-8",
    dir=WORKSPACE_PATH.parent,
    prefix="workspace.",
    suffix=".tmp",
    delete=False,
) as handle:
    handle.write(json.dumps(workspace, ensure_ascii=False, indent=2) + "\n")
    temporary_workspace_path = Path(handle.name)
os.replace(temporary_workspace_path, WORKSPACE_PATH)

manifest_path = RESULT_ROOT / f"{RUN_TAG}_obsidian_workspace_path_repair_manifest.csv"
with manifest_path.open("w", encoding="utf-8-sig", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=["old_path", "new_path", "action", "candidate_count"])
    writer.writeheader()
    writer.writerows(manifest_rows)

replaced_count = len([row for row in manifest_rows if row["action"].startswith("replaced")])
removed_count = len([row for row in manifest_rows if row["action"].startswith("removed")])

print(f"Workspace lastOpenFiles before: {len(original_last_open_files)}")
print(f"Workspace lastOpenFiles after: {len(repaired_last_open_files)}")
print(f"Replaced stale paths: {replaced_count}")
print(f"Removed stale paths: {removed_count}")
print(f"Workspace backup: {workspace_backup_path.relative_to(VAULT_ROOT)}")
print(f"Manifest: {manifest_path.relative_to(VAULT_ROOT)}")
