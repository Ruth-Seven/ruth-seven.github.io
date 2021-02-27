---
title: 232. Implement Queue using Stacks
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2021-01-23 18:22:22
---





## [232. Implement Queue using Stacks](https://leetcode-cn.com/problems/implement-queue-using-stacks/)



## 思路：

两个队列一个入队元素，一个出队元素。

<!-- more -->

## 代码：





```c++
class MyQueue {
    stack<int> s1, s2;
public:
    /** Initialize your data structure here. */
    MyQueue() {
        
    }
    
    /** Push element x to the back of queue. */
    void push(int x) {
        s1.push(x);
        // cout << x << endl;
    }
    
    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        if(s2.size() == 0){
            while(s1.size()){
                s2.push(s1.top());
                s1.pop();
            }
        }
        if(s2.size() == 0) return -1;

        int t = s2.top();
        s2.pop();
        return t;
    }
    
    /** Get the front element. */
    int peek() {
        if(s2.size() == 0){
            while(s1.size()){
                s2.push(s1.top());
                s1.pop();
            }
        }
        return s2.top();
    }
    
    /** Returns whether the queue is empty. */
    bool empty() {
        return s1.size() == 0 && s2.size() == 0;
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */
```