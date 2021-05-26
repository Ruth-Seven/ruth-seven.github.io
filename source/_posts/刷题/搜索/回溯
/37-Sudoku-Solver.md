---
title: 37. Sudoku Solver
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-12-05 10:00:30
---






## [37. Sudoku Solver](https://leetcode-cn.com/problems/sudoku-solver/)



## 思路：

dfs搜索，可以用位运算优化，懒得看了

<!-- more -->

## 代码：

```c++
class Solution {

public:
    vector<vector<int>> col, row, cell;
    vector<pair<int, int>> blank;
    // int dx[4] = {0, 0, -1, 1};
    // int dy[4] = {-1, 1, 0, 0};
    int n;
    int flag  = 0;
    int getC(int x, int y){
        return (x / 3) * 3 + y / 3;
    }
    void solveSudoku(vector<vector<char>>& board) {
        n = board.size();
        row = cell = col = vector<vector<int>>(n, vector<int>(n + 1, 0)); //bugs: num -> idx
        // cout << row[0][0];
        for(int i = 0; i < n; ++i){
            for(int j = 0; j < n; ++j){
                if(board[i][j] == '.') {
                    blank.push_back(make_pair(i, j));
                    continue;
                }
                int t = board[i][j] - '0';                
                row[i][t] = 1;
                col[j][t] = 1;
                cell[getC(i, j)][t] = 1;
                
            }
        }
        dfs(board, 0);
    }
    
    void dfs(vector<vector<char>> &board, int pos){
        // cout << pos << ' ' << flag << " " << blank.size() << endl;
        if(flag || pos == blank.size()){
            flag = 1;
            return;
        }
        int x = blank[pos].first;
        int y = blank[pos].second;
        // cout << x << ' ' << y << endl;
        if(board[x][y] == '.'){
            for(int i = 1; i <= 9; ++i){
                if(!row[x][i] && !col[y][i] && !cell[getC(x, y)][i]){
                    // cout << i << "@" << endl;
                    row[x][i] = 1;
                    col[y][i] = 1;
                    cell[getC(x, y)][i] = 1;
                    board[x][y] = i + '0';
                    dfs(board, pos + 1);
                    if(flag) return;
                    row[x][i] = 0;
                    col[y][i] = 0;
                    cell[getC(x, y)][i] = 0;
                    board[x][y] = '.';
                }
            }
        }

    }
};
```