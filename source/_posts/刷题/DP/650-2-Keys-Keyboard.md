---
title: 650. 2 Keys Keyboard
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-12-21 08:34:03
---




## [650. 2 Keys Keyboard](https://leetcode-cn.com/problems/2-keys-keyboard/)



## 思路：

dp[i] 为长度为i的字符串需要的最小操作数。

1. 反推
2. 最小质数
3. 素数分解

<!-- more -->

## 代码：

这个空间速度

```c++
class Solution {
public:
    int minSteps(int n) {
        vector<int> dp( n + 1, INT_MAX);
        dp[1] = 0;
        for(int i = 1; i < n; i++){
            if(dp[i] != INT_MAX){
                if(i + i <= n){
                    
                    for(int j = i * 2, k = 2; j <=n; j += i, k++){
                        dp[j] = min(dp[i] + k, dp[j]);
                    }
                }
                
            }
        }
        return dp[n];
    }
};
```



这种思路有一点：为啥最小的j就会是dp[i]最小呢？



```C++
class Solution {
public:
    int minSteps(int n) {
        vector<int> dp( n + 1, INT_MAX);
        dp[1] = 0;
        int h = sqrt(n);
        for(int i = 2; i <= n; i++){
            dp[i] = i;
            for(int j = 2; j <= h; j++){
                if(i % j == 0){
                    dp[i] = dp[j] + dp[i / j];
                    break;
                }
            }
        }
        return dp[n];
    }
};
```



素数分解

```c++
class Solution {
public:
    int minSteps(int n) {
        int factor = 2, ans = 0;
        while(n > 1){
            while(n % factor == 0 && n > 1){
                n /= factor;
                ans += factor; //选择（复制 + 粘粘）的一个复合操作是最快的，所以用最小的素数步骤进行一次操作
                //之所以是素数步骤， 是因为合数都被比他小的素数因子所分解了
            }
            factor++;
        }
        return ans;
    }
};
```