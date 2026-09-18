## 2026-09-18 Refresh button stability

### Objective
修复 LLM Wikid 刷新按钮导致 Obsidian 笔记被移动后，旧标签仍显示但打开失败的问题。

### Input
- 输入文件：`llm-wikid/raw/**/*.md`、根目录 `Clippings/*.md`
- 工作区状态：`.obsidian/workspace.json`
- 物种：不适用
- 数据类型：Obsidian Markdown 笔记

### Scripts
- `scripts/02_refresh_llm_wikid.ps1`
- `scripts/06_auto_route_wechat_raw_refined.py`
- `scripts/09_import_web_clipper_to_wikid_raw.py`
- `scripts/10_repair_obsidian_workspace_paths.py`

### Changes
- 自动路由读取 `.obsidian/workspace.json` 的 `lastOpenFiles`，跳过当前打开的笔记，不再移动其路径。
- Web Clipper 导入和分类同样跳过当前打开的笔记。
- 工作区修复改为先复制 `workspace.json.before-refresh`，再使用临时文件和 `os.replace` 原子更新。
- 工作区修复继续输出路径修复清单，便于追踪被延后的笔记。

### Validation
- Python 语法检查通过：
  - `python -m py_compile scripts/06_auto_route_wechat_raw_refined.py scripts/09_import_web_clipper_to_wikid_raw.py scripts/10_repair_obsidian_workspace_paths.py`
- 使用 Python 校验当前 `.obsidian/workspace.json` 为合法 JSON。
- 未直接执行全量刷新，避免在验证阶段再次移动笔记。

### Result Summary
刷新过程中，当前正在打开的笔记保持原路径；关闭笔记后，下次刷新才会重新参与自动分类。

### Interpretation
问题根因不是 Markdown 内容被删除，而是自动路由使用 `shutil.move` 改变了正在打开笔记的路径。Obsidian 标签保留旧路径，因此形成“名称仍在、文件打不开”的表象。

### Problems and Notes
- PowerShell `ConvertFrom-Json` 读取当前工作区时受默认嵌套深度限制影响；Python `json.loads` 校验通过。
- 当前修改未恢复历史上已经失效的旧标签；重新打开前可关闭失效标签，或运行一次修复脚本。

### Next Step
关闭需要整理的笔记后，再点击刷新按钮；观察输出中 `skip_open_note` 和 `deferred_open_note` 记录。

## 2026-09-18 CRISPR-Combo note image repair

### Objective
修复 [[CRISPR-Combo突破多年生植物再生瓶颈 Nature Communications｜CRISPR-Combo在马铃薯、柑橘、草莓和杨树中实现高效再生与编辑]] 中两处无法加载的远程图片。

### Input
- 输入文件：`llm-wikid/raw/articles/科研/玉米遗传转化/CRISPR-Combo突破多年生植物再生瓶颈 Nature Communications｜CRISPR-Combo在马铃薯、柑橘、草莓和杨树中实现高效再生与编辑.md`
- 失效链接：`https://relay-1.bijitongbu.site/p/ce3ad5b48dc7ed7d3ab8405cf1cc802f.png`
- 失效链接：`https://relay-1.bijitongbu.site/p/e3e324a2b3dd5351be7a807b0f0ebff5.png`

### Scripts
- 无新增脚本

### Commands
```bash
# 使用 HEAD 请求确认两个远程图片均返回 404
# 使用本地占位 PNG 替换远程坏链
```

### Output
- `result/2026-09-18_crispr_combo_missing_section_icon.png`
- `result/2026-09-18_crispr_combo_missing_regeneration_figure.png`

### Result Summary
两个远程图片链接均已替换为 Obsidian 本地嵌入图片，笔记不再依赖已失效的 relay 图片服务。

### Interpretation
图片无法加载的直接原因是远程中转链接返回 404，不是 Markdown 语法或 Obsidian 设置问题。当前修复采用本地占位图保留版面位置和失效来源，避免坏链继续影响阅读。

### Problems and Notes
未在仓库中找到这两个哈希对应的原始图片文件；如果后续拿到原图，可直接覆盖同名 `result/2026-09-18_crispr_combo_missing_*.png` 文件。

### Next Step
建议后续批量扫描 `relay-1.bijitongbu.site` 图片链接，将可下载图片本地化，404 图片统一标记并回源补图。
