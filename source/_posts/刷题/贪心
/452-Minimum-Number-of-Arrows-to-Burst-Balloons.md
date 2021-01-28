---
title: 452. Minimum Number of Arrows to Burst Balloons
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-10-13 08:26:09
---

#### [452. Minimum Number of Arrows to Burst Balloons](https://leetcode-cn.com/problems/minimum-number-of-arrows-to-burst-balloons/)

类似于leetcode435贪心题

<!-- more -->





## 思路：

用贪心的策略尽可能的射击气球末尾，可以用末尾排序，遍历增加箭数即可。

## 代码：

> 按气球开始排序，与原本思路上的思路等价

```c++
class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        sort(points.begin(), points.end(), [](vector<int> a, vector<int> b)
            {   
                if(a[0] == b[0]) return a[1] < b[1];
                else return a[0] < b[0];}
            );
        

        int num = 0;
        int end = -1;
        for(int i = 0; i < points.size();){
            num++;
            end = points[i][1];
            i++;
            while(i < points.size() && end >= points[i][0]){             
                end = min(end, points[i][1]);
                i++;
           
            } 

        }
        return num;
    }
};
```



