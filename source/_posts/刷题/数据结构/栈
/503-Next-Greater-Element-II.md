---
title: 503. Next Greater Element II
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
date: 2021-01-30 15:11:34
tags:
categories:
---





## [503. Next Greater Element II](https://leetcode-cn.com/problems/next-greater-element-ii/)





## 思路：



单调栈！比较更大值的神。

遍历数组维护单调栈，在排除栈中更小的元素时，就已经为他们找到了更大值。为了保证数组是环形查找的，可以插入两次数组元素。

<!-- more -->

## 代码：

```c++
class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        int n = nums.size();
        vector<int> bigger(n, -1);
        stack<pair<int, int>> sta;
        for(int i = 0; i < 2; ++i){
            for(int j = 0; j < n; ++j){
                while(sta.size() && sta.top().second <nums[j]){
                    auto [pos, num] = sta.top();
                    sta.pop();
                    if(bigger[pos] == -1 )bigger[pos] = nums[j];
                }
                sta.push({j, nums[j]});
            }
        }
        return bigger;
    }
};
```