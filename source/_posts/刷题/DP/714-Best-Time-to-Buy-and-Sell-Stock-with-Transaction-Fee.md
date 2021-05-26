---
title: 714. Best Time to Buy and Sell Stock with Transaction Fee
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-12-26 08:40:39
---








## [714. Best Time to Buy and Sell Stock with Transaction Fee](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)

## 思路：

做过了309题的话，这题就非常容易解决。注意fee的费用在交易完成后结算，不然可能有手续费没有扣完的尴尬情况。

<!-- more -->

>  ![image-20201226081801949](http://static.come2rss.xyz/image-20201226081801949.png)

## 代码：

空间可优化

```c++
class Solution {
public:
    int maxProfit(vector<int>& prices, int fee) {
        int d = prices.size(); 
        if(d <= 1) return 0;
        vector<vector<int>> dp(d, vector<int>(2));
        dp[0][0] = -prices[0];
        for(int i = 1; i < d; ++i){
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i]);
            dp[i][1] = max(dp[i -1][1], dp[i][0] + prices[i] - fee);
        }
        return dp[d- 1][1];
        
    }
};
```