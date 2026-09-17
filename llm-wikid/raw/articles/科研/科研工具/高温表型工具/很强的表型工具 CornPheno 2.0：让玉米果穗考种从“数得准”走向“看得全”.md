---
description: 很强的表型工具/
author: 植物表型资讯
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=MzI0Mjg5ODI1Ng==&mid=2247545960&idx=2&sn=25afe5c65783d7e0b60b22a2073334c6&chksm=e8f81f7f72f15ec21a563b51e7b13726b914fc2aadfaf8841da5b66439af77ffdd4f2f0a77b1&mpshare=1&scene=1&srcid=0701YNA5B9qLRSGjMPRqPnuG&sharer_shareinfo=ef63c423f08b39172e1a8bd096da590d&sharer_shareinfo_first=ef63c423f08b39172e1a8bd096da590d#rd
saved: 2026-07-01
tags:
  - 笔记同步助手
  - 科研/玉米
id: 8cb0e6be-6176-47ab-a5e2-cd8d58b254cf
---

# CornPheno 2.0：让玉米果穗考种从“数得准”走向“看得全”
#笔记同步助手
## 来源
[原文链接](https://mp.weixin.qq.com/s?__biz=MzI0Mjg5ODI1Ng==&mid=2247545960&idx=2&sn=25afe5c65783d7e0b60b22a2073334c6&chksm=e8f81f7f72f15ec21a563b51e7b13726b914fc2aadfaf8841da5b66439af77ffdd4f2f0a77b1&mpshare=1&scene=1&srcid=0701YNA5B9qLRSGjMPRqPnuG&sharer_shareinfo=ef63c423f08b39172e1a8bd096da590d&sharer_shareinfo_first=ef63c423f08b39172e1a8bd096da590d#rd)
## 正文
公众号名称：植物表型资讯

作者名称：

发布时间：2026-07-01 06:10

![[llm-wikid/raw/assets/images/a73251a40590f03e106a9bb9c0cc50e2_MD5.png]]

![[llm-wikid/raw/assets/images/76cee1378eb91f60d9efb6b1a4a05321_MD5.png]]

![[llm-wikid/raw/assets/images/e732e84264d9a7e195dbba55bf4c15d6_MD5.png]]

![[llm-wikid/raw/assets/images/dcdd8384c592847bf91df6fb6a8b7f3c_MD5.png]]

本文是韩志国博士在南北学苑微信群的值日文章。

各位老师好！今天是2026年6月30日，我是韩志国，代表30小组（继往开来）值日。今天我想给大家分享全新升级的CornPheno 2.0玉米果穗考种技术。

我们于2024年1月份发布的微信小程序**OpenPheno**（[Plant Methods, 2025](https://mp.weixin.qq.com/s?__biz=MzI5NTAwODE3NA==&mid=2649898961&idx=2&sn=9d98f398904791ec787b786768e9a61d&scene=21#wechat_redirect)），是一个面向农业从业人员的免费AI小工具，涵盖籽粒考种、果穗考种（[Plant Phenomics, 2025](https://mp.weixin.qq.com/s?__biz=MzI5NTAwODE3NA==&mid=2649899605&idx=3&sn=d9781f828d581b387dbdfb589e20f2b6&scene=21#wechat_redirect)）、麦穗计数、叶面积分析等10个模块。该小程序发布以来，得到了全球农业从业人员的欢迎，目前有2.4万多人在使用该工具。

其中，玉米果穗考种模块**CornPheno**，由宏表型实验室和华中科技大学联合开发。它把手机拍照、AI 识别和玉米果穗表型提取连到了一起。2025 年发表在 Plant Phenomics 的 CornPheno 工作，以点查询 Transformer 为核心，让手机端开放环境下的玉米果穗考种成为可能：拍下一张果穗图像，系统可以返回穗粒数、穗行数、单行粒数等关键指标。

我们近期全新发布的**CornPheno 2.0**则继续往育种现场更真实、更复杂的方向走。它不是简单把模型“再调准一点”，而是围绕实际使用中最常遇到的几个问题进行系统升级：一张图里不止一穗怎么办？只拍到单面，能不能估计整穗结构？遇到非黄色、缺粒、排列不规则的材料还能不能稳？除了数粒数，能不能顺手把穗长、穗宽、秃尖也量出来？

**一**

**从 1.0 到 2.0：升级的是整套考种能力**

![[llm-wikid/raw/assets/images/9349c75d5a23d38ad5c0cd09f2cb84a6_MD5.png]]

CornPheno 1.0 的核心，是用 CornPET对玉米籽粒进行点级定位，再通过行结构分析方法识别穗行，最终输出穗粒数、穗行数和单行粒数。它的价值在于把“数一穗玉米”从人工流程变成了可解释的图像智能流程：模型不只是给出一个总数，还能告诉我们每个籽粒大致在哪里。

但育种现场从来不只面对“标准黄色、单穗、单面、排列规则”的理想样本。CornPheno 2.0 的优化目标可以概括为四句话：**由单穗到多穗，由单面到整穗，由简单到复杂，由单一表型到多表型**。换句话说，它要解决的不是实验室里的一张漂亮图，而是田间、样品台和批量考种流程里真正会遇到的复杂图像。

**二**

**多穗同框：一张图里有多穗，也能逐穗分析**

![[llm-wikid/raw/assets/images/9af41fd9ab05a128ed36332a53bbedee_MD5.png]]

在实际采集时，样品往往不会乖乖地一穗一图。多穗同框、背景干扰、边缘遮挡和摆放不整齐都很常见。CornPheno 2.0 增加了多穗同框检测与表型分析能力：系统先在整张图中找到每一个果穗，再把单穗区域交给穗粒计数模块处理，最后按单穗输出对应表型结果。从功能上看，这意味着用户不必频繁调整拍摄节奏，也不必先手动裁剪每个果穗。对于育种材料批量拍摄、样品盘集中采集和制种企业质检场景，多穗同框可以显著降低采集负担。

背后的技术思路并不复杂：用目标检测模型先“找穗”，再用 CornPET 继续“数粒”。对于置信度较低、但可能是真实果穗的区域，系统还会结合穗粒点数量和行结构信息进行二次判断。这样做的好处是，检测负责把目标框出来，点查询模型负责给出更细的籽粒结构，两者互相补位。

在现有实验中，多穗同框场景下的穗粒数预测取得了 R²=0.9551 的结果，说明这一路线已经能够较好支撑多穗图像中的单穗定位、区域裁剪和粒数估计。

**三**

**整穗估计：只拍单面，也尽量看见背后的结构**

穗行数是玉米果穗表型里非常重要的一类结构性指标。传统上，如果要准确判断整穗行数，往往需要人工翻看、旋转果穗，或者依赖更复杂的三维采集设备。但在手机拍摄或普通相机采集中，最自然、最高效的方式通常还是单面成像。

CornPheno 2.0 面向这一问题提出了整穗检测思路：不强行要求 3D 采集，而是基于单面可见籽粒点、行结构和几何先验，推断背侧不可见的穗行信息。也就是说，系统看到的是一面图像，但输出目标从“单面行数”扩展到“整穗行数”。这里不需要用户理解具体算法，只需要知道：系统不是凭空猜背面，而是根据玉米果穗本身具有规律性的行列结构来进行约束推断。

在已有测试中，整穗行数估计在图像级别的准确率达到 72.86%，在同一果穗多图像投票后的编号级准确率达到 85.71%，误差控制在两行以内的准确率可达 100%。这意味着在工程应用层面，CornPheno 2.0 已经具备把“单面拍摄”推进到“整穗表型估计”的实用潜力。

**四**

**复杂样本增强：非黄色、缺粒、异形，也要尽量稳**

真实玉米材料并不总是标准黄色，也不总是颗粒饱满、排列整齐。育种材料里常会出现非黄色籽粒、缺粒、秃尖、行列扭曲、边缘模糊、异形果穗等情况。对人来说，这些样本只是“难看一点”；对算法来说，却可能导致聚类不稳、边界误分和行标签偏移。

CornPheno 2.0 因此把复杂样本作为重点增强对象。一方面，通过补充和清洗数据，让模型见过更多真实材料的变化；另一方面，通过改进行检测流程，让系统不再过度依赖标准黄色、规则排列和清晰边界。

这一能力的意义在于，CornPheno 2.0 不只服务于展示图，也服务于问题样本。对于育种工作者来说，真正有价值的往往正是那些形态特殊、抗性表现异常或发育不均衡的材料。系统能否在这些样本上保持稳定，决定了它能否进入实际筛选流程。

已有实验显示，在非黄色样本上，穗粒数预测 R² 达到0.9256；在不规则样本上，穗粒数预测 MAE 从69.57 降至 56.47，R² 提升至 0.9708；复杂样本穗行数预测准确率也从 76.5% 提升到 80.9%。这些结果说明，2.0 的重点不是只在标准样本上更漂亮，而是在困难样本上更可靠。

**五**

**多表型扩展：不止粒数，还能量穗长、穗宽和秃尖**

![[llm-wikid/raw/assets/images/4a867a63e6b071aec1f2cf8d0ebbe813_MD5.png]]

对于玉米考种来说，穗粒数只是起点。穗长、穗宽、秃尖长度等形态指标，同样关系到材料评价、产量估计和异常发育筛查。过去这些指标往往需要人工尺量或额外设备记录，流程分散，数据标准也不完全一致。

CornPheno 2.0 将果穗形态测量纳入同一套图像分析流程。系统通过关键点定位和几何距离计算，对果穗的长度、宽度和秃尖区域进行测量，让“数粒”和“量形”在同一张图像上完成。

这类功能对实际应用很直接：穗长穗宽可以用于材料外观和产量潜力评估，秃尖长度可以辅助识别授粉不良、营养不足或环境胁迫导致的异常发育。对于批量样本而言，自动化测量不仅节省时间，也让不同批次、不同人员之间的数据更容易对齐。

在当前实验条件下，穗长、穗宽和秃尖长度测量的 R² 分别达到0.9719、0.9489 和 0.9687，显示出较好的形态测量一致性。

**六**

**底座更稳更轻更快：CornPET++ 让部署更接近现场**

![[llm-wikid/raw/assets/images/01dabf08307f83c90266f09387b8592f_MD5.png]]

功能越多，并不意味着系统可以越来越重。要真正走向手机端、边缘端或低成本部署，模型必须更快、更轻、更省显存。CornPheno 2.0 的底座升级中，CornPET++ 承担了这一角色。

CornPET++ 的思路可以理解为“保留有用的点级定位能力，针对玉米图片的特点，剪掉不适合玉米单穗计数的冗余”。这些技术听起来很“技术”，但落到用户侧就是三件事：结果更稳，等待更短，部署成本更低。已有统一实验口径下，最终模型的R² 从 0.760 提升到 0.879；平均推理速度提升三倍，显存需求降低到原来的1/8，计算量是先前的一半，CornPET++为部署模型提供了极大的优势，实现了更稳、更快、更轻。

**七**

**技术路线：先点、再线、再到整穗和多表型**

CornPheno 2.0 把“点”作为基础，用“框”解决多穗，按“线”理解结构，以“形”扩展表型。

CronPheno2.0的优势在于，它不是让一个黑箱直接吐出所有结果，而是让每一步都有可以观察、可以解释、可以修正的中间信息。对农业表型应用而言，可解释性并不是锦上添花，而是让育种人员愿意信任和使用系统的重要前提。

八

**面向应用：把考种从“单点工具”变成“批量流程”**

CornPheno 2.0 的价值，不在于替代育种专家的判断，而在于把重复、耗时、容易出错的基础表型提取交给 AI。它可以服务于育种材料快速初筛、多穗样本批量计数、复杂果穗异常筛查、制种质量评价和田间采样后的统一数据整理。

对科研人员来说，CornPheno 2.0 提供的是更丰富、更标准化的表型数据；对育种单位来说，它提供的是更低成本的批量考种能力；对后续智能育种系统来说，它则是把图像、结构和数值表型连接起来的数据入口。

从“牙咬、手摸、眼瞪”的经验式考种，到“一张图生成多项表型”的现代 AI 标尺，CornPheno 2.0 让玉米果穗表型提取更接近真实生产场景。它从CornPheno 1.0 的单穗开放环境计数出发，进一步走向多穗、整穗、复杂样本和多表型分析。下一步，当这些能力与移动端、边缘端和育种数据平台更紧密结合，玉米考种将不再只是一个低效环节，而会成为智能育种链条中稳定、快速、可追溯的数据入口。

  

## 关于宏表型实验室

> 宏表型实验室是慧诺瑞德（PhenoTrait）旗下新型研究机构，拥有价值2000多万的各类型高通量表型平台，立足于农业科技变革、产业驱动创新，开展引领性的植物表型技术与装备应用研究、产学研一体化的共性技术联动突破，以及提供高质量植物表型技术服务等，长远发展目标是协同创新、持续发力、纵深推进植物表型技术的基础性与系统化应用，使之成为数字农业与智慧育种的新质生产力。​自研自走式（TraitGo）、轨道式（TraitDiscover）、传送式（PhenoConveyor）、落地式（TraitScanner、TraitScanChamber Pro、Trait4D Pro）、台式（TraitScanChamber、RootPheno3D、SeedHSI、See3DSpec）、物联网式（Pheno-IoT）等各种类型表型平台，全国落地应用数百套。​在国际上首次提出“植物表型就是为植物体检”的概念，并被广泛接受和传播；提出植物表型技术的三位一体概念，将表型传感器对应人的眼睛，自动化系统对应人的身体，软件和算法对应人的大脑（其中软件对应大脑皮层、算法对应神经网络）；提出基于单目深度估计的表型算法DepthCropSeg和跨场景跨物种植物表型分割基石模型DepthCropSeg++，为田间表型数据分割节省了70%的工作量；提出利用智能手机进行低成本三维表型测量的方案MobilePheno3D，解决了三维表型测量的大范围落地应用问题。​
> 
> 目前承担国家和地方课题各1项，在《Trends in Plant Science》、《IEEE Journal of Selected Topics in Signal Processing》、《Computer & Electronics in Agriculture》、《Plant Phenomics》、《The Crop Journal》、《aBIOTECH》、《Smart Agriculture Technology》、《Plant Methods》等国际学术期刊发表论文13篇，授权发明专利27项，其它类型知识产权百余项。

![[llm-wikid/raw/assets/images/5227d4a3e24947174e655f45e4b1608d_MD5.png]]

韩志国

2026年6月30日

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
> -   [植物表型资讯2026年1-12月目录汇总](https://mp.weixin.qq.com/s?__biz=MzI0Mjg5ODI1Ng==&mid=2247545207&idx=3&sn=02f7b6d9e481f22a7930333d47753784&scene=21#wechat_redirect)
>     
> -   ****[植物表型资讯分类专辑直通车](https://mp.weixin.qq.com/s?__biz=MzI5NTAwODE3NA==&mid=2649889890&idx=1&sn=055b1892264f8f5294311106aa93ff02&scene=21#wechat_redirect)****
>     
> -   ****[最畅销的田间表型平台长什么样？](http://mp.weixin.qq.com/s?__biz=MzI5NTAwODE3NA==&mid=2649890729&idx=1&sn=a86eb8a0ca44eb10ef723fca5c13510d&chksm=f45c9d68c32b147eaadb4d8c9d95f7f4deb6c2731fdb2dd0bab80822855c4ca9b690e792f341&scene=21#wechat_redirect)****
>     

![[llm-wikid/raw/assets/images/37015bcbd69e47c74ade937b01f58492_MD5.jpg]]

> 📹 视频内容（上图为封面），请前往原文观看：[在公众号原文中观看](https://mp.weixin.qq.com/s?__biz=MzI0Mjg5ODI1Ng==&mid=2247545960&idx=2&sn=25afe5c65783d7e0b60b22a2073334c6&chksm=e8f81f7f72f15ec21a563b51e7b13726b914fc2aadfaf8841da5b66439af77ffdd4f2f0a77b1&mpshare=1&scene=1&srcid=0701YNA5B9qLRSGjMPRqPnuG&sharer_shareinfo=ef63c423f08b39172e1a8bd096da590d&sharer_shareinfo_first=ef63c423f08b39172e1a8bd096da590d#rd)

![[llm-wikid/raw/assets/images/89c9c1451767ca2ea6b6ea7a86431a2f_MD5.jpg]]

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/3f39b83b_1782878490629?u=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzI0Mjg5ODI1Ng%3D%3D%26mid%3D2247545960%26idx%3D2%26sn%3D25afe5c65783d7e0b60b22a2073334c6%26chksm%3De8f81f7f72f15ec21a563b51e7b13726b914fc2aadfaf8841da5b66439af77ffdd4f2f0a77b1%26mpshare%3D1%26scene%3D1%26srcid%3D0701YNA5B9qLRSGjMPRqPnuG%26sharer_shareinfo%3Def63c423f08b39172e1a8bd096da590d%26sharer_shareinfo_first%3Def63c423f08b39172e1a8bd096da590d%23rd&s=obsidian)
