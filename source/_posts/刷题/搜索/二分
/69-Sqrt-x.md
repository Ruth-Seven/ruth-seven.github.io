---
title: 69. Sqrt(x)
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-10-27 08:14:13
---



这题还是蛮不错的，二分和牛顿迭代法的练习入门题。



#### [69. Sqrt(x)](https://leetcode-cn.com/problems/sqrtx/) 二分  - 牛顿迭代法

##### <!-- more -->





## 思路：

二分x或者牛顿迭代计算都可。

## 代码：

```c++

class Solution {
public:
    int mySqrt(int x) {
        long l = 0, r = x, mid;
        while(l < r){
            mid = (l + r) / 2;
            if(mid * mid < x) l = mid + 1;
            else r = mid;
        }
        if(l * l == x)
            return l;
        else 
            return l - 1;

    }
};



```

​	

牛顿迭代法

```c++


// 牛顿迭代法
class Solution {
public:
    //写的时候瞎想的 挺好用
    int mySqrt(int x) {
        double ans = x, last = ans + 1;
        double gap = 1e-3;
        if(x == 0) return 0;
        while(abs(ans - last) > gap){

            last = ans;
            ans = ans - (ans * ans - x) / (double)(2 * ans); 
        }
        return int(ans);
        

    }
};

//上一个方法的公式简化版， 击败100%
//而且考虑到了double运算速度慢，精度要求不高，可以使用long来代替，且保证不会遗漏答案。
class Solution {
public:
    int mySqrt(int x) {
        long res = x;
        while(res * res > x){
            res = (res +  x/ res ) /2;
        }
        return res;
    }
};

```

