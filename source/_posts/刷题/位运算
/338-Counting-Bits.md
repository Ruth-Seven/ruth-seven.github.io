---
title: 338. Counting Bits
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2021-01-19 11:18:02
---




## [338. Counting Bits](https://leetcode-cn.com/problems/counting-bits/)



## 思路：

利用二进制上数字变化，将数字计算转移。

<!-- more -->

## 代码：

```c++
class Solution {
public:
    vector<int> countBits(int nums) {
        vector<int> dp(nums + 1);
        for(int i = 1; i <= nums; ++i){
            dp[i] = (i & 1) ? dp[i - 1] + 1 : dp[i >> 1];
        }
        return dp;
    }
};
```