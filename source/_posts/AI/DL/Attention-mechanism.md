---
title: Attention mechanism
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2021-01-15 11:55:46
---




# Attention mechanism
> 阅读 《A survey on Natural Language Processing (NLP) & applications in insurance》的论文中的The Attention Mechanism部分所做的笔记。

<!-- more -->

Attention机制提出的目的就是为了把在句子里的不同词语附上不同的权重，类比与人类观察物体时会给不同的物体分配不同的时长和注意力。

以最经典的scaled DOt-Product Attention 和 Multi-Head Attention 为例：
![image-20210115113529144](http://static.come2rss.xyz/image-20210115113529144.png)

单头Attention是多头Attention的组合部分，先讲单头。

QKV是三个输入X变换的向量，分别定义为“query”，“key”和“value”。

![image-20210115113733398](http://static.come2rss.xyz/image-20210115113733398.png)

![image-20210115113744158](http://static.come2rss.xyz/image-20210115113744158.png)

最后经过$W^0 \in  \R^{d_V \times p}$仿射变化，得到

![image-20210115113802113](http://static.come2rss.xyz/image-20210115113802113.png)

其中整个过程用到了4个系数矩阵$W^Q \in  \R^{p \times d_q}$，$W^K  \in  \R^{p \times d_k}$, $W^V \in  \R^{p \times d_v}$和$W^0 \in  \R^{d_V \times p}$ 

> 其中，$d_v = d_k = d_q$
>
> 

理解Scaled Dot-Product Attention部分，多头的部分就简单了。多头就是把同一组输入喂给多组同结构的单头Attention，然后把多组$Attention(Q,V,K)$concatenate起来,最后进行仿射变换。

有公式：
$$
z_i = Attention(Q_i, k_i, V_i) \in \R^{n \times d_v} \\
C = Concat(Z_i) \in \R ^{n \times (d_v * h)}\\
Z = CW^0 \in \R^{n * p}
$$

> 注意一下， 两者的Z和QVK意义基本相同。

最后在文章的最后说明一下多头Attention的意义：多个相同结构的机制组合一起，更多是通过多组参数来降低注意力集中在不该集中的地方的概率。以此提高模型的鲁棒性。