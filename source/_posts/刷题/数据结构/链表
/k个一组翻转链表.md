---
title: k个一组翻转链表
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
date: 2021-09-23 09:11:51
tags:
categories:
---




#### [25. K 个一组翻转链表](https://leetcode-cn.com/problems/reverse-nodes-in-k-group/)



## 思路

添加伪头节点，减少复杂度

提交之前模拟运行

多种控制条件选择最简单的

<!-- more -->

## 代码

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
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode tempHead;
        tempHead.next = head;
        ListNode* p1 = &tempHead, *p2 = p1;
        int counter = 0;

        while(p2) {
            counter = 0;
            while(counter < k && p2) {
                p2 = p2->next;
                counter++;
            }
            if(counter == k && p2) {
                ListNode* Kend = p1->next;
                ListNode* Khead = p1;
                ListNode* p = Kend->next;
                ListNode* nextp = nullptr;
                for(int i = 1; i < k; i++){ 
                    nextp = p->next;
                    p->next = Khead->next;
                    Khead->next = p;
                    p = nextp; 
                }
                Kend->next = p;
                p1 = p2 = Kend; 
            } 
        }
        return tempHead.next;
    }
};
```