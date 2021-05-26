---
title: 213. House Robber II
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-12-28 15:41:47
---





## [213. House Robber II](https://leetcode-cn.com/problems/house-robber-ii/)



## 思路：



首和尾的数字元素不能同时选择的。那么直接把列表拆分成两个$[0,...., n - 2]$和$[1,.....,n-1]$，分开DP就行了。

使用$dp[i]$表示数组在元素$i$上所能获得的最大金钱。

> 当然也可进行动作拆分。

<!-- more -->

## 代码：

```c++
class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        if(n == 0) return 0;
        else if(n <= 1) return nums[0];
        return max(getdp(nums, 0, n - 1), getdp(nums, 1, n));
    }

    int getdp(vector<int> nums, int s, int e){
        if(s >= e) return 0;
        if(s + 2 <= e) //初始化
            nums[s + 1] = max(nums[s], nums[s + 1]); 
        for(int i = s + 2; i < e; ++i){
            nums[i] = max(nums[i - 2] + nums[i], nums[i - 1]);
        }
        return nums[e - 1];
    }
};
```