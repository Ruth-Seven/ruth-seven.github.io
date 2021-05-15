---
title: 326. Power of Three
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
categories:
date: 2021-01-08 10:16:01
tags:
---








## [326. Power of Three](https://leetcode-cn.com/problems/power-of-three/)

直接上代码：

<!-- more -->

思路

```c++
class Solution {
public:
    bool isPowerOfThree(int n) {
        if(n == 1) return true;
        if(n < 3) return false;
        int newn;
        while(n >= 3){
            newn = n / 3;
            if(newn * 3 != n) return false;
            n = newn;
        }
        return n == 1;
    }
};
```

不断整除判断余数是否为零

```c++
class Solution {
public:
    bool isPowerOfThree(int n) {        
        if(n < 1) return false;        
        while(n % 3 == 0){
            n /= 3;
        }
        return n == 1;
    }
};
```

3的k+1次幂必定可以被3的k次幂整除

```c++
class Solution {
public:
    bool isPowerOfThree(int n) {        
        // int  maxn = pow(3,floor(log(INT_MAX) / log(3))); //1162261467
        // cout << maxn << endl;
        return n > 0 && 1162261467 % n == 0;
    }
};
```



3进制算法：数1

```c++
class Solution {
public:
    bool isPowerOfThree(int n) {        
        int ct = 0, oldn = n;
        while(n){
            ct += n % 3;
            if(ct > 1) return false;
            n /= 3;
        }
        return oldn > 0;
    }
};
```