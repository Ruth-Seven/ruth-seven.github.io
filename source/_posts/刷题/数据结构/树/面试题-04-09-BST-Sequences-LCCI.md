---
title: 面试题 04.09. BST Sequences LCCI
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
date: 2021-04-01 16:08:51
tags:
categories:
---








# [面试题 04.09. BST Sequences LCCI](https://leetcode-cn.com/problems/bst-sequences-lcci/)



懵树下你和我，快乐刷刷题

## 思路

二叉树的构建，是从根节点开始的，每构建的一个节点，就添加了一个可能两个新扩展节点，我们可以在其中任意选择一个节点新构建，如此递归下去，完成整棵树的构建。

那么，我们需要模拟整棵树的构建遍历过程，用`deque`存储每次构建时可以选择的节点，递归构造。如果`deque`为空，说明建构完成，把记录构建顺序的`path`加入答案即可。建构完成后回溯进行下一个节点的构建。

<!-- more -->

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
    vector<vector<int>> ansSet;
    vector<int> path;
    deque<TreeNode*> que;

public:
    vector<vector<int>> BSTSequences(TreeNode* root){        
        if(root) que.push_back(root);
        BSTSequencesCore();
        return ansSet;
    }

    void BSTSequencesCore() {
        if(que.size() == 0){
            ansSet.push_back(path);
            return;
        }
        for(int i = 0, size = que.size(); i < size; ++i){
            auto node = que.front(); 
            que.pop_front();
            path.push_back(node->val);
            if(node->left) que.push_back(node->left);
            if(node->right) que.push_back(node->right);

            // 选择有效节点，进入递归
            BSTSequencesCore();
            
            // 回溯状态
            path.pop_back();
            if(node->left) que.pop_back();
            if(node->right) que.pop_back();
            que.push_back(node); // 回溯状态要逆序‘’
            
        }
    }
};
```

