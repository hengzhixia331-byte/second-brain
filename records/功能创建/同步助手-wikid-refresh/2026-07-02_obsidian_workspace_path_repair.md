## 2026-07-02 12:07 obsidian_workspace_path_repair

### Objective
定位并修复运行 [[llm_wikid_refresh_button]] 后 raw 笔记被外部脚本移动，导致 Obsidian 最近文件列表仍指向旧路径、笔记打开失败或无法删除的问题。

### Input
- 输入文件：
  - [[微信 agent 体验完微信Agent以后，我觉得这就是微信有史以来最大的更新。]]
  - [[学习 AI 这个封装了我3年自媒体经验的AI热点网站，今天向所有人免费开放。]]
  - [[app 蒸馏 盘点16个把自己蒸馏成Skills的国民级App。]]
- Obsidian 按钮：[[llm_wikid_refresh_button]]
- 工作区状态：`.obsidian/workspace.json`
- 数据类型：Obsidian Markdown vault 自动分类与路径缓存
- 物种：不适用

### Scripts
- `scripts/02_refresh_llm_wikid.ps1`
- `scripts/06_auto_route_wechat_raw_refined.py`
- `scripts/10_repair_obsidian_workspace_paths.py`

### Commands
```bash
python scripts/06_auto_route_wechat_raw_refined.py
python scripts/10_repair_obsidian_workspace_paths.py
```

### Parameters
- raw_root: `llm-wikid/raw`
- workspace: `.obsidian/workspace.json`
- route_manifest: `result/2026-07-02_wechat_raw_auto_route_manifest.csv`
- workspace_repair_manifest: `result/2026-07-02_120247_obsidian_workspace_path_repair_manifest.csv`

### Output
- 修改：`scripts/06_auto_route_wechat_raw_refined.py`
- 新增：`scripts/10_repair_obsidian_workspace_paths.py`
- 修改：`scripts/02_refresh_llm_wikid.ps1`
- 输出：`result/2026-07-02_wechat_raw_auto_route_manifest.csv`
- 输出：`result/2026-07-02_120247_obsidian_workspace_path_repair_manifest.csv`

### Result Summary
- [[微信 agent 体验完微信Agent以后，我觉得这就是微信有史以来最大的更新。]] 的真实文件位置为 `llm-wikid/raw/articles/待细分/微信 agent 体验完微信Agent以后，我觉得这就是微信有史以来最大的更新。.md`。
- [[学习 AI 这个封装了我3年自媒体经验的AI热点网站，今天向所有人免费开放。]] 的真实文件位置为 `llm-wikid/raw/articles/学习AI/工具流程/学习 AI 这个封装了我3年自媒体经验的AI热点网站，今天向所有人免费开放。.md`。
- [[app 蒸馏 盘点16个把自己蒸馏成Skills的国民级App。]] 当前没有找到 raw 原文，只剩 `llm-wikid/wiki/sources/vault-app-蒸馏-盘点16个把自己蒸馏成skills的国民级app.md` 源卡片。
- `scripts/06_auto_route_wechat_raw_refined.py` 已修复：`raw/articles/*.md`、`raw/ideas/*.md`、`raw/bookmarks/*.md` 不再被视为已完成分类，会继续进入叶子目录或 `待细分`。
- `scripts/10_repair_obsidian_workspace_paths.py` 已新增：根据 manifest 和当前 raw 文件索引替换 Obsidian `lastOpenFiles` 中的旧路径，无法定位真实文件的旧路径会从最近文件列表移除。

### Interpretation
这不是 Markdown 文件内容损坏，而是外部 Python 脚本用 `shutil.move` 移动文件后，Obsidian 当前会话仍缓存旧路径。旧路径例如 `llm-wikid/raw/微信 agent ...md` 已不存在，所以 Obsidian 会表现为打开失败；对不存在的假路径执行删除，也会表现为无法删除。

### Problems and Notes
- 当前 Obsidian 进程正在运行，`.obsidian/workspace.json` 会被 Obsidian 内存状态写回；因此外部脚本直接修复 workspace 文件后，可能被正在运行的 Obsidian 覆盖。
- 路径缓存修复脚本适合在 Obsidian 关闭后执行，或作为后续后台/定时修复流程的基础。
- [[app 蒸馏 盘点16个把自己蒸馏成Skills的国民级App。]] 的 raw 原文当前缺失，需要后续从同步源重新拉取或从备份恢复；本次没有凭源卡片摘要重建原文，避免生成不完整假原文。

### Decision Rationale
优先修正自动分类脚本的入口层判定，避免新同步文件停在 `raw/articles`、`raw/ideas`、`raw/bookmarks` 根层。对 Obsidian 最近文件缓存，使用结构化 JSON 和 manifest 精确替换路径；对无法定位真实文件的条目只清理缓存，不伪造原始笔记。

### Next Step
关闭 Obsidian 后运行 `python scripts/10_repair_obsidian_workspace_paths.py`，再重新打开 vault，可清理当前会话缓存里残留的假路径。后续如果需要完全自动化，应增加一个“Obsidian 退出后再修复 workspace”的后台任务。
