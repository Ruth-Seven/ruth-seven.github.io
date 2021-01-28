---
title: 790. Domino and Tromino Tiling
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-10-07 11:26:39
---

这题真的需要很多考虑

<!-- more -->

### 思路：

### DP

可以进行bit dp，设置`dp[status]`为当前列为状态`status`时的拼接方法。

```c++
status = 0b00 : 上下格子都为空
status = 0b10 : 上格子填好，下格子为空
status = 0b01 : 下格子填好，上格子为空
status = 0b11 : 上下格子都填好
```

所以就是有以下DP方程转移方式：

![img](http://static.come2rss.xyz/possible.png)

注意`dp[0]=0`。



### 找规律

另一种方法也是我一开始想的方法，不过想错了，没有考虑托米诺和多米诺无限增长的可能性。😑🤐



参考以为大佬的[博文](https://blog.csdn.net/ccnuacmhdu/article/details/103412944)

![img](http://static.come2rss.xyz/20191208142123502.png)





## 代码：

### DP

```c++
class Solution {
public:
    int numTilings(int N) {
        const int MOD = 1e9 + 7;
        // int[] dp= new int[]{1,0,0,0};
        long  *dp = new long[]{1, 0, 0, 0};
        for(int i = 0; i < N; ++i){
            long *ndp = new long[4];
            ndp[0b00] = (dp[0b00] + dp[0b11]) % MOD;
            ndp[0b01] = (dp[0b00] + dp[0b10]) % MOD;
            ndp[0b10] = (dp[0b01] + dp[0b00]) % MOD;
            ndp[0b11] = (dp[0b00] + dp[0b01] + dp[0b10]) %  MOD;
            delete []dp;
            dp = ndp;
        }   

        return dp[0];


    }
};
```

另外上述线性变换可以替换为矩阵乘法的变换形式，不过太稀疏了……

### 找规律：

```C++

class Solution {
public:
    int numTilings(int N) {
        const int MOD = 1e9 + 7;
        int sum0 = 1, sum1 = 1, sum2 = 2, sum3 = 5, sum;
        for(int i = 4; i <= N; ++i){
            sum = ((sum3 * 2) % MOD + sum1) % MOD;
            sum1 = sum2;
            sum2 = sum3;
            sum3 = sum;
        }
        if(N == 1) return 1;
        else if(N == 2) return 2;
        else if(N == 3) return 5;
        return sum;


    }
};s
```