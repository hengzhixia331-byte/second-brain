## 2026-07-02 02:38 web_clipper_to_wikid_raw

### Objective
将 Obsidian Web Clipper 抓取的网站资料接入 `llm-wikid/raw/clippings/`，在 clippings 内建立分类准则、自动分类子目录和剪藏元数据，并复用已有按钮 [[llm_wikid_refresh_button]] 触发完整刷新。

### Input
- 输入文件：`Clippings/*.md` 或 `llm-wikid/raw/clippings/*.md`
- 参考基因组：不适用
- 物种：不限定；分类规则优先覆盖植物科学、玉米育种、植物逆境、生信分析、AI 工具、财经、生活健康与商业想法
- 数据类型：Obsidian Web Clipper Markdown 网页剪藏

### Scripts
- `scripts/09_import_web_clipper_to_wikid_raw.py`
- `scripts/02_refresh_llm_wikid.ps1`
- `scripts/06_auto_route_wechat_raw_refined.py`
- `scripts/01_organize_existing_notes_to_llm_wikid.py`

### Commands
```bash
python scripts/09_import_web_clipper_to_wikid_raw.py
python -m py_compile scripts/09_import_web_clipper_to_wikid_raw.py scripts/01_organize_existing_notes_to_llm_wikid.py scripts/06_auto_route_wechat_raw_refined.py
powershell -NoProfile -ExecutionPolicy Bypass -File "E:\5-newplanet\new planet\scripts\02_refresh_llm_wikid.ps1"
```

### Parameters
- Web Clipper 兼容入口：`Clippings/*.md`
- Wikid raw 入口：`llm-wikid/raw/clippings/`
- 分类准则笔记：`llm-wikid/raw/clippings/Web Clipper Classification Rules.md`
- 自动分类字段：`wikid_auto_category`, `wikid_concept`, `wikid_classification_basis`, `wikid_classified_at`
- random_seed：不适用

### Output
- 输出脚本：`scripts/09_import_web_clipper_to_wikid_raw.py`
- 更新按钮链路：`scripts/02_refresh_llm_wikid.ps1`
- 分类准则：`llm-wikid/raw/clippings/Web Clipper Classification Rules.md`
- 已分类剪藏：`llm-wikid/raw/clippings/bioinformatics_analysis/使用GCTA （GREML）来估计SNP-遗传力 SNP Heritability.md`
- Manifest：`result/2026-07-02_023759_web_clipper_import_manifest.csv`

### Result Summary
新增 Web Clipper 导入脚本后，按钮刷新链路变为：Web Clipper 剪藏导入与分类 -> 微信 raw 路由 -> LLM Wikid source/concept 重建 -> `qmd update`。现有 1 条 GCTA/GREML 剪藏被归入 `bioinformatics_analysis/`，并写入 [[Bioinformatics Analysis]] 相关元数据和 `## Auto Classification` 区块。

### Interpretation
技术上，网页剪藏现在拥有稳定入口、可复现分类规则和 manifest 追踪。知识管理上，植物科学与生信资料会优先进入与 [[Plant Stress Resilience]]、[[Maize Genetic Transformation]]、[[Maize Yield and Breeding]]、[[Plant Phenotyping and Imaging]]、[[Bioinformatics Analysis]] 等主题一致的 clippings 子目录，便于后续人工复核和 wiki 编译。

### Problems and Notes
PowerShell 控制台显示中文内容时存在编码显示异常，但 Python 按 UTF-8 读取分类准则文件时中文内容正常。根目录 `Clippings/` 当前为空，因此本次没有从兼容入口移动新文件。

### Decision Rationale
保留 `Clippings/*.md` 作为兼容入口，同时推荐 Web Clipper 直接保存到 `llm-wikid/raw/clippings/{{title}}`。自动分类采用确定性关键词规则，不调用外部模型，便于复现和手动调整。`scripts/06_auto_route_wechat_raw_refined.py` 对 `clippings/` 保持原位，避免网页剪藏被微信路由规则搬出 clippings。

### Next Step
在 Obsidian Web Clipper 中将保存位置设置为 `llm-wikid/raw/clippings/{{title}}`。后续如发现 `general_reference/` 中积累较多高价值资料，应把关键词补充进 `scripts/09_import_web_clipper_to_wikid_raw.py` 的 `CATEGORY_RULES`。
