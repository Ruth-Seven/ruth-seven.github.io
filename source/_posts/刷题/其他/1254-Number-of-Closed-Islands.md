---
title: 1254. Number of Closed Islands
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-08-07 14:11:56
---

<!-- more -->



#### [1254. Number of Closed Islands](https://leetcode-cn.com/problems/number-of-closed-islands/)

难度MD

**思路**：DFS或者并查集

1. 排除法：将所有接触过边界的0块排除掉，接下来统计所有的0块数量就是岛屿的数量啦~
2. 直接法：考虑成为岛屿的条件——岛屿上所有0块都不与边界相交。

接下来只需要写DFS或者BFS就👌。

1. 考虑使用并查集

**排除法**



```
class Solution {
public:
	//保持和第二种写法一致，add参数实际上是多余的
    void findBlockOf0(int x, int y,int N, int M, vector< vector<int> > &grid, int &add){
        if(x < 0 || x >= N || y < 0 || y >= M || grid[x][y] == 1) return;
        //if(grid[x][y] == 1) add = 1;
        grid[x][y] = 1;
        findBlockOf0(x, y+1, N, M, grid, add);
        findBlockOf0(x, y-1, N, M, grid, add);
        findBlockOf0(x+1, y, N, M, grid, add);
        findBlockOf0(x-1, y, N, M, grid, add);
        return;
    }

    int closedIsland(vector<vector<int>>& grid) {
        int N = grid.size(), M = grid[0].size(), counts, add;
        //排除掉那些不是island的blocks of 0
        for(int i=0;i < M; i++){
            findBlockOf0(0,i, N, M, grid, counts);
            findBlockOf0(N-1,i, N, M, grid, counts);
        }
        for(int i=0;i < N;i++){
            findBlockOf0(i,0,N,M, grid, counts);
            findBlockOf0(i,M-1, N, M, grid, counts);
        }
        //接下来所有的0块都可以算作island
        counts = 0;
        for(int x = 0 ;x < N;x++){
            for(int y=0; y < M; y++ ){
                if(grid[x][y] != 0) continue;
                findBlockOf0(x, y, N, M, grid, add);
                counts += 1;
            }                                         
        }
        return counts;
    }
};
```

**直接法**

```
class Solution {
    public:
	// 注意遍历的时候不能剪枝，否则就会就会出现岛屿断裂成多个“单独”岛屿而计数过多
    void findBlockOf0(int x, int y,int N, int M, vector< vector<int> > &grid, int &add){
        if(x < 0 || x >= N || y < 0 || y >= M || grid[x][y] == 1) return;
        if(x == 0 || x == N-1|| y == 0 || y == M-1 ) add = 0;
        grid[x][y] = 1;
        // 这里的四个方向其实可以用FOR写的更优雅一些
        findBlockOf0(x, y+1, N, M, grid, add);
        findBlockOf0(x, y-1, N, M, grid, add);
        findBlockOf0(x+1, y, N, M, grid, add);
        findBlockOf0(x-1, y, N, M, grid, add);
        return;
    }

    int closedIsland(vector<vector<int>>& grid) {
        int N = grid.size(), M = grid[0].size(), counts;
        counts = 0;
        for(int x = 0 ;x < N;x++){
            for(int y=0; y < M; y++ ){
                if(grid[x][y] != 0) continue;
                int add = 1;
                findBlockOf0(x, y, N, M, grid, add);
                counts += add;
            }                                         
        }
        return counts;
    }
};
```

尝试使用BFS写第二种写法~

```
class Solution {
public:
	// BFS
    int findBlockOf0(int x, int y,int N, int M, vector< vector<int> > &grid){
        int dX[4] = {0, 0, -1, 1}, dY[4] = {1, -1, 0, 0}, nX, nY;
        int flag = 1;
        queue< vector<int> > que;
        que.push( {x, y});
        grid[x][y] = 1;
        while( !que.empty() ){
            vector<int> point = que.front();
            que.pop();
            int x = point[0], y = point[1];
            //注意 所有的点都需要判断是否在边界上
            if(x  == 0 || x == N - 1 ||y == 0 || y == M - 1) flag = 0;
            for(int i=0;i < 4; i++){
                nX = x + dX[i];
                nY = y + dY[i];
                if(nY >= 0 && nY < M && nX >=0 && nX < N && grid[nX][nY] == 0){                
                    grid[nX][nY] = 1;
                    que.push({nX, nY});
                    
                }
            }
        }
        return flag;
    }

    int closedIsland(vector<vector<int>>& grid) {
        int N = grid.size(), M = grid[0].size(), counts;
        counts = 0;
        for(int x = 0 ;x < N;x++){
            for(int y=0; y < M; y++ ){
                if(grid[x][y] != 0) continue;
                counts +=  findBlockOf0(x, y, N, M, grid);
            }                                         
        }
        return counts;
    }
};
```

并查集

改日再战