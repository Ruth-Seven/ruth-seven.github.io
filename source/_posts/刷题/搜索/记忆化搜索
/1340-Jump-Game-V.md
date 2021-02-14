---
title: 1340. Jump Game V
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-10-05 11:04:43
---
这个题目还是蛮入门的……
## 思路：

这题如果采用DP的思想去做，很难。第一，如果设$dp[t][i]$为第i个数字为终点,最多移动t步的情况下最大经过的数字个数，那么DP转移方程就涉及到搜索上一层合理数字，复杂度大增（离线可计算，但是还是不快）。

> 后面给的第二种算法就是该版本。

第二，如果$dp[t][i]$为第i个数字为起点,最多走t步的最大经过的数字个数，虽然由于顺着题目的意思，相比上一种方法减少了搜索上一层的合理数字，但还是不够快。可以从DP版本1中看出来，许多状态转移的计算都是无谓的。时间复杂度为$O(N^2D)$，即使有一点点剪枝也没法AC。

第三，通过记忆化搜索的方法，可以大幅减少重复计算。  





<!-- more -->



## 代码：



```c++
class Solution {
public:
    // f[i]:从i开始最多可以visit的数字
    vector<int> f;

    void dfs(vector<int> &arr, int id, int d, int n){
        if(f[id] != -1) return;
        f[id] = 1;        
        for(int i = id + 1; i < id + d + 1 && i < n && arr[id] > arr[i]; i++){
            dfs(arr, i, d, n);
            f[id] = max(f[id], f[i] + 1);
        }
            
        for(int i = id - 1; i > id - d - 1 && i >= 0 && arr[id] > arr[i]; i--){
            dfs(arr, i, d, n);        
            f[id] = max(f[id], f[i] + 1);
        }            
    }
    int maxJumps(vector<int>& arr, int d) {
        int len = arr.size();
        f.resize(len, -1);
        
        for(int i = 0;i < len; i++){
            dfs(arr, i, d ,len);        
        }
        return *max_element(f.begin(), f.end());
    }
};
```

DP版本1：

```c++

class Solution {
public:
    int maxJumps(vector<int>& arr, int d) {
        int len = arr.size();
        vector<int> dp[2];
        dp[0].resize(len, 1);
        dp[1].resize(len, 0);
        int maxstep = 0, flag = 1;
        int newl = 0, oldl = 1;
        while(flag){
            flag = 0;    
            swap(newl, oldl);

            for(int i = 0; i < len; i++){
                for(int j = i + 1; j < d + i + 1 && j < len && arr[j] < arr[i]; ++j){
                    int newv = dp[oldl][j] + 1;
                    if(newv > dp[newl][i]){
                        dp[newl][i] = newv;
                        flag = 1;
                    }                    
                }
                for(int j = i - 1; j > i - d - 1 && j >= 0 && arr[j] < arr[i]; --j){
                    int newv = dp[oldl][j] + 1;
                    if(newv > dp[newl][i]){
                        dp[newl][i] = newv;
                        flag = 1;
                    }                    
                }                
            }
        }
        int v = -1;
        // for(int i = 0; i < len; ++i)
        //     v = max(v, dp[newl][i]);
        for(int i = 0; i < len; ++i)
            v = max(v, dp[oldl][i]);
        
        return v;
    }
};
```



DP版本2：

```c++

class Solution {
public:
    int maxJumps(vector<int>& arr, int d) {
        int len = arr.size();
        vector<vector<int> > dp(2, vector<int>(len, 0));
        vector<vector<int> > bigger(len,vector<int>(0,0));
        vector<int> ischanged(len, 1);
        for(int i = 0;i < len; i++){
            int low = max(0, i - d);
            int high = min(len - 1, i + d);
            for(int j = i - 1; j >= low; j--)
                if(arr[i] > arr[j]) bigger[j].push_back(i);
                else break;
            
            for(int j = i + 1; j <= high; j++)
                if(arr[i] > arr[j]) bigger[j].push_back(i);
                else break;                 
        }


        int maxstep = 0, flag = 1;
        int newl = 0, oldl = 1;
        while(flag){
            flag = 0;    
            swap(newl, oldl);

            for(int i = 0; i < len; i++){
                if(ischanged[i] == 0) continue;
                ischanged[i] = 0;
                for(int j = 0; j < bigger[i].size(); j++){
                    int newv = dp[oldl][bigger[i][j]] + 1;
                    if(newv > dp[newl][i]){
                        dp[newl][i] = newv;
                        flag = 1;
                        ischanged[i] = 1;
                    }
                    // dp[newl][i] = max(dp[newl][i], dp[oldl][bigger[i][j]] + 1);                    
                }
                maxstep = max(dp[newl][i], maxstep);
            }
        }

        return maxstep + 1;
    }
};
```

