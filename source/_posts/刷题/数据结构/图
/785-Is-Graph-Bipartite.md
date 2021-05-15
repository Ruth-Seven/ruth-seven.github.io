---
title: 785. Is Graph Bipartite?
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
date: 2021-02-24 12:17:57
tags:
categories:
---








# [785. Is Graph Bipartite?](https://leetcode-cn.com/problems/is-graph-bipartite/)



## 思路：

二分图染色问题，实际是就是判断任意一条边的形式是否有矛盾。

$O(E +N )$

<!-- more -->

## 代码：

```c++
class Solution {
public:
    int flag = 0;
    vector<int> color;

    bool isBipartite(vector<vector<int>>& graph) {
        int n = graph.size();
        color.resize(n, 0);
        for(int i = 0;i < n; ++i){
            if(color[i] == 0) colorize(graph, i, 1);
            if(flag) return false;
        }
        return true;
    }

    void colorize(vector<vector<int>>& graph, int u, int ctype){
        if(color[u]){
            if(color[u] * ctype == -1) flag = 1;
            return;
        }
        color[u] = ctype;
        for(auto v : graph[u]) colorize(graph, v, -ctype);
    }
};
```

