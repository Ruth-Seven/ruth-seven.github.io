---
title: 547. Friend Circles
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-11-22 09:45:38
---




## [547. Friend Circles](https://leetcode-cn.com/problems/friend-circles/)

## 思路：

dfs搜索人头就行。

<!-- more -->

## 代码：

```c++
class Solution {
public:
    int n;

    void colorize(vector<vector<int>>& M, vector<int>& vis,int x){
        vis[x] = 1;
        for(int i = 0; i < n; ++i){            
            if(!vis[i] && M[x][i]){                
                colorize(M, vis, i); 
            }             
        }
    }
    int findCircleNum(vector<vector<int>>& M) {
        n = M.size();
        vector<int> vis(n, 0);
        int ct = 0;
        for(int i = 0; i < n; ++i){
            if(!vis[i]){
                ct++;
                colorize(M, vis, i);
            }            
        }
        return ct;
    }
};
```