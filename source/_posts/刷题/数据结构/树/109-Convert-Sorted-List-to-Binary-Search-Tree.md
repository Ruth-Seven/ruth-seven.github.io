---
title: 109. Convert Sorted List to Binary Search Tree
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
date: 2021-03-04 08:54:37
tags:
categories:
---




## 思路：

链表实际上给出的是二叉树前序的结果，因为AVL树任意左右子树高度不超过1，我们可以选择链表中点，并将链表的长度尽可能一样长的两部分划分到左右子树，所以高度性质可以维持住。

在中序遍历链表，控制子树长度，即可构建符合题意的AVL树。

<!-- more -->



## 代码：

```c++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
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
    TreeNode* sortedListToBST(ListNode* head) {
        int len = sizeOfList(head);
        return sortedListToBSTCore(head, 0, len - 1);
    }
    
    int sizeOfList(ListNode* head){
        ListNode *p = head;
        int len = 0;
        while(p){
            p = p->next;
            ++len;
        }
        return len;
    }
    TreeNode* sortedListToBSTCore(ListNode* &head, int lhs, int rhs) {
        if(lhs > rhs) return nullptr;
        int mid = (lhs + rhs + 1) / 2;
        TreeNode* lchild = sortedListToBSTCore(head, lhs, mid - 1);
        TreeNode* root = new TreeNode(head->val);
        head = head->next;
        TreeNode* rchild = sortedListToBSTCore(head, mid + 1, rhs);
        root->left = lchild;
        root->right = rchild;
        return root;
    }
};
```

