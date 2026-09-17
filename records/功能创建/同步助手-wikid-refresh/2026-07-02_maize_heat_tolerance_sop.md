## 2026-07-02 01:54 maize_heat_tolerance_sop_design

### Objective
为玉米耐高温性状研究搭建一套可复现 SOP 框架，覆盖研究假设、材料选择、热胁迫处理、表型采集、分子采样、统计建模、候选基因验证与记录归档。

### Input
- 物种：玉米，Zea mays L.
- 数据类型：田间/温室表型、环境监测数据、基因型数据、可选转录组/代谢组/生理指标数据。
- 目标性状：高温胁迫下的产量保持、花粉活力、结实率、ASI、叶片光合与膜稳定性等。
- 参考基因组：后续若进入基因定位或转录组分析，建议固定一个版本，例如 B73 RefGen_v5，并在所有脚本和记录中保持一致。

### Scripts
- 本次为 SOP 设计，没有生成分析脚本。

### Commands
```bash
# No command executed for analysis.
```

### Parameters
- species: maize
- stress_type: heat stress
- design_priority: phenotype-first, input-standard-first
- recommended_stages: seedling, VT/R1, grain filling
- replication: biological replicates and randomized block design required

### Output
- 方案记录：`records/2026-07-02_maize_heat_tolerance_sop.md`

### Result Summary
建议将玉米耐高温 SOP 拆分为七个模块：研究定义、材料与实验设计、高温处理、表型与生理测定、分子组学采样、统计遗传分析、候选基因验证与版本化记录。核心原则是先固定目标生育期、耐热性状定义、热胁迫强度和样本编码，再开展大规模表型或组学分析。

### Interpretation
玉米耐热性不是单一性状，而是生育期、组织、胁迫强度和恢复能力共同决定的复合性状。抽雄吐丝期对高温尤其敏感，常影响花粉活力、ASI、授粉结实和最终产量；苗期和灌浆期则更适合研究早期存活、光合系统稳定性、膜脂过氧化、抗氧化酶活和籽粒灌浆效率。

### Problems and Notes
- 如果未定义目标生育期和热胁迫阈值，后续表型、GWAS/QTL 和组学结果会难以比较。
- 不建议一开始同时测所有指标，应先建立最小可复现表型体系，再扩展组学和功能验证。

### Decision Rationale
采用 phenotype-first SOP，是因为耐高温研究的瓶颈通常不是模型复杂度，而是表型定义、环境记录、样本编码和重复设计不稳定。先稳定输入规范，可以减少后续分析中的人为偏差和不可追溯问题。

### Next Step
根据具体研究目标选择主线：品种筛选、QTL/GWAS 定位、转录组机制解析、候选基因功能验证或育种预测模型。

## 2026-07-02 02:04 company_collaboration_hi_edit_sop_design

### Objective
围绕大型种业公司资源，设计玉米耐高温材料筛选 SOP 与约 10 个候选基因 Hi-Edit 单倍体编辑转化验证计划的协同框架。

### Input
- 合作场景：依托先正达等大型种业公司的育种、转化、表型、基因型、田间试验和数据平台资源。
- 候选对象：约 10 个耐高温相关候选基因。
- 技术路径：Hi-Edit 单倍体编辑转化、后续材料筛选与功能验证。
- 数据类型：候选基因证据、编辑材料信息、温室/田间热胁迫表型、分子检测、产量及育种性状。

### Scripts
- 本次为合作策略与 SOP 框架设计，没有生成分析脚本。

### Commands
```bash
# No command executed for analysis.
```

### Parameters
- candidate_gene_number: approximately 10
- collaboration_mode: company platform plus research-side candidate gene package
- sop_goal_1: Hi-Edit validation of candidate genes
- sop_goal_2: scalable heat-tolerance screening pipeline
- priority: IP clarity, trait definition, stage-gate design, multi-environment validation

### Output
- 追加记录：`records/2026-07-02_maize_heat_tolerance_sop.md`

### Result Summary
建议将合作拆成两条主线：一条是候选基因 Hi-Edit 验证项目，另一条是公司级耐高温材料筛选 SOP。前者强调候选基因证据矩阵、编辑目标、材料流转、分子确认、表型验证和阶段闸门；后者强调公司种质资源、多环境试验、高通量表型、数据标准和育种决策指标。

### Interpretation
大型公司资源的价值不只在于转化平台，更在于种质库、DH/单倍体育种体系、多地点试验网络、环境监测、高通量表型、质量体系、知识产权和育种决策链。研究者应带去标准化的候选基因证据包和可量化 SOP 原型，而不是只带基因列表。

### Problems and Notes
- 进入公司合作前需要明确知识产权、材料归属、数据归属、发表边界、商业化权利和保密范围。
- 10 个基因不应平行等权推进，建议按证据强度和育种价值分层。
- Hi-Edit 验证应避免只关注编辑成功率，还要把可育性、背景遗传效应、产量代价和多环境稳定性纳入阶段评价。

### Decision Rationale
采用双主线设计，是因为候选基因验证和公司筛选 SOP 的目标不同：候选基因项目追求因果验证，筛选 SOP 追求规模化、标准化和育种决策可用。两条线共享表型体系和数据标准，可以降低重复建设成本。

### Next Step
准备一份公司沟通包：候选基因证据矩阵、编辑优先级、目标性状定义、SOP v1.0、样本编码规则、阶段闸门、知识产权问题清单和预期交付物。
