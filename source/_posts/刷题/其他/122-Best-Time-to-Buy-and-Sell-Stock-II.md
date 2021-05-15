---
title: 122. Best Time to Buy and Sell Stock II
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-10-15 07:02:41
---



<!-- more -->



## 思路：

贪心做每一个可以交易的交易就行

> ![image-20201226081801949](http://static.come2rss.xyz/image-20201226081801949.png)

## 代码：

```c++
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int sum = 0;
        for(int i = 0; i < prices.size() - 1; ++i){
            sum += (prices[i] < prices[i + 1] )? prices[i + 1] - prices[i] : 0; 
        }
        return sum;
    }
};
```

