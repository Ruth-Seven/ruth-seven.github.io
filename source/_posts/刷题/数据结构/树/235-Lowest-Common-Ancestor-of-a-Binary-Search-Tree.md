---
title: 235. Lowest Common Ancestor of a Binary Search Tree
thumbnail: 'http://static.come2rss.xyz/温哥华东部的弗雷泽河.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-09-27 11:37:57
---

## [235. Lowest Common Ancestor of a Binary Search Tree](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

<!-- more -->



## 思路：

搜索树的LCA比较简单，利于二分性质即可。

## 代码：

```c++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(root->val < min(p->val, q->val)){
            return lowestCommonAncestor(root->right, p, q);
        }else if(root->val > max(p->val, q->val) ){
            return  lowestCommonAncestor(root->left, p, q);
        }else{
            return root;
        }
    }
};
```

