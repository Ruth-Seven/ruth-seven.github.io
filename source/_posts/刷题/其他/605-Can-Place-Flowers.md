---
title: 605. Can Place Flowers
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
categories:
date: 2020-10-13 08:26:22
tags:
---

<!-- more -->



#### [605. Can Place Flowers](https://leetcode-cn.com/problems/can-place-flowers/)

这题还是典型的贪心，不过写的时候nt；

## 思路：

用贪心的策略尽可能先种花，这种策略不会影响结果。只需要在遍历下考虑两边和边界情况就行了。

## 代码：

```c++

class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int res = 0, fn = flowerbed.size();

        for(int i = 0; i < flowerbed.size(); ++i){
            if(flowerbed[i] == 0 && (i == 0 || flowerbed[i - 1] == 0) && (fn - 1 == i ||flowerbed[i + 1] == 0 )){
                 ++res;
                 flowerbed[i] = 1;
             }

        }
        return res >= n;
    }
};
```

版本二：

```c++
class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int res = 0, fn = flowerbed.size();
        if(fn == 1 && flowerbed[0] == 0)
            return n <= 1;
        for(int i = 0; i < flowerbed.size(); ++i){
            if(flowerbed[i] == 0 &&
             ( i == 0 && flowerbed[1] == 0 || i == (fn - 1) && flowerbed[fn - 2] == 0 || (i < fn - 1 && i > 0 && flowerbed[i -1] ==0 && flowerbed[i + 1] == 0))){
                 ++res;
                 flowerbed[i] = 1;
             }

        }
        return res >= n;
    }
};
```

