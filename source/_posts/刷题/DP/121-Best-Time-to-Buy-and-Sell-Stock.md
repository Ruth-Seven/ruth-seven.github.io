---
title: 121. Best Time to Buy and Sell Stock
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-12-23 09:44:30
---




## [121. Best Time to Buy and Sell Stock](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/)

## 思路：

记录最值。<!-- more -->

> ![image-20201226081801949](http://static.come2rss.xyz/image-20201226081801949.png)


## 代码：

```c++
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if(prices.size() == 0) return 0;
        int profit = 0;
        int minv = prices[0];
        for(auto v : prices){
            minv = min(minv, v);
            profit = max(profit, v - minv);
        }
        return profit;
    }
};
```