---
title: 747. Largest Number At Least Twice of Others
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
categories:
date: 2020-09-24 09:05:25
tags:
---

#### [747. Largest Number At Least Twice of Others](https://leetcode-cn.com/problems/largest-number-at-least-twice-of-others/)

<!-- more -->

EZ

## 思路：

沙雕题目。

## 代码：

```c++
class Solution {
public:
    int dominantIndex(vector<int>& nums) {
        int numbig = -1, numlitter= -1, idx = -1;
        if(nums.size() == 1) return 0;
        for(int i = 0; i < nums.size(); i++){
            if(nums[i] > numbig){
                idx = i;
                numlitter = numbig;
                numbig = nums[i];
            }
            else if(nums[i] > numlitter){
                numlitter = nums[i];
            }
        }
        if(numbig >= numlitter * 2 ){
            return idx;
        }
        else return -1;
    }
};
```

