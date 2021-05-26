---
title: 451. Sort Characters By Frequency
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-11-16 09:15:47
---




## [451. Sort Characters By Frequency](https://leetcode-cn.com/problems/sort-characters-by-frequency/)

## 思路：

统计每个字符出现的频率， 按频率排序或者建立堆获取最大值。

<!-- more -->

>  击败100

## 代码：

```c++

class Solution {
public:
    string frequencySort(string s) {
        int count[258] = {0};
        int len = s.size();
        for(int i = 0; i < len ; ++i){
            count[s[i]]++;
        }
        priority_queue< pair<int, int>, vector<pair<int, int>>, less<pair<int, int> > > pq; 
        for(int i = 0; i < 258; ++i){
            if(count[i] != 0)
                pq.push( make_pair(count[i], i));
        }
        string ans = "";
        while(pq.size()){
            pair<int, int> t = pq.top(); 
            pq.pop();
            int time = t.first;
            int ichar = t.second;
            string single(time, (char)ichar);
            ans +=  single;        
        }
        return ans;
    }
};
```