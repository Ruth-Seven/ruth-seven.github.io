---
title: 300. Longest Increasing Subsequence
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-12-13 09:28:13
---




## [300. Longest Increasing Subsequence](https://leetcode-cn.com/problems/longest-increasing-subsequence/)



## 思路：

1. dp，复杂度$O(n^2)$。
2. 贪心，用$d[i]$维护长度为i的子串结尾数字的最小值。在遍历的过程中更新，增长d[i]。同时d[i]的单调性，可轻松证明。$o(nlogn)$。

> 如果求解的不是strictly increasing subsequence，只需要稍稍修改一下即可。

<!-- more -->



## 代码：

dp

```c++
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();
        if(n == 0) return 0;
        vector<int> dp(n, 1);
        int maxl = 1;
        for(int  i = 1; i < n; i++){
            for(int j = 0; j < i; ++j){
                if(nums[j] < nums[i] && dp[j] + 1 > dp[i] ){
                    dp[i] = dp[j] + 1;
                    maxl = max(dp[i], maxl);
                }
            }
        }
        return maxl;
    }
};
```



贪心+二分

```c++
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();
        if(n == 0) return 0;
        vector<int> d;
        int len = 0;
        for(int i = 0;i < n; ++i){
            if(len == 0 || d[len - 1] < nums[i]){
                d.push_back(nums[i]);
                len++;
                // cout << len ;
            }else{
                auto it = lower_bound(d.begin(), d.end(), nums[i]);
                if( *it > nums[i]){ //搜索第一个j，使得nums[j - 1]  < d[i] < nums[j],只需要两个条件lower_bound和大于号组合就行！
                    *it = nums[i];                
                }
                
            }
        }
        return len;
    }
};
```