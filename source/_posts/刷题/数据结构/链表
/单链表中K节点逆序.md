---
title: 单链表中K节点逆序
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
date: 2021-06-26 09:45:38
tags:
categories:
---

<!-- more -->



## 思路

超级大杂烩，左程云出的题的风格。

K节点逆序+ K节点检测 + 链表链接



## 代码



```c++
# include <bits/stdc++.h>
using namespace std;

struct list_node{
    int val;
    struct list_node * next;
};

list_node * input_list()
{
    int val, n;
    scanf("%d", &n);
    list_node * phead = new list_node();
    list_node * cur_pnode = phead;
    for (int i = 1; i <= n; ++i) {
        scanf("%d", &val);
        if (i == 1) {
            cur_pnode->val = val;
            cur_pnode->next = NULL;
        }
        else {
            list_node * new_pnode = new list_node();
            new_pnode->val = val;
            new_pnode->next = NULL;
            cur_pnode->next = new_pnode;
            cur_pnode = new_pnode;
        }
    }
    return phead;
}


list_node * reverse_knode(list_node * head1, int K)
{
    list_node whead = {0, head1};
    list_node *before, *pre, *p, *next; // pre, p, next 单单在K个节点逆序起作用； bofore指向逆序链表的前一个节点
    p = head1;
    before = &whead;
    
    while(p) {
        int k = 0;
       list_node *now = before;
        while(k < K){
            k++;
            if (now) now = now->next;
        
        }
        if(now == nullptr) break;
        
        k = 0;
        pre = nullptr;
        list_node *kend = before->next;
        while(k < K) {
            k++;    
            next = p->next;
            p->next = pre;
            pre = p;
            p = next;
            if(next) next = next->next;
        }
        before->next = pre;
        kend->next = p;
        
        before = kend;
        
    }
    return whead.next;

}

void print_list(list_node * head)
{
    while (head != NULL) {
        printf("%d ", head->val);
        head = head->next;
    }
    puts("");
}

int main ()
{
    list_node * head = input_list();
    int K;
    scanf("%d", &K);
    list_node * new_head = reverse_knode(head, K);
    print_list(new_head);
    return 0;
}
```

