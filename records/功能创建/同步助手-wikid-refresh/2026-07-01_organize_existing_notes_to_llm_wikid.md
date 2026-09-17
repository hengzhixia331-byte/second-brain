## 2026-07-01 13:31 organize_existing_notes_to_llm_wikid

### Objective
理解并应用 [[LLM Wikid]] 知识库模板，将当前 Obsidian vault 中已经存在的 Markdown 笔记整理为 `source` 与 `concept hub` 两层知识结构。

### Input
- 输入文件：当前 vault 内原有 `.md` 笔记
- 排除目录：`.obsidian/`、`llm-wikid/`、`records/`、`scripts/`、`result/`、`copilot/`、`Excalidraw/`
- 数据类型：Obsidian Markdown notes
- 物种与研究方向：以玉米、植物抗逆、植物表型、生物信息学分析为主要科学主题，同时保留 AI、投资、生活等非科研主题。

### Scripts
- `scripts/01_organize_existing_notes_to_llm_wikid.py`

### Commands
```bash
python scripts/01_organize_existing_notes_to_llm_wikid.py
```

### Parameters
- MIN_CONTENT_CHARS: 500
- source_dir: `llm-wikid/wiki/sources/`
- concept_dir: `llm-wikid/wiki/concepts/`
- output_report: `llm-wikid/wiki/outputs/vault_import_report.md`
- inventory_csv: `result/2026-07-01_vault_note_inventory.csv`
- skipped_csv: `result/2026-07-01_vault_note_skipped.csv`

### Output
- 总索引：`llm-wikid/wiki/index.md`
- 来源卡片：`llm-wikid/wiki/sources/vault-*.md`
- 主题枢纽：`llm-wikid/wiki/concepts/*.md`
- 整理报告：`llm-wikid/wiki/outputs/vault_import_report.md`
- 导入清单：`result/2026-07-01_vault_note_inventory.csv`
- 跳过清单：`result/2026-07-01_vault_note_skipped.csv`

### Result Summary
- 导入内容型笔记：37 篇
- 跳过笔记：81 篇
- 创建主题枢纽：10 个
- 原始笔记未移动、未改写、未删除

主题分布如下：

| Concept Hub | Imported Notes |
|---|---:|
| [[Maize Yield and Breeding]] | 10 |
| [[AI for Research]] | 7 |
| [[Bioinformatics Analysis]] | 5 |
| [[Research Tools and Methods]] | 5 |
| [[Career and Business Ideas]] | 2 |
| [[Finance and Investment]] | 2 |
| [[Maize Genetic Transformation]] | 2 |
| [[Plant Phenotyping and Imaging]] | 2 |
| [[Life and Health]] | 1 |
| [[Plant Stress Resilience]] | 1 |

### Interpretation
本次整理建立了一个“原始笔记不动、知识层可迭代”的结构。原笔记相当于 source，`llm-wikid/wiki/sources/` 中的卡片负责链接与概览；`llm-wikid/wiki/concepts/` 中的主题页负责聚合多个来源，便于后续做机制总结、实验设计对比、基因/通路/表型提取和跨笔记综合。

从植物科学角度看，当前 vault 的主要积累集中在玉米育种、植物抗逆、植物表型工具、玉米遗传转化和生信分析方法。后续最值得深入的方向是把这些 source cards 转换为机制型 synthesis，例如玉米耐旱耐热指标体系、玉米遗传转化瓶颈、表型工具与多组学联合分析策略。

### Problems and Notes
- 第一次运行脚本时，CSV 输出字段缺少 `slug` 与 `stem`，Python 原始错误完整暴露后已修正。
- PowerShell 默认输出中文显示异常，但 Python 以 UTF-8 读取生成文件内容正常。
- 被跳过的文件主要是插件/system 目录、Excalidraw 画布和短笔记。
- 当前整理为关键词确定性分类，不等同于人工深度阅读。

### Decision Rationale
选择索引式导入而非移动原笔记，是为了保护当前 Obsidian vault 的既有目录、图片引用和 wikilink 关系。[[LLM Wikid]] 本质强调 source tracing、concept hubs、confidence、counter-arguments 和 data gaps，因此第一步应先建立可追踪的知识层，再逐步做人工审核与深度 synthesis。

### Next Step
优先人工审阅 [[Bioinformatics Analysis]]、[[Maize Genetic Transformation]]、[[Plant Stress Resilience]]、[[Maize Yield and Breeding]] 和 [[Plant Phenotyping and Imaging]]。对近似重复内容先在原始笔记层面合并，再进行机制、基因、通路、表型和验证证据的深度整理。

## 2026-07-01 20:03 WeChat Messenger and LLM Wikid linkage

### Objective
确认 `wechat-messenger` 与 [[LLM Wikid]] 的实际联动逻辑，回答是否必须把文件单独交给 Codex，还是只要文件已经在 vault 里就可以直接整理。

### Input
- `llm-wikid/README.md`
- `llm-wikid/CLAUDE.md`
- `llm-wikid/.claude/settings.json`
- `llm-wikid/.claude/commands/wiki-ingest.md`
- `.obsidian/plugins/wechat-messenger/data.json`
- `.obsidian/plugins/wechat-messenger/manifest.json`

### Scripts
- 无新脚本

### Commands
```bash
Get-Content -Raw llm-wikid/README.md
Get-Content -Raw llm-wikid/CLAUDE.md
Get-Content -Raw llm-wikid/.claude/settings.json
Get-Content -Raw llm-wikid/.claude/commands/wiki-ingest.md
Get-Content -Raw .obsidian/plugins/wechat-messenger/data.json
Get-Content -Raw .obsidian/plugins/wechat-messenger/manifest.json
```

### Output
- `wechat-messenger` 是采集与本地化插件，不是 `[[LLM Wikid]]` 的知识编排引擎。
- `[[LLM Wikid]]` 的核心流程是 `raw/` -> 解析 -> 分类 -> `wiki/`，由 agent 或 Codex 读取 vault 内文件后生成结构化页面。
- 只要文件已经存在于 vault 里，就可以直接整理，不需要先“丢进 Codex”再人工搬运。

### Result Summary
`wechat-messenger` 会把微信内容同步到 vault 的指定目录，并处理图片、附件、本地化等采集动作；`[[LLM Wikid]]` 则负责把 vault 里的原始材料编译成 wiki 页面、source cards、concept hubs 和 `[[wikilinks]]` 网络。两者是串联关系，不是同一个系统。

### Interpretation
你的理解可以简化成一句话：`wechat-messenger` 负责把信息带进 vault，`[[LLM Wikid]]` 负责把信息变成知识。Codex 不需要接收“额外上传”的文件，只要它能读到当前 vault 中的 Markdown 和附件，就能按 `[[LLM Wikid]]` 的规则整理。

### Problems and Notes
- `wechat-messenger` 当前配置里有自动同步、图片本地化、附件下载等能力，但没有看到它自动生成 `wiki/` 页面或概念枢纽的逻辑。
- `[[LLM Wikid]]` 的整理流程仍依赖明确的 ingest/query 命令或 agent 运行，而不是 Obsidian 插件单独完成。

### Decision Rationale
把“采集”和“编排”拆开是最稳的。采集由插件负责，编排由 `[[LLM Wikid]]` 的 Claude/Codex 流程负责，这样 vault 里的原始记录可以持续积累，而知识层可以按需迭代，不需要中间再复制一份给 Codex。

### Next Step
如果你愿意，我下一步可以直接帮你把 `wechat-messenger` 产出的内容，整理成一套适合 `[[LLM Wikid]]` 的输入规范，让微信消息自动落到 `raw/bookmarks/`、`raw/ideas/` 或 `raw/articles/` 的对应位置。 

## 2026-07-01 20:43 Local watcher for WeChat Messenger -> LLM Wikid

### Objective
建立不依赖 GitHub 的本地联动方案，让 `wechat-messenger` 同步进 vault 后自动触发 `[[LLM Wikid]]` 刷新。

### Input
- `scripts/01_organize_existing_notes_to_llm_wikid.py`
- `scripts/02_refresh_llm_wikid.ps1`
- `scripts/03_watch_vault_refresh_llm_wikid.ps1`
- `.obsidian/plugins/wechat-messenger/data.json`
- `llm-wikid/wiki/`

### Scripts
- `scripts/01_organize_existing_notes_to_llm_wikid.py`
- `scripts/02_refresh_llm_wikid.ps1`
- `scripts/03_watch_vault_refresh_llm_wikid.ps1`

### Commands
```bash
python scripts/01_organize_existing_notes_to_llm_wikid.py
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\02_refresh_llm_wikid.ps1
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\03_watch_vault_refresh_llm_wikid.ps1
```

### Parameters
- PollSeconds: 15
- QuietSeconds: 60
- MIN_CONTENT_CHARS: 500

### Output
- `llm-wikid/wiki/index.md`
- `llm-wikid/wiki/sources/vault-*.md`
- `llm-wikid/wiki/concepts/*.md`
- `llm-wikid/wiki/outputs/vault_import_report.md`
- `result/*_vault_note_inventory.csv`
- `result/*_vault_note_skipped.csv`
- `result/watcher_stdout.txt`

### Result Summary
- `scripts/01_organize_existing_notes_to_llm_wikid.py` 已改为按当前日期生成结果名，不再写死 `2026-07-01`。
- `scripts/01_organize_existing_notes_to_llm_wikid.py` 已改为保留既有 `date_created`，只更新 `date_modified`。
- `scripts/03_watch_vault_refresh_llm_wikid.ps1` 已能在后台常驻，日志显示 `watcher started`。
- `scripts/02_refresh_llm_wikid.ps1` 已成功运行并更新 `llm-wikid/wiki`。

### Interpretation
现在的链路是：`wechat-messenger` 把内容同步进 vault -> watcher 检测到 Markdown 变化 -> 调用 `02_refresh_llm_wikid.ps1` -> 运行 `01_organize_existing_notes_to_llm_wikid.py` -> `qmd update` 刷新索引。  
这意味着你不需要手动把文件交给 Codex，只要它在 vault 中，自动链路就能处理。

### Problems and Notes
- 初次后台启动时，PowerShell 参数中的空格路径导致 `-File` 解析失败，已通过给脚本路径加引号修正。
- `03_watch_vault_refresh_llm_wikid.ps1` 使用轮询，不是文件系统事件监听，所以有 15 秒轮询和 60 秒静默窗口。
- `qmd` 当前只跑了 `update`，后续如果你要更强搜索，还可以单独补 `qmd embed`。

### Decision Rationale
选择轮询而不是事件监听，是为了先做出稳定、少依赖的本地链路。当前实现完全放在 vault 内，便于你直接接在 `wechat-messenger` 后面，不需要额外服务。

### Next Step
如果你要，我下一步可以继续做两件事之一：  
1. 把 `wechat-messenger` 的落盘目录进一步细分成 `raw/bookmarks/`、`raw/articles/`、`raw/ideas/` 的输入规范。  
2. 给 watcher 加一个可选的 `qmd embed` 步骤，自动更新向量索引。
