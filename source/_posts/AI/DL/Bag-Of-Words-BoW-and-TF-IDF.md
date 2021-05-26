---
title: Bag Of Words (BoW) and TF-IDF
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2021-01-15 14:47:11
---




## Bag Of Words (BoW) and TF-IDF

> 阅读 《A survey on Natural Language Processing (NLP) & applications in insurance》的论文中的The Attention Mechanism部分所做的笔记。

<!-- more -->

Bag of words词袋模型就是简单的对每个句子进行字频统计。但是有明显的缺点：1. 没有词序信息。2. 字典太大的话，每个句子的向量会过大。

Term Frequency-Inverse Document Frequency (Tf-Idf)是词袋的优化方法。他在词频统计的基础上，

用公式：
$$
tf(w,d) = \frac {\text{number of times the word w appears in d}}{\text{total number of words in d}}
\\
idf(w,d) = log\frac{len(d)}{df(w)}
\\
tf-idf = tf(w,d) * idf(w,d)
$$
其中$tf(w,d)中$$d$是`the d set of sentence`，$w$是word。$idf(w,d)$中$df(w)$包含$w$的句子数量，$len(d)$是句子的总数量。

例子：

![image-20210115143642182](http://static.come2rss.xyz/image-20210115143642182.png)

![image-20210115143630237](http://static.come2rss.xyz/image-20210115143630237.png)

![image-20210115143648645](http://static.come2rss.xyz/image-20210115143648645.png)





那么我们就可以理解到， $idf(w,d)$就是就是强调词$w$的稀缺性，值越大说明越稀缺，这个词也就越重要。