---
title: 309. Best Time to Buy and Sell Stock with Cooldown
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-12-26 08:33:38
---




## [309. Best Time to Buy and Sell Stock with Cooldown](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)

## 思路：

无限购买，每个prices都可以设置为一个购买点。把状态按照已经购买状态$f[i][0]$、处于冷冻状态的刚卖出$f[i][1]$和不处于冷冻期的卖出状态$f[i][2]$，分成三个部分，可以写出dp转移方程：
$$
\begin{split}
f[i][0] &= max(f[i - 1][0], f[i - 1][2] - prices[i]) \\\\
f[i][1] &= f[i - 1][0] + prices[i]\\\\
f[i][2] &= max(f[i - 1][1],  f[i - 1][2]) \\
\end{split}
$$
初始化$f[0][0]= -prices[0]$，最后取结果$max(f[n-1])[1], f[n-1][2])$。

DP状态方程巧妙在把一个状态拆分成不同的并行状态，同时在不同状态可以相互转移，自然的添加了一次购买，一次卖出，一次等待的限制。



<!-- more -->

>  ![image-20201226081801949](http://static.come2rss.xyz/image-20201226081801949.png)

## 代码：



```c++
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int d = prices.size(); 
        if(d <= 1) return 0;
        vector<vector<int>> dp(d, vector<int>(3));
        dp[0][0] = -prices[0];
        for(int i = 1; i < d; ++i){
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] - prices[i]);
            dp[i][1] = dp[i - 1][0] + prices[i];
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1]);
        }
        return max(dp[d - 1][1], dp[d - 1][2]);
    }
};
```