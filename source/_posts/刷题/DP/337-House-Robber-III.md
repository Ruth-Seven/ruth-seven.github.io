---
title: 337. House Robber III
thumbnail: 'http://static.come2rss.xyz/simptab-wallpaper-20201027164551.png'
toc: true
top: 10
date: 2021-04-30 12:28:23
tags:
categories:
---



# [337. House Robber III](https://leetcode-cn.com/problems/house-robber-iii/)

## 思路：

这里的dp推错了，尴尬啊。

一个简单的树上DP

<!-- more -->

## 代码：

```c++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
    using tii =  tuple<int, int>;
public:
    int rob(TreeNode* root) {
        tii res = stelan(root);
        return max(get<0>(res), get<1>(res));
    }

    tii stelan(TreeNode* root){
        if(!root) return make_tuple(0, 0);
        tii left = stelan(root->left);
        tii right = stelan(root->right);
        // dp 推导式： 
        // dp[i][0] = max(dp[i * 2][1], dp[i * 2][0]) +  max(dp[i * 2 + 1][1], dp[i * 2 + 1][0])
        // dp[i][1] = val[i] + dp[i * 2][0] + dp[i * 2 + 1][0];
        return make_tuple(max(get<0>(left), get<1>(left)) + max(get<0>(right), get<1>(right)),
                         get<0>(left) + get<0>(right) + root->val);        
    }
};
```

