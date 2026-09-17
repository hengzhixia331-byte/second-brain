---
author: 橙君
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=MzYzNTg5MzIxMQ==&mid=2247488565&idx=1&sn=7a7bc173558e87eb7e51e8ba4de10123&chksm=f1e30172eb22b94451c921c58a17bfbe566913c0bc018a15b46d3041f4adf06ebcda2b6eccf5&mpshare=1&scene=1&srcid=0630mqdgohTx2AYKH0YKOpxG&sharer_shareinfo=a932525081b0d7f1864f1f35377d6bf1&sharer_shareinfo_first=a932525081b0d7f1864f1f35377d6bf1#rd
saved: 2026-06-30 08:43:48
tags:
  - 笔记同步助手
id: 686c8f02-cc9d-4b84-8ef2-1b83524a612a
---

公众号名称：AgriPulse

作者名称：橙君

发布时间：2026-06-30 00:00

![[llm-wikid/raw/assets/images/5f5f529ee3628e7e98fd8632f8032592_MD5.png||112]]

![[llm-wikid/raw/assets/images/33cb7ca072089c19dcfa2da912c60924_MD5.png||280]]

![[llm-wikid/raw/assets/images/439318b8444e7d885ec67c97b1e25c48_MD5.png||60]]

### 通用颜色面积分析工具 UCAA 发布 一张图片，自动统计颜色面积

在果实采后、植物表型和食品品质研究中，我们经常需要回答一个很简单的问题：

**某种颜色区域到底占了多少面积？**

  

### 例如：

果肉褐变面积是多少？

果皮着色率是多少？

叶片黄化比例是多少？

病斑或坏死区域占多少？

这类分析往往依赖 ImageJ 手动圈选、手动调阈值、手动统计。样品少时还可以接受，一旦一张图里有几十个样品，工作量就会迅速增加，而且不同操作者之间也容易产生差异。

为了解决这一问题，我们开发了一个基于 R 语言的开源工具：

  

## UCAA：Universal Color Area Analyzer

## （通用颜色面积自动分析工具）

  

**它能做什么？**

  

### UCAA 可以从一张原始图片中自动完成：

  

1.  样品主体识别
    
2.  从左到右、从上到下自动编号
    
3.  第一列参考颜色自动提取
    
4.  目标颜色区域识别
    
5.  目标颜色面积比例计算
    
6.  结果表格输出
    
7.  识别效果图输出
    
8.  柱状图自动绘制
    

  

**整个流程不需要手动圈选 ROI。**

**不只是褐变分析**

最初，这个脚本是为果实褐变指数（Browning Index，BI）分析开发的。

现在脚本已升级为通用颜色面积分析版本，只需修改一行参数：

target\_color <- "brown"

即可选择不同分析对象。

目前支持：

target\_color <- "brown" # 褐变面积target\_color <- "black" # 黑色/坏死面积target\_color <- "red" # 红色面积target\_color <- "yellow" # 黄色面积target\_color <- "green" # 绿色面积target\_color <- "custom" # 自定义颜色

不仅可以用于果肉褐变，也可以扩展到果皮着色、叶片黄化、组织培养褐化、坏死斑和病斑面积统计等多种图像表型分析。

**核心思路：以正常颜色作为参考**

UCAA 并不是简单地使用固定颜色阈值。

它默认将图片第一列样品作为正常参考，自动计算参考样品的代表颜色，然后结合：

  

1.  RGB 颜色距离
    
2.  色相 Hue
    
3.  饱和度 Saturation
    
4.  亮度 Value
    
5.  是否变暗
    
6.  是否更饱和
    

  

共同判断目标颜色区域。

这样做的好处是，即使不同图片之间存在一定光照、曝光或白平衡差异，程序仍然可以根据当前图片中的参考样品进行自适应校正。

### 输出结果目录

运行脚本后，会在脚本所在文件夹自动生成：

  

### 1\. color\_area\_each\_object.csv

  

每个样品一行，包含：

  

1.  样品编号
    
2.  行号
    
3.  列号
    
4.  样品总面积
    
5.  目标颜色面积
    
6.  目标颜色面积比例
    

  

### 2\. color\_area\_overlay.png

  

在原图上用红色标出识别到的目标颜色区域，并标注每个样品的编号和面积比例。

这张图主要用于检查识别是否准确。

![[llm-wikid/raw/assets/images/f05fd193be155783016fc5dfce900c8c_MD5.png]]

### 3\. color\_area\_barplot.png

  

自动绘制每个样品的目标颜色面积比例柱状图，可用于实验记录、汇报或论文初步作图。

![[llm-wikid/raw/assets/images/48fd78ef234aba33bfba5cb4f4409df4_MD5.png]]

### 4\. color\_area\_parameters.csv

  

保存本次分析使用的参考颜色和参数，便于结果复现。

### 示例所用图片出自以下论文：

![[llm-wikid/raw/assets/images/c4572b439fb9adc94437b8db0721ad01_MD5.png]]

![[llm-wikid/raw/assets/images/11354558a4bbe9e40a70d188b81f7f59_MD5.png]]

### 整理成干净背景的图片

![[llm-wikid/raw/assets/images/c2c319550302330c6bc466e87aa4d5f7_MD5.png]]

**使用方法很简单**

第一次使用时，先安装所需 R 包。

脚本顶部已经写好了安装命令，删除前面的 # 后运行一次即可。

之后，只需要修改两处：

第一，修改图片路径：

img\_path <- "你的图片路径"

第二，选择目标颜色：

target\_color <- "brown"

如果只是分析果实褐变，保持默认即可。

**哪些参数最常调？**

多数情况下，默认参数可以直接运行。

如果识别效果不理想，优先调整这几个参数：

delta\_rgb\_min <- 0.14

这是颜色距离阈值。数值越小，识别越敏感；数值越大，识别越保守。

min\_target\_area <- 30

这是最小目标颜色面积。噪点多时调大，小斑点漏检时调小。

min\_object\_area <- 1800

这是最小样品面积。样品漏检时调小，背景杂点被识别时调大。

row\_gap\_fraction <- 0.065

这是自动编号的行识别容差。如果编号顺序不对，可以调整这个参数。

**适用场景**

UCAA 可用于多类颜色表型定量分析。

例如：

果实采后研究：

果肉褐变

鲜切果蔬褐变

冷害斑

氧化损伤

腐烂面积

果实成熟研究：

果皮黄化

果皮红色覆盖率

着色面积

失绿程度

植物表型分析：

叶片黄化

叶片失绿

坏死面积

病斑面积

组织培养褐化

食品品质评价：

烘焙着色

加工变色

氧化变色面积

**注意事项**

UCAA 是基于图像的面积分析工具，适合统计某种颜色区域所占比例。

它不能完全替代色差仪对 L\*、a\*、b\* 等标准颜色参数的测定。

更合适的定位是：

UCAA 用于颜色区域面积定量，色差仪用于标准颜色参数测定。

两者可以互补。

**写在最后**

很多图像表型分析并不复杂，真正耗费时间的是重复操作：圈图、调阈值、统计、整理、作图。

UCAA 的目标就是把这些重复步骤自动化。

从一张图片开始，自动识别样品，自动统计目标颜色面积，自动输出表格和图像结果。

如果你正在做果实褐变、果皮着色、叶片黄化、病斑面积或组织培养褐化分析，这个工具或许可以帮你节省大量时间。

  

### 脚本名称：

  

UCAA\_reference\_color\_area\_analyzer\_v1.R

  

### 工具定位：

  

通用颜色面积自动分析工具

  

### 核心功能：

  

一张图片，自动完成颜色区域识别、面积统计与可视化。

### AgriPulse

点击链接或复制整段内容，打开「夸克APP」即可获取。

链接：https://pan.quark.cn/s/dad6c81e0183?pwd=6zpG

提取码：6zpG

  

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/4eb5646d_1782780226653?u=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzYzNTg5MzIxMQ%3D%3D%26mid%3D2247488565%26idx%3D1%26sn%3D7a7bc173558e87eb7e51e8ba4de10123%26chksm%3Df1e30172eb22b94451c921c58a17bfbe566913c0bc018a15b46d3041f4adf06ebcda2b6eccf5%26mpshare%3D1%26scene%3D1%26srcid%3D0630mqdgohTx2AYKH0YKOpxG%26sharer_shareinfo%3Da932525081b0d7f1864f1f35377d6bf1%26sharer_shareinfo_first%3Da932525081b0d7f1864f1f35377d6bf1%23rd&s=obsidian)