---
title: 236. Lowest Common Ancestor of a Binary Tree
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
date: 2021-03-04 09:26:57
tags:
categories:
---





## 思路：

1. 递归搜索，判断左右子树已经当前节点是否有`p`和`q`。
2. 记录下父节点，转化为两条链表的公共子节点。

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
public:
    TreeNode *target;
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        dfs(root, p, q);
        return target;
    }

    int dfs(TreeNode* root, TreeNode* p, TreeNode* q){
        if(!root) return 0;
        int leftRes = dfs(root->left, p, q);
        int rightRes = dfs(root->right, p, q);
        int midRes = 0;
        if(root == p) midRes = 1;
        else if(root == q) midRes = 2;


        if(!target && 
        (root == p && root == q || leftRes + rightRes + midRes == 3)) target = root;
        
        return leftRes + rightRes + midRes;
    }
};
```





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
    TreeNode *target;
    unordered_map<TreeNode*, TreeNode*> fa;
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        dfs(root, nullptr);
        TreeNode* p1 = p, *p2 = q;
        while(p1 != p2){
            p1 = fa[p1] ? fa[p1] : q;
            p2 = fa[p2] ? fa[p2] : p;
        }        
        return p1;
    }

    void dfs(TreeNode* root, TreeNode* father){
        if(!root) return;
        fa[root] = father;
        dfs(root->left, root);
        dfs(root->right, root);
    }
};
```

