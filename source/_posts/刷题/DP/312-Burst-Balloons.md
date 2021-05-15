---
title: 312. Burst Balloons
thumbnail: 'http://static.come2rss.xyz/simptab-wallpaper-20201026154850.png'
toc: true
top: 10
date: 2021-05-05 14:50:56
tags:
categories:
---





# [312. Burst Balloons](https://leetcode-cn.com/problems/burst-balloons/)




## 思路：

 `Hard`题做了才有收获啊！`lc`上题库里几道经典的具有锻炼思维和思考能力的题。

1. 拿到手，首先映入脑海里明显应该是贪心或者分治算法：仔细思考一下，贪心发现没有依据，也没有例子；分治算法把考虑把求取问题`dp(l, r)`——开区间的`(l,r)`一组气球全部戳爆以后，可以获取最大金币数量。如果第一选取`k`个气球戳爆，则有子问题`(l,k)`和`(k,r)`，但是可以发现两个子问题是相互依赖的。也就是说一个问题解的选择会影响另一个问题的解的选择。所以这个思路也不行。

2. `Amazing`的是，我们可以反过来考虑问题！我们把整个过程逆序，把戳爆存在的气球，变成从一个气球都不存在，添加一个个不存在的气球。`dp(l, r)`问题就是在寻找，把`(l, r)`中的所有位置填满气球，可以获得最大金币数量。思考一下如何分解为子问题：
   $$
   dp(l, r) = max_{i = l + 1}^{r - 1}[dp(l , i) + dp(i, r) + nums[i] * nums[l] * nums[r]]
   $$
   具体计算可以用记忆化搜索和DP计算。

> 看了下大神的解法，居然还有用启发式搜索的！太顶了！



<!-- more -->



## 代码：



记忆化搜索（自顶向下搜索）：

```c++
class Solution {
    vector<vector<int>> dp;
    int n = 0;
public:
    int maxCoins(vector<int>& nums) {
        nums.insert(nums.begin(), 1);
        nums.push_back(1);
        n = nums.size();
        dp.resize(n, vector<int>(n));
        search(nums, 0, n - 1);
        return dp[0][n - 1];
    }

    int search(vector<int>&nums, int l, int r){ // find max coins in search scope (left, right).
        
        if(dp[l][r]) return dp[l][r];
        int maxCoins = 0;
        for(int i = l + 1; i < r; ++i){
            int amount = search(nums, l, i) + search(nums, i, r) + nums[l] * nums[r] * nums[i];
            maxCoins = max(maxCoins, amount);
        }
        return dp[l][r] = maxCoins;

    }

};
```



DP计算（自底向上搜索）：

```c++
class Solution {
    vector<vector<int>> dp;
    int n = 0;
public:
    int maxCoins(vector<int>& nums) {
        nums.insert(nums.begin(), 1);
        nums.push_back(1);
        n = nums.size();
        dp.resize(n, vector<int>(n)); // find max coins in search scope (left, right).

        // for(int len = 1; len < n - 1; ++len){
        //     for(int i = 0; i + len + 1 < n; ++i){
        //         int j = i + len + 1;
        //         for(int k = i + 1; k < j; ++k){
        //             dp[i][j] = max(dp[i][j], 
        //                     dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j]);
        //         }
        //     }
        // }
        // 更Cache一点的写法应该是
        for(int j = 2; j < n; ++j){
            for(int i = j - 2; i >= 0; --i){
                for(int k = j - 1; k > i; --k){ //从j出发更快~
                // for(int k = i + 1; k < j; ++k){
  					dp[i][j] = max(dp[i][j], 
                            dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j]);                  
                }
            }
        }
        return dp[0][n - 1];
    }

};
```

> 考虑下`cache`优化计算过程