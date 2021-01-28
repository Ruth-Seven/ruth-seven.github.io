---
title: 310. Minimum Height Trees
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-12-06 09:51:10
---





## [310. Minimum Height Trees](https://leetcode-cn.com/problems/minimum-height-trees/)

## 思路：

1. （超时）bfs
2. 拓扑排序变形。从图的边缘点逆向追溯到中心点，可以直接获取到目标点。又有题目性质猜得，没有孤立点（除非n=1），没有环。那么目标点至多只有两个。

<!-- more -->s





```c++
class Solution {
public:    
    vector<vector<int>> map;

    vector<int> findMinHeightTrees(int n, vector<vector<int>>& edges) {
       map.resize(n);
       for(int i = 0; i < edges.size(); ++i){
           int x = edges[i][0];
           int y = edges[i][1];
            map[x].emplace_back(y);
            map[y].emplace_back(x);
       }
       int minl = n - 1;
       vector<int> root;
       for(int i = 0; i < n; ++i){
           vector<bool> vis(n, false);
           int len = dfs(i, vis, 0);
        
           if(len < minl){
               root.clear();
               minl = len;
           }
           if(len == minl){
               root.push_back(i);
           }
       }
        return root;
    }

    int dfs(int v, vector<bool>&vis, int len){
        vis[v] = 1;
        int maxlen = len;
        for(auto u : map[v]){        
            if(!vis[u]){
            // cout << v << ' ' << u << ' ' << len << endl;
                maxlen = max(maxlen, dfs(u, vis, len + 1)); // bugs: maxv = max(maxv, dfs(maxv + 1));
            }
        }
        return maxlen;
    }
};
```



拓扑AC

```c++
class Solution {
public:    
    vector<vector<int>> map;
    vector<int> degree;
    vector<int> findMinHeightTrees(int n, vector<vector<int>>& edges) {
       map.resize(n);
       degree.resize(n);
       for(int i = 0; i < edges.size(); ++i){
           int x = edges[i][0];
           int y = edges[i][1];
            map[x].emplace_back(y);
            map[y].emplace_back(x);
            degree[x]++;
            degree[y]++;
       }
       queue<int> que;
       int m = 0;
        for(int i = 0;i < n; ++i){
            if(degree[i] == 1){
                que.push(i);
            }
            if(degree[i] > 0) ++m;
        }
        vector<int> root;
        while(que.size()){
            m -= que.size();
            if(m == 0) break;
            // cout << m << endl;
            while(que.size()){                
                int u = que.front();                
                que.pop();
                for(auto v : map[u]){
                    degree[v]--;
                    degree[u]--;
                    if(degree[v] == 0) root.push_back(v);
                }
            }

            for(int i = 0; i < n; ++i){
                if(degree[i] == 1){
                    que.push(i);
                }
            }
        }
        if(root.size() == 0)
        while(que.size()){
            root.push_back(que.front());
            que.pop();
        }
        if(n == 1) root.push_back(0);
        return root;
    }
};

```

利用性质优化一下

```c++
class Solution {
public:    
    vector<vector<int>> map;
    vector<int> degree;
    vector<int> findMinHeightTrees(int n, vector<vector<int>>& edges) {
       map.resize(n);
       degree.resize(n);
       for(int i = 0; i < edges.size(); ++i){
           int x = edges[i][0];
           int y = edges[i][1];
            map[x].emplace_back(y);
            map[y].emplace_back(x);
            degree[x]++;
            degree[y]++;
       }
       queue<int> que;
       int m = n;
        for(int i = 0;i < n; ++i){
            if(degree[i] == 1){
                que.push(i);
            }            
        }
        vector<int> root;
        while(m > 2){            
            m -= que.size();
            int size = que.size();
            for(int i = 0; i < size; ++i){                
                int u = que.front();                
                que.pop();
                for(auto v : map[u]){
                    degree[v]--;
                    if(degree[v] == 1){
                       que.push(v);
                    }
                }
            }
        }

        if(root.size() == 0)
        while(que.size()){
            root.push_back(que.front());
            que.pop();
        }
        if(n == 1) root.push_back(0);
        return root;
    }
};
```