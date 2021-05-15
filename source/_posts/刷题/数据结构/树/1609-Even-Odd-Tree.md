---
title: 1609. Even Odd Tree
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-10-18 13:22:57
---


<!-- more -->

## 思路:

层序遍历。记录边界即可。



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
    
    bool isEvenOddTree(TreeNode* root) {
        if(root == nullptr ) return false;
        queue<TreeNode *> que;
        vector<int> a;
        int level = 0, num = 1, nextn = 0;;
        que.push(root);
        while(!que.empty()){
            TreeNode *t = que.front();
            que.pop();
            a.push_back(t->val);
            num--;
            if(t->left){
                que.push(t->left);
                nextn++;
            }
            if(t->right){
                que.push(t->right);
                nextn++;            
            }            
            if(num == 0){
                num = nextn;
                nextn = 0;
                int flag = 1;
                if(a.size() < 1) continue;

                if(level & 1){
                    for(int i = 1; i < a.size(); i++){
                        if(a[i] >= a[i - 1] || a[i]%2 == 1 )
                            flag = 0;
                    }
                    if(a[0]%2 == 1) flag = 0;
                }
                else{
                    for(int i = 1; i < a.size(); i++){
                        if(a[i] <= a[i - 1] || a[i]%2 == 0)
                            flag = 0;
                    }                
                    if(a[0]%2 == 0) flag = 0;

                }
           
                a.clear();
                level ++;
                if(!flag) return false;
            }   
        }
        return true;
    }
};
```

