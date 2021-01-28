---
title: 202. Happy Number
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2021-01-15 09:18:59
---



## [202. Happy Number](https://leetcode-cn.com/problems/happy-number/)

## 思路：

1. set查重复数字作为重复数字的抽取方法，循环遍历
2. 假设该步骤总会找到一个数字环，快慢指针法可以类比到该算法。值得注意的，最后happy number最后形成是的数字`1`的自环，必定停留在`1`上。而非 happy number最后形成的环一定没有1。
3. <!-- more -->

![fig1](http://static.come2rss.xyz/202_fig1.png)



![fig2](http://static.come2rss.xyz/202_fig2.png)

## 代码：



```c++
class Solution {
public:
    bool isHappy(int n) {
        unordered_set<int> nums; //hashset更快
        while(n != 1 && nums.count(n) == 0){
            int newn = n,sum = 0;
            while(newn){
                sum += (newn % 10 ) * ( newn % 10 );
                newn /= 10;
            }
            nums.insert(n);
            n = sum;
        }
        if(n == 1) return true;
        else return false;

    }
};
```





快慢指针法

```c++
class Solution {
public:
    int next(int n){
        int newn = n,sum = 0;
        while(newn){
            sum += (newn % 10 ) * ( newn % 10 );
            newn /= 10;
        }
        return sum;    
    }
    bool isHappy(int n) {
        int p1 = next(n);
        int p2 = next(next(n));
        while(p1 != p2){
            p1 = next(p1);
            p2 = next(next(p2));
        }
        if(p1 == 1) return true;
        else return false;

    }
};
```