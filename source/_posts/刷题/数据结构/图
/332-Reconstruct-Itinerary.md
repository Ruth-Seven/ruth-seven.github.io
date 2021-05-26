---
title: 332. Reconstruct Itinerary
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2021-01-28 14:43:49
---




## [332. Reconstruct Itinerary](https://leetcode-cn.com/problems/reconstruct-itinerary/)

图论补充知识：

通过图中所有边恰好一次且行遍所有顶点的通路称为**欧拉通路**。

通过图中所有边恰好一次且行遍所有顶点的回路称为**欧拉回路**。

<!-- more -->

具有欧拉回路的无向图称为**欧拉图**。

具有欧拉通路但不具有欧拉回路的无向图称为**半欧拉图**。

因为本题保证至少存在一种合理的路径，也就告诉了我们，这张图是一个欧拉图或者半欧拉图。我们只需要输出这条欧拉通路的路径即可。



如果没有保证至少存在一种合理的路径，我们需要判别这张图是否是欧拉图或者半欧拉图，具体地：

对于**无向图** G，G 是欧拉图当且仅当 G 是连通的且没有奇度顶点。

对于**无向图** G，G 是半欧拉图当且仅当 G 是连通的且 G 中恰有 2个奇度顶点。

对于有向图 G，G 是欧拉图当且仅当 G 的所有顶点属于同一个强连通分量且每个顶点的入度和出度相同。

对于**有向图** G，G 是半欧拉图当且仅当 G 的所有顶点属于同一个强连通分量且

+ 恰有一个顶点的出度与入度差为 1；
+ 恰有一个顶点的入度与出度差为 1；
+ 所有其他顶点的入度和出度相同。

## 思路：

首先，以站点为点，tickets为单向边，可建有向图。

题目保证了欧拉图的存在，我们需要在图上寻找一条字母序最小的欧拉通路。我们可以使用Hierholzer 算法求出该通路，其中优先遍历字母序最小的站点即可。

#### Hierholzer 算法

算法流程如下：

1. 从某点开始出发，遍历该图
2. 每次移动后，删除刚刚经过的边（DFS）
3. 当遍历该节点结束后，也就是没有其他路径可走，把节点记录下来。

因为每次记录的节点都是当时遍历时最后退出的节点，所以必定比之前压入的节点在欧拉图前，同时由于删边的性质和起点是欧拉通路的起点，保证了路径的有效性。所以一定能搜到。

> 一开始把票当成点，相同的点当成边，把简单的欧拉问题变成了复杂的旅行商问题，我干！



## 代码：

```c++
class Solution {
public:
    map<string, priority_queue<string, vector<string>, greater<string>>> vec;

    vector<string> path;

    void dfs(string curr){
        while(vec.count(curr) && vec[curr].size()){
            string tmp = vec[curr].top();
            vec[curr].pop();
            dfs(tmp);
        }
        path.emplace_back(curr);
    }
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        for(auto &item : tickets){
            vec[item[0]].push(item[1]);
        }
        dfs("JFK");
        reverse(path.begin(), path.end());
        return path;
    }
};
```