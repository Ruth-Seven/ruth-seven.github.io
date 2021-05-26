---
title: 594. Longest Harmonious Subsequence
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
date: 2021-01-30 15:11:50
tags:
categories:
---





## [594. Longest Harmonious Subsequence](https://leetcode-cn.com/problems/longest-harmonious-subsequence/)





## 思路：



一道经典的最大递增子序列的变形题

结果用DP思路做了半天，发现越做复杂！？？？？

怀疑人生的同时发现自己的思路还是太窄了。

<!-- more -->





## 代码：

```c++
class Solution {
public:
    int findLHS(vector<int>& nums) {
        int n = nums.size();
        unordered_map<int, int> ct;
        int maxl = 0;
        for(auto & v : nums){
            ct[v]++;
            int t = max(ct[v+1], + ct[v - 1]);
            if(t) maxl = max(t + ct[v], maxl);            
        }
        return maxl;
        
    }
};
```