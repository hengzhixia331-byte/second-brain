---
description: /
author: PhenoTrait
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=MzI0Mjg5ODI1Ng==&mid=2247546012&idx=1&sn=a516fc3ff06e60b1c32933d271c38c70&chksm=e81b0ab6d9679c1af444216049e14dc1f90229243fe0c6d939da0dd80d99d81ac3fa6959466e&mpshare=1&scene=1&srcid=0704rTj6U4Emhyplm3tdKwRj&sharer_shareinfo=3437c0148ddc340680fbaf278ea09835&sharer_shareinfo_first=3437c0148ddc340680fbaf278ea09835#rd
saved: 2026-07-04
tags:
id: 902f6e8d-75a6-43f3-9a58-631185dba691
---

# Crop-IRM：作物种质资源器官表型智能识别与管理系统研发
#笔记同步助手
## 来源
[原文链接](https://mp.weixin.qq.com/s?__biz=MzI0Mjg5ODI1Ng==&mid=2247546012&idx=1&sn=a516fc3ff06e60b1c32933d271c38c70&chksm=e81b0ab6d9679c1af444216049e14dc1f90229243fe0c6d939da0dd80d99d81ac3fa6959466e&mpshare=1&scene=1&srcid=0704rTj6U4Emhyplm3tdKwRj&sharer_shareinfo=3437c0148ddc340680fbaf278ea09835&sharer_shareinfo_first=3437c0148ddc340680fbaf278ea09835#rd)
## 正文
公众号名称：植物表型资讯

作者名称：PhenoTrait

发布时间：2026-07-04 06:10

原文链接：[https://doi.org/10.3390/agriculture16090996](https://doi.org/10.3390/agriculture16090996)

[![](https://relay-1.bijitongbu.site/p/75fcb4e753208d48813a4baab4d69280.png)](https://mp.weixin.qq.com/s?__biz=MzI0Mjg5ODI1Ng==&mid=2247543603&idx=1&sn=1934aa52afcb6c193cc31378277c99af&scene=21#wechat_redirect)

[![](https://relay-1.bijitongbu.site/p/a40f351414a0370994442c0d69441f83.png)](https://mp.weixin.qq.com/s?__biz=MzI0Mjg5ODI1Ng==&mid=2247542326&idx=1&sn=319fcf4914cb0336c3edaa47ea0a997c&scene=21#wechat_redirect)

[![](https://relay-1.bijitongbu.site/p/8baedb92a932f15e7124b29e109c0212.png)](https://mp.weixin.qq.com/s?__biz=MzI0Mjg5ODI1Ng==&mid=2247540829&idx=2&sn=1ceb9dc2997c7324cc97bfa786512d80&scene=21#wechat_redirect)

[![](https://relay-1.bijitongbu.site/p/21460de0e7d258efd01dda63a6bf3a31.png)](https://mp.weixin.qq.com/s?__biz=MzI0Mjg5ODI1Ng==&mid=2247537489&idx=1&sn=1e789f5c892a55c1581351b338d987e8&scene=21#wechat_redirect)

作物种质资源田间表型数据的传统采集方式普遍效率低下，且主观性较强。种质资源是育种创新的核心基础，需通过精准的表型性状鉴定，方可实现资源的有效评价与高效利用。因此，种质资源数据的高效化、标准化管理在育种全流程中至关重要。

针对上述痛点，本文研发了一套以作物器官特征为核心的智能识别与信息化管理系统—Crop-IRM。该系统两大模块构成：用于项目统筹管理与数据导出的网页端，以及面向野外数据采集、实时上传的微信小程序，双端均嵌入轻量化图像分析模型。

本研究以大豆为试验材料，构建多套大豆表型性状高清数据集；依托YOLOv11系列模型，分别搭建适用于目标检测、图像分类、实例分割与姿态估计的专项分析模型，完成各类表型性状的智能化解析。

模型测试结果表明，所有算法的平均精度均值（mAP@0.5）均高于94%，Top1分类准确率达0.999。​实际场景验证显示，系统完成100张图像的批量推理耗时仅0.71～3.03秒，综合识别准确率超98%。​以上结果说明，该平台可对花、叶片、荚果等多类器官表型数据开展高效管理与智能解析，大幅降低人工目视分类的人力成本。​平台采用模块化、标准化架构设计，具备种质资源通用化管理能力。​另外，针对玉米、小麦、水稻等非大豆类作物，其数据管理、二维码关联、田间调查等基础功能可直接复用。

Crop-IRM可为作物种质资源田间表型鉴定提供一体化智能识别与管理，显著提升表型数据采集与分析的工作效率及客观规范性，同时为精准育种、智慧农业发展提供可靠的决策支撑工具。

![](https://relay-1.bijitongbu.site/p/652cbf5b877b1204dacd7dcef637b093.png)

图1. 系统架构图

![](https://relay-1.bijitongbu.site/p/6c34f47f105f24155f1108ffb11263f2.png)

图2. Crop-IRM平台操作流程说明

![](https://relay-1.bijitongbu.site/p/362922c307960cec42b15d8e47b18e8e.png)

图3. 数据集构建。(a)图像采集方式；(b)不同类别图像示例；(c)数据集划分详情与模型选择

![](https://relay-1.bijitongbu.site/p/6cda7097d0a9ea8ec004f89dd5a90b80.png)

图4. 各模型测试结果样本图。 (a)S\_L\_YOLOv11-seg模型；(b)N\_L\_YOLOv11-det模型；(c)C\_F\_YOLOv11-cls模型；(d)N\_PS\_YOLOv11-det模型；(e)C\_P\_YOLOv11-pose模型；(f)PC\_P\_YOLOv11-cls模型；(g)D\_S\_YOLOv11-det模型

![](https://relay-1.bijitongbu.site/p/a2a81899c14b2b5ee7eedef885676db3.png)

表1. 不同数据集下的模型性能

![](https://relay-1.bijitongbu.site/p/dd58a1903d2ac4e04726847b0ae72d1d.png)

表2. 模型测试结果

**来 源**

> Zhang, J.; Yang, C.; Peng, H.; Wei, X.; Zou, J.; Wang, S.; Lu, Z.; Tan, X.; Yang, F. Crop-IRM: An Intelligent Recognition and Management System for Organ Characteristics of Crop Germplasm Resources. Agriculture 2026, 16, 996. https://doi.org/10.3390/agriculture16090996

> **编辑**

> JAYz

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

![](https://relay-1.bijitongbu.site/p/ed9c9df40b1c7eafe4d45af985e8b9c9.png)

> 📹 视频内容（上图为封面），请前往原文观看：[在公众号原文中观看](https://mp.weixin.qq.com/s?__biz=MzI0Mjg5ODI1Ng==&mid=2247546012&idx=1&sn=a516fc3ff06e60b1c32933d271c38c70&chksm=e81b0ab6d9679c1af444216049e14dc1f90229243fe0c6d939da0dd80d99d81ac3fa6959466e&mpshare=1&scene=1&srcid=0704rTj6U4Emhyplm3tdKwRj&sharer_shareinfo=3437c0148ddc340680fbaf278ea09835&sharer_shareinfo_first=3437c0148ddc340680fbaf278ea09835#rd)

![](https://relay-1.bijitongbu.site/p/8380c9b3114e49e918206c3d47c5d95e.png)

![|50](https://relay-1.bijitongbu.site/p/cac44b71989d3e4eeb1d9ab7046fbd5f.png)

**戳这里，阅读原文**

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/8e10c2b7_1783125382429?u=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzI0Mjg5ODI1Ng%3D%3D%26mid%3D2247546012%26idx%3D1%26sn%3Da516fc3ff06e60b1c32933d271c38c70%26chksm%3De81b0ab6d9679c1af444216049e14dc1f90229243fe0c6d939da0dd80d99d81ac3fa6959466e%26mpshare%3D1%26scene%3D1%26srcid%3D0704rTj6U4Emhyplm3tdKwRj%26sharer_shareinfo%3D3437c0148ddc340680fbaf278ea09835%26sharer_shareinfo_first%3D3437c0148ddc340680fbaf278ea09835%23rd&s=obsidian)
