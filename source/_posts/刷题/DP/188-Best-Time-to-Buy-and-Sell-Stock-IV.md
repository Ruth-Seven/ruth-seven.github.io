---
title: 188. Best Time to Buy and Sell Stock IV
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-12-25 09:48:17
---

## [188. Best Time to Buy and Sell Stock IV](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/)



## 思路：

把transaction拆分为买buy和卖sell，`sell[i][j]`代表对于第`i`个物品，第`j`次卖操作后最大利润。`buy`和`sell`的转移方程如代码所示。

> 形式上更像一个状态转移机。
>
> ![image-20201226081801949](http://static.come2rss.xyz/image-20201226081801949.png)


<!-- more -->



## 代码：



```c++
class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        int d = prices.size();
        if(d < 2) return 0;
        k = min(k, d);// 超过n的k是没有意义的
        // buy一开始啥利润都没有应该为0，但是由于购买后利润可能会为负数，所以必须初始化为-INF
        vector<int> buy(k + 1, INT_MIN), sell(k + 1, 0);
        for(int i = 0;i < d; ++i){
            for(int j = 1; j <= k; ++j){
                buy[j] = max(buy[j], sell[j - 1] - prices[i]); 
                sell[j] = max(sell[j], buy[j] + prices[i]);
            }
        }
        return sell[k];
    }
};
```

其中不优化空间的转移方程如下：

```c++
        for(int i = 0;i < d; ++i){
            for(int j = 1; j <= k; ++j){
                buy[i][j] = max(buy[i - 1][j], sell[i - 1][j - 1] - prices[i]); 
                sell[i][j] = max(sell[i - 1][j], buy[i - 1][j] + prices[i]);
            }
        }

```

