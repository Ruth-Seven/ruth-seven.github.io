---
title: 218. The Skyline Problem
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2021-01-26 11:16:58
---

<!-- more -->



## [218. The Skyline Problem](https://leetcode-cn.com/problems/the-skyline-problem/)







## 思路：

扫描线算法：

想像一根竖线，从左到右进行扫描，记录下当前竖线所有线段的高度（除去左端点），每遇到一个端点就挑选出最高点，并输出即可。这里可以观察到，此算法把一根直线拆分两个端点来看待，遇到右端点就记录维持该线段的高度，遇到左端点就删除该线段的高度。



具体算法，直接看代码，其中左端点的Height取负值记录非常巧妙，既利用了set集合的升序性质，同时在遍历的时优先选择了新建筑，不至于产生“建筑间的空隙”。

## 代码：

```c++
class Solution {
public:
    vector<vector<int>> getSkyline(vector<vector<int>>& buildings) {
        multiset<pair<int, int>> loc;
        for(auto &e : buildings){
            loc.insert({e[0], -e[2]});
            loc.insert({e[1], e[2]});
        }
        vector<vector<int>> ans;
        vector<int> last{0,0};
        multiset<int> height{0}; //多个高度可能相同
        cout << last[0] << endl;

        for(auto &[pos, h] : loc){
            if(h < 0) height.insert(-h);
            else height.erase(height.find(h));

            int maxh = *height.rbegin();
            // cout << pos << ' ' << h << ' ' << maxh << endl;
            if(maxh != last[1]){
                last[0] = pos;
                last[1] = maxh;
                ans.emplace_back(last);                
            }
        }
        return ans;

    }
};


```