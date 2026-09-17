---
author: 橙君
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=MzYzNTg5MzIxMQ==&mid=2247488565&idx=2&sn=d39bb0e27877ee800d4f7a4ed301f6e7&chksm=f10b6ef82b0e796da8e702c34cd124e9b6d1e76d36bafd2ae19cd76f2198fc6cd4550669f1ea&mpshare=1&scene=1&srcid=0630hwLK1vcv8UiWigbEYlRg&sharer_shareinfo=8c2e29683c87d328219941701df7b97f&sharer_shareinfo_first=8c2e29683c87d328219941701df7b97f#rd
saved: 2026-06-30 08:44:21
tags:
  - 笔记同步助手
id: 9d3b6415-1066-4f6f-be85-87f5c4ffe9a0
---

公众号名称：AgriPulse

作者名称：橙君

发布时间：2026-06-30 00:00

![[llm-wikid/raw/assets/images/5f5f529ee3628e7e98fd8632f8032592_MD5.png||112]]

![[llm-wikid/raw/assets/images/33cb7ca072089c19dcfa2da912c60924_MD5.png||280]]

![[llm-wikid/raw/assets/images/439318b8444e7d885ec67c97b1e25c48_MD5.png||60]]

**WGCNA、基因功能模块网络图****及bulk转录组虚拟敲除代码自取**

///

俩月来，我们围绕植物多组学数据分析开发了一系列 R 脚本，力求将复杂分析流程标准化、一键化，降低生物信息学分析门槛。目前已整理发布三个常用工具包：一键式 WGCNA、基因功能模块网络图脚本及模板和虚拟敲除分析流程。

其中，一键式 WGCNA集成了数据预处理、软阈值筛选、模块构建、性状相关性分析、Hub 基因挖掘及图形绘制，可快速完成完整的 WGCNA 分析；基因功能模块网络图脚本及模板可整合 GO、KEGG、表达量和网络关系，生成适用于论文展示的功能模块网络图；虚拟敲除分析流程则基于转录组数据模拟关键基因扰动后的表达变化，结合通路富集和网络分析，辅助预测候选基因的潜在功能。

这些脚本兼顾易用性、可重复性和论文级可视化，可用于转录组、代谢组及多组学联合分析，适合功能基因挖掘、调控网络解析和分子机制研究。希望这些工具能帮助更多科研人员减少重复的数据处理工作，把更多精力投入到科学问题本身。

资源链接：

**一键式WGCNA（紫金配色版）：**  
https://pan.quark.cn/s/447870a767b7

![[llm-wikid/raw/assets/images/7fe727ea846f674654d7a55605321023_MD5.png]]

**基因功能模块网络图脚本及模板：**

https://pan.quark.cn/s/3f66f4d87c2f

![[llm-wikid/raw/assets/images/986b961521e018919ec6aa135df01b3b_MD5.jpg]]

**bulk转录组虚拟敲除：**

https://pan.quark.cn/s/3f8aed7c3b57

![[llm-wikid/raw/assets/images/9e15f8e68d09f329cee4f162d4f87fba_MD5.png]]

**AgriPulse**

使用方法见历史推送：

[筛了一百个候选基因，凭什么就敲这一个？先做虚拟敲除再说](https://mp.weixin.qq.com/s?__biz=MzYzNTg5MzIxMQ==&mid=2247484751&idx=1&sn=9c47eed6e9ea3a019c0cb81655a9c9c7&scene=21#wechat_redirect)

[R语言O基础保姆教程 | 一键式加权基因共表达网络分析 (WGCNA）](https://mp.weixin.qq.com/s?__biz=MzYzNTg5MzIxMQ==&mid=2247486773&idx=2&sn=d52b269a58178b18980f7ee5d7e37f3b&scene=21#wechat_redirect)

[告别Cytoscape手搓，WGCNA后R语言一键绘制基因功能模块网络图](https://mp.weixin.qq.com/s?__biz=MzYzNTg5MzIxMQ==&mid=2247485715&idx=1&sn=5106772f5f691fd537ae33c8f15094f8&scene=21#wechat_redirect)

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/c52739a5_1782780260210?u=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzYzNTg5MzIxMQ%3D%3D%26mid%3D2247488565%26idx%3D2%26sn%3Dd39bb0e27877ee800d4f7a4ed301f6e7%26chksm%3Df10b6ef82b0e796da8e702c34cd124e9b6d1e76d36bafd2ae19cd76f2198fc6cd4550669f1ea%26mpshare%3D1%26scene%3D1%26srcid%3D0630hwLK1vcv8UiWigbEYlRg%26sharer_shareinfo%3D8c2e29683c87d328219941701df7b97f%26sharer_shareinfo_first%3D8c2e29683c87d328219941701df7b97f%23rd&s=obsidian)