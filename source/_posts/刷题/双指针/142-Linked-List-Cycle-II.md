---
title: 142. Linked List Cycle II
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-10-19 13:53:17
---


<!-- more -->



## 思路：

用快慢指针`fast`，`slow`去发现链表中的圆，再使用一个指针和`p1`一起遍历链表：

![fig1](http://static.come2rss.xyz/142_fig1.png)

`2(a + b)  = a + b + (b + c ) *n `得到

`a = c + (b + c ) *(n - 1)` 

如此可以推得，如果从`p0`从head和`slow`一起出发，会在环的入口处相遇。如此就可以推得算法的正确性。

另外开始验证，`fast`和`low`会在第一个`low`指针的第一圈相遇。

> 设置两个指针相遇时，`low`指针走了路程`s1 = a + s + n(b + c)`，`fast`指针走了路程`s2 = a + s + k(b + c)`。同时有`s1 * 2 = s2`，则有`a + s = (k - 2n)(b +c)`。

上面的证法不行：

设`slow`刚入环的时候，`fast`在距离环入口的位置`B`，慢指针走了`C`,最后设环长为`L`。

`C % L = (2 *C + B) % L`

等价于

`C + NL =  2 * C + B`

`C = NL - B ` 当N==1，有`0<=C<=B`

当然，需要另外一个推理：

两个步长分别为1和2的指针，经过必定能相遇，可以通过遍历所有状态得知。



## 代码

```c++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        ListNode *p1 = head, *p2 = head;
        int flag = 0, cyclen = 0, tlen = 0;
        while(p1){
            p1 = p1->next;
            if(p1 == nullptr) return nullptr;
            p1 = p1->next;
            p2 = p2->next;
            if(p1 == p2) break;            
        }
        if(p1 == nullptr) return nullptr;
        // while(1){
        //     p1 = p1->next->next;
        //     p2 = p2->next;
        //     cyclen++;   
        //     if(p1 == p2) break;         
        // }
        ListNode *p0 = head;
        while(p0 != p1){
            p0 = p0->next;
            p1 = p1->next;
            tlen++;
        }
        return p0;
    }
};
```

