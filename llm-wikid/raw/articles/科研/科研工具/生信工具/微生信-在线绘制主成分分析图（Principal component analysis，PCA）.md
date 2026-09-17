---
title: "微生信-在线绘制主成分分析图（Principal component analysis，PCA）"
source: "https://www.bioinformatics.com.cn/plot_basic_PCA_plot_034"
author:
published:
created: 2026-07-01
description: "在线绘制主成分分析图"
tags:
  - "clippings"
---
**[基础绘图](https://www.bioinformatics.com.cn/?keywords=%E5%9F%BA%E7%A1%80%E7%BB%98%E5%9B%BE)**- [饼图](https://www.bioinformatics.com.cn/?keywords=%E9%A5%BC%E5%9B%BE)
- [线图](https://www.bioinformatics.com.cn/?keywords=%E7%BA%BF%E5%9B%BE)
- [点图](https://www.bioinformatics.com.cn/?keywords=%E7%82%B9%E5%9B%BE)
- [柱状图](https://www.bioinformatics.com.cn/?keywords=%E6%9F%B1%E7%8A%B6%E5%9B%BE)
- [面积图](https://www.bioinformatics.com.cn/?keywords=%E9%9D%A2%E7%A7%AF%E5%9B%BE)
**[转录组绘图](https://www.bioinformatics.com.cn/?keywords=%E8%BD%AC%E5%BD%95%E7%BB%84%E7%BB%98%E5%9B%BE)**- [小提琴图](https://www.bioinformatics.com.cn/?keywords=%E5%B0%8F%E6%8F%90%E7%90%B4%E5%9B%BE)
- [火山图](https://www.bioinformatics.com.cn/?keywords=%E7%81%AB%E5%B1%B1%E5%9B%BE)
- [聚类热图](https://www.bioinformatics.com.cn/?keywords=%E7%83%AD%E5%9B%BE)
- [GO，Pathway图](https://www.bioinformatics.com.cn/?keywords=pathway)
- [Venn图](https://www.bioinformatics.com.cn/?keywords=%E6%96%87%E6%81%A9%E5%9B%BE)
**[(宏)基因组绘图](https://www.bioinformatics.com.cn/?keywords=%E5%9F%BA%E5%9B%A0%E7%BB%84%E7%BB%98%E5%9B%BE)**- [染色体图](https://www.bioinformatics.com.cn/?keywords=%E6%9F%93%E8%89%B2%E4%BD%93%E5%9B%BE)
- [SNP密度图](https://www.bioinformatics.com.cn/?keywords=SNP)
- [circos图](https://www.bioinformatics.com.cn/?keywords=circos)
- [物种累积曲线](https://www.bioinformatics.com.cn/?keywords=%E7%89%A9%E7%A7%8D%E7%B4%AF%E7%A7%AF%E6%9B%B2%E7%BA%BF)
- [花瓣图](https://www.bioinformatics.com.cn/?keywords=%E8%8A%B1%E7%93%A3%E5%9B%BE)
**[临床绘图](https://www.bioinformatics.com.cn/?keywords=%E4%B8%B4%E5%BA%8A%E7%BB%98%E5%9B%BE)**- [生存曲线](https://www.bioinformatics.com.cn/?keywords=%E7%94%9F%E5%AD%98%E6%9B%B2%E7%BA%BF)
- [森林图](https://www.bioinformatics.com.cn/?keywords=%E6%A3%AE%E6%9E%97%E5%9B%BE)
**[其他](https://www.bioinformatics.com.cn/?keywords=%E5%85%B6%E4%BB%96)**- [地图](https://www.bioinformatics.com.cn/?keywords=%E5%9C%B0%E5%9B%BE)
- [PCA](https://www.bioinformatics.com.cn/?keywords=PCA)
**[常用工具](https://www.bioinformatics.com.cn/?keywords=%E5%B7%A5%E5%85%B7)**- [长宽数据转换](https://www.bioinformatics.com.cn/basic_long_format_data_and_wide_format_data_exchange_by_reshape2_t015)
- [基因共表达](https://www.bioinformatics.com.cn/basic_lncrna_mrna_pearson_spearman_coexpression_analysis_t013)
- [fasta工具箱](https://www.bioinformatics.com.cn/fasta_sequence_file_format_t003)
- [DESeq2差异分析](https://www.bioinformatics.com.cn/basic_rnaseq_raw_count_differentially_expressed_analysis_by_deseq2_t014)
- [limma差异分析](https://www.bioinformatics.com.cn/basic_differentially_expressed_analysis_by_limma_t018)
- [肿瘤纯度](https://www.bioinformatics.com.cn/basic_tumor_purity_estimation_by_estimate_t016)
- [GOID分配分类信息](https://www.bioinformatics.com.cn/batch_assign_goid_into_go_term_bp_cc_mf_t019)

### 主成分分析（PCA）

**简介**  
[主成分分析](https://www.bioinformatics.com.cn/?keywords=pca) （Principal component analysis，PCA）利用正交变换对一系列可能相关的变量的观测值进行线性变换，从而投影为一系列线性不相关变量的值，这些不相关变量称为主成分（Principal Components）。PCA是最简单的以特征量分析多元统计分布的方法。通常情况下，这种运算可以被看作是揭露数据的内部结构，从而更好的解释数据的变量的方法。调用fviz\_pca\_ind函数绘图，默认ellipse.level=0.95  
**数据说明**  
行为特征（例如基因，蛋白，代谢物等），列为样品。第一行为样品名，第二行为组名，第3+行为特征。图中坐标轴Dim1和Dim2为第一、第二主成分（即潜在变量对差异的解释率）；点代表样品（individuals），不同颜色表示不同分组。调用：prcomp计算PCA，FactoMineR包绘图。  
该包默认对数据进行center和scale转化。  
**论文例子**  
[\[Nature communications\] Sympathetic axonal sprouting induces changes in macrophage populations and protects against pancreatic cancer. Fig4h](https://pmc.ncbi.nlm.nih.gov/articles/PMC9007988/)

| 输入 | [示例数据](https://www.bioinformatics.com.cn/static/sample_data/034_PCA_sample_data.xlsx) |
| --- | --- |
| 输出 | ![](https://www.bioinformatics.com.cn/static/img/onlineplots_img/034_basic_PCA_plot.png) |

### 如何引用？

建议直接写网址。助力10000+篇 [（google学术）](https://www.bioinformatics.com.cn/static/img/paper.png) ，9000+篇 [（知网）论文](https://www.bioinformatics.com.cn/static/img/paper2.png)  
**正式引用：** Tang D, Chen M, Huang X, Zhang G, Zeng L, Zhang G, Wu S, Wang Y. [SRplot: A free online platform for data visualization and graphing](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0294236). PLoS One. 2023 Nov 9;18(11):e0294236. doi: 10.1371/journal.pone.0294236. PMID: 37943830.  
**方法章节：** Heatmap was plotted by https://www.bioinformatics.com.cn (last accessed on May 4, 2026), an online platform for data analysis and visualization.  
**致谢章节：** We thank Mingjie Chen (Shanghai NewCore Biotechnology Co., Ltd.) for providing data analysis and visualization support.  
  
![](https://www.bioinformatics.com.cn/static/img/gzh2.jpg)