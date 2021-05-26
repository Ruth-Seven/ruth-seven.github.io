---
title: 695. Max Area of Island
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
categories:
date: 2020-11-19 10:58:40
tags:
---






## [695. Max Area of Island](https://leetcode-cn.com/problems/max-area-of-island/)

、

## 思路：

深度优先搜索

<!-- more -->

## 代码：

```c++

class Solution {
public:
    int dx[4] = {-1, 1, 0, 0};
    int dy[4] = {0, 0, 1, -1};
    int n, m;
    int maxAreaOfIsland(vector<vector<int>>& grid) {        
        if(grid[0].size() == 0) return 0;
        n = grid.size(), m = grid[0].size();
        vector< vector<int>> vis(n, vector<int>(m, 0));

        int maxA = 0;
        for(int i = 0; i < n; ++i){
            for(int j = 0; j < m; ++j){            
                int tempA = 0;
                if(grid[i][j] == 1 && vis[i][j] == 0){
                    area(grid, i, j, vis, tempA);
                    maxA = max(maxA, tempA);
                }                    
            }
        }
        return maxA;
    }
    
    void area(vector<vector<int>>& grid, int x, int y, vector<vector<int>>& vis, int &ct){//bug
        // cout << x << ' ' << y << endl;        
        if( x < 0 || x >=n || y < 0 || y >= m || vis[x][y] == 1 || grid[x][y] == 0 ) return;//bug
        vis[x][y] = 1; //bug        
        ct += 1;        
        for(int k = 0; k < 4; ++k)
            area(grid, x + dx[k], y + dy[k], vis, ct);        
    }
};
```