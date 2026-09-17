## 2026-08-25 生成植物育种与生物信息学简历

### Objective
结合 vault 知识网络与既有交流，生成一份最大化展示植物科学、玉米育种、生物信息学、智能表型和 AI 育种能力的中文简历。

### Input
- 输入知识页：`llm-wikid/wiki/index.md`
- 输入知识页：`llm-wikid/wiki/concepts/Maize Yield and Breeding.md`
- 输入知识页：`llm-wikid/wiki/concepts/Plant Stress Resilience.md`
- 输入知识页：`llm-wikid/wiki/concepts/Plant Phenotyping and Imaging.md`
- 输入知识页：`llm-wikid/wiki/concepts/Bioinformatics Analysis.md`
- 输入知识页：`llm-wikid/wiki/concepts/Maize Genetic Transformation.md`
- 物种与方向：以玉米为核心，延伸至一般作物抗逆与智能育种

### Scripts
- 本次未生成脚本；任务为知识库内容综合与简历写作。

### Commands
```powershell
Get-ChildItem -File -Recurse llm-wikid\wiki -Filter *.md
Get-Content -Raw llm-wikid\wiki\index.md
```

### Parameters
- 输出语言：中文
- 输出风格：专业、抓眼、可投递
- Obsidian 链接：使用 `[[Note Name]]`
- Markdown 表格：本次未使用
- 证据原则：不补写 vault 未记录的教育、任职、论文和量化成果

### Output
- `result/2026-08-25_plant_breeding_bioinformatics_resume.md`

### Result Summary
完成一版以“植物育种 × 生物信息学 × AI 育种”为定位的简历，重点呈现玉米产量与株型、抗旱耐热耐盐、智能表型、组学分析、遗传转化、CRISPR-Cas12a 和育种决策闭环能力。

### Interpretation
当前知识网络显示，核心优势不是单一工具熟练度，而是能将田间育种目标、植物生理机制、表型数据、遗传分析和 AI 技术连接起来。简历因此采用“问题导向 + 技术链 + 生物学解释”的叙事方式。

### Problems and Notes
- vault 中尚未明确记录姓名、学历、工作经历、项目成果、软件熟练度和可核验量化指标。
- 当前版本适合作为能力画像与投递底稿；正式求职前需要补齐个人履历事实。
- 知识页部分存在编码异常和导入型页面结构，简历使用了可确认的主题级信息，未直接复制异常标题。

### Decision Rationale
采用“育种目标—表型—机制—数据—决策”主线，避免将简历写成论文阅读清单或工具列表；同时明确能力边界，避免把文献学习误写成已完成的实验成果。

### Next Step
补充个人基本信息、教育经历、任职经历、代表项目、论文专利、工具熟练度和量化成果，随后可生成一页版、学术版、种业公司版和英文版简历。
