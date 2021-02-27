---
title: 739. Daily Temperatures
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2021-01-23 18:21:51
---



## [739. Daily Temperatures](https://leetcode-cn.com/problems/daily-temperatures/)



## 思路：

1. 单调栈；用单调栈维护从后往前遍历当前元素的最大值，便可以轻松获取当前元素之后的最大值下标，即可以更新下一个更大元素的时间差。

2. KMP失败匹配算法；从后往前遍历，当前元素的更大值要么是当前元素的下一个元素，要么是下一个元素的更大值，要么是下一个元素的更大值的更大值……如此“递归”查找可得下一个最大值。如果查找不到，就不存在最大值。

   <!-- more -->



## 思路：





```c++
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& T) {
        int n = T.size();
        stack<int> pos, val;
        vector<int> day(n);
        for(int i = n - 1; i >= 0; --i){

            if(!val.empty()){
                while(val.size() && val.top() <= T[i]){
                    val.pop();
                    pos.pop();
                }
            }
            if(val.empty()) day[i] = 0;
            else day[i] = pos.top() - i;

            if(val.empty() || val.top() >=  T[i]){
                pos.push(i);
                val.push(T[i]);
            }
        }
        return day;
    }
};
```

简化版

```c++
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& T) {
        int n = T.size();
        stack<int> pos, val;
        vector<int> day(n);
        for(int i = n - 1; i >= 0; --i){

            while(val.size() && val.top() <= T[i]){
                  
                val.pop();
                pos.pop();
            }
            if(val.size())day[i] = pos.top() - i;
            if(val.empty() || val.top() >=  T[i]){ //  取smaller元素加入队列，也可以直接添加，毕竟上面有pop;
                pos.push(i);
                val.push(T[i]);
            }
        }
        return day;
    }
};
```



```c++
// KPM构造数组思路启发得来
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& T) {
        int n = T.size();
        vector<int> day(n);
        for(int i = n - 2; i >= 0; --i){
            int pos = i + 1;
            while(T[pos] <= T[i]){  // 尽量从day偏移更多元素
                if(day[pos] == 0) break; // 此后没有更大的元素
                pos += day[pos];
            }
            if(T[pos] > T[i]) day[i] = pos - i;
        }
        return day;
    }
};


```