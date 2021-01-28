---
title: 204. Count Primes
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2021-01-07 11:06:15
---




## [204. Count Primes](https://leetcode-cn.com/problems/count-primes/)

## 思路：

1. 埃氏筛 $O(nloglogn)$
2. 线性筛$O(nlogn)$，不过由于取模的运算量太大，速度可能还不如埃氏筛

<!-- more -->

## 代码：

埃氏筛

```c++
class Solution {
public:
    int countPrimes(int n) {
        if(n <= 1) return 0;
        vector<int> prime(n + 10);
        int idx = 0;        
        for(int i = 2; i < n; ++i){
            if(prime[i] == 0){
                prime[idx++] = i;
                if(sqrt(INT_MAX) > i)
                for(int j = i * i; j <= n; j += i)
                    prime[j] = 1;
            }
        }
        return idx;
    }
};
```

线性筛

```c++
class Solution {
public:
    int countPrimes(int n) {
        if(n <= 1) return 0;
        vector<int> prime(n + 10);
        int idx = 0;        
        for(int i = 2; i < n; ++i){
            if(prime[i] == 0)
                prime[idx++] = i;

            for(int j = 0; j < idx && prime[j] * i < n; ++j){
                prime[prime[j] * i] = 1;
                if(i % prime[j] == 0) break;
            }
            
        }
        return idx;
    }
};
```

