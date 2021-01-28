---
title: 633. Sum of Square Numbers
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-10-24 09:34:40
---

## [633. Sum of Square Numbers](https://leetcode-cn.com/problems/sum-of-square-numbers/)

<!-- more -->

## 思路：

1. 二分

2. 分解质因子判断费马平方定理条件是否成立

   >  任何一个等于两个数的平方之和的数的所有值为$(4k+3)$的因子次幂是偶数的。

3. 双指针法遍历即可（击败100%）



## 代码：

双指针法

```c++

class Solution {
public:
    bool judgeSquareSum(int c) {
        long long  sum, a = 0, b = (long long)(sqrt(c));
        while(a <= b ){
            sum  = a * a + b * b;
            if(sum > c) b--;
            else if(sum < c) a++;
            else break;
        }
        if(sum == c) return true;
        else return false;
    }
};




```



判断费马平方定理：

```c++
class Solution {
public:
    bool judgeSquareSum(int c) {
        // int d = (int)sqrt(c), ori  = c ;
        // for(int i = 2; i <= d + 1 && c != 1; ++i){
        for(int i = 2; i <= c; ++i){
            if(c % i == 0){
                int t = 0;
                while(c % i == 0){
                    ++t;
                    c /= i;
                }
                if((i + 1) % 4 == 0){
                    if(t & 1) return false;
                }
            }
        }
        // if(c == ori && (c + 1) % 4 == 0) return false;
        return true;

    }
};
```

