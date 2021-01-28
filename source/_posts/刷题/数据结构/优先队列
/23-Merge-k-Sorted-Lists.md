---
title: 23. Merge k Sorted Lists
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2021-01-24 21:10:48
---





## [23. Merge k Sorted Lists](https://leetcode-cn.com/problems/merge-k-sorted-lists/)

## 思路：



优先队列排node就行。<!-- more -->

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
class Solution {
    class Node{
        
    public:
        ListNode *p;
        Node(ListNode *_p): p(_p){}
        friend bool operator < (Node p1, Node p2){
            return p1.p->val > p2.p->val;
        }
        // friend bool operator < (string s1, string s2){
        //     return s1.name < s2.name;
        // }
    
    };
    priority_queue<Node> pq;
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        for(auto &p : lists) 
            if(p) pq.push(Node(p));
        ListNode *root , *p, *oldp;
        p =  nullptr;
        oldp = root = new ListNode();
        while(pq.size()){
            p = pq.top().p;
            pq.pop();
            if(p->next) pq.push(Node(p->next));
            oldp->next = p;
            oldp = p;
            
        }
        return root->next;
    }
};
```