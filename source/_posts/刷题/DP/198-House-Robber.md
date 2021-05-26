---
title: 198. House Robber
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-12-07 09:16:58
---



## [198. House Robber](https://leetcode-cn.com/problems/house-robber/)



## 思路：



1. 将偷和不偷的两种状态分别记录到两个dp上，dp方程见代码1
2. 如果不分解，记$dp[i]$为在房子$i$所能获得最大的金钱收益，应该可以比较偷窃第$i$房子加上之前$i-2$个房子所能偷窃的最大金额，和只偷窃前$i-1$房子的最大金额。
> ![image-20201207091040289](http://static.come2rss.xyz/image-20201207091040289.png)

<!-- more -->

## 代码：

代码1

```	c++
class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        if(n == 0) return 0;
        vector<int> dp1(n, 0);
        vector<int> dp0(n, 0);
        dp0[0] = 0; dp1[0] = nums[0];
        
        for(int i = 1; i < n; ++i){
            dp0[i] = max(dp0[i - 1], dp1[i - 1]);
            dp1[i] = dp0[i - 1] + nums[i];
        }
        return max(dp1[n - 1], dp0[n - 1]);
    }
};
```



dp2

100%

```c++
class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        if(n == 0) return 0;
        else if(n == 1) return nums[0];
        vector<int> dp(n, 0);
        dp[0] = nums[0];
        dp[1] = max(nums[0], nums[1]);
        for(int i = 2; i < n; ++i){
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i]);            
        }
        return dp[n - 1];
    }
};
```