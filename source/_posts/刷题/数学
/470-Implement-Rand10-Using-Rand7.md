---
title: 470. Implement Rand10() Using Rand7()
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2021-01-15 09:20:43
---



## [470. Implement Rand10() Using Rand7()](https://leetcode-cn.com/problems/implement-rand10-using-rand7/)



## 思路：

利用7进制生成等概率数值，同时限制生成数的范围，保证取余的范围内各个余数的生成概率相等

<!-- more -->



## 代码：

第一次wa是因没有考虑取余后映射的数字的生成概率不等了。



```c++
// The rand7() API is already defined for you.
// int rand7();
// @return a random integer in the range 1 to 7

class Solution {
public:
    //利用7进制生成等概率数值，同时限制生成数的范围，保证取余的范围内各个余数的生成概率相等
    int rand10() {
        int c;
        do{            
            int a = rand7()- 1;
            int b = rand7() - 1;
            c = a * 7 + b;
        }while(c >= 40);
        return c % 10 + 1;
    }
};
```