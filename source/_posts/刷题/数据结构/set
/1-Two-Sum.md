---
title: 1. Two Sum
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2021-01-25 15:44:50
---




## [1. Two Sum](https://leetcode-cn.com/problems/two-sum/)

## 思路：



hash即可

练习一下 STL。

<!-- more -->

## 代码：





```c++
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_set<int> sset;
        map<int, int> ridx;
        for(int i = 0; i < nums.size(); ++i){
            int k = nums[i];
            if(sset.count(target - k)){
                return {ridx[target - k], i};
            }

            sset.insert(k);
            ridx[k] = i;
        }
        return {0 , 0};
    }
};
```

直接用map更好

```c++
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {        
        map<int, int> ridx;
        for(int i = 0; i < nums.size(); ++i){
            int k = nums[i];
            if(ridx.count(target - k)){
                return {ridx[target - k], i};
            }
            ridx[k] = i;
        }
        return {0 , 0};
    }
};
```