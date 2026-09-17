---
description: 《The Plant Journal》发表拜耳与佐治亚大学团队BINN框架：嵌入通路先验的稀疏网络，训练整合多组学，推断仅需基因型。玉米数据精度显著优于GBLUP，敏感性分析可发现非线性/上位性效应基因。合成代谢模型验证机制恢复能力。为精准育种提供可解释AI新工具。/
author: AgriBrain
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=MzI0MDI5NjM2NA==&mid=2247521844&idx=1&sn=9b1246039e6daa2a4876162671341cde&chksm=e81ad1416ce8d0bc321d91463dfab65bcfba39bd944f3d409e4d1819ca3842ee13c7cee17fb3&mpshare=1&scene=1&srcid=0818IiB5f8Yl2HjqsioxEIYG&sharer_shareinfo=19abdc00bb8525717521924cad65e3f7&sharer_shareinfo_first=19abdc00bb8525717521924cad65e3f7#rd
saved: 2026-08-18
tags:
  - 笔记同步助手
id: 0520dd4e-7d13-4376-8ad5-9aeb43f69ea4
---

# The Plant Journal|拜耳&佐治亚大学团队开发BINN模型：嵌入生物学知识的神经网络，助力精准育种
#笔记同步助手
## 来源
[原文链接](https://mp.weixin.qq.com/s?__biz=MzI0MDI5NjM2NA==&mid=2247521844&idx=1&sn=9b1246039e6daa2a4876162671341cde&chksm=e81ad1416ce8d0bc321d91463dfab65bcfba39bd944f3d409e4d1819ca3842ee13c7cee17fb3&mpshare=1&scene=1&srcid=0818IiB5f8Yl2HjqsioxEIYG&sharer_shareinfo=19abdc00bb8525717521924cad65e3f7&sharer_shareinfo_first=19abdc00bb8525717521924cad65e3f7#rd)
## 正文
公众号名称：农业之巅

作者名称：AgriBrain

发布时间：2026-08-18 08:00

> ![](https://relay-1.bijitongbu.site/p/58267bd22848ca66523d12f5e5502396.png)
> 
> 2026年8月，拜耳作物科学和佐治亚大学的Katiana Kontolati团队在植物科学权威期刊**The Plant Journal**发表了题为**Biology-informed neural networks learn nonlinear representations from omics data to improve genomic prediction and biological discovery**的研究论文。提出了融合生物学先验的神经网络框架，旨在解决传统**基因组预测模型**精度有限且难以整合多组学知识的问题。该研究的核心创新在于构建了一种“**基因型—生物学知识—表型**”的网络架构，该模型通过eQTL/代谢通路构建稀疏连接，训练时融入多组学知识，推断时仅需输入基因型数据。在玉米数据和合成代谢模型中，**BINN(Biology-informed neural networks)**在数据不充分情况下显著优于GBLUP等基线，其敏感性分析能发现传统方法遗漏的非线性/上位性效应基因。为**基因组选择和基因挖掘**提供了兼具精度与可解释性的新工具。
> 
> ![](https://relay-1.bijitongbu.site/p/599ed213a45c0304b07c644232dd5174.png)
> 
> 关键词：作物育种；基因组预测；基因组选择；基因型-表型建模；基于生物学知识的神经网络；通路引导的机器学习
> 
> doi.org/10.1111/tpj.710769
> 
>   

![|18](https://relay-1.bijitongbu.site/p/d137004135259fbd4ab9ddb8cf630bea.png)

**01**

## 核心思路：让网络架构“长”出生物学结构

传统神经网络平等对待所有SNP标记，依靠全连接层建立基因型与表型的关联，参数庞大，不仅容易过拟合，也难以从生物学角度给出合理解释。

BINN的设计理念截然不同：让网络架构本身嵌入生物学先验知识。

具体而言，研究团队构建了一个“**基因型→生物学知识→表型**”(G2B2P)的三层架构：

**●输入层：**SNP标记数据

**●中间层：**由生物学实体(基因或代谢物)构成的通路子网络

**●输出层：**目标表型预测

关键创新在于：模型不是让所有SNP都随意连接，而是借助已知的生物学知识，只让与同一通路相关的SNP连接起来，从而大幅减少参数，避免过拟合。同时，每个通路内部保留全连接，用于捕捉基因之间的复杂互作；最后再设一层整合各通路的信息，兼顾局部精细与全局协同。

![](https://relay-1.bijitongbu.site/p/d4be4102d81601e98ed37b7250a6f0a2.png)

图1.基于生物学的神经网络框架示意图

![|18](https://relay-1.bijitongbu.site/p/5ae458f01f94565c57ee52180ee72d4f.png)

**02**

## 训练与推断解耦：兼顾精度与实用性

多组学数据(如转录组、代谢组)蕴藏着丰富的预测信息，但在实际育种中，新选育的品系通常只能获得基因型数据，难以同步获取其表达谱或代谢谱。

BINN巧妙地将训练与推断阶段解耦，化解了这一问题。

**●训练阶段：**模型充分利用多组学数据，既用于构建稀疏网络结构，也通过软约束损失函数对中间层潜变量进行弱监督

**●推断阶段：**仅需输入**基因型**数据即可输出**表型预测**，完全契合现有**育种**流程

这一设计使得BINN既吸纳了多组学信息的预测优势，又兼顾了**基因组选择**所必需的操作便捷性。

![|18](https://relay-1.bijitongbu.site/p/3d5ab9f5e3334136a39dc2af6c95c3d9.png)

**03**

## 玉米数据验证：精度提升与基因发现

研究以玉米**TWAS**数据集验证BINN，在多次训练和测试划分中，其Spearman秩相关系数显著优于GBLUP，在育种关注的亚群体中优势更突出。在保留约**1000**个基因或性状时，模型在紧凑性与精度间取得最佳平衡。

研究还测试了BINN在不同群体间的适用性。当训练数据中不含主流杂种优势群时，BINN依然表现稳定。不过，当面对甜玉米、热带种质等亲缘关系较远的群体时，过于固定的先验知识反而限制了模型的适应能力。

BINN另一优势在于生物学发现。后验敏感性分析通过扰动中间层潜变量，能识别传统**TWAS/GWAS**遗漏的非线性或上位性效应基因，除已知开花基因外，还发现一批新候选基因。BINN虽未接受过表达量预测的训练，其潜变量却与真实基因表达显著相关，这说明模型在没有人为干预的情况下，自行捕捉到了具有生物学内涵的信号。

![](https://relay-1.bijitongbu.site/p/671b4b616f7873a01ace0c4e90f15e4f.png)

图2.BINN提升基因型-表型预测精度与发现能力

![|18](https://relay-1.bijitongbu.site/p/e5666bd0a4737eb97e5d030246887fd7.png)

**04**

## 合成代谢组学验证：已知因果下的模型检验

为了验证BINN是否真能抓住背后的生物学规律，研究团队搭建了一个“已知答案”的模拟系统——用数学方程模拟植物分枝过程中四种激素和糖类之间的相互作用。

在不同样本量下的测试发现：当数据较少时，BINN的表现明显优于传统方法，这说明借助通路信息引导模型学习，能在灵活性和稳定性之间找到更好的平衡；当数据充足时，BINN也不输给全连接网络，还能保留捕捉复杂关系的能力。

在部分样本能测到中间代谢物的情况下，研究给模型加了一道“辅助题”——鼓励其中间层的表征尽量接近真实的代谢物数据。结果发现，只要有50%的样本提供辅助信息，模型精度就能达到100%信息时的水平，抗干扰能力很强；但如果只有10%，辅助信息就起不到什么作用。

即便完全不给中间代谢物的信息，BINN自己学到的中间表征仍然与生长素、细胞分裂素、蔗糖等关键物质高度吻合，只有独脚金内酯稍弱。进一步分析还证实，蔗糖和生长素是对最终表型影响最大的两条通路，这与模拟系统的真实设定完全一致。

![](https://relay-1.bijitongbu.site/p/00a453c4a8223efbb5a6ea4637234d6f.png)

图3.BINN在合成代谢组学中的验证结果

![|18](https://relay-1.bijitongbu.site/p/dc3493a9afbba22c5c254bcb294f25bc.png)

**05**

## 总结与展望：精准育种的可解释AI新范式

BINN框架为**作物基因组预测**开辟了新路径：

**●精度提升：**数据不充分时，预测精度仍明显优于GBLUP等传统方法

**●实用便捷：**实际使用时只需提供基因型数据，可直接与现有育种流程衔接

**●可解释性强：**通过敏感性分析能找到传统手段容易漏掉的非线性效应基因

**●灵活可扩展：**支持多种组学数据、软约束调节以及跨群体应用

不过研究也指出了它的短板：模型效果高度依赖先验知识的准确程度，如果知识本身有偏差或面对亲缘关系较远的群体，过于固定的先验反而会限制模型发挥；另外，软约束带来的提升并不稳定，在代谢组数据上有效，换到转录组数据就几乎看不到增益。

该研究提出了**基于生物学的神经网络框架(BINN)**，区分了模型训练与推断两个阶段——训练时整合**多组学数据**与**通路先验**构建稀疏网络结构，推断时仅需**基因型**数据即可预测**表型**。通过玉米真实数据和合成代谢模型两类案例验证，BINN在数据不充足的条件下预测精度显著优于GBLUP等基线，其敏感性分析还能发现传统关联分析难以捕捉的**非线性/上位性效应基因**，为**作物基因组选择**与**候选基因挖掘**提供了兼具精度与可解释性的新工具。

doi.org/10.1111/tpj.710769

![](https://relay-1.bijitongbu.site/p/050940ef58c26d09446a1fc2fc969ab0.png)

> 📹 此处为视频内容（vid: wxv\_4504136091452801024）（上图为封面），未能直接提取，请前往原文查看：[在公众号原文中观看](https://mp.weixin.qq.com/s?__biz=MzI0MDI5NjM2NA==&mid=2247521844&idx=1&sn=9b1246039e6daa2a4876162671341cde&chksm=e81ad1416ce8d0bc321d91463dfab65bcfba39bd944f3d409e4d1819ca3842ee13c7cee17fb3&mpshare=1&scene=1&srcid=0818IiB5f8Yl2HjqsioxEIYG&sharer_shareinfo=19abdc00bb8525717521924cad65e3f7&sharer_shareinfo_first=19abdc00bb8525717521924cad65e3f7#rd)

![](https://relay-1.bijitongbu.site/p/53afbdcbd26a9fbefd33b234754f45e7.png)

“

**加入“农业之巅交流群”**

_/ Join in_

扫描下方二维码加小编微信，拉您进入交流群。请您备注一下：**企业/机构/学校+研究方向+姓名**，以便小编能够拉您进入目标交流群，营销广告人员勿扰。

“农业之巅交流群”是农业+人工智能交叉领域的前沿交流阵地，这里定期分享国内外**植物表型**、**智能育种**、**智慧农业**领域前沿的研究资讯，期待与您共创农业未来。

![](https://relay-1.bijitongbu.site/p/e1fb8d21c476b753528e0517d2fafd6e.png)

![](https://relay-1.bijitongbu.site/p/2147affa35c10517ec2cb68b53c80ee0.png)

_**Recommended**_

**推荐阅读**

<table style="border-collapse: collapse"><tbody><tr><td data-colwidth="100.0000%" width="100.0000%" style="border: 1px solid #ddd; padding: 6px 10px"><div style="text-align: left; background-color: rgb(255, 255, 255)"><div style="color: rgb(0, 0, 0)"><div style="text-align: center; font-size: 12px; color: rgb(23, 75, 155)"><p style="color: rgb(0, 0, 0)"><strong><span><a class="normal_text_link mp_article_text_link" target="_blank" style="color: rgb(23, 75, 155)" href="https://mp.weixin.qq.com/s?__biz=MzI0MDI5NjM2NA==&amp;mid=2247519039&amp;idx=2&amp;sn=227f126ca5a84b414aef9b0ae7d970ac&amp;scene=21#wechat_redirect" textvalue="" linktype="text" data-linktype="2">高精度全基因组选择AI平台GSBrain P系列</a></span></strong></p></div></div></div></td></tr><tr><td data-colwidth="100.0000%" width="100.0000%" style="border: 1px solid #ddd; padding: 6px 10px"><div style="text-align: left; background-color: rgb(255, 255, 255)"><div style="color: rgb(0, 0, 0)"><div style="text-align: center; font-size: 12px; color: rgb(23, 75, 155)"><p style="color: rgb(0, 0, 0)"><strong><span><a class="normal_text_link mp_article_text_link" target="_blank" style="color: rgb(23, 75, 155)" href="https://mp.weixin.qq.com/s?__biz=MzI0MDI5NjM2NA==&amp;mid=2247517436&amp;idx=2&amp;sn=5ffcb9f1c801c26e7df952b41d63ad2e&amp;scene=21&amp;poc_token=HKHbAmqjrLOf_xLx9Y68DCEWhYqeA7Gly9RqHs0B#wechat_redirect" textvalue="" linktype="text" data-linktype="2">近端表型自动化分析系统PhenoAI Near</a></span></strong></p></div></div></div></td></tr><tr><td data-colwidth="100.0000%" width="100.0000%" style="border: 1px solid #ddd; padding: 6px 10px"><div style="text-align: left; background-color: rgb(255, 255, 255)"><div style="color: rgb(0, 0, 0)"><div style="text-align: center; font-size: 12px; color: rgb(23, 75, 155)"><p style="color: rgb(0, 0, 0)"><strong><span><a class="normal_text_link mp_article_text_link" target="_blank" style="color: rgb(23, 75, 155)" href="https://mp.weixin.qq.com/s?__biz=MzI0MDI5NjM2NA==&amp;mid=2247517437&amp;idx=1&amp;sn=8ea6982449d874db9996beb1b0511109&amp;scene=21&amp;poc_token=HNjbAmqj_Xv9PMn8GJeNxeBfkLvSJdJCEtSWmFxk#wechat_redirect" textvalue="" linktype="text" data-linktype="2">无人机一体化分析系统PhenoAI air</a></span></strong></p></div></div></div></td></tr><tr><td data-colwidth="100.0000%" width="100.0000%" style="border: 1px solid #ddd; padding: 6px 10px"><div style="text-align: left; background-color: rgb(255, 255, 255)"><div style="color: rgb(0, 0, 0)"><div style="text-align: center; font-size: 12px; color: rgb(23, 75, 155)"><p style="color: rgb(0, 0, 0)"><strong><span><a class="normal_text_link mp_article_text_link" target="_blank" style="color: rgb(23, 75, 155)" href="https://mp.weixin.qq.com/s?__biz=MzI0MDI5NjM2NA==&amp;mid=2247490803&amp;idx=1&amp;sn=74569da41f038d8b2f69da789ce9bb14&amp;chksm=e91c5430de6bdd26e83a9224f20f34775fb2ae85879b979736fe823c2e7fc5a1dc73743f3196&amp;token=1649967276&amp;lang=zh_CN&amp;scene=21#wechat_redirect" textvalue="" linktype="text" data-linktype="2">植物表型AI算法平台PhenoAI Flow</a></span></strong></p></div></div></div></td></tr><tr><td data-colwidth="100.0000%" width="100.0000%" style="border: 1px solid #ddd; padding: 6px 10px"><div style="text-align: left; background-color: rgb(255, 255, 255)"><div style="color: rgb(0, 0, 0)"><div style="text-align: center; font-size: 12px; color: rgb(23, 75, 155)"><p style="color: rgb(0, 0, 0)"><strong><span><a class="normal_text_link mp_article_text_link" target="_blank" style="color: rgb(23, 75, 155)" href="https://mp.weixin.qq.com/s?__biz=MzI0MDI5NjM2NA==&amp;mid=2247490860&amp;idx=1&amp;sn=bf7a889f2b18da720ba321d0cb14941e&amp;chksm=e91c55efde6bdcf93747405d68d59a25573cba59f294f233d517c5d2883b34896b78cc8bd8a6&amp;token=1649967276&amp;lang=zh_CN&amp;scene=21#wechat_redirect" textvalue="" linktype="text" data-linktype="2">实验教学平台GrowthBrain E系列</a></span></strong></p></div></div></div></td></tr><tr><td data-colwidth="100.0000%" width="100.0000%" style="border: 1px solid #ddd; padding: 6px 10px"><div style="text-align: left; background-color: rgb(255, 255, 255)"><div style="color: rgb(0, 0, 0)"><div style="text-align: center; font-size: 12px; color: rgb(23, 75, 155)"><p style="color: rgb(0, 0, 0)"><strong><span><a class="normal_text_link mp_article_text_link" target="_blank" style="color: rgb(23, 75, 155)" href="https://mp.weixin.qq.com/s?__biz=MzI0MDI5NjM2NA==&amp;mid=2247496841&amp;idx=4&amp;sn=7e83c308c3a703c73b73701afa142fad&amp;scene=21&amp;poc_token=HBDcAmqjm228i_yn6k6869M3hx8q1TEaR3_tggpk#wechat_redirect" textvalue="" linktype="text" data-linktype="2">无代码AI平台GrowthBrain</a></span></strong></p></div></div></div></td></tr></tbody></table>

#基因组预测 #作物育种 #可解释AI #多组学整合 #BINN

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/f3b52863_1787014124517?u=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzI0MDI5NjM2NA%3D%3D%26mid%3D2247521844%26idx%3D1%26sn%3D9b1246039e6daa2a4876162671341cde%26chksm%3De81ad1416ce8d0bc321d91463dfab65bcfba39bd944f3d409e4d1819ca3842ee13c7cee17fb3%26mpshare%3D1%26scene%3D1%26srcid%3D0818IiB5f8Yl2HjqsioxEIYG%26sharer_shareinfo%3D19abdc00bb8525717521924cad65e3f7%26sharer_shareinfo_first%3D19abdc00bb8525717521924cad65e3f7%23rd&s=obsidian)
