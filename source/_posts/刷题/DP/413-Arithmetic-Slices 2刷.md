---
title: 413. Arithmetic Slices 2刷
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-12-07 09:35:30
---




## [413. Arithmetic Slices](https://leetcode-cn.com/problems/arithmetic-slices/)



## 思路：

1. dp[i]以数字ith为结尾的最长arithmetic sequence的长度，（被包含的dp[k]==0）
2. $dp[i]$以数字i th为结尾的arithmetic sequence的数目个数。

<!-- more -->

## 代码：



```c++
class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& A) {
        int  n = A.size();
        vector<int> dp(n, 0);
        if(n < 2) return 0;
        for(int i = 2; i < n; ++i){
            if(A[i - 1] - A[i - 2] == A[i] - A[i - 1]){
                dp[i] = dp[i - 1] + 1; 
                dp[i - 1] = 0;                
            }//
        }
        int res = 0;
        for(int i = 2; i < n; ++i){
            if(dp[i]){
                res += (dp[i] +  1) * dp[i] / 2;
            }
        }
        return res;
    }
};
```

也可以直接加

```c++
class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& A) {
        // vector<int> dp(A.size(), 0);
        int sum = 0, lsum = 0;
        
        for(int i = 2; i < A.size(); i++){
            if(A[i] - A[i - 1] == A[i - 1] - A[i - 2]){                
                lsum++;//长度为3，4，……，lsum的以A[i]为结尾的arithmetic sequence
                sum += lsum;
            }else lsum  = 0;
// 
        }
        return sum;
    }
};


```