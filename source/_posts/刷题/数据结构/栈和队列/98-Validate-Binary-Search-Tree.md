---
title: 98. Validate Binary Search Tree
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
date: 2021-04-22 15:56:21
tags:
categories:
---

# [98. Validate Binary Search Tree](https://leetcode-cn.com/problems/validate-binary-search-tree/)



## 思路：

不要把二叉树的性质搞错了，是任一个节点的值大于其**所有**左节点的值，小于等于**所有**右节点的值，而非左节点。

如此直接验证所有节点的是否大于左子树的最大值，小于右子树的最小值即可。

<!-- more -->

## 代码

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
// class Solution {
// public:
//     bool isValidBST(TreeNode* root) {
//         if(!root) return true;
//         bool flag = (root->right ? (root->val < root->right->val) : true) 
//                     && (root->left ? (root->val > root->left->val) : true);
        
//         return flag && isValidBST(root->right) && isValidBST(root->left);
//     }
// };

class Solution {
public:
    inline TreeNode* minNode(TreeNode* root){
        while(root->left) root = root->left;
        return root;
    }

    inline TreeNode* maxNode(TreeNode* root){
        while(root->right) root = root->right;
        return root;
    }
    
    bool isValidBST(TreeNode* root) {
        if(!root) return true;
        bool flag = (root->right ? (root->val < minNode(root->right)->val) : true) 
                    && (root->left ? (root->val > maxNode(root->left)->val) : true);
        
        return flag && isValidBST(root->right) && isValidBST(root->left);
    }
};
```

