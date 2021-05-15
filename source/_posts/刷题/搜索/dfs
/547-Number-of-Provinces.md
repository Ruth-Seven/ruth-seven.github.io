---
title: 547. Number of Provinces
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2021-01-07 11:05:57
---





## [547. Number of Provinces](https://leetcode-cn.com/problems/number-of-provinces/)

## 思路：

多次dfs判断连通团即可

<!-- more -->

## 代码：







```c++
class Solution {
public:

    int findCircleNum(vector<vector<int>>& isConnected) {
        int res = 0, n = isConnected.size();
        vector<int> vis(n);
        for(int i = 0; i < n; ++i){
            if(!vis[i]){
                ++res;
                dfs(vis, isConnected, i);
            }
        }
        return res;
    }
     
    void dfs(vector<int> &vis, vector<vector<int>> &g, int k){
        if(vis[k]) return;
        vis[k] = 1;
        for(int i = 0; i < g.size(); ++i){
            if(g[k][i]) dfs(vis, g, i);
        }
    }
};
```

