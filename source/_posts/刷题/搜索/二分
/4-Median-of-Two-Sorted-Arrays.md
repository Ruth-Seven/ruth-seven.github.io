---
title: 4. Median of Two Sorted Arrays
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-11-12 10:09:16
---








# [4. Median of Two Sorted Arrays](https://leetcode-cn.com/problems/median-of-two-sorted-arrays/)  - 第K大 + 二刷



## 思路：

将查找中位数扩大为更广义的解法：求解第$K$位的数字。每次在`A`,`B`两个数组中划分出两个`k/2`个元素，并排除划分出的最后一个数字比较小的数组，然后减去对应的排除的数组的数字个数，更新$K$值。直到$K==1$，或者其中一个数组为空。

> 详细题解[如下](https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/xun-zhao-liang-ge-you-xu-shu-zu-de-zhong-wei-s-114/)

<!-- more -->

## 代码：



```c++
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int len1 = nums1.size(), len2 = nums2.size();
        int alllen = len1 + len2;
        if(alllen % 2 == 1){
            return findKthNum(nums1, nums2, alllen / 2 + 1);
        }else 
            return (findKthNum(nums1, nums2, alllen / 2 ) + findKthNum(nums1, nums2, alllen / 2 + 1) ) / 2;
    }
    double findKthNum(vector<int>& nums1, vector<int>& nums2, int k){
        int idx1 = 0, idx2 = 0;
        int len1 = nums1.size(), len2 = nums2.size();
        while(1){
            if(idx1 == len1) return nums2[idx2 + k - 1];
            if(idx2 == len2) return nums1[idx1 + k - 1];
            if(k == 1) return min(nums1[idx1], nums2[idx2]);

            int half = k / 2;
            int newidx1 = min(idx1 + half, len1) - 1;
            int newidx2 = min(idx2 + half, len2) - 1;
            if(nums1[newidx1] >  nums2[newidx2]){
                k -= newidx2 - idx2 + 1;
                idx2 = newidx2 + 1;            
            }else{
                k -= newidx1 - idx1 + 1;
                idx1 = newidx1 + 1;
                
            }
            
        }
    }
};
```



```c++

// 思考一下follow up
// 如果K组有序数据，要选出第K大数据你怎么计算呢？ 扩展一下就可以了！
//以下是二刷，不是followup 
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int len1 = nums1.size(), len2 = nums2.size();
        int alllen = len1 + len2;
        if(alllen % 2 == 1){
            return findKthNum(nums1, nums2, alllen / 2 + 1);
        }else 
            return (findKthNum(nums1, nums2, alllen / 2 ) + findKthNum(nums1, nums2, alllen / 2 + 1) ) / 2;
    }
    // k： 第K个数据（‘第’默认从1开始数起 ）
    double findKthNum(vector<int>& nums1, vector<int>& nums2, int k){ 
        
        int n = nums1.size(), m = nums2.size();
        int idx1 = 0, idx2 = 0;
        while(1){
            if(idx1 == n) return nums2[idx2 + k - 1]; // 判断临界点
            if(idx2 == m) return nums1[idx1 + k - 1];
            if(k == 1) return min(nums1[idx1], nums2[idx2]);

            // k >= 2
            int newidx1 = min(k / 2 + idx1, n) - 1; // min 防止溢出
            int newidx2 = min(k / 2 + idx2, m) - 1;  
            if(nums1[newidx1] > nums2[newidx2]){// 结尾数字小的可以直接忽略前串
                k -= newidx2 - idx2 + 1;  
                idx2 = newidx2 + 1; // 多进一个数字
            }else{
                k -= newidx1 - idx1 + 1;
                idx1 = newidx1 + 1;
            }
        }

    }    
};
```

