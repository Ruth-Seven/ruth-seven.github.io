---
title: 1143. Longest Common Subsequence
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
categories:
date: 2020-12-15 21:23:07
tags:
---




## [1143. Longest Common Subsequence](https://leetcode-cn.com/problems/longest-common-subsequence/)

## 思路：



`dp[i][[j]`为text1和text2在位置i,j的最长公共子序列。

<!-- more -->

## 代码：

80%

```c++
class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int n = text1.size(), m = text2.size();
        if(n == 0 || m == 0) return 0;
        vector<vector<int>> dp;
        dp.resize(n, vector<int>(m, 0));        
        int flag = 0;
        for(int i = 0; i < n; i++){            
            if(flag || text1[i] == text2[0]){
               flag = 1; 
                dp[i][0] = 1;
            }
        }
        flag = 0;
        for(int i = 0; i < m; i++){
            if(flag || text1[0] == text2[i]){
                flag = 1;
                dp[0][i] = 1;
            }
        }

        for(int i = 1; i < n; ++i){
            for(int j = 1; j < m; ++j){
                if(text1[i] == text2[j]){
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                }else dp[i][j] = max(dp[i][j -1], dp[i - 1][j]);
                // cout << dp[i][j] << ' ';
            }
            // cout<< endl;
        }
        return dp[n - 1][m - 1];
    }
};
```