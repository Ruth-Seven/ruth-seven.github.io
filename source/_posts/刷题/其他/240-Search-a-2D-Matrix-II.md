---
title: 240. Search a 2D Matrix II
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2021-01-22 11:31:54
---




## [240. Search a 2D Matrix II](https://leetcode-cn.com/problems/search-a-2d-matrix-ii/)



## 思路：

由于matrix在行和列上的递增， 在左下角和右上角有特殊的性质。在左下角有，`A[i][j]`比上面的数字都打， 比右边的数字都小。所以可以比较`target`和`A[i][j]`数字大小来排除，上面一列或者右边一行的所有数字。递归的下去可以搜索到应有的数字。

如果没有就会出界。
<!-- more -->

## 代码：

```c++
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int x, y, n = matrix.size();
        x = n - 1; 
        y = 0;
        while(x != 0 || y != n -1){
            if(target == matrix[x][y]) return true;
            else if(target > matrix[x][y]) y++;
            else if(target < matrix[x][y]) x--;
            if(x < 0 || y >= n) return false;
        }
        return false;
    }
};
```