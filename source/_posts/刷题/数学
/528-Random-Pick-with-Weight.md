---
title: 528. Random Pick with Weight
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2021-01-10 10:05:09
---




## [528. Random Pick with Weight](https://leetcode-cn.com/problems/random-pick-with-weight/)

## 思路：

通过前缀和映射权重到数组，方便通过二分查找进行随机抽取。

<!-- more -->

## 代码：

```c++
class Solution {
    vector<int> w;
    int n;
    int mod;
public:
    Solution(vector<int>& _w) : w(_w) {
        int sum = 0;
        for(auto &i : w){
            sum += i;
            i = sum;
        }
        mod = sum;
        n = w.size();
    }
    
    int pickIndex() {
        int s = rand() % mod; // 在[0, sum) 随机抽取一个数，作为映射下标
        auto it = lower_bound(w.begin(), w.end(), s); // find the first iterator that this element is not less the value; value <= (*it)
        if(*it == s) it++;
        return it - w.begin();
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(w);
 * int param_1 = obj->pickIndex();
 */
```

手写二分

```c++
class Solution {
    vector<int> w;
    int n;
    int mod;
public:
    Solution(vector<int>& _w) : w(_w) {
        int sum = 0;
        for(auto &i : w){
            sum += i;
            i = sum;
        }
        mod = sum;
        n = w.size();
    }
    
    int pickIndex() {
        int s = rand() % mod; // 在[0, sum) 随机抽取一个数，作为映射下标
        int l = 0, r = n - 1;
        while(l < r){
            int mid = (r - l) / 2 + l;
            if(w[mid] <= s) l = mid + 1;
            else r = mid;
        }
        return r;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(w);
 * int param_1 = obj->pickIndex();
 */
```