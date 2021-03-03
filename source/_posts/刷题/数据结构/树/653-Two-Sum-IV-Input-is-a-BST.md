---
title: 653. Two Sum IV - Input is a BST
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
date: 2021-03-03 15:58:11
tags:
categories:
---









## 思路：



利用BST性质， 前序遍历数据的同时，搜索对应的`k - val`。

当然可以搜索一遍，同时`hash`遍历的数据，转化为一般的两数之和。



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
    bool findTarget(TreeNode* root, int k) {
        int flag = 0;
        findSum(root, root, k, flag);
        return flag;
    }
    void findSum(TreeNode* root, TreeNode* head, int k, int &flag){
        if(!root) return;
        findSum(root->left, head, k, flag);
        if(root->val > (k + 1) / 2) return; //剪枝
        TreeNode* p = findT(head, k - root->val);
        if(p != nullptr && p != root){
            flag = 1;
            return;
        }
        findSum(root->right, head, k, flag);

    }
    TreeNode* findT(TreeNode* root, int T){
        if(!root) return nullptr;
        if(root->val == T) return root;
        if(root->val < T) return findT(root->right, T);
        else return findT(root->left, T);
    }
};
```

