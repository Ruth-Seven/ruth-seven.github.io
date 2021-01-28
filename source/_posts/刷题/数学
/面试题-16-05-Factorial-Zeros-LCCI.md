---
title: 面试题 16.05. Factorial Zeros LCCI
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-09-24 09:24:55
---

#### [面试题 16.05. Factorial Zeros LCCI](https://leetcode-cn.com/problems/factorial-zeros-lcci/)

<!-- more -->

## 思路：

尾零个数等于所有相乘数字的5的质因子个数，比如$f(11)= 1 + 1$

关于快速求出：可以使用整除5，25，125……$5^k$的思路求出。

## 代码：

```c++
class Solution {
public:

    int trailingZeroes(int n) {
        int numof5 = 0;
        while(n >= 5){
            n /= 5;
            numof5 += n;
        }
        return numof5;
    }
};
```

