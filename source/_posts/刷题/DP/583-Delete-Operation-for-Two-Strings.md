---
title: 583. Delete Operation for Two Strings
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-12-29 09:06:59
---






## [583. Delete Operation for Two Strings](https://leetcode-cn.com/problems/delete-operation-for-two-strings/)



## 思路：

此题可以转化为最长公共子序列（LCS）。用动态规划解决LCS即可。

<!-- more -->

## 代码：

```c++
class Solution {
public:
    int minDistance(string word1, string word2) {
        int n = word1.size(), m = word2.size();
        // vector<vector<int>> dp(n + 1, vector<int>(m + 1)); //vector分配空间耗时很大，同时占用的空间也大 
        int dp[n + 1][m + 1];
        memset(dp, 0, sizeof(dp));
        for(int i = 1; i <= n; ++i){
            for(int j = 1; j <= m;- ++j){
                if(word1[i - 1] == word2[j - 1]){
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                }else dp[i][j] = max(dp[i][j - 1], dp[i - 1][j]);
            }
        }
        return n + m - 2 * dp[n][m];
    }
};


```





## 运行效率：

leetcode的运行时间真是的迷，不过数据集太小了，确实难以准确评估。

![image-20201229090424332](D:\个人文件\重要文件\闲书与笔记\MD暂存文件\image-20201229090424332.png)