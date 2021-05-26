---
title: 448. Find All Numbers Disappeared in an Array
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2021-01-22 11:32:10
---




## [448. Find All Numbers Disappeared in an Array](https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array/)

## 思路：

把nums当做已经出现的元素的向量表，重点是遍历的元素过程中"递归"地置位元素。



<!-- more -->

## 代码：



```c++
class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        for(int i = 0; i < nums.size(); ++i){
            int t = nums[i];
            if(t < 0) continue;
            while(nums[t - 1] > 0){
                int newt = nums[t - 1];
                nums[t - 1] =  nums[t - 1] == -1 ? -2 : -1;
                t = newt;
            }
        }
        vector<int> ans;
        for(int i = 0; i < nums.size(); ++i){
            if(nums[i] > 0) ans.push_back(i + 1);
        }
        return ans;

    }
};
```