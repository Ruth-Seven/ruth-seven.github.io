---
title: 322. Coin Change
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-12-18 09:52:58
---



## [322. Coin Change](https://leetcode-cn.com/problems/coin-change/)

## 思路：

完全背包思路，注意一下初始值。

<!-- more -->

## 代码：

```c++
class Solution {
public:
    const int INF =  INT_MAX / 2;
    int coinChange(vector<int>& coins, int amount) {
        vector<int> dp(amount + 1, INF); // 简化 初始化为-1 不好利用min 过滤;使用条件 优化方向(dp[i]--)从初始条件（dp[i] = INF）开始，
        // 也许更好的初始值是 amount + 2;
        dp[0] = 0;
        for(auto v : coins){
            for(int i = v; i <= amount; ++i){
                dp[i] = min(dp[i], dp[i - v] + 1);               
            }
        }
        return dp[amount] == INF ? -1 : dp[amount];
    }
};
```