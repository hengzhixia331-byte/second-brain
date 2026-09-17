---
author: 生物世界
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=MzU1MzMxMzcyMg==&mid=2247801668&idx=4&sn=98685f69f80d1c62210fca66600d5f72&chksm=fa13b553f3eb7985fb797e14d123b4f43bc3e2874fdb12d11f8a779d3b0098cf9f74013ba54d&mpshare=1&scene=1&srcid=0619qXJkUhgbumHj1OBiurQb&sharer_shareinfo=6c8518b88ab35d6ccc72beab23d4ad72&sharer_shareinfo_first=6c8518b88ab35d6ccc72beab23d4ad72#rd
saved: 2026-06-28 18:15:23
tags:
  - 科研工具
  - 笔记同步助手
id: ddc08970-0ecf-4945-a1e3-c7cd41325db6
---

公众号名称：生物世界

作者名称：生物世界

发布时间：2026-05-29 12:12

原文链接：[https://www.nature.com/articles/s41592-026-03105-x](https://www.nature.com/articles/s41592-026-03105-x)

![[llm-wikid/raw/assets/images/1577a09cbcc000eb7116f4ebac3f3e82_MD5.png]]

![[llm-wikid/raw/assets/images/b85c2834fcd3c938bdfae65b1866370a_MD5.jpg]]

编辑丨王多鱼

排版丨水成文

RNA 不仅是遗传信息传递的中间载体，更通过与 RNA 结合蛋白（RBP）及其他 RNA 分子之间形成广泛而精细的相互作用网络，构建了细胞内高度复杂的 RNA 调控机器，在基因表达各层级发挥核心作用。然而，RNA-RNA 和 RNA-RBP 互作具有高度动态性、条件依赖性和结构复杂性，其系统解析长期受到实验噪声高、数据异质性强以及技术平台差异显著等因素的制约。

近年来，尽管 CLIP-seq 和 RNA 互作组（interactome）测序技术的快速发展为全转录组尺度解析 RNA 互作网络提供了新方法，但不同实验策略产生的数据在信号特征和解析逻辑上存在较大差异，同时测序结果中普遍包含大量背景噪声和假阳性信号，严重制约了真实互作事件的准确识别与功能挖掘。

2026 年 5 月 25 日，中山大学的杨建华/李斌/屈良鹄团队联合希望之城国家医疗中心陈建军教授团队（周克任博士、黄钧鸿博士、刘树榕副教授、郑武健博士、刘顺研究员为论文共同第一作者）在 **_Nature_****_Methods 期刊_**发表了题为：An encyclopedic regulatory and functional atlas of RNA interactomes 的研究论文。

**该研究开发了** **rbsSeeker 和 rriScan 等系列计算机算法，系统整合并分析了数千个互作组测序数据集，鉴定了大规模高置信度 RBP 结合位点与 RNA 互相关系，并将相关结果全面整合至 ENCORI 平台 （** **https://rnasysu.com/encori/****），系统解析了 RBP 结合特征和 RNA-RNA 互作调控网络，为深入理解 RNA 调控网络及其生物学功能****提供了****新方法、新资源和新平台。**

**![[llm-wikid/raw/assets/images/939a3c6785fd76d0bd68923f7d0aa3b7_MD5.png]]**

该研究针对 RNA 互作识别中背景噪音高、数据异质性大和系统整合不足等关键挑战，开发了基于统一的泊松与二项分布统计框架的 rbsSeeker，对多种 CLIP-seq 数据进行建模，在单碱基交联位点和结合峰层面实现高精度识别；系统基准测试（benchmark）显示，其在 RBP 结合基序（motif）富集度、结合位点密度、跨重复一致性、结合区域偏好性等方面均优于目前多种主流方法。

为系统解析 RNA 之间复杂的相互作用，研究团队进一步开发了基于统一罚分策略的 RNA-RNA 互作分析软件 rriScan，可对 PARIS、RIC-seq 和 LIGR-seq 等多种高通量 RNA 互作组测序数据进行统一、高精度分析，并构建高置信的互作调控。​研究以经典的 snoRNA-rRNA 互作为基准，在与随机模型及现有资源的比较中显著富集已知真实互作事件，并在 ROC 分析中 AUC 达到 0.943，体现出高灵敏度与高特异性。​这些结果表明，rriScan 为 RNA-RNA 互作网络研究提供了可靠而高效的分析框架。​

![[llm-wikid/raw/assets/images/1f8b66b2beaae8c6ea70549f8a8fdba1_MD5.png]]

图1\. 开发新算法和新平台构建RNA互作组百科全书

在此基础上，研究团队利用 rbsSeeker 和 rriScan 系统分析了超过 2675 套公开 CLIP-seq 数据以及多种 RNA 互作组学数据，并进一步开发了 TDMDScore 和 RBP-MotifScan 及 Pathway 等分析工具，共同构建了 ENCORI 平台（图1）。​ENCORI 可系统解析 RNA-RNA 互作、miRNA 靶向降解以及 RBP 识别序列特征等关键调控机制。​同时，ENCORI 整合了泛癌（Pan-Cancer）数据、shRNA-RBP 筛选数据及 degradome-seq 降解组数据，并提供 API 接口与可视化分析功能。​研究人员可以通过 ENCORI 方便地探索 RNA 互作网络、RNA 结合蛋白识别序列特征，以及 RNA 在肿瘤和遗传疾病中的潜在调控机制（图2）。​

![[llm-wikid/raw/assets/images/03d71afe4bf4c95a355e3cba8ff26695_MD5.png]]

图2\. 人类RNA结合蛋白的各种结合特性

此外，研究团队通过实验验证 ENCORI 鉴定的各种互作关系，取得了一系列重要生物学发现。​研究发现并实验验证了 CPSF6 是一种新的 m6A 相关蛋白，参与 RNA 稳定性调控；首次揭示“孤儿” snoRNA—SNORA49 能够直接结合 28S rRNA 并指导其假尿苷修饰（图3）；同时构建了新的 TDMDScore 模型，系统识别了大量靶标介导的 miRNA 降解（TDMD）事件，为理解 miRNA 稳定性调控提供了新的理论依据。​这些成果表明，ENCORI 不仅是 RNA 互作数据资源平台，更是推动 RNA 功能与机制研究的重要研究基础设施。​

![[llm-wikid/raw/assets/images/9ed704886bbbe6264e98951c98973320_MD5.png]]

图3\. 实验验证SNORA49能够直接结合28S rRNA并指导其假尿苷修饰

综上所述，这项研究工作自主开发了多个计算机算法工具，在统一框架下对海量互作组数据进行了系统分析，构建新一代 RNA 互作组分析平台 ENCORI，为研究非编码 RNA、mRNA 及 RNA 结合蛋白在生命活动和疾病发生中的调控作用与分子机制提供了一个全面、开放且高效的平台。

论文链接：

**https://www.nature.com/articles/s41592-026-03105-x**

![[llm-wikid/raw/assets/images/422c5e87007ed12200044d13214bf85e_MD5.png||171]]

![[llm-wikid/raw/assets/images/f2d12432d23c0214c24258b3dc41f8fc_MD5.jpg]]

![[llm-wikid/raw/assets/images/e9d377216276f9530394c4cf98c71427_MD5.jpg]]

![[llm-wikid/raw/assets/images/963f2d790da05c144509b541d87138cf_MD5.jpg]]

![[llm-wikid/raw/assets/images/433ba2e1bee1f39ab2d456207c21c38c_MD5.jpg]]

![[llm-wikid/raw/assets/images/c2f562cbb8b3f91e59cd0ca8ecd9e998_MD5.jpg]]

设置**星标**，不错过精彩推文

![[llm-wikid/raw/assets/images/a539cebfbfbb917d24a7a6e40270e61f_MD5.jpg]]

![[llm-wikid/raw/assets/images/508b5a9ca5116c08913ff9311fff0438_MD5.jpg]]

**开放转载**

欢迎转发到朋友圈和微信群

> **微信加群**
> 
> 为促进前沿研究的传播和交流，我们组建了多个**专业交流群**，长按下方二维码，即可添加小编微信进群，由于申请人数较多，添加微信时请备注：**学校**/**专业**/**姓名**，如果是**PI**/**教授**，还请注明。
> 
> ![[llm-wikid/raw/assets/images/34e713cb2a186e983db1e3ea746a9965_MD5.jpg]]

**点****在看****，传递你的品味**

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/11ea1d2d_1782641719224?u=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzU1MzMxMzcyMg%3D%3D%26mid%3D2247801668%26idx%3D4%26sn%3D98685f69f80d1c62210fca66600d5f72%26chksm%3Dfa13b553f3eb7985fb797e14d123b4f43bc3e2874fdb12d11f8a779d3b0098cf9f74013ba54d%26mpshare%3D1%26scene%3D1%26srcid%3D0619qXJkUhgbumHj1OBiurQb%26sharer_shareinfo%3D6c8518b88ab35d6ccc72beab23d4ad72%26sharer_shareinfo_first%3D6c8518b88ab35d6ccc72beab23d4ad72%23rd&s=obsidian)