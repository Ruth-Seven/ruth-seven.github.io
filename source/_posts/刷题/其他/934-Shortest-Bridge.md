---
title: 934. Shortest Bridge
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
categories:
date: 2020-11-28 10:04:11
tags:
---




## [934. Shortest Bridge](https://leetcode-cn.com/problems/shortest-bridge/)



## 思路：

一次dfs搜索一个岛屿，一次bfs搜最短路径。

<!-- more -->

## 代码：

```c++
class Solution {
public:
    int n, m;
    int dx[4] = {-1, 1, 0, 0};
    int dy[4] = {0, 0, -1, 1};
    class Point{
    public:
        int x;
        int y;
        int dis;
        Point(int _dis, int _x, int _y){
            x = _x;
            y = _y;
            dis = _dis;
        }        
        friend bool operator <(const Point &a, const Point &b){
            return a.dis > b.dis;
        }
    };

    bool check(int x, int y){
        return !(x < 0 || x >= m || y < 0 || y >= n );
    }
    void getIslang(vector<vector<int>>& A, vector<vector<int>>& vis, 
                priority_queue<Point> &island, int x, int y){
        if( !check(x,y) || vis[x][y] || A[x][y] == 0) return;
        island.push(Point(0, x, y));
        vis[x][y] = 1;
        for(int i = 0; i < 4; ++i){
            int nx = x + dx[i];
            int ny = y + dy[i];
            getIslang(A, vis, island, nx , ny);
        }
    }

    int shortestBridge(vector<vector<int>>& A) {
        m = A.size();
        if(m == 0) return -1;
        n = A[0].size();
        vector<vector<int>> vis(m, vector<int>(n, 0));
        priority_queue<Point> que;
        int flag = 1;
        for(int i = 0; flag &&  i < m; ++i){
            for(int j = 0; j < n; ++j){
                if(A[i][j] == 1){
                    flag = 0;
                    getIslang(A, vis, que, i, j);
                    break;
                }

            }
        }
        // cout << que.size() << endl;
        while(que.size()){
            Point p = que.top();
            que.pop();
            // cout << p.x  << " " << p.y  << endl;
            for(int i = 0; i < 4; ++i){
                int nx = p.x + dx[i];
                int ny = p.y + dy[i];
                
                if(!check(nx, ny)) continue;

                if(!vis[nx][ny]){
                    vis[nx][ny] = 1;
                    
                    if(A[nx][ny] == 1){
                        return p.dis;
                    }else{
                        que.push(Point(p.dis + 1, nx, ny));
                    }
                }
            }
        }
        return -1;
    }
};
```