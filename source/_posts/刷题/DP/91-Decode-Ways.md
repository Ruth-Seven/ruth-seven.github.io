---
title: 91. Decode Ways
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-12-11 09:59:25
---




## [91. Decode Ways](https://leetcode-cn.com/problems/decode-ways/)

## 思路：

$dp[i]$表示数字字符子串$S[0...i]$所能表示的字符串数量。dp方程见代码。

注意点：

1. $0$无法被直接表示，因此dp方程分支扩大了一倍。
2. 为了方便初始化，可以添加前缀零。

<!-- more -->

## 代码：



```c++

class Solution {
public:
    int numDecodings(string s) {
        s = "00" + s; //添加前缀，方便设置dp初始值
        int n = s.size();
        vector<int>dp(n, 0);
        if(n == 2 || s[2] == '0') return 0;
        dp[0] = dp[1] = 1;
        
        for(int i = 2; i < n; ++i){            
            if(s[i - 1] == '1' || (s[i - 1] == '2' && s[i] < '7')){                
                if(s[i] == '0') dp[i] = dp[i - 2];
                else dp[i] = dp[i - 2]  + dp[i - 1];
            }
            else if(s[i] == '0') dp[i] = 0;
            else dp[i] = dp[i - 1];
        }
        return dp[n - 1];
    }
};
```