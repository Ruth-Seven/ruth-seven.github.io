---
title: 413. Arithmetic Slices
thumbnail: 'http://static.come2rss.xyz/北大西洋的大青鲨.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-09-28 08:02:55
---





#### [413. Arithmetic Slices](https://leetcode-cn.com/problems/arithmetic-slices/)

题目简单，倒是遇到一个bug：new一个size==0的数组会越界错误。

<!-- more -->

ez



## 思路：

dp[i]表示以i为终点的arthmetic array的数量。

## 代码：

```c++
class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& A) {
        int *dp = new int[0];
        int sum = 0;
        memset(dp, 0, sizeof(dp));
        for(int i = 2; i < A.size(); i++){
            if(A[i] - A[i - 1] == A[i - 1] - A[i - 2]){
                dp[i] = dp[i - 1] + 1;                
                sum += dp[i];
            }
        }
        return sum;
    }
};


// 3: 1
// 4: 2 + 1  = 3
// 5: 3 + 2 + 1 =6;
```

优化空间。

```c++
class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& A) {
        // vector<int> dp(A.size(), 0);
        int sum = 0, lsum = 0;
        
        for(int i = 2; i < A.size(); i++){
            if(A[i] - A[i - 1] == A[i - 1] - A[i - 2]){                
                lsum++;
                sum += lsum;
            }else lsum  = 0;
// 
        }
        return sum;
    }
};


// 3: 1
// 4: 2 + 1  = 3
// 5: 3 + 2 + 1 =6;


```

