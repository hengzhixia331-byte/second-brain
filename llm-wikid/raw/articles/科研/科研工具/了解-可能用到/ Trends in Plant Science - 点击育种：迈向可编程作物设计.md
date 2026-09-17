---
description: /
author: PhenoTrait
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=MzI0Mjg5ODI1Ng==&mid=2247546272&idx=1&sn=0e7ef5cbaed198457c271da3fd13fd81&chksm=e8bd0f3294e856cbbbe7bed1634bb9d13de0ff1c9009ec29a5145bbb2679e36d0c2e86305ade&mpshare=1&scene=1&srcid=0717okLubIZSPhs8y7TXXcBF&sharer_shareinfo=6150a23a6b5c42334b684c6dca2daa7f&sharer_shareinfo_first=6150a23a6b5c42334b684c6dca2daa7f#rd
saved: 2026-07-17
tags:
  - 笔记同步助手
id: 135a7f3b-84e0-4082-8c1a-e0e577f2b945
---

# Trends in Plant Science | 点击育种：迈向可编程作物设计
#笔记同步助手
## 来源
[原文链接](https://mp.weixin.qq.com/s?__biz=MzI0Mjg5ODI1Ng==&mid=2247546272&idx=1&sn=0e7ef5cbaed198457c271da3fd13fd81&chksm=e8bd0f3294e856cbbbe7bed1634bb9d13de0ff1c9009ec29a5145bbb2679e36d0c2e86305ade&mpshare=1&scene=1&srcid=0717okLubIZSPhs8y7TXXcBF&sharer_shareinfo=6150a23a6b5c42334b684c6dca2daa7f&sharer_shareinfo_first=6150a23a6b5c42334b684c6dca2daa7f#rd)
## 正文
公众号名称：植物表型资讯

作者名称：PhenoTrait

发布时间：2026-07-17 06:10

原文链接：[https://www.sciencedirect.com/science/article/pii/S1360138526002104](https://www.sciencedirect.com/science/article/pii/S1360138526002104)

[![](https://relay-1.bijitongbu.site/p/75fcb4e753208d48813a4baab4d69280.png)](https://mp.weixin.qq.com/s?__biz=MzI0Mjg5ODI1Ng==&mid=2247543603&idx=1&sn=1934aa52afcb6c193cc31378277c99af&scene=21#wechat_redirect)

[![](https://relay-1.bijitongbu.site/p/a40f351414a0370994442c0d69441f83.png)](https://mp.weixin.qq.com/s?__biz=MzI0Mjg5ODI1Ng==&mid=2247542326&idx=1&sn=319fcf4914cb0336c3edaa47ea0a997c&scene=21#wechat_redirect)

[![](https://relay-1.bijitongbu.site/p/8baedb92a932f15e7124b29e109c0212.png)](https://mp.weixin.qq.com/s?__biz=MzI0Mjg5ODI1Ng==&mid=2247540829&idx=2&sn=1ceb9dc2997c7324cc97bfa786512d80&scene=21#wechat_redirect)

[![](https://relay-1.bijitongbu.site/p/21460de0e7d258efd01dda63a6bf3a31.png)](https://mp.weixin.qq.com/s?__biz=MzI0Mjg5ODI1Ng==&mid=2247537489&idx=1&sn=1e789f5c892a55c1581351b338d987e8&scene=21#wechat_redirect)

粮食安全仍是全球战略首要任务。​人口增长、膳食结构改变以及气候波动预计将在限制耕地、极端天气和新病虫害等约束下，进一步增加对农产品的需求。​作物育种已从基因型驱动的生物表型选择，发展到分子育种、基因组选择（GS）和基因编辑。​然而，面对由非加性效应和基因型与环境互作（G×E）主导的复杂多基因性状，传统的基因组预测在面对分布偏移（新环境、新季节或新遗传背景）时表现出预测准确性下降的问题。​现有的预测模型和工具通常只优化了单一的育种选择决策，难以协调跨越多年育种计划的杂交序列、资源分配、基因编辑决策以及多环境试验设计。

为了突破这一局限，本文提出了“点击育种（Click Breeding）”概念，将整个育种计划视为一个可编程、可模拟、可优化的整体设计单元。

**点击育种(Click Breeding)的核心概念**

“点击育种”是一种设计驱动的全新范式，它将育种策略视为可执行的计算程序，而非松散耦合的单一任务组合。其中，“点击（Click）”包含双重含义：

  

-   呼应“点击化学（Click Chemistry）”，强调育种操作的模块化、高效率与可组合性。
    

-   引入软件工程中“一键运行（click to run）”的隐喻，将育种意图转化为结构化、机器可读且版本化的代码规范，实现端到端、可审计的流程。
    

  

![](https://relay-1.bijitongbu.site/p/62eda9f7753c628bb7d1d23024fc817d.png)

图1 点击育种框架的架构。

点击育种将人工智能、生物学建模和实验工作流集成到一个统一的设计系统中。​育种目标和约束首先由编码器与规范器（encoders & specifiers）编码为机器可读的规范。​AI设计智能体（AI design agents）生成候选育种策略，包括亲本组合、基因编辑和多代杂交计划。​这些策略利用模拟不同环境情景下基因型表现的性状级数字孪生（trait-level digital twins）进行评估，并通过多目标优化（MOO）识别平衡产量、抗逆性、稳定性、成本和遗传多样性的帕累托高效策略。​这个内部的“设计-测试”循环（design-to-test loop）在进行任何田间投入前，在计算机（in silico）中快速迭代 。​选定的策略随后由可执行接口编译为可重复的实验操作，包括基因编辑、杂交、表型鉴定和田间试验。​实验结果（包括高通量表型分析获取的数据）通过迭代的“设计-构建-测试-学习”（DBTL）循环反馈至系统，在连续世代中更新模型并精炼智能体策略。

**机器可读的声明式育种规范**

点击育种通过声明式文件，将育种目标、约束、阶段和治理要求转化为结构化的文字说明。以下为“水稻耐旱育种项目（Rice\_Drought\_2026）”的系统规范说明书：

  

-   项目基本信息
    

项目名称：Rice\_Drought\_2026

物种：亚洲水稻（Oryza sativa）

育种目标：选育气候适应型高产栽培品种

  

-   育种目标与权重分配
    

首要目标：最大限度提高产量（权重：0.50）

次要目标 1：最大限度提高耐旱指数（权重：0.30）

次要目标 2：控制生育期（天数）在 110 至 135 天之内（权重：0.20）

  

-   限制性约束条件
    

近交系数：最大不得超过 0.10

群体多样性：必须保持多样性

育种世代：最大循环代数为 6 代

  

-   工作流阶段设计
    

设计优化阶段：采用进化算法进行全局优化

亲本选择阶段：采用基因组预测方法

杂交阶段：每世代最大杂交组合数限制为 50 个

基因编辑阶段：采用 CRISPR 激活技术，靶向编辑内源基因 OsNAC45 和OsDREB2A

田间评估阶段：在热带冬季育种基地、亚热带灌溉田以及温带试验田三处环境进行

  

-   决策与不确定性要求
    

预测准确度：跨地点验证R²≥0.60，跨年份验证R²≥0.55

不确定性：采用经过校准的不确定度估算，最大认知不确定性限制在 0.15 以内，校准覆盖率达 0.90

脱靶评估：必须执行

  

-   系统治理与安全合规
    

最终输出成果：杂交计划书、编辑计划书、田间试验设计方案、育种综合报告

监管审查：在中国境内执行并需满足生物安全审查要求

追踪与记录：开启全程审计日志记录，并启用全套系统版本控制

**AI设计智能体与策略生成**

相较于传统基因组选择仅评估单代候选个体的优劣，AI设计智能体能够解决跨越世代的“路线图”问题。

  

-   进化算法（EAs）：适用于整体架构相对固定、需在庞大空间中搜索最佳杂交方案、编辑路径及资源配置的场景。
    

-   强化学习（RL）：将育种视为部分可观测环境下的顺序决策问题，能够针对动态导入的实验数据实时自适应调整决策
    

  

![](https://relay-1.bijitongbu.site/p/1b7772cf7b8c15b98fe314c2d6f4348b.png)

图2 用于探索育种策略的AI设计智能体。

AI设计智能体在可能存在的多代育种策略的大规模组合空间中进行导航，每种策略都明确规定了亲本选择、杂交序列以及跨越世代的选择标准。​智能体核心采用两种互补的优化范式：进化算法（EA）通过迭代杂交和变异候选策略来提升群体的整体适应度；强化学习（RL）则通过与模拟育种环境的奖惩互动来学习顺序决策策略。​生成的策略候选会被传递到输出模块，在该模块中，由预测模型和数字孪生构建的预测评估循环会对每个候选方案进行评分。​高水平的设计会经历迭代设计优化，最终产生平衡产量、稳定性和资源效率等多重目标的帕累托最优策略。​选定的策略通过外部实体循环（outer in vivo loop）反馈回组合空间，随着真实实验数据的积累实现持续改进。

**性状级数字孪生(Trait-Level Digital Twins)**

数字孪生是点击育种进行计算机预设计（design-before-build）的基石，主要支持“假设（what-if）”反事实模拟、不确定性量化和实验优先级排序。其典型架构采用“混合模型”：将基于物理或生理机制的模型（如 APSIM, DSSAT 捕获碳水能量平衡约束）与神经网络模型（如 GNN, Transformer 捕获非线性残差和复杂 G×E 模式）深度融合。

![](https://relay-1.bijitongbu.site/p/d666e57b037a0ecd7c1769e569057611.png)

图3 点击育种的计算机设计基础设施。

（A）性状级数字孪生集成了基因组、表型、生理和环境四类输入数据，将其导入耦合的预测模型、作物生长模型和管理模块中，构建作物系统的虚拟模型。​这些模型能够模拟不同环境和农业实践下的基因型表现，实现在计算机中对育种策略的评估，并产生涵盖产量稳定性、遗传增益、环境抗逆性、成本效益和多样性维持等多目标的决策就绪输出。​数字孪生还可以生成反事实场景，例如预测假定基因型的表现或评估未来气候条件下的抗逆性。​（B）育种计划通常需要同时追求多个目标。​多目标优化算法在候选育种策略空间中搜索并识别平衡遗传增益、产量稳定性、抗逆性、多样性维持和成本效益的帕累托最优方案。​产生的帕累托前沿将可行的、潜在获利的策略与由显式约束（如最大同胞杂交、最低多样性阈值和试验容量）定义的不可行区域分隔开。​沿前沿分布的策略提供了不同的折中方案，使育种家能够选择与区域优先权和风险承受力相契合的设计方案，而非采用单一的固定最优解。

**技术成熟度评估（TRL）**

点击育种并非一个单一、即装即用的软件平台，而是由一系列处于不同技术成熟度级别（TRL）的支撑技术与组件共同构成的复杂系统。

为了让大家更直观地了解各项关键技术目前的发展阶段、当前应用状态以及未来需要突破的瓶颈，研究作者在论文中对 15 项核心技术组件进行了系统性成熟度评估。

![](https://relay-1.bijitongbu.site/p/243c93925cefd1d991a80304bac1cbc9.png)

表1 点击育种组件技术的技术成熟度（TRLs）。

TRL 评分反映了作者基于已发表的示范成果对当前实际运行成熟度的评估。近期组件（TRL≥6）可直接基于现有基础设施进行部署；中期组件（TRL 3-5）需要进一步的验证；长期组件（TRL 1-2）目前仍属于前沿研究攻关目标。

**困难与挑战**

将进化算法（EAs）和强化学习（RL）的生成能力转化为可付诸行动的育种程序，需要显式地处理可行性、安全性和可扩展性的约束。然而，将强化学习（RL）应用于实际育种程序时，面临着四个相互关联的结构性约束，这限制了其近期可行性：

1.数据稀疏性 (Data sparsity)：一个世代只能产生一个表型观测周期，而田间试验的成本使得广泛的探索变得极其高昂。尽管离线和基于模型的强化学习提供了务实的替代方案，但其效果取决于底层数字孪生的保真度。

2.模拟与现实之间的鸿沟 (Sim-to-real gap)：这一鸿沟依然巨大；在计算机（in silico）中训练的策略可能会利用模拟器的虚假人为特征，而不是真正的生物学关系，从而在违反模拟器假设的田间条件下导致性能急剧下降。

3.奖励作弊 (Reward hacking)：这带来了一种特定风险，即智能体发现的策略最大化了奖励函数，但却产生了在生物学上不合理或在农学上不可接受的结果（例如：极端的矮化和种子活力的丧失）。

4.奖励设计的复杂性 (Complexity of reward design)：目标是多维的，奖励会延迟整整一个世代，而且次优杂交决策的后果可能会在多个周期内处于潜伏状态。因此，我们将强化学习定位为自适应程序管理的长期范式，而不是立即可用的操作工具。

**未来与展望**

几个近期的优先事项将决定这一愿景如何快速投入运行：

1.决策级数字孪生 (Decision-grade digital twins)：需要预测准确性、校准的不确定性以及在分布偏移下的鲁棒性。实现这些特性需要系统性的多环境验证和主动学习驱动的数据收集。

2.因果接地 (Causal grounding)：设计智能体必须在因果上接地，以避免采用那些利用历史数据中 spurious（虚假）关联的策略。

3.可执行接口 (Executable interfaces)：必须从工作流编排器演变为具备治理意识的编译器，从而将监管合规和生物安全检查嵌入到设计中，而不是作为下游的附加物。

4.标准化 (Standardization)：跨育种组织的数格式、设计规范和审计协议的标准化，对于可重复性和跨项目学习至关重要。

5.跨学科收敛 (Convergence)：实现“育种即代码”最终将需要植物生物学、机器学习、合成生物学和监管科学的收敛。这些前沿的进展将加速气候适应型、高产作物的选育，并建立大规模负责任部署AI驱动育种所需的问责和透明度框架。

**总结**

点击育种通过闭环、计算机引导的工作流，替代了经验性、反应性的“观察-选择-重复”循环，在进行高成本的田间试验部署前，对育种计划整体进行生成、压力测试并编译为可审计的操作。通过整合AI设计智能体、性状级数字孪生、约束性多目标优化和可执行接口，该框架解决了当前预测性育种的一个根本限制：在训练集内的高准确度，并不等同于在多代、多环境和多目标交织的复杂真实育种程序中做出最优决策。

实现“育种即代码”（Breeding as Code）需要植物生物学、机器学习、合成生物学和监管科学的深度交叉融合。我们在本综述中探讨的一系列挑战和问题——包括智能体泛化、数据效率、上位性建模、跨管辖区治理以及前瞻性验证等——共同勾勒出了一幅清晰明了且富有前景的研究路线图。

**来 源**

> Dai, B., Tian, Y., Chai, J., Liu, F., Chen, S., Tang, K., 2026. Click Breeding: Toward programmable crop design. Trends in Plant Science.

> **编辑**

> 一点白

> **扩展阅读**

> -   ****[植物表型资讯2018年1-12月目录汇总](http://mp.weixin.qq.com/s?__biz=MzI0Mjg5ODI1Ng==&mid=2247487688&idx=2&sn=c51d69cd1acbda7d4758740d6127b5d2&chksm=e97414f7de039de1b263c583ac8ef0357e71d0354cfd5c3195253fc9a31a1834cff0dcfd5a8a&scene=21#wechat_redirect)****
>     
> -   **[植物表型资讯2019年1-12月目录汇总](http://mp.weixin.qq.com/s?__biz=MzI0Mjg5ODI1Ng==&mid=2247491277&idx=1&sn=ee8b1714676be269e0f51e6d7d3ccdeb&chksm=e9741af2de0393e483b3f2c894b6b3186973bfdeba52efb5a5f9607b76b84e40e88090d5e9cb&scene=21#wechat_redirect)**
>     
> -   **[植物表型资讯2020年1-12月目录汇总](http://mp.weixin.qq.com/s?__biz=MzI0Mjg5ODI1Ng==&mid=2247497147&idx=1&sn=b8c6c36dc19211649e9abada73f14315&chksm=e977f184de0078920b29178dd2b734cfd31d1ba6c1483c20c5f13d8e719ae9dd777aa217fdb9&scene=21#wechat_redirect)**
>     
> -   **[植物表型资讯2021年1-12月目录汇总](https://mp.weixin.qq.com/s?__biz=MzI0Mjg5ODI1Ng==&mid=2247504203&idx=3&sn=d45de43a4dd64388592dff3ed430a6ec&scene=21#wechat_redirect)**
>     
> 
> -   **[植物表型资讯2022年1-12月目录汇总](http://mp.weixin.qq.com/s?__biz=MzI0Mjg5ODI1Ng==&mid=2247512950&idx=2&sn=573e421c63b9356d512260e53e87bba6&chksm=e977b749de003e5f2295baec66a3d0fa8489e3e1d8ccd2dcacf26905dbf76ffa45172e5be952&scene=21#wechat_redirect)**
>     
> -   **[植物表型资讯2023年1-12月目录汇总](http://mp.weixin.qq.com/s?__biz=MzI0Mjg5ODI1Ng==&mid=2247522585&idx=3&sn=3707549a6b6880aa39976b09bffcc84c&chksm=e9779d26de00143005840a5796c8b828575836990b6bc90ef22b7d88b6b1d2a0f9cc1c72fc65&scene=21#wechat_redirect)**
>     
> -   **[植物表型资讯2024年1-12月目录汇总](https://mp.weixin.qq.com/s?__biz=MzI0Mjg5ODI1Ng==&mid=2247533799&idx=4&sn=f6c07a40d65ea5e1dcd58de9fbe8773c&scene=21#wechat_redirect)**
>     
> -   **[植物表型资讯2025年1-12月目录汇总](https://mp.weixin.qq.com/s?__biz=MzI0Mjg5ODI1Ng==&mid=2247541876&idx=5&sn=d9e3217a5f8c41cef7d6fbfb87d0f08b&scene=21#wechat_redirect)**
>     
> -   [植物表型资讯2026年1-12月目录汇总](https://mp.weixin.qq.com/s?__biz=MzI0Mjg5ODI1Ng==&mid=2247545960&idx=4&sn=5ebabda1bc7d31072eb413dd49f28d8e&scene=21#wechat_redirect)
>     
> -   ****[植物表型资讯分类专辑直通车](https://mp.weixin.qq.com/s?__biz=MzI5NTAwODE3NA==&mid=2649889890&idx=1&sn=055b1892264f8f5294311106aa93ff02&scene=21#wechat_redirect)****
>     
> -   ****[最畅销的田间表型平台长什么样？](http://mp.weixin.qq.com/s?__biz=MzI5NTAwODE3NA==&mid=2649890729&idx=1&sn=a86eb8a0ca44eb10ef723fca5c13510d&chksm=f45c9d68c32b147eaadb4d8c9d95f7f4deb6c2731fdb2dd0bab80822855c4ca9b690e792f341&scene=21#wechat_redirect)****
>     

![](https://relay-1.bijitongbu.site/p/02cca3bc61a971ea15ad986b158f6569.png)

> 📹 视频内容（上图为封面），请前往原文观看：[在公众号原文中观看](https://mp.weixin.qq.com/s?__biz=MzI0Mjg5ODI1Ng==&mid=2247546272&idx=1&sn=0e7ef5cbaed198457c271da3fd13fd81&chksm=e8bd0f3294e856cbbbe7bed1634bb9d13de0ff1c9009ec29a5145bbb2679e36d0c2e86305ade&mpshare=1&scene=1&srcid=0717okLubIZSPhs8y7TXXcBF&sharer_shareinfo=6150a23a6b5c42334b684c6dca2daa7f&sharer_shareinfo_first=6150a23a6b5c42334b684c6dca2daa7f#rd)

![](https://relay-1.bijitongbu.site/p/8380c9b3114e49e918206c3d47c5d95e.png)

![|50](https://relay-1.bijitongbu.site/p/cac44b71989d3e4eeb1d9ab7046fbd5f.png)

**戳这里，阅读原文**

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/9f67bb48_1784249869787?u=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzI0Mjg5ODI1Ng%3D%3D%26mid%3D2247546272%26idx%3D1%26sn%3D0e7ef5cbaed198457c271da3fd13fd81%26chksm%3De8bd0f3294e856cbbbe7bed1634bb9d13de0ff1c9009ec29a5145bbb2679e36d0c2e86305ade%26mpshare%3D1%26scene%3D1%26srcid%3D0717okLubIZSPhs8y7TXXcBF%26sharer_shareinfo%3D6150a23a6b5c42334b684c6dca2daa7f%26sharer_shareinfo_first%3D6150a23a6b5c42334b684c6dca2daa7f%23rd&s=obsidian)
