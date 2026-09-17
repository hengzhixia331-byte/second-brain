from pathlib import Path
from datetime import datetime
import csv
import json
import shutil


# =========================
# 可修改参数
# =========================
VAULT_ROOT = Path(r"E:\5-newplanet\new planet")
RAW_ROOT = VAULT_ROOT / "llm-wikid" / "raw"
RESULT_ROOT = VAULT_ROOT / "result"
WECHAT_CONFIG = VAULT_ROOT / ".obsidian" / "plugins" / "wechat-messenger" / "data.json"

RUN_TAG = datetime.now().strftime("%Y-%m-%d")

GROUP_TARGETS = {
    "学习AI": RAW_ROOT / "articles" / "学习AI",
    "生活": RAW_ROOT / "articles" / "生活",
    "科研": RAW_ROOT / "articles" / "科研",
    "股票": RAW_ROOT / "articles" / "股票",
    "赚钱想法": RAW_ROOT / "ideas" / "赚钱想法",
}

WECHAT_FOLDER_TEMPLATE = "llm-wikid/raw/{{{labels.0.name}}}"
WECHAT_ATTACHMENT_FOLDER = "llm-wikid/raw/assets"
WECHAT_IMAGE_FOLDER = "llm-wikid/raw/assets/images"

OLD_IMAGE_PREFIX = "笔记同步助手/images/"
OLD_ATTACHMENT_PREFIX = "笔记同步助手/attachments/"
NEW_IMAGE_PREFIX = "llm-wikid/raw/assets/images/"
NEW_ATTACHMENT_PREFIX = "llm-wikid/raw/assets/"


# =========================
# 线性迁移流程
# =========================
RESULT_ROOT.mkdir(parents=True, exist_ok=True)

manifest_rows = []
for group_name, target_dir in GROUP_TARGETS.items():
    source_dir = VAULT_ROOT / group_name
    target_dir.parent.mkdir(parents=True, exist_ok=True)

    for source_file in sorted(source_dir.rglob("*")):
        if source_file.is_file():
            relative_file = source_file.relative_to(source_dir)
            manifest_rows.append({
                "group": group_name,
                "source_path": str(source_file.relative_to(VAULT_ROOT)),
                "target_path": str((target_dir / relative_file).relative_to(VAULT_ROOT)),
                "bytes": source_file.stat().st_size,
            })

    shutil.move(str(source_dir), str(target_dir))

for md_path in sorted(RAW_ROOT.rglob("*.md")):
    text = md_path.read_text(encoding="utf-8")
    text = text.replace(OLD_IMAGE_PREFIX, NEW_IMAGE_PREFIX)
    text = text.replace(OLD_ATTACHMENT_PREFIX, NEW_ATTACHMENT_PREFIX)
    md_path.write_text(text, encoding="utf-8")

wechat_data = json.loads(WECHAT_CONFIG.read_text(encoding="utf-8"))
wechat_data["folder"] = WECHAT_FOLDER_TEMPLATE
wechat_data["attachmentFolder"] = WECHAT_ATTACHMENT_FOLDER
wechat_data["imageAttachmentFolder"] = WECHAT_IMAGE_FOLDER
WECHAT_CONFIG.write_text(json.dumps(wechat_data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

with (RESULT_ROOT / f"{RUN_TAG}_wechat_raw_migration_manifest.csv").open("w", encoding="utf-8-sig", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=["group", "source_path", "target_path", "bytes"])
    writer.writeheader()
    writer.writerows(manifest_rows)

print(f"Moved groups: {len(GROUP_TARGETS)}")
print(f"Moved files: {len(manifest_rows)}")
print(f"WeChat folder template: {WECHAT_FOLDER_TEMPLATE}")
