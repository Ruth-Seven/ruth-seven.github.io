---
title: 167. Two Sum II - Input array is sorted
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-10-17 08:41:18
---

<!-- more -->

## 思路：

双指针遍历。复杂度$O(n)$。

## 代码：

```c++
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int n = numbers.size();
        int l = 0, r = n - 1;
        while(l < r){
            int s = numbers[l] + numbers[r];
            if(s > target) r--;
            else if(s < target) l++;
            else break;
        }
        // vector<int> v(2,0);
        // v[0] = l + 1; v[1] = r + 1;
        // return v;
        return {l + 1, r + 1};    
    }
};
```

