---
title: 48. Rotate Image
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2021-01-22 11:31:37
---



## [48. Rotate Image](https://leetcode-cn.com/problems/rotate-image/)



## 思路：



原地翻转的思路：比较简单。

1. 翻转做法。先上下翻转， 后对角线翻转
2. 四个对应的矩阵元素作为旋转点，顺势将矩阵划分为四个旋转部分。遍历一个部分并旋转其中成组的所有元素即可。

<!-- more -->

## 代码：



沙雕代码：

```c++
class Solution {
public:

    void rotate_ele(int x, int y, vector<vector<int>> &matrix){
        int n = matrix.size() - 1;
        vector<pair<int, int>>  idx;
        idx.push_back({x, y});
        idx.push_back({y, n - x});
        idx.push_back({n - x, n- y});
        idx.push_back({n- y, x});
        int ordv = matrix[idx[0].first][idx[0].second];
        for(int i = 0; i < 4; ++i){
            int bi = (i + 1) % 4;
            int &rotated = matrix[idx[bi].first][idx[bi].second]; // alias;
            int newv = rotated;
            rotated = ordv;
            ordv = newv;
        }
        // for(int i = 0; i < n + 1; ++i){
        //     for(int j = 0; j < n + 1; ++j){
        //         cout << matrix[i][j] << " ";                
        //     }
        //     cout << endl;
        // }
    
    }
    //发现旋转规律
    // 1, 0 
    // 0, 2
    // 2, 3
    // 3, 1

    // 0, 0
    // 0, 3
    // 3, 3
    // 3, 0
    void rotate(vector<vector<int>>& matrix) {
        if(matrix.size() == 0) return;
        int cerX, cerY; 
        cerX = cerY = (matrix.size() - 1) / 2; // 中间数下标
        
        //划分旋转点
        // 按一个点旋转对应的4个点，组成一组进行旋转。各个组的旋转起点如下：
        //  1 1 1 0
        //  0 1 0 0 
        //  0 0 0 0
        //  0 0 0 0 

        // 1 1 0 
        // 0 1 0
        // 0 0 0
        for(int i = 0; i <= cerX; ++i){
            for(int j = i; j < matrix.size() - 1 - i; ++j){                
                rotate_ele(i, j, matrix);
            }            
        }
    }
};
```



简化一下

```c++


class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        if(matrix.size() == 0) return;
        int cerX, cerY, n = matrix.size() - 1; 
        cerX = cerY = (matrix.size() - 1) / 2; // 中间数下标
        
        for(int i = 0; i <= cerX; ++i){
            for(int j = i; j < matrix.size() - 1 - i; ++j){                
                int temp = matrix[i][j];
                matrix[i][j] = matrix[n - j][i];
                matrix[n - j][i] = matrix[n - i][n - j];
                matrix[n - i][n - j] = matrix[j][n - i];
                matrix[j][n - i] = temp;
            }            
        }
    }
};
```



翻转做法

```c++
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        if(matrix.size() == 0) return;
        int cerX, cerY, n = matrix.size() - 1; 
        cerX = cerY = (matrix.size() - 1) / 2; // 中间数下标
		// 上下翻转        
        for(int i = 0; i <= cerX; ++i){
            for(int j = 0; j < matrix.size(); ++j){                
                swap(matrix[i][j], matrix[n - i][j]);
            }            
        }
		// 对角线翻转
        for(int i = 0; i <= matrix.size(); ++i){
            for(int j = i + 1; j < matrix.size(); ++j){                
                swap(matrix[i][j], matrix[j][i]);
            }            
        }
    }
};
```