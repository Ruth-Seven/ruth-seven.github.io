---
title: 450. Delete Node in a BST
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
date: 2021-03-03 14:28:21
tags:
categories:
---





## 思路：

删除一个只有一个子节点，或者没有子节点的节点，比较简单。

删除有两个子节点的节点`A`，需要把找一个比`A`大的最小子节点`B`来替换该`A`。那么同时也需要递归的删除节点`B`。



<!-- more -->

## 代码：

如果二叉树结构是父子儿子结构代码会更简单。

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
    void print(TreeNode* root){
        if(!root) return;
        print(root->left);
        cout << root->val << " " ; 
        print(root->right);
    }
    TreeNode* deleteNode(TreeNode* root, int key) {
        if(!root) return nullptr;
        // print(root); cout << root->val << endl; 
        if(key > root->val){
            root->right = deleteNode(root->right, key);
            return root;
        }
        if(key < root->val){
            root->left = deleteNode(root->left, key);            
            return root;
        }
        //delete the note without right child.
        if(!root->right){
            TreeNode *temp = root->left;
            delete root;
            return temp;        
        }
        //delete the node with right child.
        TreeNode* rightMinP = getMinNode(root->right);
        TreeNode* newp = new TreeNode(rightMinP->val);
        // recursively delete the minimum node.
        root->right = deleteNode(root->right, rightMinP->val); //Because of updating left child link //bugs
        // cout << "@" << root->val << endl;        
        // print(root);
        // cout << "$" << newp->val << endl;
        newp->left = root->left;
        newp->right = root->right;
        delete root;
        return newp;    
    }

    TreeNode * getMinNode(TreeNode* root){
        if(!root) return nullptr;
        TreeNode* p = root;
        while(p->left){
            p = p->left;
        }
        return p;
    }
};
```

