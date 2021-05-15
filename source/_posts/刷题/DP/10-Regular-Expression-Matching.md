---
title: 10. Regular Expression Matching
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-12-23 09:44:57
---




## [10. Regular Expression Matching](https://leetcode-cn.com/problems/regular-expression-matching/)

## 思路：

hard的DP题，思路见代码。

<!-- more -->

## 代码：



```c++
class Solution {
public:
    bool isMatch(string s, string p) {
        int  n = s.size(), m = p.size();
        vector<vector<bool>> dp(n + 1, vector<bool>(m + 1, false));
        dp[0][0] = true;
        for(int j = 1; j <= m; j++){
            if(j > 1 && p[j - 1] == '*') dp[0][j] = dp[0][j - 2];
            for(int i = 1; i <= n; i++){
                if(p[j - 1] == '.') dp[i][j] = dp[i - 1][j - 1];
                else if(p[j - 1] != '*') dp[i][j] = dp[i - 1][j - 1] && s[i - 1] == p[j - 1];
                else if(s[i - 1] != p[j - 2] && p[j - 2] != '.')
                    dp[i][j] = dp[i][j -2];
                else // C* 子串可以匹配
                // 1. 重复模式 C, 比如 [aa，a*] -> [a，a*]，[ba，ba*] -> [b，ba*] (-> [b，b])
                // 2. 放弃匹配 C, 比如 [b，ba*] -> [b，b]
                // 我尝试去掉了 3 也是可以过的呵呵~ 
                // 3. 第一次匹配 C, 比如 [a，a*] -> [a ，a]
                //这题难就难在这, 想到状态转移方程
                    dp[i][j] = dp[i -1][j] || dp[i][j - 2] ;//|| dp[i][j - 1];
            }
        }
        return dp[n][m];
    }
};

```