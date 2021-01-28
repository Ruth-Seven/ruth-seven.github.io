---
title: 190. Reverse Bits
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2021-01-17 18:22:31
---



## [190. Reverse Bits](https://leetcode-cn.com/problems/reverse-bits/)



## 思路：

<!-- more -->

## 代码：

```c++
class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t z = 0;
        int k = 0;
        while(k <= 31){
            z = (z << 1) | (n & 1);
            n >>= 1;
            k++;
        }
        return z;
    }
};
```