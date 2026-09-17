from pathlib import Path
from datetime import datetime
import csv
import shutil


# =========================
# 可修改参数
# =========================
VAULT_ROOT = Path(r"E:\5-newplanet\new planet")
RAW_ROOT = VAULT_ROOT / "llm-wikid" / "raw"
RESULT_ROOT = VAULT_ROOT / "result"

RUN_TAG = datetime.now().strftime("%Y-%m-%d")

SKIP_TOP_DIRS = {"assets", "x-archive"}
CANONICAL_TOP_DIRS = {"articles", "bookmarks", "ideas", "papers", "clippings"}
CANONICAL_INBOX_DIRS = {"articles", "bookmarks", "ideas"}

# 强规则：命中后直接路由到对应叶子
ROUTE_RULES = [
    # 赚钱想法 - 优先级高于 AI/科研/股票，避免商业想法被正文链接带偏
    {
        "name": "idea_image_monetization",
        "keywords": ["赚钱", "餐饮店", "菜品图", "小店出图", "生图用", "imagize", "变现", "出图"],
        "target": ["ideas", "赚钱想法", "生图变现"],
    },
    {
        "name": "idea_website_monetization",
        "keywords": ["造景推广", "视觉网站", "网站做造景", "推广", "获客", "落地页"],
        "target": ["ideas", "赚钱想法", "视觉网站"],
    },
    {
        "name": "idea_brand_content",
        "keywords": ["ai从0到1做品牌", "做品牌", "品牌", "风格提示词", "复制图片转风格", "qiaomu"],
        "target": ["ideas", "赚钱想法", "品牌内容"],
    },
    {
        "name": "idea_job_hunt",
        "keywords": ["找工作", "自救", "职业", "求职", "简历", "面试"],
        "target": ["ideas", "赚钱想法", "求职转型"],
    },
    {
        "name": "idea_tools_flow",
        "keywords": ["同步助手_2026", "watcher", "qmd", "obsidian 自动化"],
        "target": ["ideas", "赚钱想法", "工具流程"],
    },

    # 学习 AI
    {
        "name": "ai_prompt_image",
        "keywords": ["提示词", "prompt", "image prompts", "风格提示词", "图片转风格"],
        "target": ["articles", "学习AI", "提示词与生图"],
    },
    {
        "name": "ai_code_automation",
        "keywords": ["codex", "vibecoding", "前端三天", "代码自动化", "脚本", "workflow"],
        "target": ["articles", "学习AI", "代码自动化"],
    },
    {
        "name": "ai_product_website",
        "keywords": ["产品网站", "落地页", "视觉网站", "web design"],
        "target": ["articles", "学习AI", "产品与网站"],
    },
    {
        "name": "ai_model_observation",
        "keywords": ["chat-gpt", "chatgpt", "gpt", "claude", "llm", "世界模型", "智能体", "生成式"],
        "target": ["articles", "学习AI", "模型观察"],
    },

    # 生活
    {
        "name": "life_parenting",
        "keywords": ["疫苗", "乙肝", "宝宝", "小宝", "育儿", "儿童", "亲子"],
        "target": ["articles", "生活", "健康育儿"],
    },
    {
        "name": "life_health",
        "keywords": ["健康", "养生", "疾病", "医疗", "体检", "护理"],
        "target": ["articles", "生活", "健康知识"],
    },

    # 科研 - 植物抗逆
    {
        "name": "science_stress_heat",
        "keywords": ["耐高温", "耐热", "热胁迫", "高温胁迫", "heat stress", "high temperature"],
        "target": ["articles", "科研", "植物抗逆", "耐高温"],
    },
    {
        "name": "science_stress_cold",
        "keywords": ["耐寒", "低温", "冷胁迫", "冷害", "cold stress"],
        "target": ["articles", "科研", "植物抗逆", "耐寒"],
    },
    {
        "name": "science_stress_drought",
        "keywords": ["耐旱", "抗旱", "干旱", "drought", "水分亏缺", "渗透调节"],
        "target": ["articles", "科研", "植物抗逆", "耐旱"],
    },
    {
        "name": "science_stress_salt",
        "keywords": ["耐盐", "盐胁迫", "盐害", "nacl"],
        "target": ["articles", "科研", "植物抗逆", "耐盐"],
    },
    {
        "name": "science_stress_light",
        "keywords": ["耐光强", "强光", "高光", "光抑制", "photoinhibition", "李家洋团队最新cell"],
        "target": ["articles", "科研", "植物抗逆", "耐光强"],
    },
    {
        "name": "science_stress_cold_nature",
        "keywords": ["重磅！我国植物领域再发《nature》", "我国植物领域再发《nature》"],
        "target": ["articles", "科研", "植物抗逆", "耐寒"],
    },
    {
        "name": "science_stress_mechanism",
        "keywords": ["隐藏密码", "染色体外环状dna", "抗逆机制"],
        "target": ["articles", "科研", "植物抗逆", "抗逆机制"],
    },

    # 科研 - 工具 / 方法
    {
        "name": "science_pheno_tool",
        "keywords": ["ucaa", "cornpheno", "多光谱", "成像", "分光光度法", "颜色面积", "表型", "叶温", "植物生理特征"],
        "target": ["articles", "科研", "科研工具", "高温表型工具"],
    },
    {
        "name": "science_bioinfo_tool",
        "keywords": ["wgcna", "pca", "bulk", "转录组", "rna", "单细胞", "featurecounts", "deseq", "edger", "salmon", "kallisto", "网络分析", "差异表达"],
        "target": ["articles", "科研", "科研工具", "生信工具"],
    },
    {
        "name": "science_transform",
        "keywords": ["crispr", "cas", "转化率", "植物遗传转化", "农杆菌", "愈伤", "novocast", "基因编辑"],
        "target": ["articles", "科研", "玉米遗传转化"],
    },
    {
        "name": "science_maize_system",
        "keywords": ["授粉时间差", "穗内", "源-库", "收获指数", "果穗", "花丝", "吐丝", "籽粒", "产量协同"],
        "target": ["articles", "科研", "玉米知识体系"],
    },
    {
        "name": "science_breeding_disease",
        "keywords": ["病虫害", "病害", "虫害", "防治", "褐斑病", "顶腐病", "玉米螟", "三遍药", "田间管理"],
        "target": ["articles", "科研", "育种改良", "育种知识-病害-田间管理"],
    },
    {
        "name": "science_breeding_high_protein",
        "keywords": ["高蛋白玉米", "高蛋白", "蛋白质含量"],
        "target": ["articles", "科研", "育种改良", "高蛋白玉米"],
    },
    {
        "name": "science_breeding_seminar",
        "keywords": ["南北学苑", "南北学院", "陆镇威", "讲座", "报告", "思考"],
        "target": ["articles", "科研", "育种改良", "南北学苑"],
    },
    {
        "name": "science_breeding_ai",
        "keywords": ["ai育种", "种业新说", "基础设施", "智能育种", "机器学习", "模型预测"],
        "target": ["articles", "科研", "育种改良", "AI育种"],
    },
    {
        "name": "science_research_news",
        "keywords": ["cell press", "iscience", "nature communications", "nature methods", "biorxiv", "对话科学家", "论文", "综述", "方法", "平台", "算法", "液态金属", "多孔材料"],
        "target": ["articles", "科研", "科研工具", "了解-可能用到"],
    },

    # 股票
    {
        "name": "stock_analysis",
        "keywords": ["两融", "融资融券", "研报", "复盘", "估值", "策略", "财经", "金融", "股民", "盘面", "仓位", "业绩"],
        "target": ["articles", "股票", "大牛博主学思路"],
    },
    {
        "name": "stock_mining",
        "keywords": ["矿业", "有色", "黄金", "白银", "锂矿", "煤炭", "采掘", "资源股"],
        "target": ["articles", "股票", "挖矿人"],
    },
    {
        "name": "stock_policy",
        "keywords": ["a股", "股市", "交易所", "新规", "规则", "盘后", "盘中", "涨跌幅", "重大调整", "行情", "市场", "数据中心", "内存", "涨价潮", "券商", "证券"],
        "target": ["articles", "股票", "前沿消息"],
    },
]

ARTICLE_HINTS = [
    "mp.weixin.qq.com",
    "## 正文",
    "原文链接",
    "公众号",
    "微信公众号",
    "来源",
]

URL_HINTS = ["http://", "https://"]

DOMAIN_KEYWORDS = {
    "科研": ["科研", "植物", "玉米", "育种", "转化", "抗逆", "表型", "生信", "论文", "nature", "biorxiv", "iscience", "cell press", "方法", "算法"],
    "股票": ["股票", "股市", "证券", "券商", "财经", "金融", "两融", "交易所", "涨跌幅", "a股", "市场", "行情", "资源股", "有色", "黄金", "锂矿"],
    "学习AI": ["学习ai", "ai", "chatgpt", "codex", "claude", "prompt", "提示词", "llm", "agent", "vibecoding"],
    "生活": ["生活", "健康", "疫苗", "宝宝", "育儿", "医疗"],
    "赚钱想法": ["赚钱", "商业", "副业", "品牌", "推广", "生图", "网站", "变现", "造景"],
}

DOMAIN_DEFAULTS = {
    "article": {
        "科研": ["articles", "科研", "科研工具", "了解-可能用到"],
        "股票": ["articles", "股票", "前沿消息"],
        "学习AI": ["articles", "学习AI", "工具流程"],
        "生活": ["articles", "生活", "日常记录"],
        "赚钱想法": ["ideas", "赚钱想法", "商业想法"],
        None: ["articles", "待细分"],
    },
    "idea": {
        "科研": ["ideas", "赚钱想法", "商业想法"],
        "股票": ["ideas", "赚钱想法", "商业想法"],
        "学习AI": ["ideas", "赚钱想法", "工具流程"],
        "生活": ["ideas", "赚钱想法", "商业想法"],
        "赚钱想法": ["ideas", "赚钱想法", "商业想法"],
        None: ["ideas", "待细分"],
    },
    "bookmark": {
        "科研": ["bookmarks", "科研"],
        "股票": ["bookmarks", "股票"],
        "学习AI": ["bookmarks", "学习AI"],
        "生活": ["bookmarks", "生活"],
        "赚钱想法": ["bookmarks", "赚钱想法"],
        None: ["bookmarks", "待细分"],
    },
}

DOMAIN_ORDER = ["科研", "股票", "学习AI", "赚钱想法", "生活"]
DOMAIN_HIT_BONUS = {
    "科研": ["articles", "科研", "植物", "玉米", "育种", "转化", "抗逆", "表型", "生信"],
    "股票": ["articles", "股票", "股市", "证券", "券商", "财经", "金融", "两融"],
    "学习AI": ["articles", "学习AI", "ai", "codex", "chatgpt", "claude"],
    "赚钱想法": ["ideas", "赚钱想法", "赚钱", "商业", "副业", "品牌"],
    "生活": ["articles", "生活", "健康", "疫苗", "宝宝", "育儿"],
}

DOMAIN_MIN_SCORE = 2
DOMAIN_MIN_MARGIN = 1


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
    half = len(cleaned) // 2
    if len(cleaned) % 2 == 0 and cleaned[:half] == cleaned[half:]:
        return cleaned[:half]
    return cleaned


def contains_any(text, keywords):
    return any(keyword.lower() in text for keyword in keywords)


def build_haystack(path, text):
    body = strip_frontmatter(text)
    return f"{path.as_posix()} {path.stem} {text[:6000]} {body[:6000]}".lower(), body


def routing_haystack(path, text):
    parts = path.parts
    tokens = [path.stem]
    if parts[0] not in CANONICAL_TOP_DIRS:
        tokens.extend(parts[:-1])
    return " ".join(tokens).lower()


def infer_kind(relative_parts, haystack, body_length):
    if relative_parts[0] == "ideas":
        return "idea"
    if relative_parts[0] == "bookmarks":
        return "bookmark"
    if any(hint in haystack for hint in URL_HINTS) and body_length < 1200 and not contains_any(haystack, ARTICLE_HINTS):
        return "bookmark"
    return "article"


def first_matching_rule(route_text):
    for rule in ROUTE_RULES:
        if contains_any(route_text, rule["keywords"]):
            return rule
    return None


def score_domain(route_text, relative_text):
    scores = {}
    for domain in DOMAIN_ORDER:
        score = 0
        for keyword in DOMAIN_KEYWORDS[domain]:
            if keyword.lower() in route_text:
                score += 1
        for keyword in DOMAIN_HIT_BONUS[domain]:
            if keyword.lower() in relative_text:
                score += 1
        scores[domain] = score

    ordered = sorted(scores.items(), key=lambda item: (-item[1], DOMAIN_ORDER.index(item[0])))
    best_domain, best_score = ordered[0]
    second_score = ordered[1][1] if len(ordered) > 1 else 0
    return best_domain, best_score, second_score


def fallback_target(kind, domain):
    return DOMAIN_DEFAULTS[kind].get(domain, DOMAIN_DEFAULTS[kind][None])


def infer_target_parts(relative_parts, haystack, route_text, body_length):
    if relative_parts[0] == "clippings":
        return list(relative_parts[:-1]), "keep_web_clipper_clipping", "keep"

    rule = first_matching_rule(route_text)
    if rule is not None:
        return rule["target"], rule["name"], "rule"

    is_entry_file = relative_parts[0] in CANONICAL_INBOX_DIRS and len(relative_parts) == 2
    if relative_parts[0] in CANONICAL_TOP_DIRS and not is_entry_file:
        return list(relative_parts[:-1]), "keep_canonical", "keep"

    relative_text = " ".join(relative_parts).lower()
    kind = infer_kind(relative_parts, haystack, body_length)
    domain, best_score, second_score = score_domain(route_text, relative_text)

    if best_score < DOMAIN_MIN_SCORE or (best_score - second_score) < DOMAIN_MIN_MARGIN:
        return fallback_target(kind, None), "fallback_uncertain", "fallback"

    return fallback_target(kind, domain), f"fallback_{domain}", "fallback"


def remove_empty_parents(start_dir):
    current = start_dir
    while current.parent != RAW_ROOT:
        if any(current.iterdir()):
            break
        current.rmdir()
        current = current.parent


RESULT_ROOT.mkdir(parents=True, exist_ok=True)

all_md_files = sorted([
    path for path in RAW_ROOT.rglob("*.md")
    if path.name != "" and not path.name.endswith(".excalidraw.md")
])

moved_rows = []
kept_count = 0

for source_path in all_md_files:
    if source_path.name == "Web Clipper Classification Rules.md":
        continue

    relative_parts = source_path.relative_to(RAW_ROOT).parts
    first_dir = relative_parts[0]

    if first_dir in SKIP_TOP_DIRS:
        continue

    text = source_path.read_text(encoding="utf-8")
    haystack, body = build_haystack(source_path.relative_to(RAW_ROOT), text)
    route_text = routing_haystack(source_path.relative_to(RAW_ROOT), text)

    target_parts, rule_name, route_mode = infer_target_parts(relative_parts, haystack, route_text, len(body))
    target_path = RAW_ROOT.joinpath(*target_parts) / source_path.name

    if target_path == source_path:
        kept_count += 1
        continue

    target_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(source_path), str(target_path))
    remove_empty_parents(source_path.parent)

    moved_rows.append({
        "source_path": str(source_path.relative_to(VAULT_ROOT)),
        "target_path": str(target_path.relative_to(VAULT_ROOT)),
        "rule_name": rule_name,
        "route_mode": route_mode,
        "source_kind": infer_kind(relative_parts, haystack, len(body)),
        "body_length": len(body),
    })

with (RESULT_ROOT / f"{RUN_TAG}_wechat_raw_auto_route_manifest.csv").open("w", encoding="utf-8-sig", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=["source_path", "target_path", "rule_name", "route_mode", "source_kind", "body_length"])
    writer.writeheader()
    writer.writerows(moved_rows)

print(f"Scanned raw notes: {len(all_md_files)}")
print(f"Moved raw notes: {len(moved_rows)}")
print(f"Kept in place: {kept_count}")
print(f"Manifest: result/{RUN_TAG}_wechat_raw_auto_route_manifest.csv")
