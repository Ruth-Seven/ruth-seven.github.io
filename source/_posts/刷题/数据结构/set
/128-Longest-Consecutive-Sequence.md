---
title: 128. Longest Consecutive Sequence
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2021-01-25 15:44:42
---







## [128. Longest Consecutive Sequence](https://leetcode-cn.com/problems/longest-consecutive-sequence/)

## 思路：



1. sort排序
2. 用set去重，在序列的第一个数字上搜索连续数字长度值！

<!-- more -->





## 代码：



sort

```c++
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if(nums.size() == 0) return 0;

        sort(nums.begin(), nums.end());
        int mlen = 1, len = 1;
        
        for(int i = 1; i < nums.size(); ++i){
            if(nums[i] == nums[i - 1] + 1){
                len++;
            }else if(nums[i] != nums[i - 1]) len = 1;
            mlen = max(mlen, len);
        }
        return mlen;
    }
};
```

set优化

```c++
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if(nums.size() == 0) return 0;

        int mlen = 1;
        unordered_set<int> sset;
        for(auto &v : nums) sset.insert(v);
        for(auto &v : sset){
            if(sset.count(v - 1)) continue; // 只有连续序列的第一个数才能计算后续长度
            int len = 1;
            while(sset.count(len + v)){
                len++;
            }
            mlen = max(mlen, len);
            // cout << v << ' ' << len; // unordered_set 遍历的数字不是有序的            
        }
        return mlen;
    }
};
```