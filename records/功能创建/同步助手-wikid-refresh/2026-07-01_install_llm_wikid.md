## 2026-07-01 13:20 install_llm_wikid

### Objective
将 GitHub 仓库 `https://github.com/shannhk/llm-wikid.git` 安装到当前 Obsidian vault 中，便于在 Obsidian 内浏览和使用 [[LLM Wikid]] 知识库模板。

### Input
- 输入来源：`https://github.com/shannhk/llm-wikid.git`
- 数据类型：Obsidian vault template / Markdown knowledge base
- 当前 vault：`E:\5-newplanet\new planet`

### Scripts
- 未生成分析脚本。

### Commands
```bash
git clone --depth 1 https://github.com/shannhk/llm-wikid.git llm-wikid
curl -L https://codeload.github.com/shannhk/llm-wikid/zip/refs/heads/main -o llm-wikid-main.zip
```

### Parameters
- install_path: `llm-wikid/`
- source_branch: `main`
- install_mode: GitHub zip download and local extraction

### Output
- 输出目录：`llm-wikid/`
- 关键文件：`llm-wikid/README.md`
- 关键文件：`llm-wikid/CLAUDE.md`
- 知识库入口：`llm-wikid/wiki/index.md`
- 原始资料入口：`llm-wikid/raw/clippings/`

### Result Summary
`llm-wikid` 已作为独立 Obsidian vault 模板安装到当前 vault 的 `llm-wikid/` 子目录。该仓库不是 Obsidian 社区插件；仓库中没有 `manifest.json`，因此不应安装到 `.obsidian/plugins/`。

### Interpretation
[[LLM Wikid]] 的核心用途是把原始资料放入 `raw/`，再由 AI agent 生成结构化 `wiki/` 页面并维护 `[[wikilinks]]`。当前安装方式保留了仓库原始结构，适合在 Obsidian 中直接打开 `llm-wikid/` 文件夹作为单独 vault，或在当前 vault 中作为一个子知识库浏览。

### Problems and Notes
- `git clone` 和 `git ls-remote` 访问 GitHub HTTPS 时出现连接重置。
- 改用 `https://codeload.github.com/shannhk/llm-wikid/zip/refs/heads/main` 下载 zip 成功。
- 当前 vault 未检测到 `.obsidian/plugins/obsidian-git` 插件。

### Decision Rationale
根据仓库 README，推荐安装方式是克隆为 `my-wiki` 并在 Obsidian 中作为 vault 打开。由于该仓库不是插件，选择安装到 `llm-wikid/` 子目录，避免污染当前 vault 的 `.obsidian/plugins/` 配置。

### Next Step
在 Obsidian 中打开 `llm-wikid/wiki/index.md` 查看入口；如需完整独立使用，可通过 Obsidian 的 Open Vault 选择 `E:\5-newplanet\new planet\llm-wikid`。
