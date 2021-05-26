---
title: 106. Construct Binary Tree from Inorder and Postorder Traversal
toc: true
top: 10
tags:
categories:
date: 2020-09-25 08:24:07
---

hello world 

## [106. Construct Binary Tree from Inorder and Postorder Traversal](https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)

![img](http://static.come2rss.xyz/西班牙韦斯卡.jpg)

<!-- more -->

## 思路：

递归的将中序遍历的序列分开，并建立中间节点的值

## 代码：

递归。

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

    TreeNode* buildTreeCore(vector<int>& inorder, vector<int>& postorder, int ins, int inend, int posts, int poste){
        if(ins >= inend || posts >= poste) return NULL;

        TreeNode *node = new TreeNode(postorder[poste - 1]);
        int pos = ins;
        while(inorder[pos] != postorder[poste - 1]){
            pos++;
        }
        node->left = buildTreeCore(inorder, postorder, ins, pos, posts, posts + pos - ins);
        node->right = buildTreeCore(inorder, postorder, pos + 1, inend, posts + pos - ins, poste - 1);
        return node;

    }
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
       return buildTreeCore(inorder, postorder, 0, inorder.size(), 0, postorder.size());
    }
};



```

