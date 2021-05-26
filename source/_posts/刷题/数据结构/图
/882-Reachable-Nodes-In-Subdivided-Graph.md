---
title: 882. Reachable Nodes In Subdivided Graph
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
date: 2021-03-02 17:19:28
tags:
categories:
---







## 思路：

`subdivision nodes`可以化为路径的长度，将此问题转化为可以用dijstra求解的问题。

每次遍历到最新最短的节点都可以进行求出此点相连的边的可以累加`subdivistion nodes`的个数，但是需要控制重复累加比较麻烦。最后采用记录下每条边可到达的点，最后统一累计即可。



<!-- more -->

## 代码：



```c++
class Solution {
public:
    vector<vector<pair<int, int>>> road;
    vector<int> vis, dis;
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    map<pair<int, int>, int> used; // 其实dijsktra算法对于是可以做到每subdivision nodes只更新一次的，但是不好计算;
    int reachableNodes(vector<vector<int>>& edges, int maxMoves, int n) {
        road.resize(n);
        vis.resize(n);
        dis.resize(n, INT_MAX);
        for(auto e : edges){            
            road[e[0]].emplace_back(e[1], e[2] + 1);
            road[e[1]].emplace_back(e[0], e[2] + 1); // node, subdivision nodes + 1 = distantce
        }        
        pq.push({0, 0}); // distance, node;
        dis[0] = 0;
        int sumnode = 0;
        while(pq.size()){
            auto  [_, u] = pq.top(); pq.pop();
            // cout << u << endl;
            if(vis[u]) continue;
            if(dis[u] > maxMoves) break;
            vis[u] = 1;
            ++sumnode;
            for(auto [v, len] : road[u]){
                if(dis[v] > dis[u] + len){
                    dis[v] = dis[u] + len;
                    pq.push({dis[v], v});
                }
                used[{u, v}] = min(dis[u] + len, maxMoves) - dis[u];
            } 
        }
        for(auto edges : edges){
            int u = edges[0], v = edges[1], len = edges[2];
            sumnode += min(used[{u, v}] + used[{v, u}], len);
        }
        return sumnode;
    }
};
```

