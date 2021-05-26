---
title: 75. Sort Colors
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-11-17 08:21:54
---




#### [75. Sort Colors](https://leetcode-cn.com/problems/sort-colors/)

彩虹题

<!-- more -->

## 思路：

1. 直接桶排
2. 有趣的三指针算法。

## 代码：

桶排

```c++
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int count[3] = {0};
        for(int i = 0; i < nums.size(); ++i){
            count[nums[i]]++;
        }
        int k = 0;
        for(int i = 0; i < 3; ++i){
            
            while(count[i] > 0){
                nums[k++] = i;
                count[i]--;
            }
        }        
    }   
};
```

三指针

```c++
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int n = nums.size();
        int p0 = 0, p1 = n - 1;
        for(int i = 0; i <= p1; ++i){
            while(nums[i] == 2 && p1 >= i){
                swap(nums[i], nums[p1]);
                p1--;
            }
            if(nums[i] == 0){
                swap(nums[p0], nums[i]);
                p0++;

            }

        }
    }   
};
```