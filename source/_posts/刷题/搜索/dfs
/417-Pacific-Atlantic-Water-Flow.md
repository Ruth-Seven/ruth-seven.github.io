---
title: 417. Pacific Atlantic Water Flow
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-11-24 10:15:40
---

## [417. Pacific Atlantic Water Flow](https://leetcode-cn.com/problems/pacific-atlantic-water-flow/)

## 思路：

按着题目的意思顺着流向DFS有以下问题。做了正向的代码发现有个DFS依赖问题。

网上大神给出了**[逆流](https://leetcode-cn.com/problems/pacific-atlantic-water-flow/solution/shen-du-sou-suo-dfs-by-jawhiow/)**DFS的思路。

<!-- more -->

## 代码：

```c++
class Solution {
public:
    int dx[4] = {-1, 1, 0, 0};
    int dy[4] = {0, 0, -1, 1};
    int m, n;
    // 顺流dfs搜索得色5re'rs'ze'd [re'rong'ze'dui]
    // 回流依赖问题： when height[x, y] == height[nx, ny] : 
    // type[x ,y] => type[dx, dy], type[dx ,dy] => type[x, y] , 同时DFS式的遍历方式保证了了每个
    // 节点只被访问一次，所以存在类型相互依赖关系
    // 即存在一个鸡生蛋，蛋生鸡的问题。
    // 解决方法是：没想出来
    int flow(vector<vector<int>> &matrix, vector<vector<int>> &type,  int x, int y){
        // cout << x << y << endl;
        if(x < 0 || y < 0 ) return -1;
        else if( x >= m || y >= n) return -2;

        if(type[x][y] != 0) return type[x][y];
        type[x][y] = 4; // the visited point.
        
        int nx, ny, f1 = 0, f2 = 0, t = 0; //bugs: initailization: flag = 1;
        for(int i = 0; i < 4; ++i){
            nx = x + dx[i];
            ny = y + dy[i];            
            if( (nx < 0 || ny < 0) || (nx >= m || ny >= n) ||  matrix[nx][ny] <= matrix[x][y]){ //bugs: nx, ny
                
                t = flow(matrix, type, nx, ny);                
                if(t == -1 || t == 1 || t == 3) f1 = 1;
                if(t == -2 || t == 2 || t == 3) f2 = 1;
            }
        }
        if(f1 & f2) type[x][y] = 3;
        else if(f1) type[x][y] = 1;
        else if(f2) type[x][y] = 2;
        // type[x][y] = f1 & f2; // bugs 1 & 1
        return type[x][y];
    }

    int flow2(vector<vector<int>> &matrix, vector<vector<int>> &type,  int x, int y){
        // cout << x << y << endl;
        if(x < 0 || y < 0 ) return -1;
        else if( x >= m || y >= n) return -2;

        int nx, ny, f1 = 0, f2 = 0, t = 0; //bugs: initailization: flag = 1;
        for(int i = 0; i < 4; ++i){
            nx = x + dx[i];
            ny = y + dy[i];            
            if( (nx < 0 || ny < 0) || (nx >= m || ny >= n) ||  matrix[nx][ny] <= matrix[x][y]){ //bugs: nx, ny
                
                t = flow(matrix, type, nx, ny);                
                if(t == -1 || t == 1 || t == 3) f1 = 1;
                if(t == -2 || t == 2 || t == 3) f2 = 1;
            }
        }
        if(f1 & f2) type[x][y] = 3;
        else if(f1) type[x][y] = 1;
        else if(f2) type[x][y] = 2;
        // type[x][y] = f1 & f2; // bugs 1 & 2 ： 1 | 2
        return type[x][y];
    }

    // 题解：逆流写法
    void reflow(vector<vector<int>> &matrix, vector<vector<int>> &type,  int x, int y, int wtype){
        type[x][y] = type[x][y] | wtype;
        int nx, ny;
        for(int i = 0; i < 4; ++i){
            nx = x + dx[i];
            ny = y + dy[i];
            if(nx >=0 && ny >= 0 && nx < m && ny < n)
            if(matrix[x][y] <= matrix[nx][ny] && ((type[nx][ny] & wtype) == 0))
                reflow(matrix, type, nx, ny, wtype);
        }
    }

    vector<vector<int>> pacificAtlantic(vector<vector<int>>& matrix) {
        m = matrix.size();
        if(m == 0) return matrix; //return empty vector;
        n = matrix[0].size();
        vector< vector<int>> type(m, vector<int>(n, 0)), ans;   

        for(int i = 0; i < m; ++i){
            reflow(matrix, type, i, 0, 1);
            reflow(matrix, type, i, n - 1, 2);
        }
        for(int i = 0; i < n; ++i){
            reflow(matrix, type, 0, i, 1);
            reflow(matrix, type, m - 1, i, 2);
        }

                     
        for(int i = 0; i < m; ++i){
            for(int j = 0; j < n; ++j){       
                // cout << i << ' ' << j << ' ' << type[i][j] << endl;         
                if(type[i][j] == 3){
                    ans.emplace_back( vector<int>({i, j}));  // bugs initialize vector<int> a(n, i)  
                }
            }
        }
        return ans;

    }
};
```