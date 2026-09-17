## 2026-07-02 01:10 WeChat auto route button and schedule

### Objective
将微信同步后的 raw 分类流程从 Codex 对话框中移出，改为可被 Obsidian Shell Commands 手动触发、也可由 Windows 计划任务定时执行的自动化入口。

关联记录：[[2026-07-01_wechat_messenger_raw_input_spec]]

### Input
- 输入目录：`llm-wikid/raw/`
- 分类脚本：`scripts/06_auto_route_wechat_raw_refined.py`
- 刷新脚本：`scripts/02_refresh_llm_wikid.ps1`
- Obsidian Shell Commands 配置：`.obsidian/plugins/obsidian-shellcommands/data.json`
- Windows Task Scheduler

### Scripts
- `scripts/07_run_wechat_auto_route_refined.ps1`
- `scripts/08_register_wechat_auto_route_task.ps1`

### Commands
```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\07_run_wechat_auto_route_refined.ps1
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\07_run_wechat_auto_route_refined.ps1 -Embed
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\08_register_wechat_auto_route_task.ps1 -IntervalMinutes 15
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\08_register_wechat_auto_route_task.ps1 -Remove
```

### Parameters
- scheduled task name: `NewPlanet WeChat Auto Route`
- interval: `15` minutes
- embed: `false`
- log path: `result/YYYY-MM-DD_HHMMSS_wechat_auto_route_run.log`
- task action: `powershell.exe -NoProfile -ExecutionPolicy Bypass -File "E:\5-newplanet\new planet\scripts\07_run_wechat_auto_route_refined.ps1"`

### Output
- `scripts/07_run_wechat_auto_route_refined.ps1`
- `scripts/08_register_wechat_auto_route_task.ps1`
- `result/2026-07-02_010547_wechat_auto_route_run.log`
- `result/2026-07-02_010612_wechat_auto_route_run.log`
- `result/2026-07-02_011612_wechat_auto_route_run.log`
- `result/2026-07-02_011612_wechat_raw_auto_route_manifest.csv`
- `result/2026-07-02_wechat_raw_auto_route_manifest.csv`
- Windows scheduled task: `NewPlanet WeChat Auto Route`

### Result Summary
- 已注册 Windows 计划任务 `NewPlanet WeChat Auto Route`，每 15 分钟执行一次。
- 第一次自动执行扫描 `41` 条 raw 笔记，移动 `3` 条，导入 `38` 条，跳过 `3` 条，`qmd update` 成功。
- 手动触发验证任务后返回码为 `0`，扫描 `41` 条 raw 笔记，移动 `0` 条，导入 `38` 条，跳过 `3` 条，`qmd update` 成功。
- `scripts/07_run_wechat_auto_route_refined.ps1` 已补充每次运行的时间戳 manifest 副本，避免当天 manifest 被后续定时任务覆盖后丢失单次运行记录。
- Obsidian Shell Commands 中已有 `Refresh LLM Wikid` 命令，当前命令直接调用 `scripts/02_refresh_llm_wikid.ps1`；该脚本已经包含 refined routing，因此启用该插件后可从命令面板手动运行。

### Interpretation
当前链路变为：微信同步内容进入 `llm-wikid/raw/` 后，计划任务定时执行 `07_run_wechat_auto_route_refined.ps1`，该脚本调用 `02_refresh_llm_wikid.ps1`，再依次完成 refined raw routing、source card 归档和 `qmd update`。这把人工分类从交互流程中移除，同时保留 manifest 与日志，方便回溯误分样本。

### Problems and Notes
- PowerShell `ScheduledTasks` 模块在当前系统上返回 `Invalid class`，因此注册脚本改用 Windows Task Scheduler COM API，不依赖 `New-ScheduledTaskAction`。
- `schtasks.exe /Create` 对带空格 vault 路径的 `/TR` 参数解析不稳定，因此未继续使用该方案。
- 当前计划任务使用 interactive token，只在当前 Windows 用户可交互登录时稳定运行。
- `qmd embed` 仍默认关闭；需要同步更新向量索引时再用 `-Embed` 显式开启，避免每 15 分钟都触发较慢的 embedding 流程。

### Decision Rationale
优先复用既有 `scripts/02_refresh_llm_wikid.ps1`，避免复制分类、归档和 `qmd update` 逻辑。`07_` 脚本只负责提供稳定入口和运行日志，`08_` 脚本只负责注册或移除计划任务。这样按钮、计划任务、手动命令都能调用同一条自动化链路。

### Next Step
如需 Obsidian 内的显式按钮，可启用 `obsidian-shellcommands`，然后从命令面板执行 `Execute: Refresh LLM Wikid`；如需更像按钮的侧边栏或 ribbon 入口，再安装/启用 Commander 或 Buttons 插件，并让它调用同一个 PowerShell 命令。

## 2026-07-02 侧边栏主动刷新按钮

### Objective
为 [[LLM Wikid]] 刷新链路增加一个可固定在 Obsidian 左侧栏的主动调用按钮。

### Input
- Shell Commands 配置：`.obsidian/plugins/obsidian-shellcommands/data.json`
- Shell command ID：`refresh-llm-wikid`
- Shell command alias：`Refresh LLM Wikid`
- Buttons 插件：`buttons`
- 刷新脚本：`scripts/02_refresh_llm_wikid.ps1`

### Scripts
- `scripts/02_refresh_llm_wikid.ps1`

### Commands
```text
obsidian://shell-commands/?vault=new%20planet&execute=refresh-llm-wikid
```

### Parameters
- vault: `new planet`
- shell command ID: `refresh-llm-wikid`
- button note: `records/2026-07-02_llm_wikid_refresh_button.md`

### Output
- `records/2026-07-02_llm_wikid_refresh_button.md`

### Result Summary
已生成 Buttons 控制笔记 [[llm_wikid_refresh_button]]，按钮使用 Shell Commands 的 Obsidian URI 按内部 ID 调用 `refresh-llm-wikid`。

### Interpretation
当前 Buttons 插件适合生成笔记内按钮。将 [[llm_wikid_refresh_button]] 打开为阅读视图、拖到 Obsidian 左侧栏并固定后，即可作为侧边栏主动刷新入口使用。真正的左侧 ribbon 图标不是 Buttons 插件职责，若需要固定图标入口，应安装 Commander 并让 Commander 调用命令 `Execute: Refresh LLM Wikid`。

### Problems and Notes
- 未修改 `.obsidian/workspace.json`，避免直接写入 Obsidian 窗口布局造成现有工作区变化。
- Buttons 的 `type command` 依赖命令面板显示名精确匹配；本次优先使用 `obsidian://shell-commands/` URI 和内部 ID，稳定性更好。

### Decision Rationale
使用 Shell Commands 已存在的内部 ID `refresh-llm-wikid`，避免重复配置 PowerShell 命令，也避免按钮受命令面板显示名前缀变化影响。

### Next Step
在 Obsidian 中打开 [[llm_wikid_refresh_button]]，切换 Reading view，将标签页拖到左侧栏并 Pin。之后点击 `Refresh LLM Wikid` 即可主动执行刷新链路。
