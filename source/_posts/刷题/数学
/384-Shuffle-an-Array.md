---
title: 384. Shuffle an Array
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2021-01-09 19:33:02
---



## 思路：

Fisher-Yates shuffle洗牌算法：逐个遍历交换后续随机元素。

<!-- more -->

## 代码

反洗算法

```c++
class Solution {
    vector<int> origin;
public:
    Solution(vector<int>& nums) :origin(nums) {}
    
    /** Resets the array to its original configuration and return it. */
    vector<int> reset() {
        return origin;
    }
    
    /** Returns a random shuffling of the array. */
    vector<int> shuffle() {        
        vector<int> shuffled(origin); 
        if(origin.size() == 0) return shuffled;
        for(int i = origin.size() - 1; i >= 0; --i){ //还可以反着洗
            swap(shuffled[i], shuffled[rand() % (i + 1)]);
        }
        return shuffled;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(nums);
 * vector<int> param_1 = obj->reset();
 * vector<int> param_2 = obj->shuffle();
 */
```

