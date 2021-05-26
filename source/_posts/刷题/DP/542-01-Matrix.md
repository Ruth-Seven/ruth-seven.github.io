---
title: 542. 01 Matrix
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-12-08 08:55:46
---





## [542. 01 Matrix](https://leetcode-cn.com/problems/01-matrix/)

## 思路：

1. 从数字0开始bfs到1的最短路
2. 由于从数字1到最近的数字零之间的最短路径，如果不是相邻，那么必定有在路径上数字1到同样的数字0有一条最短路径。如此便可以在四个移动方向上分别dp最短路径长度即可。

<!-- more -->

## 代码：

bfs

66%

```c++
class Solution {
public:
    int dx[4] = {0, 0, -1, 1};
    int dy[4] = {-1, 1, 0, 0};

    vector<vector<int>> updateMatrix(vector<vector<int>>& matrix) {
        int n = matrix.size();
        int m = matrix[0].size();
        vector<vector<int>> dis(n, vector<int>(m , 0));
        vector<vector<int>> vis(n, vector<int>(m, 0));
        queue<pair<int,int>> que;
        for(int i = 0; i < n; ++i){
            for(int j = 0; j < m; ++j){
                if(matrix[i][j] == 0){
                    que.push(make_pair(i ,j));
                    vis[i][j] = 1;
                }                    
            }
        }
        int qsize;
        while(que.size()){
            qsize = que.size();
            for(int i = 0; i < qsize; ++i){
                pair<int,int> t = que.front();
                que.pop();
                int x = t.first;
                int y = t.second;
                // cout << x << y  << endl;
                for(int j = 0; j < 4; ++j){
                    int nx = x + dx[j];
                    int ny = y + dy[j];
                    // cout <<"@" <<  nx << ny  << endl;
                    if(nx < 0 || ny < 0 || nx >= n || ny >= m) continue;
                    if(!vis[nx][ny]){                        
                        vis[nx][ny] = 1; // exclude the deplucation of elements in queue.
                        dis[nx][ny] = dis[x][y] + 1;
                        que.push(make_pair(nx, ny));
                        // cout << nx << ' ' << ny  << ' ' << dis[nx][ny] << endl;
                    }
                }
            }
        }
        return dis;
    }
};
```



dp

97%

```c++
class Solution {
public:
    int dx[4] = {0, 0, -1, 1};
    int dy[4] = {-1, 1, 0, 0};

    vector<vector<int>> updateMatrix(vector<vector<int>>& matrix) {
        int n = matrix.size();
        int m = matrix[0].size();
        vector<vector<int>> dp(n, vector<int>(m , INT_MAX - 3)); //bugs: max value should be bigger than m and n.
        
        for(int i = 0; i < n; ++i){
            for(int j = 0; j < m; ++j){
                if(matrix[i][j] == 0){
                    dp[i][j] = 0;
                    continue;
                }
                if(i > 0) dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1);
                if(j > 0) dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1);
            }
        }
        for(int i = n - 1; i >=0; --i){
            for(int j = m - 1; j >= 0; --j){
                if(matrix[i][j] == 0) continue;
                if(i != n - 1) dp[i][j] = min(dp[i][j], dp[i + 1][j] + 1);
                if(j != m - 1) dp[i][j] = min(dp[i][j], dp[i][j + 1] + 1);
            }
        }        
        return dp;
    }
};
```