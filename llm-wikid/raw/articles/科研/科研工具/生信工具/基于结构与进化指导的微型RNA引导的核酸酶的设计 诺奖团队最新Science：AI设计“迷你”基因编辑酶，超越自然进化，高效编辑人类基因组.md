---
description: 基于结构与进化指导的微型RNA引导的核酸酶的设计/
author: 生物世界
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=Mzk0NDc0NjQxMA==&mid=2247492792&idx=1&sn=32e79453b9e3a7b52311b191ebdd5a46&chksm=c28f544683336fcdafb70d4a5d3b8fffcb79edb0970189600b6cee8f3c48f7f6c26a0bec6e55&mpshare=1&scene=1&srcid=0718GZvCx557A9D38d8FYAoK&sharer_shareinfo=75586bca7ffccb4762e897045ef8663f&sharer_shareinfo_first=75586bca7ffccb4762e897045ef8663f#rd
saved: 2026-07-18
tags:
  - 笔记同步助手
id: 46a2cfe7-9dcd-4139-8e91-3c8bbb8ef2ae
---

# 诺奖团队最新Science：AI设计“迷你”基因编辑酶，超越自然进化，高效编辑人类基因组
#笔记同步助手
## 来源
[原文链接](https://mp.weixin.qq.com/s?__biz=Mzk0NDc0NjQxMA==&mid=2247492792&idx=1&sn=32e79453b9e3a7b52311b191ebdd5a46&chksm=c28f544683336fcdafb70d4a5d3b8fffcb79edb0970189600b6cee8f3c48f7f6c26a0bec6e55&mpshare=1&scene=1&srcid=0718GZvCx557A9D38d8FYAoK&sharer_shareinfo=75586bca7ffccb4762e897045ef8663f&sharer_shareinfo_first=75586bca7ffccb4762e897045ef8663f#rd)
## 正文
公众号名称：植物基因编辑入门

作者名称：生物世界

发布时间：2026-07-18 20:24

原文链接：[https://www.science.org/doi/10.1126/science.aed6123](https://www.science.org/doi/10.1126/science.aed6123)

[![](https://relay-1.bijitongbu.site/p/d525d45d6d82e97e5cb4b1f7cd471a9f.png)](https://mp.weixin.qq.com/s?__biz=Mzg3MDY4OTM4Mg==&mid=2247495986&idx=1&sn=61a0150f98ac9db1792f20e2d4c43624&scene=21#wechat_redirect)

![](https://relay-1.bijitongbu.site/p/e7504785b36df4d5962b5342cd1bc8e3.png)

撰文丨王聪

编辑丨王多鱼

排版丨水成文

CRISPR-Cas 系统通过实现可编程的、序列特异性的 DNA 和 RNA 靶向，已彻底改变了基因组编辑技术，为精确的遗传和表观遗传调控奠定了基础。蛋白质设计有望进一步拓展这些功能，创造出具有自然界中未见的功能和特性（包括序列与结构）的 RNA 引导的核酸酶。

然而，这类设计极具挑战性，因为这些核酸酶是多结构域的核酸结合蛋白，其活性依赖于不同构象状态对 RNA 和 DNA 的协同识别、激活及切割。基于序列的生物语言模型通过进化数据训练，能够通过推断序列与功能之间的关系来生成 RNA 引导的核酸酶，但即使经过大量后续筛选，其所生成的活性核酸酶通常仍与训练时参考的序列高度相似。

结构指导的理性设计方法则提供了一种稳健策略，可采样出高度多样化的蛋白质序列，甚至包括自然界中不存在的结构，从而实现蛋白质的从头设计。尽管该方法在动态开关和 DNA 结合蛋白的设计上已取得成功，但对于具有多个功能结构域和构象状态的复杂酶（例如 RNA 引导的核酸酶）的设计，依然是一个极具吸引力却尚未解决的难题。

2026 年 7 月 15 日，CRISPR 基因编辑先驱、诺奖得主 Jennifer Doudna 教授在国际顶尖学术期刊 Science 上发表了题为：Structure and evolution-guided design of minimal RNA-guided nucleases 的研究论文。

该研究采用一种蛋白质设计策略，将结构导向的逆折叠模型与基于进化的氨基酸残基约束相结合，生成了活性强且序列多样的 TnpB 变体（最小的 CRISPR-Cas12 样核酸酶），命名为——SynTnpB。通过高通量筛选 AI 生成的变体，获得了在细菌、植物和人类细胞中保持甚至超过野生型活性的基因编辑工具。对其中序列差异化最大的变体进行冷冻电镜结构解析，揭示了其在不同构象下 RNA-DNA 界面中的稳定相互作用，证明了该方法的设计潜力。这项研究建立了一种创造非天然 RNA 引导的核酸酶及构象活性核酸结合蛋白的策略，显著扩展了可设计的蛋白质空间。

![](https://relay-1.bijitongbu.site/p/b8cf40d32b7e9ce3234775fe7d127459.png)

“迷你版”基因编辑工具

说到基因编辑，很多人首先想到的通常是被誉为“基因魔剪”的革命性工具——CRISPR-Cas9，但他的缺点也很明显——Cas9 核酸酶太大了，以至于难以通过腺相关病毒（AAV）进行递送，这大大限制了其在体内基因治疗中的应用。

于是，科学家们把目光投向了 TnpB——这是一类小得多的微型核酸酶，只有约 400 个氨基酸，不到 Cas9 一半大小。它是 CRISPR-Cas12 家族的祖先，虽然体型迷你，却能完成 RNA 引导的 DNA 切割任务。

但问题来了：自然界的野生型 TnpB 虽然能用，但还不好用。

AI 设计：不只是模仿，更是创造

传统上，想要改进这类蛋白质，科学家通常采用两种方法——

一种是基于序列的生物语言模型，它们能生成蛋白质序列，但往往只是对天然序列的“微调”，缺乏真正的创新。

另一种是结构指导的理性设计，可以创造出高度新颖的序列，但对于像 TnpB 这样需要协调多个功能域和构象状态的复杂酶来说，难度极大。

这次，研究团队玩了个“组合拳”。他们使用了名为 ESM-IF1 的反向折叠模型——这是一种 AI 模型，能够根据给定的蛋白质三维结构，逆向推导出可能折叠成该结构的氨基酸序列。

但光靠结构不够。研究团队还引入了进化信息约束：通过分析数千种天然 TnpB 的同源序列，找出哪些位点在进化中高度保守（说明很重要），哪些位点与 RNA 或 DNA 存在共进化关系（说明有相互作用）。他们将这两类关键位点“锁定”，其余位置则交给 AI 自由发挥。

![](https://relay-1.bijitongbu.site/p/cf64601932a485e0ecc511108ebc0ada.png)

基于 ESM-IF1 的 RNA 引导的核酸酶 TnpB 设计策略

研究团队成功设计出了 466 个有活性的 TnpB 变体，成功率高达 24%，其中约 8% 的活性甚至超过了天然版本。

分域设计：分而治之的智慧

该研究中的一个有趣的发现是，TnpB 的不同结构域对序列变化的容忍度截然不同。

研究团队采用了“分域设计”策略：将 TnpB 分为 REC（识别结构域）和 NUC（核酸酶结构域）两个独立模块，分别由 AI 设计优化后，再进行组合。

结果显示，NUC 结构域非常“皮实”，即使在高达 0.65 的保守性阈值下，16 个变体中仍有 13 个保持活性。而 REC 结构域则相当“娇气”，只有在最低的保守性阈值（0.25）下才有一个变体保持活性。

这种不对称性反映了不同结构域的功能差异：REC 负责识别 DNA 上的 TAM 序列，需要精确的分子识别；而 NUC 主要负责切割，对序列变化的容忍度更高。

这一发现为未来设计其他多结构域蛋白提供了重要启示：对不同模块采取不同的设计策略，可能是成功的关键。

在人类细胞中的“超常发挥”

最激动人心的结果来自人体细胞实验。

研究团队选择了 9 个最具代表性的 AI 设计变体——v1-v9，在人类细胞系 HEK293T 中测试它们对蓝色荧光蛋白（BFP）基因的敲除效率。

结果显示，来自耐辐射奇球菌的野生型 **ISDra2-TnpB 的编辑效率约为28%，而 AI 设计的 v1 和 v5 变体分别达到了 46% 和 50%——提升了近一倍！更令人振奋的是，在对内源性基因（RUNX1、EMX1等）的编辑中，v1 变体在 EMX1 位点的编辑效率是野生型的 3.8 倍，v5 则是 3.1 倍。在拟南芥原生质体中，v1 变体的**的编辑效率同样由于野生型。此外，这些 AI 设计的变体保持了良好的特异性，没有出现大量脱靶效应。****

****![](https://relay-1.bijitongbu.site/p/c5ede3d0fd705f972a6b468933c43f91.png)****

AI 设计的 TnpB 用于 HEK293T 细胞的基因编辑

这些 AI 设计的“基因剪刀”，在人类细胞以及植物细胞中的某些靶点上的编辑效果，大幅超越了自然进化了亿万年的野生型。

冷冻电镜下的“解剖学”

为了搞清楚 AI 到底做了什么，研究团队对活性最高且序列差异最大的 v7 变体进行了冷冻电镜结构解析。v7 变体与野生型仅有 77% 的序列同源性——也就是说，超过五分之一的氨基酸都被 AI 替换掉了。

冷冻电镜图像显示，在 RNA-蛋白质界面上，AI 引入了多个带正电荷的氨基酸替换（K224R、Q227R、T228R、K245R），形成了更强的静电相互作用网络，像是一双更有力的手紧紧握住 RNA 分子。

更令人惊讶的是，研究团队捕获到了一个此前从未在 TnpB 中观察到的转座子相关基序（transposon-associated motif，TAM，相当于 Cas9 的 PAM 序列）结合中间态。在这个状态下，蛋白质和 RNA 的构象类似于二元复合物，但已经与目标 DNA 有了初步接触。AI 设计的氨基酸残基稳定了这个短暂的过渡状态，使其得以被捕捉和研究。

![](https://relay-1.bijitongbu.site/p/ef0dffcf1795a67988b25feca3982c80.png)

AI 设计的 v7 变体的冷冻电镜结构揭示了 RNA-DNA 界面残基及保守的构象运动

这表明，AI 不仅仅是在复制大自然的设计方案，而是在创造新的、更优的分子相互作用网络，甚至可能改变了蛋白质的动力学行为。

意义与展望

这项研究的突破性在于——

第一，它证明了 AI 可以设计出真正创新的功能性蛋白质，而不是仅仅停留在对天然序列的微小调整。24% 的成功率在蛋白质设计领域是一个相当亮眼的数字。

第二，它为基因编辑工具的开发开辟了新路径。TnpB 的小尺寸使其非常适合通过腺相关病毒（AAV）等载体进行体内递送，而 AI 优化后活性的大幅提升，使其有望成为下一代基因治疗的候选工具。

第三，这种方法具有普适性。研究团队开发的“进化信息掩码策略”不依赖于已有的实验结构，只需进化信息即可确定关键残基。这意味着它可以应用于其他类型的 RNA 引导的核酸酶，甚至是其他多结构域蛋白质。

这项研究也完美地诠释了“站在巨人的肩膀上”，这里的“巨人”，即是亿万年来的自然进化，也是近年来飞速发展的 AI 技术——自然亿万年来进化出来的 TnpB 分子，在 AI 的帮助下，几天之内就设计出了性能更优的变体。

论文链接：

https://www.science.org/doi/10.1126/science.aed6123

[![](https://relay-1.bijitongbu.site/p/87104a4b6c2abb0a39b0be30b0426458.png)](https://mp.weixin.qq.com/s?__biz=Mzg3MDY4OTM4Mg==&mid=2247495986&idx=1&sn=61a0150f98ac9db1792f20e2d4c43624&scene=21#wechat_redirect)

![|171](https://relay-1.bijitongbu.site/p/01f171551f6f5bcaa529917b7a4d27b9.png)

![](https://relay-1.bijitongbu.site/p/e4c7ba29f23ad3c9b1add53e512f014e.png)

![](https://relay-1.bijitongbu.site/p/6e4c2070608bff55c55974f2725ea581.png)

![](https://relay-1.bijitongbu.site/p/a3cefe5d7dce009c398943e3b4d71545.png)

![](https://relay-1.bijitongbu.site/p/5561ac05629ed180d20f6fae4d8f93e4.png)

设置**星标**，不错过精彩推文

![](https://relay-1.bijitongbu.site/p/47a8d61dd0c8444b5e54552a5d12d1fd.png)

![](https://relay-1.bijitongbu.site/p/f3aca84591b6cef4eecb2962f77dfa45.png)

**开放转载**

欢迎转发到朋友圈和微信群

> **微信加群**
> 
> 为促进前沿研究的传播和交流，我们组建了多个**专业交流群**，长按下方二维码，即可添加小编微信进群，由于申请人数较多，添加微信时请备注：**学校**/**专业**/**姓名**，如果是**PI**/**教授**，还请注明。
> 
> ![](https://relay-1.bijitongbu.site/p/3723e2ced5f504df10fd7e20076a7624.png)

**点****在看****，传递你的品味**

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/2fef2988_1784378676540?u=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzk0NDc0NjQxMA%3D%3D%26mid%3D2247492792%26idx%3D1%26sn%3D32e79453b9e3a7b52311b191ebdd5a46%26chksm%3Dc28f544683336fcdafb70d4a5d3b8fffcb79edb0970189600b6cee8f3c48f7f6c26a0bec6e55%26mpshare%3D1%26scene%3D1%26srcid%3D0718GZvCx557A9D38d8FYAoK%26sharer_shareinfo%3D75586bca7ffccb4762e897045ef8663f%26sharer_shareinfo_first%3D75586bca7ffccb4762e897045ef8663f%23rd&s=obsidian)
