---
title: 406. Queue Reconstruction by Height
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-10-15 08:43:44
---

<!-- more -->

## 思路：

贪心策略，因为队列的唯一性，从头到尾`reconstruct`即可。

按`k`升序再按`h`降序，再按`k`值插入。需要在插入的同时统计维护前面身高大于`h`的人数即可。

## 代码：

```c++
class Solution {
public:
    int countBigger(int pos, vector<vector<int>> &people){
        int res = 0;
        for(int i = pos -1; i >= 0; --i){
            if(people[i][0] >= people[pos][0]) res++;
        }
        return res;
    }
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        sort(people.begin(), people.end(), [](vector<int>a, vector<int>b){
            if(a[1] == b[1]) return a[0] < b[0];
            else return a[1] < b[1];
        });
        int n = people.size();
        for(int i = 0; i < n; ++i){
            int c = countBigger(i, people);
            int k = i;
            while(c > people[k][1]){
                if(people[k-1][0] >= people[k][0]) c--;
                swap(people[k], people[k - 1]);
                k--;
                
            }

            
        }
        return people;
    }
};
```

