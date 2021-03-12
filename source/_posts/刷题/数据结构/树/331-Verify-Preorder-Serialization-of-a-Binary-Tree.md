---
title: 331. Verify Preorder Serialization of a Binary Tree
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
date: 2021-03-12 14:54:28
tags:
categories:
---



# [331. Verify Preorder Serialization of a Binary Tree](https://leetcode-cn.com/problems/verify-preorder-serialization-of-a-binary-tree/)




## 思路：



1. 按照字符串提供的数据按前序遍历伪建树，如果用完了所有字符就建树成功。
2. 前序遍历允许我们的用栈记录当前节点以及之前节点应该生长的分支数，比如碰到一个数字，上一个节点的减一分支数，插入一个当点节点的分支数2。遍历过程中，栈为空或者遍历后，字符数还有剩余，显然建树失败。

<!-- more -->

## 代码：






````c++
class Solution {
public:
    bool isValidSerialization(string preorder) {
        int pos = 0;
        // if(preorder)
        return isValidSerializationCore(preorder, pos) && pos == preorder.size() - 1; //完成条件：可以构建出一棵树，并且每个字符都使用到
    }


    bool isValidSerializationCore(string &preorder, int &pos) {
        cout << pos << endl;
        if(preorder.size() <=  pos) return false;
        
        if(preorder[pos] == '#')
            return true;
        while(isdigit(preorder[++pos])); 
        --pos;  //跳到数字的最后一个char的pos

        if(isValidSerializationCore(preorder, pos += 2) && isValidSerializationCore(preorder, pos += 2)) return true;
        return false;
    }


};
````





```c++
class Solution {
public:
    bool isValidSerialization(string preorder) {
        int pos = 0;
        stack<int> post;
        post.push(1);
        while(pos < preorder.size()){
            cout << pos <<  ' ' << post.size() << endl;
            if(post.size() == 0) return false;
            if(preorder[pos] == ',') ++pos;
            else if(preorder[pos] == '#'){ 
                ++pos;               
                if(--post.top() == 0){                    
                    post.pop();
                }
            }else if(isdigit(preorder[pos])){                
                if(--post.top() == 0){                    
                    post.pop();
                }
                post.push(2);                
                while(isdigit(preorder[++pos]));
            }
        }
        return post.size() == 0;
    }



};
```

