---
title: 494. Target Sum
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-12-31 10:20:46
---



## [494. Target Sum](https://leetcode-cn.com/problems/target-sum/)



## 思路：

<!-- more -->

## 代码：

```c++
class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int S) {
        const int T = 2001;
        if(nums.size() == 0) return 0;
        int sum = 0;
        for(auto v : nums) sum += abs(v);
        if(sum < abs(S)) return 0;
        int dp[23][T * 2]; //bugs: 20;
        memset(dp, 0, sizeof(dp));

        dp[0][T] = 1;
        for(int i = 0; i < nums.size(); ++i){
            for(int j = 0; j < T * 2; ++j){
                if(dp[i][j]){
                    dp[i + 1][j + nums[i]] += dp[i][j];
                    dp[i + 1][j - nums[i]] += dp[i][j];
        // cout << i + 1 << " "  << j + nums[i] <<  " " <<  dp[i + 1][j + nums[i]] << endl;
        // cout << i + 1 << " "  << j - nums[i] <<  " " <<  dp[i + 1][j - nums[i]] << endl;
                }
            }
            // cout << "#" << i <<endl;
        }
        return dp[nums.size()][S + T];
    }
};
```