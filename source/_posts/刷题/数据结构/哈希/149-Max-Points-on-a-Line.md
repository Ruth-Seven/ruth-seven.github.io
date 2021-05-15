---
title: 149. Max Points on a Line
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2021-01-27 23:23:34
---







## [149. Max Points on a Line](https://leetcode-cn.com/problems/max-points-on-a-line/)



## 思路：



思路差不多，但是走歪了。害~

> 整体思路是两层嵌套的for循环。两点可以确定一条直线，那么选择固定一个点，求其他点与固定点的斜率，如果斜率相同，那么斜率相同的点在同一条直线上。
> 同时要考虑，斜率可能为无穷大，也有可能两个点为同一个点。键值应该为斜率。
>
> 通过dup记录这一次内层循环中与p1相同的点。
> 通过one_round_res统计每一次内层for循环的结果。
> 将斜率无穷大定义为FLT_MAX。
>
> 键值key为斜率，其数据类型选择为long double即可通过
> `vector<vector<int>> points = { {0,0},{94911150,94911151},{94911151,94911152} };`
> 来源：[力扣（LeetCode）](https://leetcode-cn.com/problems/max-points-on-a-line/solution/cha-xi-biao-jie-fa-bu-xu-yao-jiang-xie-l-ayf2/)
><!-- more -->

## 代码：

```c++
class Solution {
public:
    int maxPoints(vector<vector<int>>& points) {
        if(points.size() == 0 ) return 0;
        int maxct = 1;        
        for(int i = 0; i < points.size(); ++i){
            // 记录经过一个点所有直线，即使斜率为无穷大
            // 因为只有一个点，无需记录直线公式中的x = c 和 x = k * y + b 中的 c, b
            unordered_map<long double, int> record; 
            int ct = 1;
            int depu = 0;
            for(int j = i + 1; j < points.size(); ++j){                
                auto p1 = points[i];
                auto p2 = points[j];
                if(p1 == p2){  // 重合点
                    ++depu;
                    continue;
                }
                if(p1[0] > p2[0]) swap(p1, p2);
                if(p2[0] == p1[0]){                    
                    ct = max(ct, ++record[DBL_MAX] + 1);                                     
                }else{
                    long double k = (long double)(p2[1] - p1[1]) / (p2[0] - p1[0]);
                    // double b = p2[1] - k * p2[0];                                     
                    ct = max(ct, ++record[k] + 1);
                }                                
            }            
            maxct = max(maxct, ct + depu);
        }        
        return maxct;
    }
};
```