---
title: random笔记
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
categories:
  - Language
  - Python
date: 2020-08-07 13:14:37
tags:
---



wrandom常用函数

<!-- more -->

`sample(list, simpleSize)`从list中抽simpleSize个元素

```
In [33]: from random import randint,sample
    ...: lst = [randint(0,50) for _ in range(100)]
    ...: print(lst[:5])
    ...: lst_sample = sample(lst,10)
    ...: print(lst_sample)
[0, 38, 31, 33, 43]
[9, 43, 31, 22, 31, 30, 14, 47, 14, 1]
```

`shuffle(lst)`随机打乱顺序

值得注意，shuffle 是对输入列表就地（in place）洗牌，节省存储空间。

```
In [34]: from random import shuffle
    ...: lst = [randint(0,50) for _ in range(100)]
    ...: shuffle(lst)
    ...: print(lst[:5]) 
[22, 49, 34, 9, 38]
```

`uniform(a,b)` 生成 [a,b) 内的一个随机数。

```andom笔记
from random import uniform
 x, y = [i for i in range(100)], [round(uniform(0, 10), 2) for _ in range
```