---
title: 297. Serialize and Deserialize Binary Tree
thumbnail: 'http://static.come2rss.xyz/simptab-wallpaper-20201027164551.png'
toc: true
top: 10
date: 2021-04-26 08:27:55
tags:
categories:
---

# [297. Serialize and Deserialize Binary Tree](https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/)



## 思路：

对于二叉树序列化，leetcode已经给出了很好的示范。思考一下，完整前缀遍历（包括空节点信息）能否构建二叉树？可以，从根到子节点前缀遍历的同时构建二叉树。同理后缀也可以。

<!-- more -->



这里我采用层序遍历的方式，构建序列化和解序列化。

下面的代码有一个小技巧，把`迭代器`的设计思想融入到代码里：把遍历的功能独立出来，只提供接口，以便快速判断有无剩余节点，该节点是否有效。





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
class Codec {
    string ser;
    int pos; // decoded pos.
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
    
        queue<TreeNode*> que;
        que.push(root);

        while(que.size()){
            TreeNode* pnode = que.front();
            que.pop();
            if(pnode){
                ser += to_string(pnode->val) + ",";
                que.push(pnode->left);
                que.push(pnode->right);
            }
            else ser += "null,";
        }
        if(ser != "") ser.erase(ser.size() - 1);
       // cout << ser << endl;
        return ser;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        ser = data;
        TreeNode *root = nullptr, *p = root;
        pos = 0;

        queue<TreeNode*> que;
        if(_isvalue()){
            root = new TreeNode(_next());
            que.push(root);

        }
        else return nullptr;

        while(que.size()){
            p = que.front(); // 为该节点构造左右节点
            que.pop();
          //  cout << p->val << ' ';
            if(!_hasnext()) break;
            if(_isvalue()){
                p->left = new TreeNode(_next());
                que.push(p->left);
            }else _next(); // 该节点的左子树为空
            if(_isvalue()){
                p->right = new TreeNode(_next());
                que.push(p->right);
            }else _next(); // 该节点的右子树为空
        } 
        //cout << endl;
        return root;

    }

    bool _isvalue(){        
        if(!_hasnext()) return false;
        if(isdigit(ser[pos]) || ser[pos] == '-') return true;
        return false;
    }

    inline bool _hasnext(){
        return !(pos >= ser.size());
    }
    int _next(){
        bool isnum = _isvalue();
        int t = pos;
        while(t < ser.size() && ser[t] != ',') ++t;
        int pre = pos;
        pos = t + 1; // 把pos移到下一个空节点null或者数字开头处
        if(isnum) return stoi(ser.substr(pre, t - pre)); 
        else return -1;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec ser, deser;
// TreeNode* ans = deser.deserialize(ser.serialize(root));
```

