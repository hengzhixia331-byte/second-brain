---
description: 作者从水稻抗旱全基因组关联分析中鉴定出稻属特异的孤儿基因 ROAD1。/
author: Mr. Han
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=Mzg3NzMzOTA3Nw==&mid=2247488645&idx=1&sn=6261081de9935996c6afaf769b5cf0df&chksm=ce513084e0dab3b4044b9d2afacf30cec29f585305da25fae65f172277345858db8ac001bee7&mpshare=1&scene=1&srcid=09186mlGBrosYXJFZKzkFcjJ&sharer_shareinfo=a5b3d13e4e2417ea346fb7c3aea207ce&sharer_shareinfo_first=a5b3d13e4e2417ea346fb7c3aea207ce#rd
saved: 2026-09-18
tags:
  - 笔记同步助手
id: 540faf8b-e42b-4504-8838-5eb39dcecf9e
---

# Cell | 一个稻属孤儿基因赋予跨物种抗旱性
#笔记同步助手
## 来源
[原文链接](https://mp.weixin.qq.com/s?__biz=Mzg3NzMzOTA3Nw==&mid=2247488645&idx=1&sn=6261081de9935996c6afaf769b5cf0df&chksm=ce513084e0dab3b4044b9d2afacf30cec29f585305da25fae65f172277345858db8ac001bee7&mpshare=1&scene=1&srcid=09186mlGBrosYXJFZKzkFcjJ&sharer_shareinfo=a5b3d13e4e2417ea346fb7c3aea207ce&sharer_shareinfo_first=a5b3d13e4e2417ea346fb7c3aea207ce#rd)
## 正文
公众号名称：生物演化与合成

作者名称：Mr. Han

发布时间：2026-07-27 04:52

作者从水稻抗旱全基因组关联分析中鉴定出稻属特异的孤儿基因 ROAD1 。功能等位基因 ROAD1 C 编码 151 个氨基酸的蛋白，可结合 ABA 信号负调控磷酸酶 OsPP2C68，竞争性限制其接触 SnRK2/SAPK，从而维持激酶磷酸化并增强干旱响应。在大田干旱条件下，携带 ROAD1 C 的近等基因系产量最高提高 34.75%；将该基因导入拟南芥、油菜、玉米、小麦和杨树，也在论文所测试的体系中增强了抗旱表型。

原文题目：An Oryza orphan gene confers trans-species drought tolerance。中文译题：一个稻属孤儿基因赋予跨物种抗旱性。

## 一、孤儿基因不是另建一条通路，而是接入保守的 ABA 信号枢纽

孤儿基因只在特定谱系中存在，通常缺乏可据同源关系推断的功能。本文的关键问题不是 ROAD1 是否与抗旱相关，而是一个稻属特异的新基因如何获得可跨物种工作的功能。作者给出的答案是：ROAD1 蛋白不取代整条 ABA 通路，而是结合高度保守的 A 类 PP2C 磷酸酶，使已有的 SnRK2–ABF/AREB 信号模块在干旱下更易被激活。

“模拟 ABA 结合型受体复合物”需要准确理解为功能模拟。ROAD1 与 PYR/PYL/RCAR–ABA 复合物都能抑制 PP2C 对 SnRK2 的去磷酸化，但论文没有解析 ROAD1–OsPP2C68 高分辨率结构，也未证明两者采用相同结合构象。AlphaFold 3 对该复合物给出的模型置信度较低，作者将 ROAD1 视为可能具有内在无序特征的蛋白。

## 二、GWAS、等位基因和遗传操作共同锁定 ROAD1

![[0907cb20273ab7467122c0722675572f_MD5.jpg]]

图 1 | 鉴定孤儿基因 ROAD1 为水稻抗旱性的主要决定因子。（A）在水稻多样性群体中以叶片卷曲评分表示抗旱性的全基因组关联分析，n = 240；红色箭头表示 1 号染色体上的显著峰。（B）ROAD1 位点的区域关联和连锁不平衡分析；首要 SNP sf01g7236023（p = 4.4 × 10−11，菱形）与因果变异 SNP8751（p = 2.2 × 10−8，三角形）呈强连锁，r2 > 0.9。（C）基于 BLAST 的 ROAD1 在稻属物种中的分类分布；同源序列仅见于 AA 基因组稻属物种，包括粳稻和籼稻、O. rufipogon、O. nivara、O. glaberrima、O. barthii、O. glumaepatula、O. longistaminata 和 O. meridionalis。（D）ROAD1 基因结构和单倍型；Hap1（ROAD1C）编码预测的全长蛋白，Hap2（ROAD1T）在编码序列第 31 个核苷酸处发生 C 到 T 变异并产生提前终止密码子。（E）ROAD1C（n = 177）和 ROAD1T（n = 21）的单倍型–表型关联，采用双侧 Wilcoxon 检验。（F、G）干旱和复水条件下，ROAD1 过表达株系与 road1 突变体相对于野生型的表型、叶片卷曲评分、结实率和单株产量，n = 4；RSWC 为土壤相对含水量，比例尺，20 cm。过表达与突变体试验独立进行，最终 RSWC 分别约为 11% 和 13%。（H、I）田间干旱条件下野生型、ROAD1 过表达和 road1 株系的表现及农艺性状，包括叶片卷曲评分、结实率、产量、鲜重、干重和每小区含水量，n = 4 个小区；采用双侧 Welch t 检验。

关联峰中的 SNP8751 把群体分为两类主要单倍型：ROAD1C 编码 151 aa 全长蛋白，ROAD1T 在第 31–33 位核苷酸形成提前终止密码子，只能产生预测的 10 aa 短肽。携带 ROAD1C 的材料叶片卷曲程度更低。过表达 ROAD1C 提高盆栽和田间干旱下的结实率与产量，敲除则产生相反结果。

这些结果把群体关联推进到因果遗传验证。作者还比较了正常供水条件，敲除或过表达并未显著改变抽穗期、株高、总颖花数、结实率、产量和千粒重。准确表述应是“在论文测试的品种、地点和条件下未发现明显生长或产量代价”，而不是断言该等位基因在所有遗传背景和环境中都没有代价。

## 三、ROAD1 起源于稻属祖先序列，并在粳稻驯化过程中富集

![[b2e4660ba659924be1c4616e649fedf2_MD5.jpg]]

图 2 | ROAD1 的演化起源及其在粳稻驯化过程中的选择。（A）ROAD1 从 O. meridionalis 中祖先序列演化的轨迹；现有序列经历插入/缺失事件和终止密码子重塑，黑色箭头表示检测到的转录信号，红色和黄色短条分别表示提前终止密码子和移码事件。（B）基于栽培稻和野生稻材料 ROAD1 编码区 SNP 构建的系统发育树；外圈表示群体，内圈表示 ROAD1 等位变异。（C–E）ROAD1 位点的选择信号；在约 1.8 Mb 的基因及侧翼区域分析核苷酸多样性 π 和 Tajima’s D，显示与粳稻分化相关的选择扫荡。（E）1,098 份栽培稻中功能型 ROAD1C 和截短型 ROAD1T 的地理分布；背景色为 1976–2021 年月平均降雨量，插图显示六个稻作区年降水量与 ROAD1C 频率的 Pearson 相关，n = 6。（F、G）遗传回补验证；展示野生型、road1 以及 ROAD1C 或 ROAD1T 回补株系的干旱表型，并定量叶片卷曲评分、结实率和单株产量，n = 5；只有 ROAD1C 恢复突变体的干旱敏感表型。比例尺，20 cm；采用单因素方差分析和 Tukey HSD 检验。

序列重建将 ROAD1 的祖先序列追溯至 O. meridionalis，作者估计其约在 120 万年前出现。小片段插入/缺失和终止密码子重塑逐步形成可编码全长蛋白的 ROAD1C。功能回补进一步表明，ROAD1C 能恢复 road1 的抗旱表型，而 ROAD1T 不能，说明群体中的关键差异确实对应蛋白编码能力。

ROAD1C 在粳稻中的频率为 98.21%（1,484/1,511），在籼稻中为 77.6%（2,141/2,759），位点周围还出现核苷酸多样性和 Tajima’s D 的选择扫荡信号。六个稻作区中，年降水量与 ROAD1C 频率呈负相关，R2 = 0.78，p = 0.02。该结果与低降水环境中的选择一致，但样本单位只有六个区域，地理相关性本身不能排除群体历史、驯化路线或其他环境变量的共同影响。

## 四、ROAD1 结合 OsPP2C68，阻止其关闭 SnRK2/SAPK 激酶

![[2eb5f7c34ba6a64c65313fb97611bda3_MD5.jpg]]

图 3 | ROAD1 与 OsPP2C68 相互作用并释放 SnRK2（SAPK）激酶活性。​（A）表达 pUBI::ROAD1-YFP 的转基因水稻根尖中 ROAD1 的核定位，比例尺，10 μm。​（B–F）分别用酵母双杂交、烟草叶片分裂荧光素酶互补、烟草叶片双分子荧光互补、水稻原生质体免疫共沉淀和体外 pull-down 验证 ROAD1–OsPP2C68 相互作用；BiFC 中 OsbZIP46-nYFP 与 OsPP2C68-cYFP 为阴性对照，PIF4-mCherry 为核标记，比例尺，20 μm。​（G）水稻原生质体免疫共沉淀验证 OsPP2C68 与 SAPK8/9/10 的相互作用。​（H）烟草中的竞争性分裂荧光素酶实验；共表达 ROAD1 破坏 OsPP2C68–SAPK9 相互作用，共表达 GFP 为阴性对照。​（I、J）竞争性免疫共沉淀和 pull-down 显示 ROAD1 与 SAPK9 竞争结合 OsPP2C68。​（K、L）SAPK9 磷酸化实验，显示 OsPP2C68 在体内使 SAPK9 去磷酸化，以及 ROAD1 在体外对这一过程的影响。​（M）有或无 ABA 处理时，野生型、road1-6 和 ROAD1 过表达株系中 SnRK2（SAPK）总磷酸化水平；抗 pS166 抗体识别与拟南芥 SnRK2.4 Ser166 同源的保守丝氨酸位点，即水稻 SAPK9 Ser176。

五种互作实验从细胞内、异源叶片和纯化蛋白三个层面支持 ROAD1 与 OsPP2C68 直接结合。OsPP2C68 原本结合 SAPK8/9/10 并使其去磷酸化；增加 ROAD1 后，OsPP2C68–SAPK9 结合逐步减弱，体外去磷酸化受阻。相应地，干旱或 ABA 条件下 road1 的 SAPK 磷酸化降低，过表达株系升高，而正常条件下各基因型的基础磷酸化接近。

遗传上，road1 ospp2c68 双突变体的表型接近 ospp2c68，支持 OsPP2C68 位于 ROAD1 下游。ROAD1-YFP 即使由组成型启动子驱动，在正常条件下蛋白丰度仍很低，干旱时才明显积累，提示胁迫依赖的蛋白稳定性可限制非胁迫条件下的持续 ABA 激活。作者将与 OsPP2C68 结合所需区域定位到 ROAD1 C 端 122–151 aa，但缺少复合物实验结构，因此“分子模拟”目前是功能类比，不是结构同源性的证明。

## 五、近等基因系在多尺度田间干旱试验中保持更高产量

![[10fd674057bf6b4fd58b053ffa6ce5cd_MD5.jpg]]

图 4 | 利用 ROAD1C 等位基因提高水稻抗旱性的育种应用。（A）盆栽抗旱试验；在优良水稻 YH998 背景中，分别携带功能型 ROAD1C 或截短型 ROAD1T 的近等基因系在穗发育期的代表性表型，并定量叶片卷曲评分和单株鲜重，n = 6，比例尺，20 cm。（B）盆栽干旱下的穗部形态、结实率和单株产量，n = 6。（C）2024 年陵水 0.5 m2 小区田间试验；展示干旱前后表型、失水率（n = 8）、干旱下蒸腾速率、气孔导度和水分利用效率（n = 22 片叶），失水率以均值 ± 标准误表示，比例尺，20 cm。（D）陵水田间试验中的穗部形态、结实率和单株产量，n ≥ 23。（E–H）2025 年武汉干旱田 2 m2 中等小区试验，包括人工灌溉处理（n = 5 个小区）和灌溉–雨养处理（n = 7 个小区）；展示田间表型并定量叶片卷曲评分和每小区产量，比例尺，7 cm。（I、J）2025 年武汉自然田灌溉–雨养处理下 15.5 m2 大小区验证；展示田间表型并定量叶片卷曲评分和每小区产量，n = 6，比例尺，7 cm。统计采用双侧 Welch t 检验；ns，p > 0.05；\*\*p < 0.01；\*\*\*p < 0.001。

作者把 ROAD1C 导入优良水稻 YH998 背景，并与仅携带 ROAD1T 的近等基因系比较。盆栽、小区和大田试验的方向一致：干旱下 ROAD1C 材料叶片卷曲较轻、结实率和产量较高。两个 2 m2 中等小区处理的每小区产量分别提高 20.81% 和 27.55%；15.5 m2 大小区中提高 34.75%。

这部分比单株复水存活实验更接近育种评价，因为它覆盖不同地点、年份、供水方案和小区尺度。正常供水时两类近等基因系的生长与产量没有明显差异。不过，现有试验仍集中在有限背景和年份，34.75% 是特定大田处理中的最高值，不应作为所有地区的固定增产幅度。

## 六、跨物种表达在五类被测试植物中增强抗旱表型

![[162d5e3882696eb9946f0cc98cd1ca5d_MD5.jpg]]

图 5 | ROAD1 在所测试植物物种中增强抗旱性。（A、B）过表达 ROAD1 提高双子叶植物的干旱存活；展示拟南芥处理后的表型和存活率，n = 4 盆，以及油菜干旱和复水后的表型、存活率与鲜重，n = 3 盆；比例尺，5 cm。（C）玉米幼苗抗旱性；展示野生型与 ROAD1 过表达株系的表型和绿色投影面积比例，n = 5 盆，比例尺，20 cm。​（D）小麦幼苗干旱和复水后的表型与存活率，n = 6 盆，比例尺，5 cm。​（E、F）玉米田间表现；2024 年张掖全生育期正常供水或减少 75% 灌溉条件下的穗部表型，比例尺，1 cm；定量株高、单穗重、单穗粒重和穗粒数，n ≥ 27。​（G–I）穗发育期小麦抗旱性；展示 2025 年武汉盆栽小麦干旱前后表型，比例尺，22 cm；测定干旱下净光合速率、蒸腾速率、气孔导度和水分利用效率，n = 11 片叶，以及生物量和单株产量，n = 10。​（J–M）木本植物杨树的抗旱恢复；展示干旱前、干旱后和恢复后的表型，比例尺，10 cm；测定干旱下气体交换参数，n ≥ 10 片叶，干旱诱导的导水率损失百分比，n = 5 株，以及复水后存活率，n = 5 个生物学重复、每个重复 3 株。​统计采用双侧 Welch t 检验。​

水稻 ROAD1 蛋白能与玉米、小麦和拟南芥的 PP2C 同源蛋白相互作用。异源表达 ROAD1C 后，拟南芥和油菜复水存活率提高，玉米和小麦幼苗在干旱下维持更大绿色面积或更高存活；玉米和小麦的田间/生殖期试验还显示产量相关性状改善。杨树中过表达材料在干旱下保持更高光合活性和水分利用效率，木质部导水率损失更低，复水存活率更高。

这些结果支持 ROAD1 可接入多个被子植物的保守 PP2C–SnRK2 模块，但“跨物种”仍应限定为论文测试的五类植物及其具体转基因材料。各物种的构建方式、发育阶段和干旱处理并不相同，不能把不同实验中的效应量直接横向比较，也不能据此断言所有被子植物都会获得相同收益。

## 七、工作模型把基因起源、ABA 调控和育种应用连成一条链

![[3577009631ca4517bd69ecd87035efe1_MD5.jpg]]

图 6 | ROAD1 介导干旱适应的分子模型。上：ROAD1 的演化轨迹。ROAD1 起源于 O. meridionalis 中的祖先序列，约 120 万年前出现；在水稻演化和驯化过程中，基因区的小片段插入/缺失和终止密码子重塑形成全长开放阅读框 ROAD1C。与水分可获得性相关的环境选择使功能型 ROAD1C 在适应较低降水区的粳稻中富集。中：ROAD1 调控干旱响应的机制。缺少功能型 ROAD1 时，PP2C 抑制 SnRK2 激酶，压低 ABF/AREB 通路并导致较弱抗旱性；功能型 ROAD1C 蛋白则通过直接隔离 PP2C，在功能上模拟 PYR/PYL/RCAR–ABA 复合物。这种解除抑制激活 SnRK2–ABF/AREB 级联，促进干旱响应基因表达并增强抗旱性。下：保守性和应用潜力。水稻 ROAD1 在多种单子叶和双子叶植物中的异源表达提示其潜在跨物种用途。

这张模型图概括了论文的三层结论：一个稻属特异的新基因通过序列重塑获得完整编码能力；其蛋白不新建信号通路，而是竞争性结合 PP2C，使古老的 ABA 激酶模块保持活化；这一接口的保守性使其在多个被测试物种中产生抗旱效应。

模型中“水分驱动的正选择”和“模拟受体复合物”是基于多类证据提出的解释，不能越过证据边界。前者得到选择扫荡、等位基因地理分布和降水相关性支持，但尚未由历史环境操纵实验直接证明；后者得到竞争结合、去磷酸化和遗传上位关系支持，但缺少 ROAD1–PP2C 的高分辨率结构。作者还未确定 ROAD1 是否与其他 A 类 PP2C 或更多蛋白结合，也未厘清它与经典 ABA–PYL 通路是否协同。

## 八、如何评价这项工作的创新性

这项工作的概念贡献是说明谱系特异的新基因可以通过“接入”而不是“替换”保守信号网络获得大效应功能。ROAD1 选择 PP2C 这一 ABA 信号枢纽，使其作用可以跨越较远的物种边界；干旱条件下蛋白稳定性上升，又为正常条件下不持续激活 ABA 信号提供了一个合理解释。

应用证据同样较完整：作者从关联定位、敲除和回补推进到优良背景近等基因系，再扩展到多尺度田间试验和异源物种。但它仍不是“可直接用于所有作物的通用抗旱开关”。高分辨率互作结构、更多遗传背景和多环境试验、长期生长代价，以及 ROAD1 对完整 ABA 调控网络的影响，都是进入育种应用前必须继续回答的问题。

### 论文来源

论文信息：Haifu Tu、Qian Liu、Tiantian Ye、Ying Ye、Xinhua Feng、Lishi Shen、Shuang Li、Siqi Bai、Xiao Liu、Xin Liu、Huaijun Wang、Xiaokai Li、Junlong Lin、Hao Wang、Yu Chen、Zhiyue Feng、Boming Ji、Jihua Ding、Wei Li、Jianwei Zhang、Mingqiu Dai、Faming Dong、Honghong Hu、Ning Tang、Xuelei Lai、Haiyan Xiong、Lizhong Xiong。An

Oryza orphan gene confers trans-species drought tolerance。Cell，2026年10月15日，研究论文（Article）。

通讯作者及通讯单位：Xuelei Lai：National Key Laboratory of Crop Genetic Improvement, College of Bio-X, Huazhong Agricultural University, Wuhan, China；Hubei Hongshan Laboratory, Wuhan, China；Haiyan Xiong：National Key Laboratory of Crop Genetic Improvement, College of Bio-X, Huazhong Agricultural University, Wuhan, China；Hubei Hongshan Laboratory, Wuhan, China；Lizhong Xiong：National Key Laboratory of Crop Genetic Improvement, College of Bio-X, Huazhong Agricultural University, Wuhan, China；Hubei Hongshan Laboratory, Wuhan, China。

原文链接：<u>https://doi.org/10.1016/j.cell.2026.07.005</u>

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/19be9abf_1789702302844?u=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzg3NzMzOTA3Nw%3D%3D%26mid%3D2247488645%26idx%3D1%26sn%3D6261081de9935996c6afaf769b5cf0df%26chksm%3Dce513084e0dab3b4044b9d2afacf30cec29f585305da25fae65f172277345858db8ac001bee7%26mpshare%3D1%26scene%3D1%26srcid%3D09186mlGBrosYXJFZKzkFcjJ%26sharer_shareinfo%3Da5b3d13e4e2417ea346fb7c3aea207ce%26sharer_shareinfo_first%3Da5b3d13e4e2417ea346fb7c3aea207ce%23rd&s=obsidian)
