---
title: 139. Word Break
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-12-13 09:28:19
---

## [139. Word Break](https://leetcode-cn.com/problems/word-break/)



## 思路：

动态规划：$dp[i]=1$表示s子串`s.substr(0,i + 1)`可以被在词典中正确切分。

<!-- more -->

## 代码:

77%

```c++
class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        // if(s.size())
        set<string> dict;
        for(auto t : wordDict)
            dict.insert(t);
        vector<int> dp(s.size(), 0);
        // int lastdo = 0;
        for(int i = 0;i < s.size(); ++i){
            if(dict.count(s.substr(0, i + 1)))
                    dp[i] = 1;                
                
            for(int j = i; j > 0; j--){
                if(dp[j - 1] && dict.count(s.substr(j, i - j + 1))){
                    dp[i] = 1;
                    break;
                }
            }
        }    
        if(dp[s.size() - 1]) return true;
        return false;
    }
};
```