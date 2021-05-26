---
title: 416. Partition Equal Subset Sum
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-12-16 08:53:38
---

## [416. Partition Equal Subset Sum](https://leetcode-cn.com/problems/partition-equal-subset-sum/)

## 思路

类似01背包的题，不过不用考虑价值。

<!-- more -->



## 代码

```c++

class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int sum = accumulate(nums.begin(), nums.end(), 0);
        if(sum % 2) return false;
        int n = nums.size();
        int target = sum / 2;
        vector<vector<int>> dp(n + 1, vector<int>(target + 1, 0));
        
        for(int i = 0; i <= n; ++i){
            dp[i][0] = 1;
        }
        for(int i = 1; i <= n; ++i){
            for(int j = nums[i - 1]; j <= target; ++j){
                dp[i][j] =  dp[i - 1][j - nums[i - 1]] || dp[i - 1][j];
            }
        }
        return dp[n][target];
    }
};
```

空间压缩



```c++

class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int sum = accumulate(nums.begin(), nums.end(), 0);
        if(sum % 2) return false;
        int n = nums.size();
        int target = sum / 2;
        vector<int> dp(target + 1, 0);    
        dp[0] = 1;        
        for(int i = 1; i <= n; ++i){
            for(int j = target; j >= nums[i - 1]; --j){//逆序
                dp[j] =  dp[j - nums[i - 1]] || dp[j];
            }
        }
        return dp[target];
    }
};
```