---
title: 560. Subarray Sum Equals K
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
date: 2021-01-29 11:47:14
tags:
categories:
---






## [560. Subarray Sum Equals K](https://leetcode-cn.com/problems/subarray-sum-equals-k/)



## 思路：

hash+ 前缀。

<!-- more -->

## 代码：





```c++
class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int n = nums.size();
        if(n == 0) return 0;
        vector<int> dp(n + 1);
        unordered_map<int, int> map;
        int ct = 0;
        map[0] = 1;
        for(int i = 1; i < n + 1; ++i) {
            dp[i] = dp[i - 1 ] + nums[i - 1];
            ct += map[dp[i] - k];
            map[dp[i]]++;
        }

        return ct;
    }
};


//错误二分，数组不保证都为正数
// class Solution {
// public:
//     int subarraySum(vector<int>& nums, int k) {
//         int n = nums.size();
//         if(n == 0) return 0;
//         vector<int> dp(n + 1);

//         for(int i = 1; i < n + 1; ++i) dp[i] = dp[i - 1 ] + nums[i - 1];

//         int ct = 0;
//         for(int i = 0; i < n; ++i){
//             int r = n - 1;
//             int l = i;
//             while(l < r){
//                 int mid = (l + r) / 2;
//                 if(dp[mid + 1] - dp[i] >= k) r = mid;
//                 else l = mid + 1;
//             }
//             if(l < n && dp[l + 1] - dp[i] == k) ct++;
//         }
//         return ct;
//     }
// };


// class Solution {
// public:
//     int subarraySum(vector<int>& nums, int k) {
//         int n = nums.size();
//         if(n == 0) return 0;
//         vector<int> dp(n + 1);

//         for(int i = 1; i < n + 1; ++i) dp[i] = dp[i - 1 ] + nums[i - 1];

//         int ct = 0;
//         for(int i = 0; i < n; ++i){
//             for(int j = i; j < n; ++j)
//                 if(k == dp[j + 1] - dp[i]) ct++;
            
//         }
//         return ct;
//     }
// };

```