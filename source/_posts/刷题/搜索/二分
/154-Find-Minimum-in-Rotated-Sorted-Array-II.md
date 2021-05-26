---
title: 154. Find Minimum in Rotated Sorted Array II
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-11-01 08:40:48
---





## [154. Find Minimum in Rotated Sorted Array II](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/)

## 思路：

这题非常具有启发性质，hard~

<!-- more -->

虽然还是二分，但是题目条件更加复杂。

话题可视化还是不错的分析方法，可惜我太懒了……

注意题目的被旋转数组部分可能长度为零。

借用答案的分析思路：

由于数组“右边”的数字一定是未被旋转的，那么一定有
$$
nums[mid] < num[right] -> 右边有序\\
nums[mid] > num[right] -> 左边有序
$$


如此便可以二分，其他情况下，可能存在
$$
nums[mid] == nums[l] == nums[r]
$$
无法进行二分，但可以发现，num[r]等于nums[mid]，所以r是可以缩减范围的。



图形化描述见[官方题解](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/solution/xun-zhao-xuan-zhuan-pai-xu-shu-zu-zhong-de-zui--16/)

## 代码：

```c++
class Solution {
public:
    int findMin(vector<int>& nums) {
        int l = 0, r = nums.size() - 1, mid;
        if(r < 0) return -1;//bug
        //加个判断击败14%->98%,说明大多数人还是直接复制粘粘答案的
        if(nums[l] < nums[r]) return nums[l];
        while(l < r){
            mid = l + (r - l) / 2;
            if(nums[mid] < nums[r]) r = mid;
            else if(nums[mid] > nums[r]) l = mid + 1;
            else r--; 
        }
        return nums[l];


    }
};

```