from pathlib import Path
from datetime import datetime
import csv
import re
import shutil


# =========================
# 可修改参数
# =========================
VAULT_ROOT = Path(r"E:\5-newplanet\new planet")
RAW_ROOT = VAULT_ROOT / "llm-wikid" / "raw"
RESULT_ROOT = VAULT_ROOT / "result"

RUN_TAG = datetime.now().strftime("%Y-%m-%d")

CANONICAL_RAW_DIRS = {
    "articles",
    "bookmarks",
    "ideas",
    "papers",
    "clippings",
    "assets",
    "x-archive",
}

TOPIC_ALIASES = [
    ("股票", ["股票", "股市", "a股", "证券", "券商", "基金", "财经", "金融", "两融", "投资", "etf", "st"]),
    ("科研", ["科研", "植物", "玉米", "育种", "转化", "抗逆", "表型", "生信", "论文", "nature", "science", "cell"]),
    ("学习AI", ["学习ai", "ai", "chatgpt", "codex", "claude", "提示词", "模型", "智能体"]),
    ("生活", ["生活", "健康", "疫苗", "小宝", "宝宝", "乙肝"]),
    ("赚钱想法", ["赚钱", "商业", "副业", "餐饮", "品牌", "推广", "生图"]),
]

ARTICLE_KIND_KEYWORDS = [
    "mp.weixin.qq.com",
    "微信公众号",
    "公众号",
    "originalurl",
    "## 正文",
    "来源",
]

BOOKMARK_KIND_KEYWORDS = [
    "http://",
    "https://",
]


# =========================
# 线性自动路由流程
# =========================
def strip_frontmatter(text):
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) == 3:
            return parts[2].strip()
    return text.strip()


def normalize_repeated_label(label):
    cleaned = label.strip()
    half_length = len(cleaned) // 2
    if len(cleaned) % 2 == 0 and cleaned[:half_length] == cleaned[half_length:]:
        return cleaned[:half_length]
    return cleaned


def compact_haystack(path, text):
    body = strip_frontmatter(text)
    return f"{path.as_posix()} {path.stem} {text[:5000]} {body[:5000]}".lower()


def contains_any(text, keywords):
    return any(keyword.lower() in text for keyword in keywords)


def infer_topic(raw_label, haystack):
    label = normalize_repeated_label(raw_label)
    combined = f"{label} {haystack}".lower()
    for topic, keywords in TOPIC_ALIASES:
        if contains_any(combined, keywords):
            return topic
    return label if label else "未分类"


def infer_source_kind(topic, haystack, body_length):
    if contains_any(haystack, ARTICLE_KIND_KEYWORDS) and body_length >= 800:
        return "articles"
    if topic == "赚钱想法" and not contains_any(haystack, ARTICLE_KIND_KEYWORDS):
        return "ideas"
    if contains_any(haystack, BOOKMARK_KIND_KEYWORDS) and body_length < 800:
        return "bookmarks"
    return "articles"


def infer_article_subdirs(topic, haystack):
    if topic == "股票":
        if contains_any(haystack, ["两融", "融资融券", "仓位", "技术面", "复盘"]):
            return ["股票", "大牛博主学思路"]
        if contains_any(haystack, ["挖矿", "矿"]):
            return ["股票", "挖矿人"]
        return ["股票", "前沿消息"]

    if topic == "科研":
        if contains_any(haystack, ["表型", "ucaa", "cornpheno", "成像", "叶温", "多光谱"]):
            return ["科研", "科研工具", "高温表型工具"]
        if contains_any(haystack, ["wgcna", "pca", "转录组", "生信", "bulk", "rna"]):
            return ["科研", "科研工具", "生信工具"]
        if contains_any(haystack, ["转化", "crispr", "cas", "编辑", "novocast"]):
            return ["科研", "玉米遗传转化"]
        if contains_any(haystack, ["耐盐", "耐旱", "耐热", "抗逆", "胁迫", "环状dna"]):
            return ["科研", "植物抗逆", "抗逆机制"]
        if contains_any(haystack, ["育种", "产量", "高蛋白", "授粉", "玉米"]):
            return ["科研", "育种改良"]
        return ["科研", "待细分"]

    return [topic]


def target_directory_for(source_kind, topic, haystack):
    if source_kind == "articles":
        return RAW_ROOT / "articles" / Path(*infer_article_subdirs(topic, haystack))
    if source_kind == "bookmarks":
        return RAW_ROOT / "bookmarks" / topic
    return RAW_ROOT / "ideas" / topic


def remove_empty_parents(start_dir):
    current = start_dir
    while current != RAW_ROOT:
        if any(current.iterdir()):
            break
        current.rmdir()
        current = current.parent


RESULT_ROOT.mkdir(parents=True, exist_ok=True)

manifest_rows = []
for source_path in sorted(RAW_ROOT.rglob("*.md")):
    relative_parts = source_path.relative_to(RAW_ROOT).parts
    first_dir = relative_parts[0]

    if first_dir in CANONICAL_RAW_DIRS:
        continue

    text = source_path.read_text(encoding="utf-8")
    body = strip_frontmatter(text)
    haystack = compact_haystack(source_path.relative_to(RAW_ROOT), text)
    raw_label = normalize_repeated_label(first_dir)
    topic = infer_topic(raw_label, haystack)
    source_kind = infer_source_kind(topic, haystack, len(body))
    target_dir = target_directory_for(source_kind, topic, haystack)
    target_path = target_dir / source_path.name

    target_dir.mkdir(parents=True, exist_ok=True)
    shutil.move(str(source_path), str(target_path))
    remove_empty_parents(source_path.parent)

    manifest_rows.append({
        "source_path": str(source_path.relative_to(VAULT_ROOT)),
        "target_path": str(target_path.relative_to(VAULT_ROOT)),
        "raw_label": raw_label,
        "source_kind": source_kind,
        "topic": topic,
        "body_length": len(body),
    })

with (RESULT_ROOT / f"{RUN_TAG}_wechat_raw_auto_route_manifest.csv").open("w", encoding="utf-8-sig", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=[
        "source_path",
        "target_path",
        "raw_label",
        "source_kind",
        "topic",
        "body_length",
    ])
    writer.writeheader()
    writer.writerows(manifest_rows)

print(f"Auto-routed raw notes: {len(manifest_rows)}")
print(f"Manifest: result/{RUN_TAG}_wechat_raw_auto_route_manifest.csv")
