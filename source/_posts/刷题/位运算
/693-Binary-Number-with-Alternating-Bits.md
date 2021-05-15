---
title: 693. Binary Number with Alternating Bits
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2021-01-19 11:18:28
---




## [693. Binary Number with Alternating Bits](https://leetcode-cn.com/problems/binary-number-with-alternating-bits/)

## 思路:

<!-- more -->

## 代码：

```c++
class Solution {
public:
    bool hasAlternatingBits(int n) {
        if(n < 1) return true;
        int obit = n & 1, bit = 0;
        n >>= 1;
        while(n){
            bit = n & 1;
            n >>= 1; 
            if(bit == obit) return false;
            obit = bit;
        }
    
        return true;
    }
};
```