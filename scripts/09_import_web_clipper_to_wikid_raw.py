from pathlib import Path
from datetime import datetime
import csv
import shutil


# =========================
# 可修改参数
# =========================
VAULT_ROOT = Path(r"E:\5-newplanet\new planet")
WEB_CLIPPER_INBOX = VAULT_ROOT / "Clippings"
WIKID_CLIPPINGS = VAULT_ROOT / "llm-wikid" / "raw" / "clippings"
RESULT_ROOT = VAULT_ROOT / "result"

TODAY = datetime.now().strftime("%Y-%m-%d")
NOW = datetime.now().strftime("%Y-%m-%d %H:%M")
RUN_TAG = datetime.now().strftime("%Y-%m-%d_%H%M%S")

CRITERIA_NOTE_NAME = "Web Clipper Classification Rules.md"
CRITERIA_NOTE_LINK = "[[Web Clipper Classification Rules]]"

CATEGORY_RULES = [
    {
        "slug": "plant_stress_resilience",
        "label": "Plant Science - Stress Resilience",
        "folder": "plant_stress_resilience",
        "concept": "Plant Stress Resilience",
        "tags": ["web-clipper", "wikid-raw", "plant-science", "stress", "physiology"],
        "keywords": [
            "抗逆", "耐旱", "干旱", "耐盐", "盐胁迫", "盐碱", "耐热", "耐高温", "高温胁迫",
            "热胁迫", "耐寒", "低温", "冷胁迫", "高光", "光抑制", "渗透调节", "活性氧",
            "drought", "salt stress", "heat stress", "cold stress", "photoinhibition", "oxidative stress",
        ],
        "criteria": "植物逆境生理、抗旱、耐盐、耐热、耐寒、高光或渗透/氧化胁迫机制。",
    },
    {
        "slug": "maize_genetic_transformation",
        "label": "Maize Genetic Transformation",
        "folder": "maize_genetic_transformation",
        "concept": "Maize Genetic Transformation",
        "tags": ["web-clipper", "wikid-raw", "plant-science", "maize", "genetic-transformation"],
        "keywords": [
            "玉米转化", "遗传转化", "转化率", "基因编辑", "愈伤", "农杆菌", "组织培养",
            "crispr", "cas", "genome editing", "transformation", "maize transformation", "callus", "agrobacterium",
        ],
        "criteria": "植物遗传转化、玉米转化体系、CRISPR/Cas 编辑、组织培养或转化效率优化。",
    },
    {
        "slug": "maize_yield_and_breeding",
        "label": "Maize Yield and Breeding",
        "folder": "maize_yield_and_breeding",
        "concept": "Maize Yield and Breeding",
        "tags": ["web-clipper", "wikid-raw", "plant-science", "maize", "breeding", "yield"],
        "keywords": [
            "玉米", "育种", "产量", "高产", "高蛋白", "籽粒", "穗", "授粉", "氮肥", "品种",
            "maize", "corn", "breeding", "yield", "grain", "kernel", "pollination",
        ],
        "criteria": "玉米产量、籽粒、授粉、育种改良、品质性状或品种评价。",
    },
    {
        "slug": "plant_phenotyping_and_imaging",
        "label": "Plant Phenotyping and Imaging",
        "folder": "plant_phenotyping_and_imaging",
        "concept": "Plant Phenotyping and Imaging",
        "tags": ["web-clipper", "wikid-raw", "plant-science", "phenotyping", "imaging"],
        "keywords": [
            "表型", "成像", "多光谱", "高光谱", "叶温", "冠层", "颜色面积", "图像分析",
            "phenotype", "phenotyping", "imaging", "multispectral", "hyperspectral", "canopy",
            "leaf temperature", "ucaa", "cornpheno",
        ],
        "criteria": "植物表型组学、图像/光谱采集、叶温、颜色面积、冠层或考种工具。",
    },
    {
        "slug": "bioinformatics_analysis",
        "label": "Bioinformatics Analysis",
        "folder": "bioinformatics_analysis",
        "concept": "Bioinformatics Analysis",
        "tags": ["web-clipper", "wikid-raw", "bioinformatics", "omics", "analysis"],
        "keywords": [
            "生信", "转录组", "基因组", "遗传力", "全基因组", "差异表达", "富集", "群体遗传",
            "gwas", "snp", "gcta", "greml", "heritability", "rna-seq", "rnaseq", "wgcna", "pca",
            "deseq2", "edger", "blast", "genome", "transcriptome", "single-cell", "bulk",
        ],
        "criteria": "生物信息学分析、组学数据、GWAS/SNP、RNA-seq、WGCNA、PCA 或统计遗传工具。",
    },
    {
        "slug": "ai_for_research",
        "label": "AI for Research",
        "folder": "ai_for_research",
        "concept": "AI for Research",
        "tags": ["web-clipper", "wikid-raw", "ai", "research-tools"],
        "keywords": [
            "人工智能", "大模型", "提示词", "智能体", "自动化", "ai", "chatgpt", "gpt",
            "claude", "codex", "prompt", "llm", "agent", "vibecoding",
        ],
        "criteria": "AI 工具、大模型、科研自动化、提示词、Agent 或代码自动化。",
    },
    {
        "slug": "research_tools_and_methods",
        "label": "Research Tools and Methods",
        "folder": "research_tools_and_methods",
        "concept": "Research Tools and Methods",
        "tags": ["web-clipper", "wikid-raw", "research", "tools", "methods"],
        "keywords": [
            "工具", "方法", "教程", "流程", "软件", "平台", "protocol", "method", "methods",
            "tutorial", "pipeline", "software", "tool", "nature methods", "biorxiv",
        ],
        "criteria": "通用科研工具、方法学、软件平台、教程、流程或 protocol。",
    },
    {
        "slug": "finance_and_investment",
        "label": "Finance and Investment",
        "folder": "finance_and_investment",
        "concept": "Finance and Investment",
        "tags": ["web-clipper", "wikid-raw", "finance", "investment"],
        "keywords": [
            "股票", "股市", "a股", "美股", "证券", "券商", "财经", "金融", "投资", "两融",
            "市场", "行情", "stock", "finance", "investment", "market", "trading",
        ],
        "criteria": "股票、证券、宏观市场、产业投资、两融、财经分析或交易策略。",
    },
    {
        "slug": "life_and_health",
        "label": "Life and Health",
        "folder": "life_and_health",
        "concept": "Life and Health",
        "tags": ["web-clipper", "wikid-raw", "life", "health"],
        "keywords": [
            "生活", "健康", "疫苗", "宝宝", "小宝", "育儿", "医疗", "疾病", "护理",
            "health", "medical", "vaccine", "parenting", "baby",
        ],
        "criteria": "生活健康、疫苗、育儿、医疗护理或日常健康知识。",
    },
    {
        "slug": "career_and_business_ideas",
        "label": "Career and Business Ideas",
        "folder": "career_and_business_ideas",
        "concept": "Career and Business Ideas",
        "tags": ["web-clipper", "wikid-raw", "career", "business"],
        "keywords": [
            "赚钱", "副业", "变现", "商业", "品牌", "推广", "求职", "简历", "面试",
            "business", "brand", "monetization", "career", "job", "side project",
        ],
        "criteria": "赚钱想法、副业、品牌内容、商业模式、求职转型或个人发展。",
    },
]

DEFAULT_RULE = {
    "slug": "general_reference",
    "label": "General Reference",
    "folder": "general_reference",
    "concept": "Uncategorized Notes",
    "tags": ["web-clipper", "wikid-raw", "uncategorized"],
    "keywords": [],
    "criteria": "没有命中上面规则的网页剪藏，先保留为待复核资料。",
}

WIKID_FIELD_PREFIXES = [
    "wikid_source:",
    "wikid_raw_inbox:",
    "wikid_auto_category:",
    "wikid_category_label:",
    "wikid_category_folder:",
    "wikid_concept:",
    "wikid_classification_basis:",
    "wikid_classified_at:",
    "wikid_category_tags:",
]

AUTO_BLOCK_START = "<!-- wikid-web-clipper-auto-classification:start -->"
AUTO_BLOCK_END = "<!-- wikid-web-clipper-auto-classification:end -->"


# =========================
# 线性导入与分类流程
# =========================
def yaml_quote(value):
    return '"' + str(value).replace('"', "'") + '"'


def yaml_list(values):
    return "[" + ", ".join(values) + "]"


def split_frontmatter(text):
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) == 3:
            return parts[1].strip("\n"), parts[2].lstrip("\n")
    return "", text


def first_heading_or_stem(path, body):
    for line in body.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem


def score_rule(haystack, rule):
    hits = []
    for keyword in rule["keywords"]:
        if keyword.lower() in haystack:
            hits.append(keyword)
    return len(hits), hits


def classify_clip(path, text):
    frontmatter, body = split_frontmatter(text)
    haystack = f"{path.as_posix()} {path.stem} {frontmatter} {body[:5000]}".lower()
    scored = []
    for index, rule in enumerate(CATEGORY_RULES):
        score, hits = score_rule(haystack, rule)
        scored.append((score, -index, rule, hits))
    scored.sort(reverse=True)
    best_score, _, best_rule, best_hits = scored[0]
    if best_score == 0:
        return DEFAULT_RULE, ["no deterministic keyword hit"]
    return best_rule, best_hits


def update_frontmatter(path, text, rule, hits):
    frontmatter, body = split_frontmatter(text)
    title = first_heading_or_stem(path, body)
    frontmatter_lines = []

    if frontmatter:
        for line in frontmatter.splitlines():
            if not any(line.startswith(prefix) for prefix in WIKID_FIELD_PREFIXES):
                frontmatter_lines.append(line)
    else:
        frontmatter_lines.append(f"title: {yaml_quote(title)}")

    concept_link = f"[[{rule['concept']}]]"
    basis = "matched keywords: " + ", ".join(hits)
    frontmatter_lines.extend([
        "wikid_source: web-clipper",
        "wikid_raw_inbox: clippings",
        f"wikid_auto_category: {rule['slug']}",
        f"wikid_category_label: {yaml_quote(rule['label'])}",
        f"wikid_category_folder: {rule['folder']}",
        f"wikid_concept: {yaml_quote(concept_link)}",
        f"wikid_classification_basis: {yaml_quote(basis)}",
        f"wikid_classified_at: {yaml_quote(NOW)}",
        f"wikid_category_tags: {yaml_list(rule['tags'])}",
    ])

    return "---\n" + "\n".join(frontmatter_lines) + "\n---\n" + body


def update_auto_block(text, rule, hits):
    concept_link = f"[[{rule['concept']}]]"
    basis = "matched keywords: " + ", ".join(hits)
    block = "\n".join([
        AUTO_BLOCK_START,
        "",
        "## Auto Classification",
        f"- Category: {rule['label']}",
        f"- Concept: {concept_link}",
        f"- Basis: {basis}",
        f"- Classified at: {NOW}",
        f"- Rule source: {CRITERIA_NOTE_LINK}",
        "",
        AUTO_BLOCK_END,
        "",
    ])

    if AUTO_BLOCK_START in text and AUTO_BLOCK_END in text:
        before = text.split(AUTO_BLOCK_START, 1)[0].rstrip()
        after = text.split(AUTO_BLOCK_END, 1)[1].lstrip()
        return before + "\n\n" + block + after

    return text.rstrip() + "\n\n" + block


def unique_path(path):
    if not path.exists():
        return path

    stem = path.stem
    suffix = path.suffix
    parent = path.parent
    index = 2
    candidate = parent / f"{stem}_{index}{suffix}"
    while candidate.exists():
        index += 1
        candidate = parent / f"{stem}_{index}{suffix}"
    return candidate


def remove_empty_category_parents(path):
    current = path
    while current != WIKID_CLIPPINGS and current.parent != current:
        if any(current.iterdir()):
            break
        current.rmdir()
        current = current.parent


def write_classification_rules():
    lines = [
        "---",
        'title: "Web Clipper Classification Rules"',
        f"date_created: {TODAY}",
        f"date_modified: {TODAY}",
        "type: sop",
        "tags: [web-clipper, wikid-raw, classification]",
        "wikid_system_note: true",
        "---",
        "",
        "# Web Clipper Classification Rules",
        "",
        "This note documents how Obsidian Web Clipper notes are routed inside `llm-wikid/raw/clippings/`.",
        "",
        "## Input Rule",
        "- Preferred Web Clipper location: `llm-wikid/raw/clippings/{{title}}`.",
        "- Compatibility inbox: root `Clippings/*.md`; the refresh button moves these notes into `llm-wikid/raw/clippings/` before classification.",
        "- One clipped webpage should be one Markdown file. Fix malformed input at the clipped note level before adding parser compatibility.",
        "",
        "## Classification Table",
        "",
        "| Folder | Category | Concept | Criteria |",
        "|---|---|---|---|",
    ]

    for rule in CATEGORY_RULES + [DEFAULT_RULE]:
        lines.append(
            f"| `{rule['folder']}` | {rule['label']} | [[{rule['concept']}]] | {rule['criteria']} |"
        )

    lines.extend([
        "",
        "## Automation",
        "- The button [[llm_wikid_refresh_button]] calls `scripts/02_refresh_llm_wikid.ps1`.",
        "- That PowerShell script calls `scripts/09_import_web_clipper_to_wikid_raw.py` before rebuilding the LLM Wikid index.",
        "- Each clipped note receives `wikid_auto_category`, `wikid_concept`, `wikid_classification_basis`, and an `## Auto Classification` block.",
        "",
        "## Review Rule",
        "- Treat automatic classification as first-pass triage.",
        "- Manually review notes in `general_reference/` first, then promote high-value notes into deeper source/concept/synthesis pages.",
        "",
    ])

    (WIKID_CLIPPINGS / CRITERIA_NOTE_NAME).write_text("\n".join(lines), encoding="utf-8")


WIKID_CLIPPINGS.mkdir(parents=True, exist_ok=True)
RESULT_ROOT.mkdir(parents=True, exist_ok=True)
write_classification_rules()

imported_paths = {}
for source_path in sorted(WEB_CLIPPER_INBOX.glob("*.md")):
    target_path = unique_path(WIKID_CLIPPINGS / source_path.name)
    shutil.move(str(source_path), str(target_path))
    imported_paths[target_path] = source_path

clip_paths = sorted([
    path for path in WIKID_CLIPPINGS.rglob("*.md")
    if path.name != CRITERIA_NOTE_NAME and not path.name.endswith(".excalidraw.md")
])

manifest_rows = []
for source_path in clip_paths:
    text = source_path.read_text(encoding="utf-8")
    rule, hits = classify_clip(source_path.relative_to(WIKID_CLIPPINGS), text)
    classified_text = update_frontmatter(source_path, text, rule, hits)
    classified_text = update_auto_block(classified_text, rule, hits)

    category_dir = WIKID_CLIPPINGS / rule["folder"]
    target_path = category_dir / source_path.name
    if target_path != source_path:
        target_path = unique_path(target_path)

    category_dir.mkdir(parents=True, exist_ok=True)
    source_path.write_text(classified_text, encoding="utf-8")

    action = "classified_in_place"
    if target_path != source_path:
        shutil.move(str(source_path), str(target_path))
        remove_empty_category_parents(source_path.parent)
        action = "moved_to_category"

    original_path = imported_paths.get(source_path, source_path)
    manifest_rows.append({
        "original_path": str(original_path.relative_to(VAULT_ROOT)),
        "source_path": str(source_path.relative_to(VAULT_ROOT)),
        "target_path": str(target_path.relative_to(VAULT_ROOT)),
        "action": action,
        "imported_from_root_clippings": str(source_path in imported_paths).lower(),
        "category_slug": rule["slug"],
        "category_label": rule["label"],
        "concept": rule["concept"],
        "matched_keywords": "; ".join(hits),
    })

manifest_path = RESULT_ROOT / f"{RUN_TAG}_web_clipper_import_manifest.csv"
with manifest_path.open("w", encoding="utf-8-sig", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=[
        "original_path",
        "source_path",
        "target_path",
        "action",
        "imported_from_root_clippings",
        "category_slug",
        "category_label",
        "concept",
        "matched_keywords",
    ])
    writer.writeheader()
    writer.writerows(manifest_rows)

moved_count = len([row for row in manifest_rows if row["action"] == "moved_to_category"])
print(f"Imported from root Clippings: {len(imported_paths)}")
print(f"Classified web clippings: {len(manifest_rows)}")
print(f"Moved into category folders: {moved_count}")
print(f"Criteria note: llm-wikid/raw/clippings/{CRITERIA_NOTE_NAME}")
print(f"Manifest: {manifest_path.relative_to(VAULT_ROOT)}")
