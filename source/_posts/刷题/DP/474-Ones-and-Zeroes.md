---
title: 474. Ones and Zeroes
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-12-18 09:30:19
---




## [474. Ones and Zeroes](https://leetcode-cn.com/problems/ones-and-zeroes/)

## 思路：



类似于01背包，但是不同 的是有两个范围限制。属于二维dp.

<!-- more -->

## 代码：

```c++
class Solution {
public:
    int findMaxForm(vector<string>& strs, int m, int n) {
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
        for(auto str : strs){
            auto [c1, c2] = count(str);
            for(int i = m; i >= c1; i--){
                for(int j = n; j >= c2; j--){
                    dp[i][j] = max(dp[i][j], dp[i - c1][j - c2] + 1);
                }
            }
        }
        return dp[m][n];
   }

   pair<int, int> count(string str){
       int c1 = 0, c2 = 0;
       for(auto c : str){
           if(c == '0') c1++;
           else c2++;
       }
       return make_pair(c1, c2);
   }
};
```