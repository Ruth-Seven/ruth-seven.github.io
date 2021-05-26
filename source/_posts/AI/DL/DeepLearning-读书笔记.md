---
title: DeepLearning 读书笔记
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
categories:
date: 2020-08-07 11:59:46
tags:
---

# DeepLearning读书笔记（1）

## 数学符号

英语名词:



> Identity matrix：单位矩阵
>
> Moore–Penrose pseudo inverse：摩尔－彭若斯广义逆
>
> Determinant：行列式
>
> Partial derivative ：偏微分
>
> Gradient ：梯度
>
> Definate integral：定积分
>
> Variance：方差
>
> Covariance：协方差
>
> Shannon entropy：香农熵
>
> Kullback-Leibler divergence：KL散度
>
> Composition of the funcitions：函数的组合
>
> parametrize：参数化
>
> softplus： 公式如下
>
> log(1+ex)log(1+ex)
>
> 
>
> The empirical distribution：经验分布（往往有训练集定义的）

疑惑处：

- (P14) jocabian matrix 和 The Hessian matrix.

## 绪论

人类作为的地球上最智能的灵长类动物，可以高效地处理许多非形式化任务——难以用数学公式描述的问题，而计算机与人类正好相反，擅长处于规则化问题。AI(artificial intelligence)拥有从数据或者世界中学习模式的能力，这称之为machine learning。

简单模型的学习能力极大的依赖于数据特征。对于复杂的特征工作，表示学习 （*representation learning*）可以从复杂的数据中学习到远远优于人类所做出的的特征表示，仅需要稍稍的人工干预。表示学习一个典型代表就是自动编码器（autoencoder）。学习特征或者设计特征的算法的目的就是为了分离出`factors of variation`——影响事物变化的因素，比如识别车任务中的车轮，识别语音中的讲话人的年龄、性别。



2021年1月15日 11:56:35 

更新：这种书，做笔记是不可能的，写写书上更高效。