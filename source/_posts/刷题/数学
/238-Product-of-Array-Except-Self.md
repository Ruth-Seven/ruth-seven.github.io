---
title: 238. Product of Array Except Self
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2021-01-12 11:10:16
---



## [238. Product of Array Except Self](https://leetcode-cn.com/problems/product-of-array-except-self/)



## 思路：

follow up 要求空间为$O(n)$，如果输输出数组不算空间的话，可以这是可以达到的。

<!-- more -->

## 代码：

```c+
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        getProduct(0, 1, nums);
        return nums;
    }

    using ll = long long;
    ll getProduct(int i, ll lprod, vector<int> &nums){        
        if(i == nums.size()) return 1;
        ll nprod = lprod * nums[i];
        ll rprod = getProduct(i + 1, nprod, nums);
        int val = nums[i];
        nums[i] = lprod * rprod;
        return val * rprod;
    }
};
```