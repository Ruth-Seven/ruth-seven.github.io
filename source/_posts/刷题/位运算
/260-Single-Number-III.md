---
title: 260. Single Number III
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2021-01-19 13:26:48
---

## [260. Single Number III](https://leetcode-cn.com/problems/single-number-iii/)



## 思路：

*划分数组*

思路非常精巧。用异或所有数组，由于异或的性质，只有两个唯一且不等的出现的数字$x$,$y$被记录下来，记为$z$。可以推测，$z$比不为零，且第一个1要么来自$x$，要么来自$y$。同时可以根据这个“第一个1”是否在其他数字上存在，将数组划分为两部分，一组是带有$x$和成对的数字，另一组类似。

如此划分数组，同时异或其中一组，就可以得到$x$或者$y$。当然也可以通过上面的$z$异或其中一个数字来得到另一个数字。

<!-- more -->

## 代码：



```c++
class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        int bitmask = 0;
        for(auto & k : nums) bitmask ^= k;
        long long key = (long)bitmask & (-(long)bitmask);
        int mask = 0;
        cout << key << endl;
        for(auto & k : nums){
            if(k & key){
                mask ^= k;
            }
        }
        return {mask, bitmask ^ mask};
    }
};
```

