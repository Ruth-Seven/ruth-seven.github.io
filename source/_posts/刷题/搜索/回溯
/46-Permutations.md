---
title: 46. Permutations
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-11-24 10:41:53
---





## [46. Permutations](https://leetcode-cn.com/problems/permutations/)2



## 思路：

回溯法确定全排列。复杂度$o(n*n!)$，（复制 * permute调用次数）。

<!-- more -->

## 代码：

```c++
class Solution {
public:
    void permuteCore(vector<int>&nums, vector<vector<int>> &res, int pos){
        int n = nums.size();
        if(n - 1 < pos){
            res.push_back(nums);
            return;
        } 
        for(int i = pos; i < n; ++i){
            swap(nums[pos], nums[i]);
            permuteCore(nums, res, pos + 1);
            swap(nums[pos], nums[i]);
        }
    }
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        permuteCore(nums, res, 0);
        return res;
    }
};
```