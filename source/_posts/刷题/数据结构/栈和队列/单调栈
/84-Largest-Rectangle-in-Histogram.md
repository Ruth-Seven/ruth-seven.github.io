---
title: 84. Largest Rectangle in Histogram
thumbnail: 'http://static.come2rss.xyz/simptab-wallpaper-20201027164551.png'
toc: true
top: 10
date: 2021-04-30 11:24:11
tags:
categories:
---

<!-- more -->

# [84. Largest Rectangle in Histogram](https://leetcode-cn.com/problems/largest-rectangle-in-histogram/)



## 思路：

1. 遍历高度数组的同时，维护形成的矩阵，并更新最大面积。
2. 观察，矩阵的面积可以不严格递增的情况下在从左到右扩展的，再严格递减的情况下可以确定出矩阵面积。正向数据缓存，逆向面积计算-> 单调栈。[read more](https://leetcode-cn.com/problems/largest-rectangle-in-histogram/solution/bao-li-jie-fa-zhan-by-liweiwei1419/)
3. 







## 代码：

```c++
class Solution {
    map<int, pair<int,int>> reg;
public:
    int largestRectangleArea(vector<int>& heights) {
        int maxarea = 0;
        for(int i = 0; i < heights.size(); ++i){
            
            for(auto &item : reg){
                auto high = item.first; 
                auto &pii = item.second;
                auto l = pii.first;
                auto &r = pii.second;
                if(high > heights[i]){
                    reg.insert({heights[i], {l, i}});
                    maxarea = max(maxarea, heights[i] *(i - l + 1));
                    reg.erase(reg.find(high), reg.end());
                    
                    break;
                } 
                else if(high <= heights[i]){
                    r = i;
                    maxarea = max(high * (r - l + 1), maxarea);
                }
            }
            if(reg.count(heights[i]) == 0){
                reg.insert({heights[i], {i, i}});
                maxarea = max(maxarea, heights[i]);
            }
        }
        return maxarea;
    }
};
```





```c++
class Solution {
    stack<int> s;
public:
    int largestRectangleArea(vector<int>& heights) {
        int maxarea = 0;
        heights.push_back(0); // 为了计算所有面积
        for(int i = 0; i < heights.size(); ++i){
            if(s.empty()) s.push(i);
            else if(heights[s.top()] < heights[i]) s.push(i);
            else if(heights[s.top()] == heights[i]) s.top() = i; // 如果相邻的高度相同，则更新；因为不更新单调栈中矩阵左边界会扩展更多
            else if(heights[s.top()] > heights[i]){         
                while(!s.empty() && (heights[s.top()] > heights[i])){                    
                    int high = heights[s.top()]; 
                    s.pop();
                    int temparea = ( i - (s.empty() ? -1 : s.top()) - 1) * high;
                    maxarea = max(maxarea, temparea);
                }
                s.push(i);   
            }   
        }
        return maxarea;
    }
};
```

> 当然，这里也可以添加一个哨兵，不过没什么影响。
>
> 