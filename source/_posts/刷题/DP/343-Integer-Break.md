---
title: 343. Integer Break
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-12-29 09:07:08
---





## [343. Integer Break](https://leetcode-cn.com/problems/integer-break/)

## 思路：

1. dp分解为两个和为n数字，求出最大积即可。

2. [数学方法题解](https://leetcode-cn.com/problems/integer-break/solution/zheng-shu-chai-fen-by-leetcode-solution/)

   <!-- more -->

## 代码：

```c++
class Solution {
public:
    vector<int> dp;
    int getmaxdp(int k){
        if(dp[k]) return dp[k];
        int maxp = 0;
        for(int i  = 1;i <= k / 2 ; i++){
            maxp = max(maxp, max(i, getmaxdp(i)) 
            * max(k - i, getmaxdp(k - i)));
            
        }
        dp[k] = maxp;
        return maxp;
    }

    int integerBreak(int n) {
        dp.resize(60);
        dp[1] = 1;
        dp[2] = 1;
        return getmaxdp(n);
    }
};
```

更简洁的拆分方法

```c++
class Solution {
public:
    vector<int> dp;
    int getmaxdp(int k){
        if(dp[k]) return dp[k];
        int maxp = 0;
        for(int i  = 1;i < k ; i++){
            maxp = max(maxp, max(i * (k - i), i * getmaxdp(k - i))); // 拆出一个整数作为因子
        }
        dp[k] = maxp;
        return maxp;
    }

    int integerBreak(int n) {
        dp.resize(60);
        dp[1] = 1;
        dp[2] = 1;
        return getmaxdp(n);
    }
};
```

正向dp

```c++
class Solution {
public:

    int integerBreak(int n) {
        vector<int> dp(60);
        dp[1] = 1;
        dp[2] = 1;
        for(int i = 3; i <= n; ++i){
            int cur = 1;
            for(int j = 1; j < i; ++j){
                cur = max(cur, max(j * (i - j), j * dp[i - j]));
            }
            dp[i] = cur;
        }
        return dp[n];
    }
};
```

数学方法

```c++
class Solution {
public:

    int integerBreak(int n) {
        if(n < 4) return n - 1; // 2:1, 3:2
        int res = 1;
        while(n > 4){ // 尽量取3为分解因子
            res *= 3;
            n -= 3;
        }
        if(n == 4) res *= 4; // n % 3 == 1, 取一个4作为分解因子
        else res *= n;
        return res;
    }
};
```