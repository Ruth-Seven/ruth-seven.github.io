---
title: 64. Minimum Path Sum
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-12-08 08:55:55
---







## [64. Minimum Path Sum](https://leetcode-cn.com/problems/minimum-path-sum/)

## 思路:

dp长度

<!-- more -->

## 代码：

```c++
class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int n = grid.size();
        if(n == 0) return 0;
        int m = grid[0].size();
        if(m == 0) return 0;
        vector<vector<int>> dp(n, vector<int>(m, 0));
        dp[0][0] = grid[0][0];
        for(int i = 1; i < m; ++i){
            dp[0][i] = dp[0][i - 1] + grid[0][i];
        }        
        for(int i = 1; i < n; ++i){
            dp[i][0] = dp[i - 1][0] + grid[i][0];
        }
        for(int i = 1; i < n; ++i){
            for(int j = 1; j < m; ++j){
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j];
            }
        }
        return dp[n - 1][m - 1];

    
    }
};
```