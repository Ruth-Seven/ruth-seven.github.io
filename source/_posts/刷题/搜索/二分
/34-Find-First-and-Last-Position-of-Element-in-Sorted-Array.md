---
title: 34. Find First and Last Position of Element in Sorted Array
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-10-28 08:39:37
---

#### [34. Find First and Last Position of Element in Sorted Array](https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

<!-- more -->

## 思路：

二分

## 代码：

```c++
class Solution {
public:
    
    int getFirst(vector<int> nums, int l, int r, int tar){
        if(nums.size() == 0) return -1;
        int mid ;
        while(l < r){
            mid = (r + l) / 2;
            if(nums[mid] < tar) l = mid + 1;
            else r = mid;
        }
    // 临界判断需要小心    
        return l != nums.size() && nums[l] == tar ? l : -1;
    }

    int getLast(vector<int> nums, int l, int r, int tar){
        if(nums.size() == 0) return -1;
        int mid ;
        while(l < r){
            mid = (r + l) / 2;
            if(nums[mid] <= tar) l = mid + 1;
            else r = mid;
        }
        return l != 0 && nums[l - 1] == tar ? l - 1 : -1;
    }
    
    vector<int> searchRange(vector<int>& nums, int target) {
        int s = -1 , e = -1, l = 0, r = nums.size();
        vector<int> res({getFirst(nums, 0, nums.size(), target) , getLast(nums, 0, nums.size(), target) });
        return res;
    }
};
```