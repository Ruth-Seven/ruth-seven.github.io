---
title: 476. Number Complement
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2021-01-19 11:18:16
---



## [476. Number Complement](https://leetcode-cn.com/problems/number-complement/)

## 思路：

数字取反前把前缀零全部转化为前缀1.



<!-- more -->

## 代码：





```c++
class Solution {
public:
    int findComplement(int num) {
        int c = 1;
        while( (num >> c) ) ++c;
        while(c <= 31){
            num = num | (1 << c);
            c++;
            // cout << num << endl;
        }
        return ~num;
    }
};
```