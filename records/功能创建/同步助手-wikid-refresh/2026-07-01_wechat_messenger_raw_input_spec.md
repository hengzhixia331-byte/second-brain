---
banner: "![[2f3d44d4f3bd7073269a87ba66de6198_MD5.png]]"
---
## 2026-07-01 22:07 WeChat Messenger raw organization and watcher update

### Objective
将 `wechat-messenger` 的落盘规范细分到 `llm-wikid/raw/bookmarks/`、`llm-wikid/raw/articles/`、`llm-wikid/raw/ideas/`，并把当前 vault 里按主题分组的微信内容整体迁入 `llm-wikid/raw/` 体系。

关联记录：[[2026-07-01_organize_existing_notes_to_llm_wikid]]

### Input
- `wechat-messenger` 当前配置：`.obsidian/plugins/wechat-messenger/data.json`
- 现有主题分组：`学习AI/`、`生活/`、`科研/`、`股票/`、`赚钱想法/`
- `llm-wikid/raw/` 目录结构
- `scripts/01_organize_existing_notes_to_llm_wikid.py`
- `scripts/03_watch_vault_refresh_llm_wikid.ps1`

### Scripts
- `scripts/04_migrate_wechat_groups_to_raw.py`
- `scripts/01_organize_existing_notes_to_llm_wikid.py`
- `scripts/03_watch_vault_refresh_llm_wikid.ps1`

### Commands
```bash
python scripts/04_migrate_wechat_groups_to_raw.py
python scripts/01_organize_existing_notes_to_llm_wikid.py
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\02_refresh_llm_wikid.ps1
```

### Parameters
- raw folder template: `llm-wikid/raw/{{{labels.0.name}}}`
- attachmentFolder: `llm-wikid/raw/assets`
- imageAttachmentFolder: `llm-wikid/raw/assets/images`
- PollSeconds: 15
- QuietSeconds: 60
- MIN_CONTENT_CHARS: 500

### Input Specification
`wechat-messenger` 的第一标签必须写成 raw-relative path。插件会把 `labels.0.name` 拼到 `llm-wikid/raw/` 后面。

| Source Type | First Label Pattern | Landing Directory | Use Case |
|---|---|---|---|
| bookmark | `bookmarks/<当前分组>` | `llm-wikid/raw/bookmarks/<当前分组>/` | 只含 URL、短链接、待解析网页入口 |
| article | `articles/<当前分组>` | `llm-wikid/raw/articles/<当前分组>/` | 公众号长文、网页正文、研究新闻、教程文章 |
| idea | `ideas/<当前分组>` | `llm-wikid/raw/ideas/<当前分组>/` | 自己的想法、项目构思、赚钱想法、微信合并消息 |

当前已迁移分组映射如下。

| Original Group | Raw Target |
|---|---|
| `学习AI/` | `llm-wikid/raw/articles/学习AI/` |
| `生活/` | `llm-wikid/raw/articles/生活/` |
| `科研/` | `llm-wikid/raw/articles/科研/` |
| `股票/` | `llm-wikid/raw/articles/股票/` |
| `赚钱想法/` | `llm-wikid/raw/ideas/赚钱想法/` |

### Output
- `llm-wikid/raw/articles/学习AI/`
- `llm-wikid/raw/articles/生活/`
- `llm-wikid/raw/articles/科研/`
- `llm-wikid/raw/articles/股票/`
- `llm-wikid/raw/ideas/赚钱想法/`
- `result/2026-07-01_wechat_raw_migration_manifest.csv`
- `result/2026-07-01_vault_note_inventory.csv`
- `result/2026-07-01_vault_note_skipped.csv`
- `llm-wikid/wiki/index.md`
- `llm-wikid/wiki/outputs/vault_import_report.md`

### Result Summary
- 现有 5 个主题分组、共 37 个文件已整体迁入 `llm-wikid/raw/`。
- `学习AI`、`生活`、`科研`、`股票` 映射到 `llm-wikid/raw/articles/`，`赚钱想法` 映射到 `llm-wikid/raw/ideas/`。
- `scripts/01_organize_existing_notes_to_llm_wikid.py` 已改为只读取 `llm-wikid/raw/`，重跑后导入 34 条、跳过 3 条短记录。
- `scripts/03_watch_vault_refresh_llm_wikid.ps1` 已改为只监控 `llm-wikid/raw/`，后续 raw 变化会触发刷新。
- `qmd update` 已完成，提示还有 58 个 unique hashes 需要 `qmd embed` 生成向量。

### Interpretation
这次调整把 `wechat-messenger` 明确成 `raw` 输入端，而把 [[LLM Wikid]] 维持为编译端。当前插件配置里，`folder` 指向 `llm-wikid/raw/{{{labels.0.name}}}`，`messageFolder` 留空时会复用该目录，因此微信同步时只要第一标签命中 `bookmarks`、`articles` 或 `ideas`，就会落到对应 raw 分类。

### Problems and Notes
- 这次迁移把原根目录分组目录整体移动到了 `llm-wikid/raw/` 体系内。
- 原始微信笔记里有大量 `![[笔记同步助手/images/...]]` 引用，因此迁移脚本同时把图片引用改成了 `llm-wikid/raw/assets/images/...`。
- `result/2026-07-01_vault_note_skipped.csv` 里的 3 条记录都是 `ideas/赚钱想法/` 下的超短笔记。

### Decision Rationale
优先把输入层整理到 `raw/`，再让 watcher 盯住 `raw`，这样后续不用再同时维护根目录主题分组和 `llm-wikid/raw` 两套入口。保留 `messageFolder` 为空，是为了让合并消息继续沿用文章目录模板，不额外引入第二套目录规则。

### Next Step

## 2026-07-01 22:48 watcher diagnosis after manual sync

### Objective
解释为什么点击笔记同步助手同步后没有稳定自动进入 [[LLM Wikid]]，并定位 `embed` 开关位置。

### Input
- 同步助手配置：`.obsidian/plugins/wechat-messenger/data.json`
- watcher 脚本：`scripts/03_watch_vault_refresh_llm_wikid.ps1`
- refresh 脚本：`scripts/02_refresh_llm_wikid.ps1`
- 归档脚本：`scripts/01_organize_existing_notes_to_llm_wikid.py`
- 跳过清单：`result/2026-07-01_vault_note_skipped.csv`

### Scripts
- `scripts/03_watch_vault_refresh_llm_wikid.ps1`
- `scripts/02_refresh_llm_wikid.ps1`
- `scripts/01_organize_existing_notes_to_llm_wikid.py`

### Commands
```bash
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\02_refresh_llm_wikid.ps1
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\02_refresh_llm_wikid.ps1 -Embed
```

### Parameters
- watcher RawRoot: `llm-wikid/raw`
- watcher QuietSeconds: 60
- watcher RunQmdEmbed: `$false`
- refresh optional switch: `-Embed`
- MIN_CONTENT_CHARS: 500

### Output
- 本次仅追加诊断记录，未修改脚本、插件配置或 [[LLM Wikid]] 内容。

### Result Summary
- 当前 watcher 只监听 `llm-wikid/raw/**/*.md`，不会监听同步助手插件内部事件。
- 当前同步助手配置里的 `folder` 为 `{{{labels.0.name}}}`，并不是强制前缀 `llm-wikid/raw/{{{labels.0.name}}}`；因此标签若不是 raw-relative path，新内容会落到 watcher 监听范围外。
- `scripts/03_watch_vault_refresh_llm_wikid.ps1` 第 8 行为 `$RunQmdEmbed = $false`，因此 watcher 触发时默认只执行 `qmd update`，不会执行 `qmd embed`。
- `scripts/02_refresh_llm_wikid.ps1` 第 1-2 行定义 `-Embed` 开关，第 14-15 行只有收到 `-Embed` 时才运行 `qmd embed`。
- Obsidian Shell Commands 当前只有 `Refresh LLM Wikid`，命令未带 `-Embed`。
- `llm-wikid/raw/ideas/赚钱想法/同步助手_2026-07-01.md` 在跳过清单中被标记为 `skip_short_note`，正文长度为 326，低于 `MIN_CONTENT_CHARS = 500`，因此不会生成 source card。

### Interpretation
这次“没有自动添加到 wikid”更准确地说有三类原因：第一，watcher 是文件系统轮询器，不是同步助手内部 hook；第二，输入必须稳定落入 `llm-wikid/raw`，否则 watcher 看不到；第三，即使 watcher 触发，短笔记仍会被归档脚本按输入规范跳过，且语义向量 `embed` 默认关闭。

### Problems and Notes
- 当前检测到两个 `03_watch_vault_refresh_llm_wikid.ps1` PowerShell 进程，应后续只保留一个 watcher，避免重复刷新。
- 若希望点击同步助手后自动归档，建议不要改同步助手插件源码，而是在 watcher 中同时监听 `.obsidian/plugins/wechat-messenger/data.json` 的 `syncAt` 与 `llm-wikid/raw` 文件稳定状态。
- 若要把短消息合并记录也纳入 [[LLM Wikid]]，优先修正输入：让同步助手把消息合并到足够长的主题笔记，或明确将短消息作为 bookmark/idea 类型单独处理；不建议在归档脚本里堆叠多分支兼容逻辑。

### Decision Rationale
优先保持输入层规范：同步助手负责把内容写入 raw，watcher 只在 raw 稳定后刷新 [[LLM Wikid]]。`embed` 单独作为开关保留，是因为生成向量索引通常更慢，也可能依赖本地模型或远程 API，不应默认每次短同步都强制运行。

### Next Step
可将现有 watcher 改造成 `同步助手完成同步 -> 等待 raw 目录静默 -> 运行归档 -> 可选运行 qmd embed` 的线性脚本，并把 Obsidian Shell Commands 里的 `Refresh LLM Wikid` 命令加上 `-Embed` 或新增一个独立的 `Refresh LLM Wikid With Embed` 命令。

## 2026-07-01 23:27 automatic routing enabled

### Objective
去除同步后手动分类步骤，让新同步内容自动进入规范 raw 子目录，并继续生成 [[LLM Wikid]] source card。

### Input
- 同步助手配置：`.obsidian/plugins/wechat-messenger/data.json`
- 自动路由脚本：`scripts/05_auto_route_wechat_raw.py`
- 刷新脚本：`scripts/02_refresh_llm_wikid.ps1`
- 归档脚本：`scripts/01_organize_existing_notes_to_llm_wikid.py`

### Scripts
- `scripts/05_auto_route_wechat_raw.py`
- `scripts/02_refresh_llm_wikid.ps1`
- `scripts/03_watch_vault_refresh_llm_wikid.ps1`

### Commands
```bash
python scripts/05_auto_route_wechat_raw.py
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/02_refresh_llm_wikid.ps1
```

### Parameters
- 自动路由源目录：`llm-wikid/raw`
- 自动路由结果目录：`llm-wikid/raw/articles|bookmarks|ideas`
- 股票主题默认子类：`前沿消息`
- 科研主题默认子类：`科研工具|玉米遗传转化|植物抗逆|育种改良`

### Output
- `result/2026-07-01_wechat_raw_auto_route_manifest.csv`
- `llm-wikid/raw/articles/股票/前沿消息/股票大调整 5%调至10%！A股重大调整！下周一，正式实施.md`
- `llm-wikid/wiki/sources/vault-股票大调整-5-调至10-a股重大调整-下周一-正式实施.md`

### Result Summary
- 新同步的股票文章已经从非规范入口自动搬到 `llm-wikid/raw/articles/股票/前沿消息/`。
- 对应的 [[LLM Wikid]] source card 已生成，不再需要手动拖拽到 articles 目录。
- 现有 watcher/refresh 链路已经变成：同步助手落 raw -> 自动路由 -> 归档脚本 -> wiki 更新。

### Interpretation
你的核心诉求其实不是“加强分类器”，而是“把人工分类这一步从流程里删除”。现在这个自动路由已经把分类责任从你手里移到脚本里了。它仍然是规则驱动的，但不再要求你逐篇手动整理目录。

### Problems and Notes
- 目前自动路由只覆盖同步助手新产生的非规范一级目录；已在规范目录中的 raw 文件不会重复搬运。
- 路由结果仍依赖关键词规则，遇到跨主题文章可能需要再补一轮规则，不建议先上复杂模型。

### Decision Rationale
先用确定性规则把输入整理进规范目录，再走原有 wiki 生成链路。这样最稳定，也最符合“优先修正输入而非增加代码兼容”的原则。

### Next Step
如果你认可这个方向，我下一步可以继续把 `scripts/05_auto_route_wechat_raw.py` 的股票/科研规则细化到你常用的主题树里，让它更少误分。

## 2026-07-02 00:35 refined raw routing rules

### Objective
细化 `llm-wikid/raw` 自动路由子类规则，减少同步助手新内容进入错误 leaf 目录的概率。

### Input
- 当前 raw 目录树：`llm-wikid/raw/articles|ideas|bookmarks`
- 自动路由脚本：`scripts/06_auto_route_wechat_raw_refined.py`
- 刷新脚本：`scripts/02_refresh_llm_wikid.ps1`

### Scripts
- `scripts/06_auto_route_wechat_raw_refined.py`
- `scripts/02_refresh_llm_wikid.ps1`

### Commands
```bash
python scripts/06_auto_route_wechat_raw_refined.py
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/02_refresh_llm_wikid.ps1
```

### Parameters
- routing evidence: filename plus non-canonical raw label
- ignored evidence: full WeChat article body and sync-helper template fields
- output manifest: `result/2026-07-02_wechat_raw_auto_route_manifest.csv`

### Output
- `scripts/06_auto_route_wechat_raw_refined.py`
- `result/2026-07-02_wechat_raw_auto_route_manifest.csv`
- refined `llm-wikid/raw/articles/科研/...`
- refined `llm-wikid/raw/articles/股票/...`
- refined `llm-wikid/raw/articles/学习AI/...`
- refined `llm-wikid/raw/ideas/赚钱想法/...`

### Result Summary
- 已细化科研分支：植物抗逆、耐高温、耐光强、耐寒、耐旱、耐盐、玉米遗传转化、玉米知识体系、育种改良、科研工具、生信工具、高温表型工具。
- 已细化股票分支：前沿消息、大牛博主学思路。
- 已细化学习AI分支：代码自动化、模型观察。
- 已细化赚钱想法分支：生图变现、品牌内容、求职转型、视觉网站、工具流程。
- 完整刷新后 `scripts/06_auto_route_wechat_raw_refined.py` 第二次运行移动数为 0，说明当前规则稳定。

### Interpretation
第一版细化规则误用了全文匹配，微信文章底部推荐链接会污染分类。因此已改为主要依赖文件名和非规范入口标签，避免同步助手模板字段如“笔记同步助手”触发全局误分。

### Problems and Notes
- `ideas/赚钱想法/工具流程/Content extracted from webpage 飞书.md` 仍保留为兜底记录，因为文件名缺少足够语义。
- 后续如果新增固定公众号或固定标签，可以继续在 `ROUTE_RULES` 中加高精度标题规则。

### Decision Rationale
自动分类优先使用高精度规则，而不是全文关键词堆叠。对植物科研内容，规则优先落到具体生物学主题；对跨域内容，优先根据文件名主题而不是正文末尾链接。

### Next Step
继续积累误分样本，把新增规则写成短标题关键词或固定标签映射，避免引入全文语义误判。
补充可选 `qmd embed` 开关，让 watcher 在需要语义检索时自动更新向量索引。
