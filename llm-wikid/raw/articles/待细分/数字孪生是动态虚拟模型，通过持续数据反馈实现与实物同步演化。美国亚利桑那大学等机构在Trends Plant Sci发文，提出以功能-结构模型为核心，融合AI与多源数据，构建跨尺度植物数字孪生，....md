---
description: 数字孪生是动态虚拟模型，通过持续数据反馈实现与实物同步演化。美国亚利桑那大学等机构在Trends Plant Sci发文，提出以功能-结构模型为核心，融合AI与多源数据，构建跨尺度植物数字孪生，为打通基因型-表型鸿沟、加速作物改良提供颠覆性框架。/
author: AgriBrain
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=MzI0MDI5NjM2NA==&mid=2247521307&idx=1&sn=741663e2dc3415d75ad84a359a5546ac&chksm=e828cc83bf17e6d223338490edf901ee4b9107a8e0aa78cb073e05ce4a2b42c71b003f139ac5&mpshare=1&scene=1&srcid=0728U9kBhmKJ1bB7i0bW8joy&sharer_shareinfo=54a437e34ea6783304b0c7e7f10b00e5&sharer_shareinfo_first=54a437e34ea6783304b0c7e7f10b00e5#rd
saved: 2026-07-28
tags:
  - 笔记同步助手
id: a2eb95b9-1594-48df-8a4d-5ace1f6f93aa
---

# Trends in Plant Science| 美国亚利桑那大学揭示植物数字孪生技术如何跨尺度推动作物品种改良
#笔记同步助手
## 来源
[原文链接](https://mp.weixin.qq.com/s?__biz=MzI0MDI5NjM2NA==&mid=2247521307&idx=1&sn=741663e2dc3415d75ad84a359a5546ac&chksm=e828cc83bf17e6d223338490edf901ee4b9107a8e0aa78cb073e05ce4a2b42c71b003f139ac5&mpshare=1&scene=1&srcid=0728U9kBhmKJ1bB7i0bW8joy&sharer_shareinfo=54a437e34ea6783304b0c7e7f10b00e5&sharer_shareinfo_first=54a437e34ea6783304b0c7e7f10b00e5#rd)
## 正文
公众号名称：农业之巅

作者名称：AgriBrain

发布时间：2026-07-28 08:00

> ![](https://relay-1.bijitongbu.site/p/b02527968bd9dbbdede1b404ad20debe.png)
> 
> 2026年7月，美国亚利桑那大学Duke Pauli团队联合多所研究机构在**Trends in Plant Science**发表了题为**Digital twins for plant and crop improvement**的观点文章。该研究系统阐述了**植物数字孪生(Digital Twins, DTs)**的概念缘起、技术架构及多尺度应用路径，指出这一框架有望成为打通**基因型—表型(G2P)鸿沟**、加速**作物遗传改良**的颠覆性工具。
> 
> ![](https://relay-1.bijitongbu.site/p/bed73acfc02bed018f26950671768a3e.png)
> 
> 关键词：数字孪生；功能-结构植物模型；基因型-表型鸿沟；作物改良；表型组学
> 
> doi.org/10.1016/j.tplants.2026.04.010
> 
>   

![|18](https://relay-1.bijitongbu.site/p/9f2c3a511bf09aec72cd70846c27bf5b.png)

**01**

**什么是植物数字孪生？**

**数字孪生技术**最早源于美国宇航局(NASA)的航天工程——通过物理复制品来模拟和测试太空飞行器。与传统模型不同，数字孪生的核心在于持续的数据反馈循环：随着新的表型数据和环境数据不断汇入，虚拟模型会同步更新、校准和进化，从而与物理实体保持“同频共振”。

在植物科学领域，数字孪生并非简单的3D可视化模型，而是一个集形态结构、生理功能和环境响应于一体的动态虚拟系统。它能够模拟从单片叶子到整个植株、再到田间冠层的生长过程，帮助研究者回答“如果改变这个基因、在那个环境下生长，植物会怎样？”这类传统实验难以高效解答的问题。

![|18](https://relay-1.bijitongbu.site/p/34270a45fdfa608e2cca54be76244663.png)

**02**

**如何构建植物级数字孪生？**

本研究主张以**功能—结构植物模型(FSPM)**为内核搭建DT。构建流程主要包含四步：首先，通过3D点云、热成像及**高光谱**等技术采集植株多源**表型**数据；其次，由**AI**驱动的数据管道完成数据清洗、分割与关键性状提取(如叶面积、叶角、蒸腾状态)；随后，利用参数初始化FSPM，并结合双向光线追踪模拟冠层内动态光环境；最后，通过数据同化机制，在每一轮新数据汇入时自动校准模型。

这一循环使得DT具备了“学习能力”——它能不断修正参数，以逼近真实的生物学过程，这是区别于传统作物模型的本质所在。

![](https://relay-1.bijitongbu.site/p/b95260dccd41a8a422204013817063f4.png)

图1.植物数字孪生的创建与工作流程

![|18](https://relay-1.bijitongbu.site/p/369767456da19b6d70e6bc115aab3e04.png)

**03**

**从叶片到小区：数字孪生的跨尺度设计**

数字孪生并非"一蹴而就"的单一模型，而是一套可跨尺度部署的通用框架——从单张叶片到整株植株，再到田间小区，每个层级都有其独特的研究问题与建模重点。

在叶片尺度上，核心在于采集真实植株的结构与生理数据，如叶面积、气孔导度、光合参数等，为上层模型提供最基础的输入参数，这是整个数字孪生的"数据起点"。

到了单株尺度，数据开始"活"起来。功能-结构模型接管模拟任务，将碳同化、源-库分配、器官生长发育、水分传输等关键生理过程整合进3D株型框架中，让**虚拟植物**具备了"生长逻辑"。

而最上层的小区尺度，关注的是冠层的整体表现：叶面积发展、辐射截获、冠层光合与蒸腾、微气候梯度——这些决定产量的群体属性，正是通过将多个单株孪生体组合并嵌套作物生长模型后"涌现"出来的。

![](https://relay-1.bijitongbu.site/p/12ddc9545ba893b9090487f95c57ba16.png)

图2.植物数字孪生在不同生物学尺度上的应用

![|18](https://relay-1.bijitongbu.site/p/6b2677e31a06e0b2ed38109c7734dde1.png)

**04**

**嵌套式框架：FSPM 与 CGM 的融合**

文章提出了**嵌套式FSPM-CGM耦合框架**：先利用田间实测变异参数化多个单株DT实例，构成虚拟冠层；FSPM负责模拟器官级碳同化与水分动态，其输出聚合后输入**作物生长模型(CGM)**，用以模拟冠层级的辐射利用效率与群体蒸腾；CGM再将更新后的环境条件反馈给FSPM，驱动下一轮生长。

该框架使得研究人员能精准量化单株性状(如叶倾角)如何“涌现”为冠层功能差异(如光穿透梯度与光合非均匀性)，为解决“叶片高水分利用效率导致冠层减产”等尺度悖论提供了新工具。

![](https://relay-1.bijitongbu.site/p/d86d93a0b1729d63447e697e65980906.png)

图3.冠层级数字孪生的嵌套FSPM-CGM框架

![|18](https://relay-1.bijitongbu.site/p/e3a2092cb7ef1cb127b2e1925633c4ee.png)

**05**

**打通基因型-表型鸿沟的三条路径**

本文研究指出DT连接基因与表型的关键在于将遗传变异映射为动态生理参数，而非终点产量：

**连续动态表型：**DT可将离散的观测“快照”延拓为连续发育轨迹，助力GWAS分析从“单一时间点性状”升级为“性状形成的动态响应模式”。

**模型参数作为功能表型：**直接测冠层温度只能定位位点，而DT推导出的“气孔对水汽压亏缺的敏感性参数”则能清晰揭示遗传变异调控植株水分平衡的生理机制。

**赋能基因组预测(GP)****：**GP可预测特定基因型的DT生理参数(而非直接预测产量)，进而初始化“合成DT”模拟目标环境下的生长轨迹。这避免了预测强G×E互作性状时的精度陷阱，显著提升跨环境泛化能力。

从单株到冠层，从快照式表型到动态模拟，从田间试错到虚拟设计，数字孪生正在把植物科学拆成结构、生理、环境与时间四层重新建模。但真正的变化不是“替代田间试验”，而是让试验问题更聚焦、让**基因型-表型**关系更可解释、让**育种**决策更前置。未来的竞争，不只是谁种得更好，而是谁更会用数字孪生理解生命系统。

该研究系统阐述了**植物数字孪生**的概念缘起、技术架构(以**功能-结构植物模型FSPM**为内核，融合**AI**数据管道与双向光线追踪)及多尺度应用路径(从叶片、单株到冠层)，并指出该框架可通过延拓连续发育轨迹、提取生理参数作为**功能表型**、赋能**基因组预测**三条路径打通**基因型-表型**鸿沟，有望成为加速**作物遗传改良**的颠覆性工具。

doi.org/10.1016/j.tplants.2026.04.010

![](https://relay-1.bijitongbu.site/p/d4c84cf854252b82e813f3d958873cca.png)

> 📹 此处为视频内容（vid: wxv\_4350290940968665102）（上图为封面），未能直接提取，请前往原文查看：[在公众号原文中观看](https://mp.weixin.qq.com/s?__biz=MzI0MDI5NjM2NA==&mid=2247521307&idx=1&sn=741663e2dc3415d75ad84a359a5546ac&chksm=e828cc83bf17e6d223338490edf901ee4b9107a8e0aa78cb073e05ce4a2b42c71b003f139ac5&mpshare=1&scene=1&srcid=0728U9kBhmKJ1bB7i0bW8joy&sharer_shareinfo=54a437e34ea6783304b0c7e7f10b00e5&sharer_shareinfo_first=54a437e34ea6783304b0c7e7f10b00e5#rd)

![](https://relay-1.bijitongbu.site/p/2d705dcb20331c7ea59a5304d2ab8000.png)

“

**加入“农业之巅交流群”**

_/ Join in_

扫描下方二维码加小编微信，拉您进入交流群。请您备注一下：**企业/机构/学校+研究方向+姓名**，以便小编能够拉您进入目标交流群，营销广告人员勿扰。

“农业之巅交流群”是农业+人工智能交叉领域的前沿交流阵地，这里定期分享国内外**植物表型**、**智能育种**、**智慧农业**领域前沿的研究资讯，期待与您共创农业未来。

![](https://relay-1.bijitongbu.site/p/d519a7292f311ec426bd519e7debac64.png)

![](https://relay-1.bijitongbu.site/p/64b2dfa2cc85c39a6de6eb53dce7016d.png)

_**Recommended**_

**推荐阅读**

<table style="border-collapse: collapse"><tbody><tr><td data-colwidth="100.0000%" width="100.0000%" style="border: 1px solid #ddd; padding: 6px 10px"><div style="text-align: left; background-color: rgb(255, 255, 255)"><div style="color: rgb(0, 0, 0)"><div style="text-align: center; font-size: 12px; color: rgb(23, 75, 155)"><p style="color: rgb(0, 0, 0)"><strong><span><a class="normal_text_link mp_article_text_link" target="_blank" style="color: rgb(23, 75, 155)" href="https://mp.weixin.qq.com/s?__biz=MzI0MDI5NjM2NA==&amp;mid=2247519039&amp;idx=2&amp;sn=227f126ca5a84b414aef9b0ae7d970ac&amp;scene=21#wechat_redirect" textvalue="" linktype="text" data-linktype="2">高精度全基因组选择AI平台GSBrain P系列</a></span></strong></p></div></div></div></td></tr><tr><td data-colwidth="100.0000%" width="100.0000%" style="border: 1px solid #ddd; padding: 6px 10px"><div style="text-align: left; background-color: rgb(255, 255, 255)"><div style="color: rgb(0, 0, 0)"><div style="text-align: center; font-size: 12px; color: rgb(23, 75, 155)"><p style="color: rgb(0, 0, 0)"><strong><span><a class="normal_text_link mp_article_text_link" target="_blank" style="color: rgb(23, 75, 155)" href="https://mp.weixin.qq.com/s?__biz=MzI0MDI5NjM2NA==&amp;mid=2247517436&amp;idx=2&amp;sn=5ffcb9f1c801c26e7df952b41d63ad2e&amp;scene=21&amp;poc_token=HKHbAmqjrLOf_xLx9Y68DCEWhYqeA7Gly9RqHs0B#wechat_redirect" textvalue="" linktype="text" data-linktype="2">近端表型自动化分析系统PhenoAI Near</a></span></strong></p></div></div></div></td></tr><tr><td data-colwidth="100.0000%" width="100.0000%" style="border: 1px solid #ddd; padding: 6px 10px"><div style="text-align: left; background-color: rgb(255, 255, 255)"><div style="color: rgb(0, 0, 0)"><div style="text-align: center; font-size: 12px; color: rgb(23, 75, 155)"><p style="color: rgb(0, 0, 0)"><strong><span><a class="normal_text_link mp_article_text_link" target="_blank" style="color: rgb(23, 75, 155)" href="https://mp.weixin.qq.com/s?__biz=MzI0MDI5NjM2NA==&amp;mid=2247517437&amp;idx=1&amp;sn=8ea6982449d874db9996beb1b0511109&amp;scene=21&amp;poc_token=HNjbAmqj_Xv9PMn8GJeNxeBfkLvSJdJCEtSWmFxk#wechat_redirect" textvalue="" linktype="text" data-linktype="2">无人机一体化分析系统PhenoAI air</a></span></strong></p></div></div></div></td></tr><tr><td data-colwidth="100.0000%" width="100.0000%" style="border: 1px solid #ddd; padding: 6px 10px"><div style="text-align: left; background-color: rgb(255, 255, 255)"><div style="color: rgb(0, 0, 0)"><div style="text-align: center; font-size: 12px; color: rgb(23, 75, 155)"><p style="color: rgb(0, 0, 0)"><strong><span><a class="normal_text_link mp_article_text_link" target="_blank" style="color: rgb(23, 75, 155)" href="https://mp.weixin.qq.com/s?__biz=MzI0MDI5NjM2NA==&amp;mid=2247490803&amp;idx=1&amp;sn=74569da41f038d8b2f69da789ce9bb14&amp;chksm=e91c5430de6bdd26e83a9224f20f34775fb2ae85879b979736fe823c2e7fc5a1dc73743f3196&amp;token=1649967276&amp;lang=zh_CN&amp;scene=21#wechat_redirect" textvalue="" linktype="text" data-linktype="2">植物表型AI算法平台PhenoAI Flow</a></span></strong></p></div></div></div></td></tr><tr><td data-colwidth="100.0000%" width="100.0000%" style="border: 1px solid #ddd; padding: 6px 10px"><div style="text-align: left; background-color: rgb(255, 255, 255)"><div style="color: rgb(0, 0, 0)"><div style="text-align: center; font-size: 12px; color: rgb(23, 75, 155)"><p style="color: rgb(0, 0, 0)"><strong><span><a class="normal_text_link mp_article_text_link" target="_blank" style="color: rgb(23, 75, 155)" href="https://mp.weixin.qq.com/s?__biz=MzI0MDI5NjM2NA==&amp;mid=2247490860&amp;idx=1&amp;sn=bf7a889f2b18da720ba321d0cb14941e&amp;chksm=e91c55efde6bdcf93747405d68d59a25573cba59f294f233d517c5d2883b34896b78cc8bd8a6&amp;token=1649967276&amp;lang=zh_CN&amp;scene=21#wechat_redirect" textvalue="" linktype="text" data-linktype="2">实验教学平台GrowthBrain E系列</a></span></strong></p></div></div></div></td></tr><tr><td data-colwidth="100.0000%" width="100.0000%" style="border: 1px solid #ddd; padding: 6px 10px"><div style="text-align: left; background-color: rgb(255, 255, 255)"><div style="color: rgb(0, 0, 0)"><div style="text-align: center; font-size: 12px; color: rgb(23, 75, 155)"><p style="color: rgb(0, 0, 0)"><strong><span><a class="normal_text_link mp_article_text_link" target="_blank" style="color: rgb(23, 75, 155)" href="https://mp.weixin.qq.com/s?__biz=MzI0MDI5NjM2NA==&amp;mid=2247496841&amp;idx=4&amp;sn=7e83c308c3a703c73b73701afa142fad&amp;scene=21&amp;poc_token=HBDcAmqjm228i_yn6k6869M3hx8q1TEaR3_tggpk#wechat_redirect" textvalue="" linktype="text" data-linktype="2">无代码AI平台GrowthBrain</a></span></strong></p></div></div></div></td></tr></tbody></table>

#AI虚拟种地 #数字孪生 #基因型 #表型 #作物遗传改良

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/0cfca0e7_1785227186695?u=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzI0MDI5NjM2NA%3D%3D%26mid%3D2247521307%26idx%3D1%26sn%3D741663e2dc3415d75ad84a359a5546ac%26chksm%3De828cc83bf17e6d223338490edf901ee4b9107a8e0aa78cb073e05ce4a2b42c71b003f139ac5%26mpshare%3D1%26scene%3D1%26srcid%3D0728U9kBhmKJ1bB7i0bW8joy%26sharer_shareinfo%3D54a437e34ea6783304b0c7e7f10b00e5%26sharer_shareinfo_first%3D54a437e34ea6783304b0c7e7f10b00e5%23rd&s=obsidian)
