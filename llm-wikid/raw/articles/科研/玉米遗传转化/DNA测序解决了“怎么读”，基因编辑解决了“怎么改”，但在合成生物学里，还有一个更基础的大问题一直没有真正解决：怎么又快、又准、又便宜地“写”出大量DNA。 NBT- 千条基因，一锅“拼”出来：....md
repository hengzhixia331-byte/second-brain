---
description: DNA测序解决了“怎么读”，基因编辑解决了“怎么改”，但在合成生物学里，还有一个更基础的大问题一直没有真正解决：怎么又快、又准、又便宜地“写”出大量DNA。/
author: 风清扬
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=MzIyNjAyMTgzMg==&mid=2650497728&idx=1&sn=956a0e083c528bf69a6e5eff5b3a7367&chksm=f19f6cd61e989f8f9ee2b6eb2ecb0ae0537b87caa6daf7bc6627c9b263bb7993175fa05bf456&mpshare=1&scene=1&srcid=0821NIXN9lA6cnglkrPk6Koh&sharer_shareinfo=1dac77593321d9f21214223da6caa35c&sharer_shareinfo_first=1dac77593321d9f21214223da6caa35c#rd
saved: 2026-08-21
tags:
  - 笔记同步助手
id: 374e04d5-363d-447c-aabb-4cf831f1b3f4
---

# NBT| 千条基因，一锅“拼”出来：DNA合成进入自组装时代
#笔记同步助手
## 来源
[原文链接](https://mp.weixin.qq.com/s?__biz=MzIyNjAyMTgzMg==&mid=2650497728&idx=1&sn=956a0e083c528bf69a6e5eff5b3a7367&chksm=f19f6cd61e989f8f9ee2b6eb2ecb0ae0537b87caa6daf7bc6627c9b263bb7993175fa05bf456&mpshare=1&scene=1&srcid=0821NIXN9lA6cnglkrPk6Koh&sharer_shareinfo=1dac77593321d9f21214223da6caa35c&sharer_shareinfo_first=1dac77593321d9f21214223da6caa35c#rd)
## 正文
公众号名称：胡纯一实验室 Hu lab

作者名称：风清扬

发布时间：2026-08-20 08:37

DNA测序解决了“怎么读”，基因编辑解决了“怎么改”，但在合成生物学里，还有一个更基础的大问题一直没有真正解决：**怎么又快、又准、又便宜地“写”出大量DNA。**

8月19日，《Nature Biotechnology》发表了题为 **High-throughput synthesis of DNA fragments by molecular self-assembly of overlapping oligonucleotides**的研究。工作由清华大学 Bryan Wei、Dongsheng Liu，CodeR Therapeutics 的 Ninuo Xia，以及中国科学院深圳先进技术研究院 Junbiao Dai 等团队完成。研究者提出了一种名为 **MOSAIC（Molecular Self-Assembly Induced Cloning）** 的高通量基因合成策略。它最有意思的地方，不是把DNA“合成得更长”，而是换了一种思路：**让大量短DNA先自己找到正确的伙伴，再借助细胞把它们修好、复制出来。**

![](https://relay-1.bijitongbu.site/p/d94b0f58e5f19c839e9ce8bc193aab78.png)

**现在的基因合成，通常先在芯片上制造大量短寡核苷酸，再把这些短片段拼接成长DNA。​芯片一次可以合成几十万条不同序列，看起来产能已经很高，但真正困难的是下一步——“拼”。​如果只拼一个基因问题不大，可一旦把几百、几千个基因的寡核苷酸混在同一个体系里，不同片段之间就可能错误配对。​尤其遇到高GC、重复序列或者容易形成复杂二级结构的DNA，错配、错拼会更加严重。​传统方法往往需要把不同反应物理隔离，或者加入复杂的酶促步骤和特异标签，通量上去了，流程却越来越复杂。**

MOSAIC抓住了DNA本身最基本的性质：互补序列天然会彼此识别。研究者把每个目标DNA设计成一组彼此重叠的寡核苷酸，不同基因之间则尽量保持“正交”，让属于同一目标的片段优先相互杂交。于是，即使把大量寡核苷酸混在一个反应体系中，它们也可以按照序列信息自动寻找正确的组装对象，形成接近完整的DNA结构。

![](https://relay-1.bijitongbu.site/p/e67ca52215c85a9eed8d1f68fe5493e4.png)

但这里还有一个关键问题：这些自组装出来的DNA并不一定是完美的共价连续分子，中间可能仍然存在缺口或切口。MOSAIC没有试图在体外把所有问题都解决，而是把后半程交给了细胞。组装产物进入宿主细胞后，细胞自身强大的DNA修复系统会进一步修补这些结构，并把正确组装的DNA作为模板恢复、克隆出来。**体外负责“找对位置”，体内负责“收尾修复”**，这正是这套方法最巧妙的地方。

这种设计带来了一个非常关键的结果：不同基因之间由错误配对造成的misalignment几乎被压到了可以忽略的水平。剩下的主要错误，更多来自寡核苷酸本身的合成误差，而这类误差相对稳定，也更容易通过测序和筛选控制。换句话说，限制大规模并行基因合成的核心问题，从“不同分子会不会拼错”，被转化成了一个更可管理的“原料准确度”问题。

![](https://relay-1.bijitongbu.site/p/aec4a35f28e32e9dedd7af35b19c3186.png)

研究者随后展示了MOSAIC的几个能力。它不仅能够处理复杂二级结构、高GC和重复序列等传统合成中的“难搞序列”，还能够直接完成环状质粒的无酶克隆。更重要的是，借助芯片寡核苷酸合成，他们在一个简单的one-pot反应中，同时完成了**超过1000种不同DNA片段的平行合成**。这已经不是传统意义上“一条一条合成基因”，而更像是把基因合成变成了一次批量制造。

![](https://relay-1.bijitongbu.site/p/9188e5026ab25c3b43974a7cb4671039.png)

更进一步，MOSAIC并不只是为了“批量制造DNA”。​研究团队还把它用于构建大规模蛋白变体文库。​以塑料降解酶PETase为例，他们利用这一策略快速生成大量序列变体，并通过后续筛选获得了性能优于已有代表性PETase的候选分子。​这说明，当DNA合成能够真正进入高通量模式以后，它和定向进化、蛋白工程之间原本很明显的技术断点也开始被打通：计算可以一次设计成千上万个序列，而实验端也开始有能力把这些设计真正“写”出来。

论文最后则用了一个更直观的实验来收尾——**GFP的组装和表达**。研究者从大量相互重叠的寡核苷酸出发，通过MOSAIC完成GFP编码序列的自组装和克隆；当这些DNA进入细胞后，最终能够产生清晰的绿色荧光。这个结果看似简单，却非常关键。因为高通量DNA合成真正需要证明的，从来不只是测序结果显示“这段DNA拼出来了”，而是这些由短片段重新构建出的基因，最终仍然能够被细胞正确读取，并产生具有功能的蛋白。

![](https://relay-1.bijitongbu.site/p/638647656854ac1c2ed6262837a4aea7.png)

因此，MOSAIC最值得关注的并不是某一个单独的数字。它真正改变的是基因合成的组织方式：过去通常是把每一条基因当成一个独立工程，分别扩增、组装和克隆；现在则可以把成百上千套寡核苷酸放进同一个体系，让序列本身决定它们应该和谁结合，再利用细胞天然的DNA修复系统完成最后的“收口”。

合成生物学一直希望把生命科学变成一种真正可规模化的工程学：先设计，再制造，最后测试。测序已经高度并行化，蛋白筛选也越来越高通量，而DNA“写入”长期处在中间的瓶颈位置。MOSAIC提供了一条很有意思的路线——**不是把DNA一条一条造得更快，而是让成千上万条DNA同时自己组装起来。**

从一锅寡核苷酸，到完整基因，再到细胞里真正亮起的绿色荧光，这可能正是这篇工作的核心意义：**高通量DNA合成开始从“拼出序列”，走向“批量制造功能”。**

![](https://relay-1.bijitongbu.site/p/a18094563784ef520ae532302d56ce7a.png)

  

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/7743ca2f_1787242394609?u=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzIyNjAyMTgzMg%3D%3D%26mid%3D2650497728%26idx%3D1%26sn%3D956a0e083c528bf69a6e5eff5b3a7367%26chksm%3Df19f6cd61e989f8f9ee2b6eb2ecb0ae0537b87caa6daf7bc6627c9b263bb7993175fa05bf456%26mpshare%3D1%26scene%3D1%26srcid%3D0821NIXN9lA6cnglkrPk6Koh%26sharer_shareinfo%3D1dac77593321d9f21214223da6caa35c%26sharer_shareinfo_first%3D1dac77593321d9f21214223da6caa35c%23rd&s=obsidian)
