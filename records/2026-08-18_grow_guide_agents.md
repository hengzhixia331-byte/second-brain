## 2026-08-18 介入 llm-wikid grow guide

### Objective
将 `llm-wikid/README.md` 的增长逻辑写入仓库级 `AGENTS.md`，作为后续 Obsidian 知识库的执行准则。

### Input
- 输入文件：`llm-wikid/README.md`
- 现有约束：仓库级工作目录、脚本、记录、结果规则

### Scripts
- 无

### Commands
```bash
# 无
```

### Parameters
- 无

### Output
- `AGENTS.md`

### Result Summary
新增仓库级 `AGENTS.md`，加入 `LLM Wikid` 型 grow guide、知识循环、Obsidian 规范、脚本/记录/结果约束。

### Interpretation
把“先编译再回答、先链接再扩展、先回写再总结”写成仓库级规则，有助于让知识库随使用持续增长。

### Problems and Notes
- 原仓库根目录未发现 `AGENTS.md`，因此新建文件。

### Decision Rationale
直接把 `README.md` 中的系统逻辑压缩成可执行约束，避免后续执行时只停留在理念层。

### Next Step
后续可将 `wiki/` 的 ingest/query/lint 流程进一步落成脚本或模板。

