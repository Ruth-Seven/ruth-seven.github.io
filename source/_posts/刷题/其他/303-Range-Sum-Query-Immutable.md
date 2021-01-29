---
title: 303. Range Sum Query - Immutable
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
date: 2021-01-29 11:46:52
tags:
categories:
---






## [303. Range Sum Query - Immutable](https://leetcode-cn.com/problems/range-sum-query-immutable/)



## 思路：

前缀和<!-- more -->

## 代码：







```c++
class NumArray {
    vector<int> nums;
public:
    
    NumArray(vector<int>& _nums) : nums(_nums) {
        nums.insert(nums.begin(), 0);
        for(int i = 1; i < nums.size(); ++i) nums[i] += nums[i - 1];
    }
    
    int sumRange(int i, int j) {
        return nums[j + 1] - nums[i];
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(i,j);
 */
```