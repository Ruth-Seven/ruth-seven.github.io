---
title: 268. Missing Number
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2021-01-19 11:18:43
---




## [268. Missing Number](https://leetcode-cn.com/problems/missing-number/)



## 思路：

1. 排序
2. 哈希
3. 异或位运算 
4. 高斯求和

3和4实现了$O(n)$的时间复杂度和$O(1)$的空间复杂度。

<!-- more -->

## 代码：



```C++

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        if(n == 0 ) return 0;
        int lose = 0;
        for(auto & k : nums){
            lose ^= k;
        }
        for(int i = 0; i <= n; ++i) lose ^= i;
        return lose;
    }
};
```