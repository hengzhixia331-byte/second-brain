from pathlib import Path
import csv
import re
from datetime import datetime


# =========================
# 可修改参数
# =========================
VAULT_ROOT = Path(r"E:\5-newplanet\new planet")
RAW_ROOT = VAULT_ROOT / "llm-wikid" / "raw"
WIKI_ROOT = VAULT_ROOT / "llm-wikid" / "wiki"
RESULT_ROOT = VAULT_ROOT / "result"

MIN_CONTENT_CHARS = 500
TODAY = datetime.now().strftime("%Y-%m-%d")
RUN_TAG = TODAY

CATEGORY_RULES = [
    {
        "slug": "maize_genetic_transformation",
        "title": "Maize Genetic Transformation",
        "kind": "concept",
        "keywords": ["玉米遗传转化", "转化率", "CRISPR", "Cas", "基因组", "转基因", "编辑技术", "NovoCAST"],
        "tags": ["plant-science", "maize", "genetic-transformation", "genome-editing"],
    },
    {
        "slug": "plant_stress_resilience",
        "title": "Plant Stress Resilience",
        "kind": "concept",
        "keywords": ["抗逆", "耐旱", "耐盐", "耐热", "热胁迫", "耐光强", "病虫害", "褐斑病", "顶腐病", "玉米螟"],
        "tags": ["plant-science", "stress", "physiology"],
    },
    {
        "slug": "maize_yield_and_breeding",
        "title": "Maize Yield and Breeding",
        "kind": "concept",
        "keywords": ["玉米", "育种", "高产", "产量", "蛋白", "氮肥", "授粉", "果穗", "考种", "AI育种"],
        "tags": ["plant-science", "maize", "breeding", "yield"],
    },
    {
        "slug": "plant_phenotyping_and_imaging",
        "title": "Plant Phenotyping and Imaging",
        "kind": "concept",
        "keywords": ["表型", "多光谱", "成像", "分光光度", "颜色面积", "UCAA", "CornPheno", "叶温"],
        "tags": ["plant-science", "phenotyping", "imaging"],
    },
    {
        "slug": "bioinformatics_analysis",
        "title": "Bioinformatics Analysis",
        "kind": "concept",
        "keywords": ["生信", "WGCNA", "bulk", "转录组", "PCA", "主成分", "基因功能模块", "RNA", "多组学"],
        "tags": ["bioinformatics", "omics", "analysis"],
    },
    {
        "slug": "ai_for_research",
        "title": "AI for Research",
        "kind": "concept",
        "keywords": ["AI", "ChatGPT", "Codex", "Claude", "世界模型", "模型", "人工智能", "转录因子结合预测"],
        "tags": ["ai", "research-tools"],
    },
    {
        "slug": "research_tools_and_methods",
        "title": "Research Tools and Methods",
        "kind": "concept",
        "keywords": ["工具", "算法", "Methods", "Nature Communications", "Cell", "iScience", "BioRxiv", "综述", "论文"],
        "tags": ["research", "tools", "methods"],
    },
    {
        "slug": "finance_and_investment",
        "title": "Finance and Investment",
        "kind": "concept",
        "keywords": ["股票", "股市", "两融", "财经", "金融", "挖矿", "投资"],
        "tags": ["finance", "investment"],
    },
    {
        "slug": "life_and_health",
        "title": "Life and Health",
        "kind": "concept",
        "keywords": ["生活", "疫苗", "乙肝", "宝宝", "小宝", "健康"],
        "tags": ["life", "health"],
    },
    {
        "slug": "career_and_business_ideas",
        "title": "Career and Business Ideas",
        "kind": "concept",
        "keywords": ["赚钱", "工作", "自救", "前端", "推广", "造景", "商业"],
        "tags": ["career", "business"],
    },
]


# =========================
# 线性整理流程
# =========================
def slugify(text):
    lowered = text.lower()
    replaced = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", lowered).strip("-")
    return replaced[:80]


def obsidian_link(path):
    return f"[[{path.stem}]]"


def wiki_filename(title):
    return f"{title}.md"


def strip_frontmatter(text):
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) == 3:
            return parts[2].strip()
    return text.strip()


def frontmatter_value(path, field):
    if not path.exists():
        return None
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    if len(parts) != 3:
        return None
    match = re.search(rf"^{re.escape(field)}:\s*(.+)$", parts[1], re.MULTILINE)
    if not match:
        return None
    value = match.group(1).strip()
    if value.startswith('"') and value.endswith('"'):
        return value[1:-1]
    if value.startswith("'") and value.endswith("'"):
        return value[1:-1]
    return value


def first_heading_or_stem(path, text):
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem


def plain_preview(text, max_chars=220):
    lines = []
    for line in text.splitlines():
        clean = line.strip()
        if clean.startswith("#"):
            clean = clean.lstrip("#").strip()
        if clean:
            lines.append(clean)
    merged = " ".join(lines)
    return merged[:max_chars]


def classify_note(path, text):
    haystack = f"{path.as_posix()} {path.stem} {text[:3000]}".lower()
    matched = []
    for rule in CATEGORY_RULES:
        score = 0
        for keyword in rule["keywords"]:
            if keyword.lower() in haystack:
                score += 1
        if score > 0:
            matched.append((score, rule))
    matched.sort(key=lambda item: (-item[0], item[1]["slug"]))
    if matched:
        return matched[0][1], [item[1] for item in matched]
    return {
        "slug": "uncategorized_notes",
        "title": "Uncategorized Notes",
        "kind": "concept",
        "keywords": [],
        "tags": ["uncategorized"],
    }, []


def source_type_for(path, text):
    haystack = f"{path.as_posix()} {path.stem} {text[:2000]}".lower()
    if "nature" in haystack or "science" in haystack or "cell" in haystack or "biorxiv" in haystack or "综述" in haystack or "论文" in haystack:
        return "article"
    if "教程" in haystack or "工具" in haystack or "代码" in haystack:
        return "notes"
    return "notes"


all_md_files = sorted(RAW_ROOT.rglob("*.md"))
candidate_rows = []
skipped_rows = []
name_counts = {}

for path in all_md_files:
    relative = path.relative_to(VAULT_ROOT)
    skip_reason = ""

    if path.name.endswith(".excalidraw.md"):
        skip_reason = "skip_excalidraw_canvas"

    if path.name == "Web Clipper Classification Rules.md":
        skip_reason = "skip_web_clipper_classification_rules"

    if skip_reason:
        skipped_rows.append({
            "path": str(relative),
            "reason": skip_reason,
            "length": path.stat().st_size,
        })
        continue

    text = path.read_text(encoding="utf-8")
    body = strip_frontmatter(text)
    if len(body) < MIN_CONTENT_CHARS:
        skipped_rows.append({
            "path": str(relative),
            "reason": "skip_short_note",
            "length": len(body),
        })
        continue

    category, all_matches = classify_note(relative, body)
    title = first_heading_or_stem(path, body)
    source_type = source_type_for(relative, body)
    preview = plain_preview(body)
    link = obsidian_link(path)
    slug = slugify(path.stem)

    name_counts[path.stem] = name_counts.get(path.stem, 0) + 1

    candidate_rows.append({
        "path": str(relative),
        "stem": path.stem,
        "title": title,
        "link": link,
        "slug": slug,
        "category_slug": category["slug"],
        "category_title": category["title"],
        "source_type": source_type,
        "length": len(body),
        "preview": preview,
        "matched_categories": "; ".join([rule["title"] for rule in all_matches]),
    })

duplicates = sorted([stem for stem, count in name_counts.items() if count > 1])

source_dir = WIKI_ROOT / "sources"
concept_dir = WIKI_ROOT / "concepts"
source_dir.mkdir(parents=True, exist_ok=True)
concept_dir.mkdir(parents=True, exist_ok=True)
RESULT_ROOT.mkdir(parents=True, exist_ok=True)

for row in candidate_rows:
    source_path = source_dir / f"vault-{row['slug']}.md"
    concept_link = f"[[{row['category_title']}]]"
    source_created = frontmatter_value(source_path, "date_created") or TODAY
    source_text = f"""---
title: "{row['title'].replace('"', "'")}"
tldr: "{row['preview'].replace('"', "'")}"
date_created: {source_created}
date_modified: {TODAY}
type: source
tags: [vault-import, {row['category_slug']}, {row['source_type']}]
source_type: {row['source_type']}
source_file: "{row['link']}"
explored: false
confidence: medium
---

# {row['title']}

## Summary
This source card was generated from an existing Obsidian note. The original note remains unchanged at {row['link']}.

## Key Takeaways
- Original note: {row['link']}
- Imported category: {concept_link}
- Local path: `{row['path']}`
- Preview: {row['preview']}

## Concepts & Entities Mentioned
- {concept_link}

## Counter-arguments
- This card is an index-level extraction, not a full critical reading of the source.
- The category assignment is based on deterministic keyword matching and should be reviewed by the user.

## Data gaps
- Full claim-level citation and biological interpretation have not yet been manually curated.
- Duplicate or near-duplicate source notes should be merged at the input-note level before deeper synthesis.
"""
    source_path.write_text(source_text, encoding="utf-8")

rows_by_category = {}
for row in candidate_rows:
    rows_by_category.setdefault(row["category_slug"], []).append(row)

for rule in CATEGORY_RULES + [{
    "slug": "uncategorized_notes",
    "title": "Uncategorized Notes",
    "tags": ["uncategorized"],
}]:
    rows = rows_by_category.get(rule["slug"], [])
    if not rows:
        continue
    tags = ", ".join(rule["tags"])
    source_links = ", ".join([f"[[vault-{row['slug']}]]" for row in rows])
    lines = []
    for row in sorted(rows, key=lambda item: item["title"]):
        lines.append(f"- [[vault-{row['slug']}]] - original note {row['link']}")

    concept_created = frontmatter_value(concept_dir / wiki_filename(rule["title"]), "date_created") or TODAY
    concept_text = f"""---
title: "{rule['title']}"
tldr: "Imported concept hub for {len(rows)} existing vault notes."
date_created: {concept_created}
date_modified: {TODAY}
type: concept
tags: [{tags}]
sources: [{source_links}]
explored: false
confidence: medium
---

# {rule['title']}

This concept hub groups existing Obsidian notes imported from the current vault. It preserves original notes as sources and provides a review queue for deeper synthesis.

## Key Ideas
- Number of linked source cards: {len(rows)}
- Import method: deterministic keyword classification from file path, title, and note body.
- Original notes were not modified.

## Source Cards
{chr(10).join(lines)}

## How It Connects
- Source cards in this hub can be reviewed and promoted into more detailed concept, entity, SOP, or synthesis pages.
- Plant science notes should be further interpreted across data quality, statistical assumptions, biology, plant physiology, and validation evidence.

## Counter-arguments
- Keyword-based grouping may over-assign broad themes such as AI, tools, or maize when titles contain overlapping terms.
- This hub is a first-pass organization layer, not a final literature review.

## Data gaps
- Manual extraction of mechanisms, genes, phenotypes, experimental designs, and validation evidence is still required.
- Near-duplicate notes should be resolved in the original vault before claim-level synthesis.
"""
    (concept_dir / wiki_filename(rule["title"])).write_text(concept_text, encoding="utf-8")

index_lines = []
for rule in CATEGORY_RULES + [{
    "slug": "uncategorized_notes",
    "title": "Uncategorized Notes",
    "tags": ["uncategorized"],
}]:
    rows = rows_by_category.get(rule["slug"], [])
    if rows:
        index_lines.append(f"- [[{rule['title']}]] - {len(rows)} imported source cards")

source_index_lines = []
for row in sorted(candidate_rows, key=lambda item: (item["category_title"], item["title"])):
    source_index_lines.append(f"- [[vault-{row['slug']}]] - {row['link']} ({row['category_title']})")

duplicate_lines = [f"- [[{stem}]]" for stem in duplicates]
if not duplicate_lines:
    duplicate_lines = ["- No duplicate note names detected among imported notes."]

index_path = WIKI_ROOT / "index.md"
index_created = frontmatter_value(index_path, "date_created") or TODAY
index_text = f"""---
title: "Wiki Index"
tldr: "Master catalog of imported vault notes organized into LLM Wikid source and concept pages."
date_created: {index_created}
date_modified: {TODAY}
explored: false
confidence: medium
---

# Wiki Index

_Scan TLDRs to find relevant pages. Load full pages only when needed._

## Imported Concept Hubs
{chr(10).join(index_lines)}

## Imported Sources
{chr(10).join(source_index_lines)}

## Input Notes Requiring Review
### Duplicate note names
{chr(10).join(duplicate_lines)}

### Skipped notes
See [[Vault Import Report]] and `result/{RUN_TAG}_vault_note_inventory.csv`.

## Recommended Next Actions
- Review plant-science hubs first: [[Maize Genetic Transformation]], [[Plant Stress Resilience]], [[Maize Yield and Breeding]], [[Plant Phenotyping and Imaging]], and [[Bioinformatics Analysis]].
- Merge exact or near-duplicate original notes before deeper synthesis.
- Promote mature topics into synthesis pages after manual review.
"""
(WIKI_ROOT / "index.md").write_text(index_text, encoding="utf-8")

report_rows = sorted(candidate_rows, key=lambda item: (item["category_title"], item["path"]))
report_path = WIKI_ROOT / "outputs" / "vault_import_report.md"
report_created = frontmatter_value(report_path, "date_created") or TODAY

with (RESULT_ROOT / f"{RUN_TAG}_vault_note_inventory.csv").open("w", encoding="utf-8-sig", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=[
        "path",
        "stem",
        "title",
        "link",
        "slug",
        "category_title",
        "category_slug",
        "source_type",
        "length",
        "matched_categories",
        "preview",
    ])
    writer.writeheader()
    writer.writerows(report_rows)

with (RESULT_ROOT / f"{RUN_TAG}_vault_note_skipped.csv").open("w", encoding="utf-8-sig", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=["path", "reason", "length"])
    writer.writeheader()
    writer.writerows(skipped_rows)

summary_lines = [
    "---",
    'title: "Vault Import Report"',
    'tldr: "First-pass organization of existing Obsidian notes into the LLM Wikid template."',
    f"date_created: {report_created}",
    f"date_modified: {TODAY}",
    "type: output",
    "tags: [vault-import, organization]",
    "explored: false",
    "confidence: medium",
    "---",
    "",
    "# Vault Import Report",
    "",
    "## Summary",
    f"- Imported notes: {len(candidate_rows)}",
    f"- Skipped notes: {len(skipped_rows)}",
    f"- Concept hubs created: {len(rows_by_category)}",
    "- Raw source notes were not modified by this compile step.",
    "",
    "## Category Counts",
    "",
    "| Concept Hub | Imported Notes |",
    "|---|---:|",
]

for category_slug, rows in sorted(rows_by_category.items()):
    title = rows[0]["category_title"]
    summary_lines.append(f"| [[{title}]] | {len(rows)} |")

summary_lines.extend([
    "",
    "## Duplicate Note Names",
    *duplicate_lines,
    "",
    "## Skipped Notes",
    "Skipped notes include system/plugin notes, Excalidraw canvases, generated records, and short notes below the configured content threshold.",
    "",
    f"See `result/{RUN_TAG}_vault_note_skipped.csv` for the full skipped-note table.",
    "",
    "## Interpretation",
    "This import creates a structured knowledge layer over the existing vault. In the plant-science domain, the highest-value next step is manual synthesis of mechanisms, experimental designs, phenotypes, genes, pathways, and validation evidence.",
    "",
    "## Next Step",
    "Review [[Bioinformatics Analysis]], [[Plant Stress Resilience]], and [[Maize Genetic Transformation]] before converting selected source cards into deeper synthesis pages.",
])

(WIKI_ROOT / "outputs").mkdir(parents=True, exist_ok=True)
(WIKI_ROOT / "outputs" / "vault_import_report.md").write_text("\n".join(summary_lines) + "\n", encoding="utf-8")

print(f"Imported notes: {len(candidate_rows)}")
print(f"Skipped notes: {len(skipped_rows)}")
print(f"Concept hubs created: {len(rows_by_category)}")
print(f"Duplicate note names: {len(duplicates)}")
