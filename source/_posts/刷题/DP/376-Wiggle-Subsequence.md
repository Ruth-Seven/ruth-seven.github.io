---
title: 376. Wiggle Subsequence
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-12-31 10:20:30
---




## [376. Wiggle Subsequence](https://leetcode-cn.com/problems/wiggle-subsequence/)

## 思路：



注意边界，气死人。

> 分析问题不够仔细透彻。

 <!-- more -->

## 代码：

```c++

class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        int n = nums.size();
        if(n == 0) return 0;
        vector<int> up(n), down(n);
        up[0] = down[0] = 1;
        for(int i = 1; i < n; ++i){
            if(nums[i] > nums[i - 1])
                up[i] = max(down[i - 1] + 1, up[i - 1]);
            else up[i] = up[i - 1];

            if(nums[i] < nums[i - 1]) 
                down[i] = max(up[i - 1] + 1, down[i - 1]);
            else down[i] = down[i - 1];
        }
        return max(up[n - 1], down[n - 1]);
    }
};
```

这道题也可以用贪心去做。取出最大波谷变化就可~