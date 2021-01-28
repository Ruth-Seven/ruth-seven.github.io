---
title: 155. Min Stack
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2021-01-23 18:22:02
---




## [155. Min Stack](https://leetcode-cn.com/problems/min-stack/)



## 思路：

用另一个栈保存另一个栈的各个元素插入，删除后的最小值。

他利用这么一个现象：后插入的大元素不会影响这个栈的最小值，反之小元素会改变。那么只要把此时小元素插入到最小栈即可，同理删除元素的时候也按值删除。

<!-- more -->

## 代码：







```c++
class MinStack {
    stack<int> s1, mins;
public:
    /** initialize your data structure here. */
    MinStack() {

    }
    
    void push(int x) {
        s1.push(x);
        if(mins.empty() || mins.top() >= x){
            mins.push(x);
        }
    }
    
    void pop() {
        if(s1.size()){
            int f = s1.top();
            s1.pop();
            if(mins.size() && f == mins.top()){
                mins.pop();
            }
        }
    }
    
    int top() {
        return s1.top();
    }
    
    int getMin() {
        return mins.top();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
```

