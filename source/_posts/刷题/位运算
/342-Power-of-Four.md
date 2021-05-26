---
title: 342. Power of Four
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2021-01-17 18:22:52
---






## [342. Power of Four](https://leetcode-cn.com/problems/power-of-four/)

## 思路：

1. 判断唯一的1的位置是否在1的倍数上
2. 检查 $log_2x$是否为偶数就能判断 `x` 是否为 4 的幂



<!-- more -->

## 代码：



```c++

class Solution {
public:
    bool isPowerOfFour(int n) {
        if(n <= 0) return false;
        while(n != 1){
            if((n & 3)) return false;
            n >>= 2;
        }
        return true;
    }
};
```