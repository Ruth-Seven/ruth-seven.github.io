---
title: 665. Non-decreasing Array
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-10-16 13:47:28
---

<!-- more -->



#### [665. Non-decreasing Array](https://leetcode-cn.com/problems/non-decreasing-array/)



## 思路：

对于任意一个$A[i]>A[i+1]$，$A[i]$和$A[i+1]$分别代表两个non-decreasing array，而合并两个的方法只有：`A[i] = A[i - 1]`和`A[i +1 ] = A[i + 2]`。

接下来只需要讨论边界条件和合并次数即可。

## 代码：

```c++

class Solution {
public:
    bool checkPossibility(vector<int>& nums) {
        int ansnum = 0;
        int n = nums.size();
        for(int i = 0; i < n - 1; ++i){
            if(nums[i] > nums[i + 1]){
                if(i ==0 || nums[i - 1] <= nums[i + 1] || i == n - 2 || nums[i] <= nums[i + 2]){
                    ansnum++;
                    if(ansnum > 1) return false;
                }   
                else return false;
                    
            }
        }
        return true;;;;;;;;;;
    }
};
```

