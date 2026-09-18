---
title: "Web Clipper Classification Rules"
date_created: 2026-09-18
date_modified: 2026-09-18
type: sop
tags: [web-clipper, wikid-raw, classification]
wikid_system_note: true
---

# Web Clipper Classification Rules

This note documents how Obsidian Web Clipper notes are routed inside `llm-wikid/raw/clippings/`.

## Input Rule
- Preferred Web Clipper location: `llm-wikid/raw/clippings/{{title}}`.
- Compatibility inbox: root `Clippings/*.md`; the refresh button moves these notes into `llm-wikid/raw/clippings/` before classification.
- One clipped webpage should be one Markdown file. Fix malformed input at the clipped note level before adding parser compatibility.

## Classification Table

| Folder | Category | Concept | Criteria |
|---|---|---|---|
| `plant_stress_resilience` | Plant Science - Stress Resilience | [[Plant Stress Resilience]] | 植物逆境生理、抗旱、耐盐、耐热、耐寒、高光或渗透/氧化胁迫机制。 |
| `maize_genetic_transformation` | Maize Genetic Transformation | [[Maize Genetic Transformation]] | 植物遗传转化、玉米转化体系、CRISPR/Cas 编辑、组织培养或转化效率优化。 |
| `maize_yield_and_breeding` | Maize Yield and Breeding | [[Maize Yield and Breeding]] | 玉米产量、籽粒、授粉、育种改良、品质性状或品种评价。 |
| `plant_phenotyping_and_imaging` | Plant Phenotyping and Imaging | [[Plant Phenotyping and Imaging]] | 植物表型组学、图像/光谱采集、叶温、颜色面积、冠层或考种工具。 |
| `bioinformatics_analysis` | Bioinformatics Analysis | [[Bioinformatics Analysis]] | 生物信息学分析、组学数据、GWAS/SNP、RNA-seq、WGCNA、PCA 或统计遗传工具。 |
| `ai_for_research` | AI for Research | [[AI for Research]] | AI 工具、大模型、科研自动化、提示词、Agent 或代码自动化。 |
| `research_tools_and_methods` | Research Tools and Methods | [[Research Tools and Methods]] | 通用科研工具、方法学、软件平台、教程、流程或 protocol。 |
| `finance_and_investment` | Finance and Investment | [[Finance and Investment]] | 股票、证券、宏观市场、产业投资、两融、财经分析或交易策略。 |
| `life_and_health` | Life and Health | [[Life and Health]] | 生活健康、疫苗、育儿、医疗护理或日常健康知识。 |
| `career_and_business_ideas` | Career and Business Ideas | [[Career and Business Ideas]] | 赚钱想法、副业、品牌内容、商业模式、求职转型或个人发展。 |
| `general_reference` | General Reference | [[Uncategorized Notes]] | 没有命中上面规则的网页剪藏，先保留为待复核资料。 |

## Automation
- The button [[llm_wikid_refresh_button]] calls `scripts/02_refresh_llm_wikid.ps1`.
- That PowerShell script calls `scripts/09_import_web_clipper_to_wikid_raw.py` before rebuilding the LLM Wikid index.
- Each clipped note receives `wikid_auto_category`, `wikid_concept`, `wikid_classification_basis`, and an `## Auto Classification` block.

## Review Rule
- Treat automatic classification as first-pass triage.
- Manually review notes in `general_reference/` first, then promote high-value notes into deeper source/concept/synthesis pages.
