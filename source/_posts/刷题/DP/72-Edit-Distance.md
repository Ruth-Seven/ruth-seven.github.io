---
title: 72. Edit Distance
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-12-21 08:33:52
---




#### [72. Edit Distance](https://leetcode-cn.com/problems/edit-distance/)

<!-- more -->

## 思路：



`dp[i][j]`表示子串`word[0……i)`和子串`word[0……j)`需要变化的最小次数。

非常巧妙啊，很快就可以敲出代码，注意初始化边缘值。

## 代码：

```c++
class Solution {
public:
    int minDistance(string word1, string word2) {
        int n = word1.size();
        int m = word2.size();
        // if(n == 0 || m == 0) return 0;
        vector<vector<int>> dp(n + 1,  vector<int>(m + 1, 0));
        for(int i = 0; i <=n; ++i){
            for(int j = 0; j <= m; ++j){
                if(i == 0) dp[i][j] = j;
                else if(j == 0) dp[i][j] = i;
                else{
                    dp[i][j] = min(dp[i-1][j - 1] + (word1[i - 1] == word2[j - 1]? 0 : 1), 
                        min(dp[i - 1][j], dp[i][j - 1]) +  1);
                }
            }
        }
        return dp[n][m];
    }
};
```