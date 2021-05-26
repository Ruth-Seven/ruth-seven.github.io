---
title: 123. Best Time to Buy and Sell Stock III
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-12-25 09:45:19
---




## [123. Best Time to Buy and Sell Stock III](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/)



## 思路：

1. 借用[简单股票](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)的思路可以双向遍历price,获取`price[0, i]`和`price[i, n]`两个时间段各自最大的花费。
2. 比较巧妙，用第一段操作的利润去抵消第二段购买时的花费，一次遍历。

> 股票的题目有很多，慢慢写。
>
> ![image-20201226081801949](http://static.come2rss.xyz/image-20201226081801949.png)

<!-- more -->

## 代码：

35%

```c++
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int d = prices.size();
        vector<int> left(d, 0), right(d, 0);
        int maxv = prices[0], minv = prices[0], maxpro = 0;
        for(int i = 0; i < d; ++i){
            if(minv > prices[i]){
                maxv = minv = prices[i];
            }
            maxv = max(maxv, prices[i]);
            maxpro = left[i] = max(left[i], max(maxpro, maxv - minv));
        }
        maxv = minv = prices[d - 1], maxpro = 0;
        for(int i = d - 1; i >= 0; --i){
            if(maxv < prices[i]){
                maxv = minv = prices[i];
            }
            minv = min(minv, prices[i]);
            maxpro = right[i] = max(right[i], max(maxpro, maxv - minv));
        }
        int res = 0;
        for(int i = 0; i < d; ++i){
            res = max(res, left[i] + right[i]);
            // cout << left[i] + right[i] << endl;
        }
        return res;
    }
};
```



93%

```c++
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int d = prices.size();
        int pro1, pro2, minp1, minp2;
        pro1 = pro2 = INT_MIN;
        minp1 = minp2 = INT_MAX;
        for(auto p : prices){
            minp1 = min(p, minp1);
            pro1 = max(pro1, p - minp1);
            minp2 = min(minp2, p - pro1);
            pro2 = max(pro2, p - minp2);
        }
        return pro2;
    }
};
```