## 2026-09-17 14:00 fix_shell_commands_button

### Objective
修复 [[llm_wikid_refresh_button]] 点击后无法识别 Shell commands 操作的问题。

### Input
- 输入文件：`llm_wikid_refresh_button.md`
- Vault：`E:\5-newplanet\new planet`
- 数据类型：Obsidian Button / Shell commands URI

### Scripts
- `scripts/02_refresh_llm_wikid.ps1`

### Commands
```text
obsidian://shell-commands/?vault=new%20planet&execute=refresh-llm-wikid
```

### Parameters
- shell command id: `refresh-llm-wikid`
- plugin: `obsidian-shellcommands` 0.23.0

### Output
- 修改 `.obsidian/community-plugins.json`
- 保留 `llm_wikid_refresh_button.md` 中的 Shell commands URI

### Result Summary
已将 `obsidian-shellcommands` 加入社区插件启用清单。插件配置中的 `refresh-llm-wikid` 命令 ID 与按钮 URI 一致。

### Interpretation
问题不是命令 ID 或 URI 拼写错误，而是插件未启用，导致 Obsidian 无法注册 `shell-commands` URI 操作。

### Problems and Notes
Obsidian 需要重新加载插件或重启后，新增启用清单才会生效。

### Decision Rationale
采用启用正确插件的最小修复，不增加按钮端兼容逻辑。

### Next Step
在 Obsidian 中执行 Reload app 或重启，然后点击按钮验证。
