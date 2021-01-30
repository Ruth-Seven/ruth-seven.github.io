---
title: 225. Implement Stack using Queues
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
date: 2021-01-30 15:12:26
tags:
categories:
---





## [225. Implement Stack using Queues](https://leetcode-cn.com/problems/implement-stack-using-queues/)





## 思路：	



其实我想到了，但是这个效率真的差。<!-- more -->



## 代码：

```c++
class MyStack {
    queue<int> q1, q2;
public:
    /** Initialize your data structure here. */
    MyStack() {

    }
    
    /** Push element x onto stack. */
    void push(int x) {
        q2.push(x);
        while(q1.size()){
            q2.push(q1.front());
            q1.pop();
        }
        swap(q1 ,q2);
    }
    
    /** Removes the element on top of the stack and returns that element. */
    int pop() {
        int temp = q1.front();
        q1.pop();
        return temp;
    }
    
    /** Get the top element. */
    int top() {
        return q1.front();
    }
    
    /** Returns whether the stack is empty. */
    bool empty() {
        return q1.size() == 0;
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */
```