---
title: 1411. Number of Ways to Paint N × 3 Grid
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-09-27 14:39:28
---

#### [1411. Number of Ways to Paint N × 3 Grid](https://leetcode-cn.com/problems/number-of-ways-to-paint-n-x-3-grid/)

<!-- more -->

题目不难，但是因为一个**累加的初始化的小bug**没有找出来而浪费了好多时间！

## 思路：

先遍历寻找可以叠放的图块，然后dp数量即可，空间状态可压缩。注意，每次dp数组后初始化问题。

当然这里也可以看成矩阵乘法。

官网的另一中解法涉及到[线性递推式的优化](https://leetcode-cn.com/problems/number-of-ways-to-paint-n-x-3-grid/solution/gei-n-x-3-wang-ge-tu-tu-se-de-fang-an-shu-by-leetc/)。

## 代码：

```c++
class Solution {
public:
    int numOfWays(int n) {
        int cmap[13][13] ={0};
        int posidx = 1;
        map<int, int> pos;
        for(int i = 0; i < 3; i++){
            for(int j = 0; j < 3; j++){
                for(int k = 0; k < 3; k++){
                    if(i == j || j == k) continue;
                    int countR = i * 100 + j * 10 + k;
                    if(pos[countR] == 0)
                        pos[countR] = posidx++;   
                    for(int s = 0; s < 3; s++){
                        for(int t = 0; t < 3; t++){
                            for(int q = 0; q < 3; q++){
                                if(s == t || t == q) continue;
                                int countC = s * 100 + t * 10 + q;
                                if(pos[countC] == 0)
                                    pos[countC] = posidx++;
                                if(i == s || j == t || k == q) continue;
                                cmap[pos[countR] - 1][pos[countC] - 1] = 1;
                            
                            }
                        }
                    }
                }
            }
        }
        cout << posidx << endl;
//          for(int i = 0; i < 12; i++) {
//               for(int j = 0; j < 12; j++)
//                 cout << cmap[i][j] << ' ';
//                 cout << endl;
//         }
        
        long long dp[2][12] = {0};
        long long MOD = 1e9 + 7;
        for(int i = 0; i < 12; i++) dp[0][i] = 1;
        for(int i = 1; i < n; i++){
            int newr = i & 1;
            int lastr = (i - 1) & 1;
            for(int j = 0; j < 12; j++){
                dp[newr][j] = 0;
                for(int k = 0; k < 12; k++)
                    if(cmap[j][k] == 1){
                        dp[newr][j] = (dp[newr][j] + dp[lastr][k]) % MOD; 
                    }
            }
//               for(int t = 0; t < 12; t++)
//                 cout << dp[newr][t] << ' ';
//                 cout << endl;            
        }
        long long  sum = 0;
        int newr = (n - 1) & 1;
        for(int i = 0; i < 12; i++){
            sum = (sum + dp[newr][i]) % MOD;
        }
        return sum;
    }
};

```

