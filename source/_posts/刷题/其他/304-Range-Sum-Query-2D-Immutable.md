---
title: 304. Range Sum Query 2D - Immutable
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
date: 2021-01-29 11:47:00
tags:
categories:
---





## [304. Range Sum Query 2D - Immutable](https://leetcode-cn.com/problems/range-sum-query-2d-immutable/)



## 思路：

二维前缀和，不仅是计算二维矩阵之和的过程可以用二维矩阵组合起来，而且二维前缀和的计算过程也可以用之前计算的矩阵简化计算。

$o(n^2)$

<!-- more -->

## 代码：





```c++

class NumMatrix {
    vector<vector<int>> summax;
public:
    NumMatrix(vector<vector<int>>& matrix) {
        int n = matrix.size() + 1;
        if(n == 1) return;
        int m = matrix[0].size() + 1;
        summax.resize(n);
        summax[0].resize(m);
        
        for(int i = 1; i < n; ++i){
            summax[i].resize(m + 1);
            for(int j = 1; j < m; ++j){
                summax[i][j] = matrix[i - 1][j - 1] + summax[i - 1][j] + summax[i][j - 1] - summax[i - 1][j - 1];   
                // cout << summax[i][j] << ' ';
            }
            // cout << endl;
        }
    }
    
    int sumRegion(int row1, int col1, int row2, int col2) {                
        return summax[row2 + 1][col2 + 1] -  summax[row2 + 1][col1] -  summax[row1][col2 + 1] +  summax[row1][col1];
        // return 0;
    }
};

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix* obj = new NumMatrix(matrix);
 * int param_1 = obj->sumRegion(row1,col1,row2,col2);
 */
```