---
title: 70. Climbing Stairs
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-12-07 09:17:08
---

## [70. Climbing Stairs](https://leetcode-cn.com/problems/climbing-stairs/)



## 思路：

dp，用两个变量存储长度为N的数组优化空间

。<!-- more --> 

## 代码：

```c++

class Solution {
public:
    int climbStairs(int n) {
        int a = 1, b = 1, c = 2, k = 2;
        while(k <= n){
            c = a + b;
            a = b;
            b = c;            
            k++;
        }
        if(n == 0) return 0;
        else if(n == 1) return 1;
        else return c;
    }
};
```