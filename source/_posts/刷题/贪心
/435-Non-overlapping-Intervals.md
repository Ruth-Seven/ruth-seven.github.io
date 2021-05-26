---
title: 435. Non-overlapping Intervals
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-10-12 09:19:14
---

还是蛮经典的题，想了想就出来了。

<!-- more -->

## 思路：

求出最少舍弃的区间，换一个角度就是留下更多的区间。为了留下的区间最多，直观上来看最好是区间长度小，起点和终点都小的区间。

通过仔细的思考，只有终点最小才能满足区间尽可能留下的条件。



## 代码：

```c++


bool cmp(vector<int>& a, vector<int>& b){
    if(a[1] == b[1])
        return a[0] < b[0];
    else return a[1] < b[1];

}
class Solution {
public:

    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        // bool (Solution::*cmpabc)(vertor<int>, vertor<int>);
        // cmpabc = &Solution::cmpab;
        int n = intervals.size();
        // for(int i = 0; i < n; i++)
        //     intervals[i].push_back(intervals[i][1] - intervals[i][0]);

        sort(intervals.begin(), intervals.end(), cmp);

        int add = 0, start = -0x7fffffff;
        for(int i = 0; i < n; ++i){
            if(start <= intervals[i][0]){
                add++;
                start = intervals[i][1];
            }
        }
        return n - add;
    }
};
```

> `sort(intervals.begin(), intervals.end(), [](vector<int>& a, vector<int>& b){return a[1] < b[1];});`最后的`sort`可以用匿名函数写写。
