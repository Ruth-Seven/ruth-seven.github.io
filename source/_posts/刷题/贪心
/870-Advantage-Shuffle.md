---
title: 870. Advantage Shuffle
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
date: 2021-02-05 20:38:14
tags:
categories:
---




# [870. Advantage Shuffle](https://leetcode-cn.com/problems/advantage-shuffle/)





## 思路

一看就是贪心

从小到大逐个寻找B的牌`b`，找出一个刚刚好比`b`大的在A中的牌`a`。因为`a`刚刚比`b`大，所以最优。找出后，加入映射，最后重构数组即可。<!-- more -->

## 代码

下饭操作

```c++
class Solution {
public:
    vector<int> advantageCount(vector<int>& A, vector<int>& B) {
        int n = A.size();
        vector<int> sortb(B);
        sort(A.begin(), A.end());
        vector<int> leftA;
        sort(sortb.begin(), sortb.end());
        // unordered_multimap<int, int> map;
        multimap<int, int> map; // 可以用 unorder_map<int, deque<int>> 代替， 代码更简洁
        int g = 0;
        for(auto b : sortb){
            while(g < n && A[g] <= b)
                leftA.push_back(A[g++]);               
            if(g < n)
                map.insert({b, A[g++]});                
        }
        int k = 0;
        for(int i = 0; i < n; ++i){
            auto it = map.lower_bound(B[i]);
            if(it != map.end()){
                auto [b, a]= *it;
                if(b == B[i]){
                    A[i] = a;
                    map.erase(it);
                }
            } 
            else A[i] = leftA[k++];
        }
        return A;
    }
};
```



