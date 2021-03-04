---
title: 897. Increasing Order Search Tree
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
date: 2021-03-04 09:09:22
tags:
categories:
---

## 思路

前序遍历 + 建树

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
public:
    TreeNode* head;
    TreeNode* increasingBST(TreeNode* root) {
        TreeNode* p =  nullptr;
        increasingBSTCore(root, p);
        return head;
    }

    TreeNode* increasingBSTCore(TreeNode* root, TreeNode* &pre) {
        if(!root) return nullptr;
        increasingBSTCore(root->left, pre);
        root->left = nullptr;
        if(pre) pre->right = root;
        else head = root; // The list of head;
        pre = root;
        increasingBSTCore(root->right, pre);
        return root;
    }
};
```



