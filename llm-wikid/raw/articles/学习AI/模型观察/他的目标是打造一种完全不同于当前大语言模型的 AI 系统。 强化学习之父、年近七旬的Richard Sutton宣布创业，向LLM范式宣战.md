---
description: 他的目标是打造一种完全不同于当前大语言模型的 AI 系统。/
author: 张锦怡
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=MzA3NTIyODUzNA==&mid=2649800688&idx=1&sn=c72ebb8252f20705c2de390191c69939&chksm=86faa7f4c106510aa19c62ae71e62de099581a64dba0e927236e076142251f1f072d6381eae5&mpshare=1&scene=1&srcid=0714YRnAFCOXSFyj9rMvpPXa&sharer_shareinfo=89c77d7c1d3a16b908f7131ddbe6615f&sharer_shareinfo_first=89c77d7c1d3a16b908f7131ddbe6615f#rd
saved: 2026-07-14
tags:
  - 笔记同步助手
id: fd265ec9-01c1-4d30-8801-0931452a1fcd
---

# 强化学习之父、年近七旬的Richard Sutton宣布创业，向LLM范式宣战
#笔记同步助手
## 来源
[原文链接](https://mp.weixin.qq.com/s?__biz=MzA3NTIyODUzNA==&mid=2649800688&idx=1&sn=c72ebb8252f20705c2de390191c69939&chksm=86faa7f4c106510aa19c62ae71e62de099581a64dba0e927236e076142251f1f072d6381eae5&mpshare=1&scene=1&srcid=0714YRnAFCOXSFyj9rMvpPXa&sharer_shareinfo=89c77d7c1d3a16b908f7131ddbe6615f&sharer_shareinfo_first=89c77d7c1d3a16b908f7131ddbe6615f#rd)
## 正文
公众号名称：DeepTech深科技

作者名称：张锦怡

发布时间：2026-07-14 13:00

> 📹 此处为视频内容，请前往原文查看：[在公众号原文中观看](https://mp.weixin.qq.com/s?__biz=MzA3NTIyODUzNA==&mid=2649800688&idx=1&sn=c72ebb8252f20705c2de390191c69939&chksm=86faa7f4c106510aa19c62ae71e62de099581a64dba0e927236e076142251f1f072d6381eae5&mpshare=1&scene=1&srcid=0714YRnAFCOXSFyj9rMvpPXa&sharer_shareinfo=89c77d7c1d3a16b908f7131ddbe6615f&sharer_shareinfo_first=89c77d7c1d3a16b908f7131ddbe6615f#rd)

![](https://relay-1.bijitongbu.site/p/5baecd0980b2845edfd329efd31b64b6.png)

就在今天，被称为“强化学习之父”的 Richard Sutton 在社交平台 X 上突然宣布，他与合作者 Khurram Javed 已经离开由传奇游戏开发者 John Carmack 创办的 AI 公司 Keen Technologies，共同创立了一家名为 Oak Lab 的新公司。这家注册于加拿大的初创企业，目标是打造一种完全不同于当前大语言模型的 AI 系统——一个能够从自身经验中持续学习、实时进化的智能体。

在宣布消息的帖子中，Sutton 对 Carmack 和 Keen Technologies 表达了敬意，但明确表示 Oak Lab 将走一条不同的路。他写道，当前的深度学习方法存在根本性的不足，需要的不是修补，而是全新理念的重构。

![](https://relay-1.bijitongbu.site/p/2becb03668414705653a510d98255549.png)

（来源：X）

现年 68 岁的 Richard Sutton，是加拿大阿尔伯塔大学计算机科学教授，在斯坦福大学获得本科学位后，于马萨诸塞大学阿默斯特分校师从 Andrew Barto 完成博士学业。他是时序差分学习的提出者，与 Barto 合著的《强化学习导论》是该领域最具影响力的教材。2025 年，二人共同获得 ACM 图灵奖，表彰他们在强化学习概念和算法基础方面的开创性贡献。此外，AlphaGo 的缔造者 David Silver、强化学习领域重要学者 Doina Precup 等人都是他的学生。

为什么不走 LLM 路线？

Oak Lab 的创立动机，与 Sutton 在 2019 年发表的那篇著名文章——《苦涩的教训》（The Bitter Lesson）有着深度关联。

在这篇短文中，Sutton 回顾了 AI 研究 70 年的历史，提出了一个核心观察：那些试图将人类领域知识内嵌到系统中的方法，最终总会被依赖大规模计算的通用方法所超越。无论是计算机象棋、语音识别还是计算机视觉，这条规律反复上演。真正有效的方法是搜索和学习，这是两种能够随计算规模无限扩展的通用手段。

这篇文章在 AI 界引发了持久讨论，许多从业者将其视为支持大语言模型规模化路线的理论依据。然而 Sutton 本人并不认同这种解读。在 2025 年 9 月接受播客主持人 Dwarkesh Patel 的访谈时，他直言当前的大语言模型并没有真正践行《苦涩的教训》的精神。他的核心论点是：大语言模型的学习来源是训练数据，而不是经验。将海量的人类文本灌入模型，本质上仍然是一种依赖人类知识的路径，与他所批评的将领域知识手工编入系统的做法并无本质区别，只是规模更大。

![](https://relay-1.bijitongbu.site/p/bfe54ac68459a677a64fdb09ab17acc6.png)

图｜Sutton 接受Dwarkesh Patel 访谈 （来源：Youtube）

Sutton 进一步指出，大语言模型擅长模仿人类的表达，但它们并不具备在运行过程中持续学习的能力。一个训练完成的模型在部署之后就停止了学习，无法从与用户的交互中获取真正的新知识，也无法评估自身输出的正确性。在他看来，真正的智能必须具备通过试错产生新发现的能力。就像 AlphaZero 不再依赖人类棋谱、而是通过数百万局自我对弈发明了全新的下法那样。

2026 年 5 月，Sutton 在麻省理工学院发表 Dertouzos 杰出讲座时更加直接地表示，作为一个庞大产业，AI 在一定程度上已经偏离了方向。

OaK 架构：从经验中生长出智能

Oak Lab 的技术核心是 Sutton 提出的 OaK 架构，全称为 Options and Knowledge（选项与知识），源自他与阿尔伯塔大学同事共同制定的长期研究路线图“阿尔伯塔计划”。

OaK 的设计建立在三条原则之上：智能体必须是通用的，启动时不预设任何特定领域知识；所有知识都必须来自经验，通过与环境的交互获取；学习的驱动力是强化学习中的累积奖励最大化。

在技术层面，OaK 围绕两个核心概念展开。“选项”（Options）是在时间上有所延伸的行为策略。不是简单的下一步动作，而是一整套行为序列及其终止条件。“知识”（Knowledge）则是智能体在执行不同选项过程中对世界的理解。智能体在运行过程中不断创建新的选项、积累关于这些选项的知识，并利用内部构建的世界模型来预测行为的长期后果。

这套机制形成一个自我强化的循环：从经验中提取特征，将有用的特征抽象为更高层次的表示，再用这些表示去构建更复杂的规划能力。这个过程是开放式的，理论上只受限于可用的计算资源。

但 Sutton 也坦率地承认了技术瓶颈。当前深度学习系统在持续学习中面临两个根深蒂固的难题：一个是灾难性遗忘，新学到的信息会覆盖已有知识；另一个是可塑性丧失，系统在学习一段时间后逐渐失去继续学习新事物的能力。他在多个场合表示，尚未解决这些核心问题，这也是他还无法展示大规模 OaK 系统实例的原因。他在 MIT 的讲座上坦言，这仍然是一个愿景，但他相信这个愿景是可以实现的。

强化学习阵营的集结

Oak Lab 的创立其实也有一定的铺垫。此前，[Sutton 的学生，被称为“AlphaGo 之父”的 David Silver 也已离开 DeepMind，于 2025 年底创立 Ineffable Intelligence，并在 2026 年 4 月获得 11 亿美元种子轮融资，估值 51 亿美元。](https://mp.weixin.qq.com/s?__biz=MzA3NTIyODUzNA==&mid=2649790615&idx=1&sn=2f88b9cf000e716b7c4793a2222bbadc&scene=21#wechat_redirect)

![](https://relay-1.bijitongbu.site/p/47567a20d00f7afcd021dfb415ad82a4.png)

图｜David Silver（来源：Google Deepmind）

Ineffable 的路线与 Oak Lab 类似，同样押注强化学习，同样认为 AI 必须摆脱对人类数据的依赖，从自身经验中发现知识。而 Sutton 和 Javed 此前所在的 Keen Technologies 也是一家信奉强化学习路线的公司。师生三方几乎同时在这一方向上发力，共同向当前主流范式发起挑战。

当然，这一立场也存在着一定的争议。批评者指出，强化学习在围棋、国际象棋等有明确胜负规则的封闭领域取得了出色成果，但在开放式的现实世界环境中，奖励信号往往模糊不清，纯粹的强化学习面临巨大挑战。此外，当前 AI 在推理和数学方面的许多进步恰恰来自将强化学习与大语言模型相结合的方法，两条路线是否必须对立，仍是一个开放问题。

参考链接：

1.https://thelogic.co/briefing/ai-pioneer-richard-sutton-launches-startup-to-build-always-learning-agents/

## 2.https://digg.com/tech/5p0hdvmr

## 3.https://x.com/mark\_k/status/2076667108688003127

## 4.https://en.wikipedia.org/wiki/Richard\_S.\_Sutton

## 5.https://thetech.com/2026/05/28/sutton-rl-lecture

## 6.https://www.dwarkesh.com/p/richard-sutton

  

运营/排版：何晨龙

注：封面/首图由 AI 辅助生成

![](https://relay-1.bijitongbu.site/p/b00f68c0e3f17897bb4d03ff0b6eeab8.png)

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/37617612_1784009792975?u=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzA3NTIyODUzNA%3D%3D%26mid%3D2649800688%26idx%3D1%26sn%3Dc72ebb8252f20705c2de390191c69939%26chksm%3D86faa7f4c106510aa19c62ae71e62de099581a64dba0e927236e076142251f1f072d6381eae5%26mpshare%3D1%26scene%3D1%26srcid%3D0714YRnAFCOXSFyj9rMvpPXa%26sharer_shareinfo%3D89c77d7c1d3a16b908f7131ddbe6615f%26sharer_shareinfo_first%3D89c77d7c1d3a16b908f7131ddbe6615f%23rd&s=obsidian)
