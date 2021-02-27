---
title: 210. Course Schedule II (Medium)
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
date: 2021-02-27 09:19:16
tags:
categories:
---




# [210. Course Schedule II](https://leetcode-cn.com/problems/course-schedule-ii/)





## 思路：

1. dfs + 判环 + 回溯 
2. 入度

<!-- more -->

## 代码：

```c++
class Solution {
public:
    vector<vector<int>> map;
    stack<int> track;
    vector<int> vis;
    int flag = 0;
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        map.resize(numCourses);
        vis.resize(numCourses);
        for(auto e : prerequisites){
            int u = e[0], v = e[1];
            map[v].emplace_back(u);
        }
        for(int i = 0; i < numCourses; ++i)
            if(!vis[i]) dfs(i);
        vector<int> ans;
        while(!track.empty()){
            ans.emplace_back(track.top());
            track.pop();
        }
        if(flag) return {};
        else return ans;
    }

    void dfs(int u){
        vis[u] = -1;
        for(auto v : map[u]){
            if(!vis[v]){
                dfs(v);
            }else if(vis[v] == -1){ // 如果第一次遍历到一个环，那么这个环一定会被全部遍历到
                flag = 1;
            }
        }
        vis[u] = 1;
        track.push(u);
    }
};

```





```c++
class Solution {
public:
    vector<vector<int>> map;
    vector<int> indegrees;
    queue<int> que;
    int flag = 0;

    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        map.resize(numCourses);
        indegrees.resize(numCourses);
        for(auto e : prerequisites){
            int u = e[0], v = e[1];
            map[v].emplace_back(u);
            ++indegrees[u];
        }
        for(int i = 0; i < numCourses; ++i)
            if(!indegrees[i]) que.push(i);
        vector<int> ans;
        
        while(!que.empty()){
           int t = que.front(); 
           ans.push_back(t);
           que.pop();
           for(auto v : map[t]){
                --indegrees[v];
                if(indegrees[v] == 0)
                    que.push(v);
           }
        }
        if(ans.size() != numCourses) return {};
        else return ans;
    }

};
```