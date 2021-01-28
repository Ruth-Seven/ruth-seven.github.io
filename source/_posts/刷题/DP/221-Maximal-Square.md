---
title: 221. Maximal Square
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-12-09 14:31:26
---







## [221. Maximal Square](https://leetcode-cn.com/problems/maximal-square/)

## 思路：

$dp[i][j]$为正方形的右下角。根据行列扩展或者三个正方形可以进行dp。

<!-- more -->

## 代码：



思考不成熟的代码

15%

```c++

class Solution {
public:

    int maximalSquare(vector<vector<char>>& matrix) {
        int n = matrix.size();
        if(n == 0) return 0;
        int m = matrix[0].size();
        vector<vector<int>> row(n, vector<int>(m, 0));
        vector<vector<int>> col(n, vector<int>(m, 0));
        vector<vector<int>> squ(n, vector<int>(m, 0));
        int maxarea = 0;
        for(int i = 0;i < n; ++i){
            for(int j = 0; j < m; ++j){
                if(matrix[i][j] == '1'){                    
                    row[i][j] = (i == 0) ? 1 : row[i - 1][j] + 1;
                    col[i][j] = (j == 0) ? 1 : col[i][j - 1] + 1;
                    int minsqu;
                    if(i == 0 || j == 0 ) minsqu = 0;
                    else minsqu = squ[i - 1][j - 1];

                    int maxl = min(col[i][j], min(row[i][j], minsqu + 1));
                    squ[i][j] = maxl;
                    maxarea = max(maxarea, maxl * maxl);                
                }else{
                    row[i][j] = col[i][j] = squ[i][j] = 0;
                }
                // cout << i  << " " << j << squ[i][j] << endl;
            }
        }
        return maxarea;
    }
};
```



真滴懒，再懒不能懒脑力。

24%

```c++
class Solution {
public:

    int maximalSquare(vector<vector<char>>& matrix) {
        int n = matrix.size();
        if(n == 0) return 0;
        int m = matrix[0].size();
        vector<vector<int>> squ(n, vector<int>(m, 0));
        int maxarea = 1;
        
        for(int i = 0;i < n; ++i){
            if(matrix[i][0] == '1') squ[i][0] = 1;
            if(matrix[0][i] == '1') squ[0][i] = 1;
        }
        
        for(int i = 1;i < n; ++i){
            for(int j = 1; j < m; ++j){
                if(matrix[i][j] == '1'){                                 
                    int maxl = min(squ[i - 1][j - 1], min(squ[i - 1][j], squ[i][j - 1])) + 1;
                    squ[i][j] = maxl;
                    maxarea = max(maxarea, maxl * maxl);                
                }else{
                    squ[i][j] = 0;
                }
                // cout << i  << " " << j << squ[i][j] << endl;
            }
        }
        return maxarea;
    }
};
```

优化时间

98%

```c++
class Solution {
public:

    int maximalSquare(vector<vector<char>>& matrix) {
        if(matrix.empty()) return 0;
        int n = matrix.size();        
        int m = matrix[0].size();
        vector<vector<int>> squ(n, vector<int>(m, 0));
        int maxl = 0;        
        for(int i = 0;i < n; ++i){
            for(int j = 0; j < m; ++j){
                if(matrix[i][j] == '1'){                                 
                   if(i > 0 && j > 0){                        
                        squ[i][j] = min(squ[i - 1][j - 1], min(squ[i - 1][j], squ[i][j - 1])) + 1;
                   }
                   else squ[i][j] = 1;
                   if(squ[i][j] >  maxl )
                        maxl = squ[i][j];
                }
            }
        }
        return maxl * maxl;
    }
};
```

