---
title: 二叉树中距离为K的节点
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
date: 2021-07-28 08:17:27
tags:
categories:
---











## 思路

这题还是有点点复杂的，距离为K的节点，完全可以分为两类，`target`节点构成树的K-dis节点，和其路径经过`target`祖父节点的节点。分类搜索即可，考虑到后者需要定点采集，所以用回溯的方式获取。

<!-- more -->

## 代码

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
    struct findedNode {
        TreeNode *node;
        int diretion;
        int distannce; 
    };
    queue<findedNode> que;
    vector<int> knodes;
    vector<int> distanceK(TreeNode* root, TreeNode* target, int k) {
        findSnode(target, 2, k);
        int isfind = 0, tempK = k;
        findTrace(root, target, isfind, tempK);
        while(que.size()) {
            findedNode n = que.front();
            que.pop();
            findSnode(n.node, n.diretion, n.distannce);
        }
        return knodes;
    }
    void findSnode(TreeNode* root, int diretion, int k) {
        if(root == nullptr) return;
        if(k == 0) {
            knodes.push_back(root->val);
            return;
        }
        if(diretion != 1) findSnode(root->right, 2, k - 1);
        if(diretion != 0) findSnode(root->left, 2, k - 1);
    }

    void findTrace(TreeNode* root, TreeNode *target, int &finded, int &k) {
        if(root == nullptr ) return;
        if(root == target) {
            finded = 1;
            return;
        }
        int diretion = 0;
        if(!finded) findTrace(root->left, target, finded, k);
        if(!finded) {
            findTrace(root->right, target, finded, k);
            diretion = 1;
        }
        if(finded && k > 0) que.push(findedNode{root, diretion, --k});
    }

};
```

