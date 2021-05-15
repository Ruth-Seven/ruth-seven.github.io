---
title: 124. Binary Tree Maximum Path Sum
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
date: 2021-04-19 09:01:33
tags:
categories:
---

# [124. Binary Tree Maximum Path Sum](https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/)





## 思路：

这题有意思在DP。但算不上hard。

树上的最大路径之和可以转化为一个节点上的左右子树连起来的路径，而左右路径的最大长度分别可以通过左右子树的路径的一部分求得。考虑到子树路径之和小于0的情况，有当前节点和左右子树路径的最大长度为：`DP[i] = max(max(DP[i * 2],0), max(DP[i * 2 + 1],0) + val` 。同时可以求出，当前节点最长路径，`pathsum = max(DP[i * 2],0) + max(DP[i * 2 + 1],0) + val`。

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
    int maxv = 0;
public:
    int maxPathSum(TreeNode* root) {
        maxv = root->val;
        maxPathSumCore(root);
        return maxv;
    }

    int maxPathSumCore(TreeNode *root){
        if(!root) return 0;
        int lv = maxPathSumCore(root->left); lv = max(0, lv);
        int rv = maxPathSumCore(root->right); rv = max(0, rv);
        maxv = max(maxv, lv + rv + root->val);
        return root->val + max(lv, rv);
    }
};
```

