---
title: 1289.Minimum Falling Path Sum2
thumbnail: 'http://static.come2rss.xyz/南京玄武湖.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-09-23 09:58:21
---





<!-- more -->

## [1289. Minimum Falling Path Sum II](https://leetcode-cn.com/problems/minimum-falling-path-sum-ii/)



## 思路：

这题比较简单，dp做就行。

寻找最小值的时候可以直接记录，或者用堆记录前2个最小值，从而快速dp。而记录的同时可以发现，之前多余dp信息无需存储，所以可以把空间复杂度从$O(n)$降到$O(1)$。

## 代码：

```C++
class Solution {
public:

    int minFallingPathSum(vector<vector<int>>& arr) {
        int dp[2][300] = {0};
        int minp[300];
        int len = arr.size();
        priority_queue<int, vector<int>, less<int>> pq;
       
        //init
        for(int i = 0; i < len; i++){
            dp[0][i] = arr[0][i];
            if(pq.size() < 2) pq.push(arr[0][i]);
            else if(pq.top() > arr[0][i]){
                pq.pop();
                pq.push(arr[0][i]);
            }
        }

        //dp
        for(int i = 1; i < len; i++){
            int nowr = i & 1;
            int lastr = (i - 1) & 1;
            
            int min2 = pq.top(); pq.pop();
            int min1 = pq.top(); pq.pop();
            for(int j = 0; j < len; j++){            
                if(min1 == dp[lastr][j])   
                    dp[nowr][j] = min2 + arr[i][j];
                else dp[nowr][j] = min1 + arr[i][j];
                if(pq.size() < 2){
                    pq.push(dp[nowr][j]);
                }
                else if(dp[nowr][j] < pq.top()){
                    pq.pop();
                    pq.push(dp[nowr][j]);
                }   
            }    
        }

        pq.pop();
        return pq.top();
    }
};
```

