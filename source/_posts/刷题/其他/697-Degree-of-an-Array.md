---
title: 697. Degree of an Array
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
categories:
date: 2020-10-11 08:28:27
tags:
---



#### [697. Degree of an Array](https://leetcode-cn.com/problems/degree-of-an-array/)

## 思路：

简单遍历，不过数据给的水，可以稍稍放松一下遍历的范围，就不用写这么长了0

<!-- more -->



## 代码：

```c++
class Solution {
public:
    int findShortestSubArray(vector<int>& nums) {
        map<int, int> s ,e, fre;
        int maxfre = 1;
        vector<int> maxnum(1, nums[0]);
        for(int i = 0; i < nums.size(); i++){
            int t = nums[i];
            if(fre[t] == 0){
                s[t] = i;
                
            }
            fre[t]++;

            if(maxfre < fre[t]){
                maxfre = fre[t];
                maxnum.clear();
                maxnum.push_back(t);
            }else if(maxfre == fre[t])
                maxnum.push_back(t);
            e[t] = i;
        } 

        int lens = 0x0fffffff;
        for(int i = 0;i < maxnum.size(); i++){
            lens = min(e[maxnum[i]] - s[maxnum[i]] + 1, lens);
        }
        return lens;
    }
};
```