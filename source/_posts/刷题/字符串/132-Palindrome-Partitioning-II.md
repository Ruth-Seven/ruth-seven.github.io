---
title: 132. Palindrome Partitioning II
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
date: 2021-03-08 11:48:05
tags:
categories:
---








# [132. Palindrome Partitioning II](https://leetcode-cn.com/problems/palindrome-partitioning-ii/)







## 思路：

`dp`，`dp[i]`表示最小分割子串数，状态转移方程为：

![image-20210308114617311](http://static.come2rss.xyz/image-20210308114617311.png)

其中子串是否为回文串可以预计算，这样就把复杂度从`o(N^3)`降到`o(N^2)`。

<!-- more -->

## 代码：





```C++
class Solution {
    vector<int> dp;
public:
    
    int minCut(string s) {
        int n = s.size();
        dp.resize(n);
        for(int i = 0; i < n; ++i){
            dp[i] = i + 1;
            for(int j = i; j >= 0; --j){
                if(isPalindrome(s, j, i)){
                    dp[i] = min(j == 0 ? 1 : dp[j - 1] + 1, dp[i]);
                }
            }
        }
        return dp[n - 1] - 1;
    }
    
    bool isPalindrome(string &s, int i, int j){
        if(i >= j) swap(i, j);
        while(i != j && i < j){
            if(s[i] != s[j]) return false;
            --j;
            ++i;
        }
        return true;
    }

 
    

};
```

预计算



```
class Solution {
    vector<int> dp;
    vector<vector<int>> isPal;
public:
    
    int minCut(string s) {
        int n = s.size();
        dp.resize(n);
        isPal.resize(n, vector<int>(n,1));
        for(int i = n - 1; i >= 0; --i){
            for(int j = i + 1; j < n; ++j){
                   // if(i == j) isPal[i][j] = 1;
                // else if(i != n- 1 && j != 0)     
                isPal[i][j] = isPal[i + 1][j - 1] && s[i] == s[j]; // s[i,j]的回文需要s[i + 1, j - 1]的回文，那么反向遍历即可。
            }
        }
        for(int i = 0; i < n; ++i){
            dp[i] = i + 1;
            for(int j = i; j >= 0; --j){
                if(isPal[j][i]){
                    dp[i] = min(j == 0 ? 1 : dp[j - 1] + 1, dp[i]);
                }
            }
        }

        return dp[n - 1] - 1;
    }
    
 
    

};
```

