---
title: 136. Single Number
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2021-01-17 18:23:16
---



## [136. Single Number](https://leetcode-cn.com/problems/single-number/)

## 思路：

<!-- more -->

## 代码：

```c++
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int key = 0;
        for(auto &k : nums){
            key = k ^ key;
        }
        return key;
    }
};
```