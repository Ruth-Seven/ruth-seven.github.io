---
title: 96. Unique Binary Search Trees
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
date: 2021-04-29 12:55:37
tags:
categories:
---




# [96. Unique Binary Search Trees](https://leetcode-cn.com/problems/unique-binary-search-trees/)s

## 思路：

理解，只要数字不重复，子树的形状可能性就与数字具体大小无关。所以可以用DP算出长度为K的子树的可能形状。

<!-- more -->

## 代码：

```c++

class Solution {
    int  allmount = 0;
    vector<int> dp;
public:
    int numTrees(int n) {
        dp.resize(n + 1);
        dp[1] = 1;
        dp[0] = 1;
        return findBST(1, n);
    }

    int findBST(int L, int R){
        if(dp[R - L + 1]) return dp[R - L + 1];
        // if(L >= R){             
        //      return 1;
        // }
        int nums = 0;
        for(int i = L; i <= R; ++i){
        
            nums += findBST(L, i - 1) * findBST(i + 1, R);
        }
        // cout << L << ' ' << R  << ' ' << nums << endl;
        dp[R - L + 1] = nums;
        return nums;
    }
};
```

