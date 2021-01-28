---
title: 461. Hamming Distance
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2021-01-17 18:23:04
---




## [461. Hamming Distance](https://leetcode-cn.com/problems/hamming-distance/)



## 思路：

<!-- more -->

## 代码：

```C++
class Solution {
public:
    int hammingDistance(int x, int y) {
        int z = x ^ y;
        int ct = 0;
        while(z){
            ct += z & 1;
            z >>= 1;
        }
        return ct;
    }
};
```