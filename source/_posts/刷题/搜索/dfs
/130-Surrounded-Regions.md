---
title: 130. Surrounded Regions
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-12-01 08:23:07
---





## [130. Surrounded Regions](https://leetcode-cn.com/problems/surrounded-regions/)



## 思路：

如果用普通dfs搜索所有区域是速度有点慢的。

但只是反过来思考，如果只所搜索所有不被包围的`O`并标记，同时翻转所有剩下的`X`，最后把所有的P翻转回来是不是会更快。

> 不搞特例的话，一般都是后者快。

<!-- more -->

## 代码：

```c++
class Solution {
public:

    int n, m;
    int dx[4] = {-1, 1, 0, 0};
    int dy[4] = {0, 0, -1, 1};

    void fill(vector<vector<char>>& board, vector<vector<bool>>& vis,vector<pair<int, int>> &path, 
                int &isea, int x , int y){
        // cout << x << ' ' << y << endl;
        vis[x][y] = 1;
        path.push_back(make_pair(x, y));

        for(int i = 0; i < 4; ++i){
            int nx = x + dx[i];
            int ny = y + dy[i];
            if(nx < 0 || ny < 0 || nx >= n || ny >= m){
                isea = 1;
                continue;
            }                
            if(!vis[nx][ny] && board[nx][ny] == 'O'){
                fill(board, vis, path, isea, nx, ny);
            }                        
        }
    }

    void solve(vector<vector<char>>& board) {
        n = board.size();
        if(n == 0) return;
        m = board[0].size();
        vector<vector<bool>> vis(n, vector<bool>(m, false));
        
        for(int i = 0; i < n; ++i){
            for(int j = 0;j < m; ++j){                
                if(!vis[i][j] && board[i][j] == 'O'){
                    vector<pair<int, int>> path;
                    int isea = 0;
                    fill(board, vis, path, isea, i, j);
                    if(isea) continue; // bugs: forgets to clear path
                    for(auto p : path){
                        board[p.first][p.second] = 'X';                        
                    }
                    
                }
            }
        }    
    }
};
```





16ms范例



```C++
class Solution {
public:
    void solve(vector<vector<char>>& board) {
        // 给出一个二维数组，找到被 x 包围的 o，然后将其转换为x
        // dfs
        if(board.empty())
            return;
        int m = board.size(), n = board[0].size();
        if (m == 1 || n == 1)
            return ;
        // 反过来思考，只改变和边界直接相连的元素
        // 首先检查第一行和最后一行的 O
        for(int i = 0;i<m;i+=m-1)
            for(int j = 0;j<n;j++)
                if(board[i][j] == 'O')
                    dfs(board,i,j,m,n);
        // 再检查第一列和最后一列的 O
        for(int j = 0;j<n;j+=n-1)
            for(int i = 0;i<m;i++)
                if(board[i][j] == 'O')
                    dfs(board,i,j,m,n);
        // 将 board 中的 O 改为 X
        // 再将 board 中的 P 改为 O
        for (auto &i:board)
            replace(i.begin(),i.end(),'O','X');
        for (auto &i:board)
            replace(i.begin(),i.end(),'P','O');
    }

    void dfs(vector<vector<char>>&board,int i, int j,int m, int n)
    {
        if(i>=0 && i<m && j>=0 && j<n && board[i][j] == 'O')
        {
            board[i][j] = 'P';
            dfs(board,i+1,j,m,n);
            dfs(board,i,j+1,m,n);
            dfs(board,i-1,j,m,n);
            dfs(board,i,j-1,m,n);
        }
    }

};
```