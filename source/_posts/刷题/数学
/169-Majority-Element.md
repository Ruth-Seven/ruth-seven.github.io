---
title: 169. Majority Element
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2021-01-15 09:20:03
---





## [169. Majority Element](https://leetcode-cn.com/problems/majority-element/)



## 思路：



#### Boyer-Moore 投票算法

<!-- more -->

## 代码：

```c++
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        if(nums.size() == 0) return -1;
        int a = nums[0];
        int ct = 0;
        for(auto k : nums){
            if(k == a){
                ++ct;
            }else if(ct > 0){
                --ct;
            }else{
                a = k;
                ++ct;
            }
        }
       return a;
       
    }
};
```



稍微简洁一点

```c++

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        if(nums.size() == 0) return -1;
        int a = nums[0];
        int ct = 0;
        for(auto k : nums){
            if(ct == 0){
                a = k;
            }
            ct += k == a ? 1 : -1;
        }
        return a;
       
    }
};
```