---
title: 540. Single Element in a Sorted Array
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
categories:
date: 2020-11-09 07:55:11
tags:
---

## [540. Single Element in a Sorted Array](https://leetcode-cn.com/problems/single-element-in-a-sorted-array/)

## 思路：

设计一个二分即可。



<!-- more -->

## 代码：

```c++
class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        int n = nums.size();
        int l = 0, r = n - 1, mid;
        while(l < r){
            mid = (l + r) / 2;
            int ct;
            if(mid == 0) return nums[0];
            if(nums[mid] == nums[mid + 1])
                ct = mid;
            else if(nums[mid] == nums[mid - 1])
                ct = mid - 1;
            else return nums[mid];
            if( (n - ct) % 2 == 0) r = mid;
            else l = mid + 1;
        }
        return nums[l];

    }
};
```

