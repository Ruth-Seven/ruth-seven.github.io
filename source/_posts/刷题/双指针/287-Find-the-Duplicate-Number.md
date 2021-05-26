---
title: 287. Find the Duplicate Number
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
date: 2021-02-05 20:37:27
tags:
categories:
---










# [287. Find the Duplicate Number](https://leetcode-cn.com/problems/find-the-duplicate-number/)

## 思路

快慢指针算法，$o(n), o(1)$。

这题的难点是看出能把数组转化为链表，而且链表中有环。<!-- more -->

## 代码



```c++
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        // return accumulate(nums.begin(), nums.end(), 0) - (nums.size()- 1) * nums.size() / 2;
        int p1 = 0, p2 = 0;
        do{
            p1 = nums[nums[p1]];
            p2 = nums[p2];
        }while(p1 != p2);
        p2 = 0;
        while(p1 != p2){
            p1 = nums[p1];
            p2 = nums[p2];
        }
      return p1; // p1才是重复的数字/idx
    }
};
```



