---
title: 77. Combinations
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-11-25 14:02:41
---





## [77. Combinations](https://leetcode-cn.com/problems/combinations/)



## 思路：

回溯，获取搭配数组，

<!-- more -->

>  $s <= n - k  + 1$

## 代码:

```c++

class Solution {
public:
    void getKnumber(vector<vector<int>>& ans, vector<int> &addt, int n, int k, int s){
        if(addt.size() == k){
            ans.push_back(addt);            
            return;
        }
        if(s > n) return;
        
        for(int i = s; i <= n - k + addt.size() + 1; ++i){
            addt.push_back(i);
            getKnumber(ans, addt, n, k, i + 1);
            addt.pop_back();
        }
    }

    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> res;
        vector<int> addt;
        getKnumber(res, addt, n, k, 1);
        return res;
    }
};
```