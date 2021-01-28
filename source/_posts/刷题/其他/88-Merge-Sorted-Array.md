---
title: 88. Merge Sorted Array
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
categories:
date: 2020-10-17 08:50:57
tags:
---


<!-- more -->

## 思路：

双指针从后向前合并即可，时间复杂度为$n(o)$，空间复杂度$O(1)$。

## 代码：

```c++
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {        
        int pos = m + n - 1, p1 = m - 1, p2 = n - 1;
        while(p1 >= 0 && p2 >= 0){
            if(nums1[p1] > nums2[p2]){
                nums1[pos] = nums1[p1--];
            }else{
                nums1[pos] = nums2[p2--];
            }
            pos--;
        }
        while(p2 >= 0){
            nums1[pos--] = nums2[p2--];
        }
    }
};
```

