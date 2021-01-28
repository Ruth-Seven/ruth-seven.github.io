---
title: 面试题-回溯DFs
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
categories:
date: 2020-08-07 13:29:35
tags:
---

<!-- more -->

收集回溯相关题目



## 面13

> 面12和13很相似，不重复写了。

### 题面：

在一个字符矩阵中寻找一条路径，路径上的字符从头到尾排列起来是给定的字符串`s`。判断有无这么一条路径。

### 思路：

DFS或者说和回朔直接暴力搜。

### 代码：

```
bool hasPathCore(char *matrix, int rows, int cols, int row, int col, char *str, int strIdx, int &isFound){
    if(strIdx < 0){
        isFound = 1;
        return true;
    }
    if(isFound) return true;
    
    visited[row * cols + col] = 1;
    int dX[] = {0, 0, -1, 1}, dY[] = {-1, 1, 0, 0};
    for(int i = 0; i < 4; ++i){
		int nX = dX[i] + row, nY = dY[i] + col, p = row * cols + col;
        if( nX >= 0 && nY >= 0 && nX < rows && nY < cols && !visited[p] && str[strIdx] ==  matrix[p])
            hashPathCore(matrix, rows, cols, row, col, str, strIdx - 1);        
    }
}

bool hasPath(char *matrix, int rows, int cols, char *str, int length){
	if(str == nullptr || matrix == nullptr)
        throw new std::exception("Invalid parameters.");
    int visited = new int[rows * cols], isFound = 0;
    memset(visited, 0, sizeof(visited));
    for(int i = 0; i < rows; ++i)
        for(int j = 0; j < cols; ++j)
            if( hasPathCore(matrix, rows, cols, i, j, str, length - 1, isFound)){//倒着搜    
            	del[] visited;            
                return true;    
            }
}
```