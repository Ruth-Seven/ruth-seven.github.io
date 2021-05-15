---
title: 239. Sliding Window Maximum
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2021-01-25 15:45:02
---







## [239. Sliding Window Maximum](https://leetcode-cn.com/problems/sliding-window-maximum/)

## 思路：



想了三种方法：

1. 朴素地确认最大值是否在窗口内
2. 使用优先队列维护窗口中的最值，但是需要注意最值是否还在窗口内
3. 使用单调双头队列维护窗口内的单调队列

> 方法3的单调队列其实和单调栈的性质如出一辙，只不过换了个队列的性质。



<!-- more -->

## 代码：

tle

```c++
class Solution {
public:
    
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int n = nums.size();
        if(k > n) return vector<int>();
        vector<int> ans(n - k + 1);
        auto p = max_element(nums.begin(), nums.begin() + k);
        ans[0] = *p;
        for(int i = 1; i < n - k + 1; ++i){
            if(nums[i - 1] == *p){
                p = max_element(nums.begin() + i, nums.begin() + i + k);
            }
            if(*(nums.begin() + i + k - 1) > *p)
                p = nums.begin() + i + k - 1;
            ans[i] = *p;
        }
        return ans;

    }
    
};
```





优先队列 

$o(nlogn)$



```c++
class Solution {
public:
    
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int n = nums.size();
        if(k > n) return vector<int>();
        vector<int> ans(n - k + 1);
       
        priority_queue<pair<int, int>> pq;
        for(int i = 0; i < k; ++i) pq.push({nums[i], i});
        ans[0] = pq.top().first;
        for(int i = 1; i < n - k + 1; ++i){
            pq.push({nums[i + k - 1], i + k - 1});
            auto [val, idx] = pq.top();
            while(idx < i){
                pq.pop();
                val = pq.top().first;
                idx = pq.top().second;
            }
            ans[i] = val;
        }
        return ans;
    }
    
};
```



双头单调队列！

```c++
class Solution {
public:
    
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int n = nums.size();
        if(k > n) return vector<int>();
        vector<int> ans(n - k + 1);
       
        deque<int> que; // 单调递减的队列
        for(int i = 0; i < n; ++i){
            if(i >= k && nums[i - k] == que.front()){ // 特定元素删除pop
                que.pop_front();
            }
            
            int t = nums[i];
            while(que.size() && que.back() < t){ // 很像单调栈的维护过程
                que.pop_back();
            }
            que.push_back(t);

            if(i >= k - 1) ans[i - k + 1] = que.front();  // 记录
        }
        
        return ans;
    }
    
};
```