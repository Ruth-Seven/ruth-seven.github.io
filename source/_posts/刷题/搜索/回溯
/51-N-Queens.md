---
title: 51. N-Queens
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-11-27 09:21:27
---



## [51. N-Queens](https://leetcode-cn.com/problems/n-queens/)

## 思路:

八皇后问题，经典问题。回溯解决。

## 代码：

```c++
class Solution {
public:
    
    void generate(vector<vector<string>> &outs, vector<int> &chess, vector<int> &hashorpos, int depth, int n){
        if(n == depth){
            
            vector<string> res(n, string(n, '.'));
            for(int i = 0; i < n; ++i){
                res[i].replace(chess[i], 1, "Q"); 
                //  cout << chess[i] << ' ' ;
            }
            // cout << endl;
            outs.emplace_back(res);
            return;
        }
    
        for(int i = 0; i < n; ++i){
            int flag = 1;
            if(!hashorpos[i]){
                #这部分判断代码可以优化，但是很麻烦，可以用hasverpos代表一层中被禁止的位置,需要标记左右方向，很麻烦。考虑到n的数量直接遍历就行，可以当做一个不变量。
                for(int j = 1; j <= depth ; ++j){
                    if(chess[depth - j] == i - j || chess[depth - j] == i + j){
                        flag = 0;
                        break;
                    }                                        
                }
                if(!flag) continue;

                chess[depth] = i;
                hashorpos[i] = 1;
                
                generate(outs, chess, hashorpos, depth + 1, n);
                                
                chess[depth] = -1;
                hashorpos[i] = 0;
                
            }
        }
    }
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> outs;
        vector<int> chess(n, -1), hashorpos(n, 0);
        generate(outs, chess, hashorpos, 0, n);
        return outs;
    }
};
```