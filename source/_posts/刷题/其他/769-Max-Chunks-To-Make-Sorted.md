---
title: 769. Max Chunks To Make Sorted
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2021-01-22 11:31:42
---



## [769. Max Chunks To Make Sorted](https://leetcode-cn.com/problems/max-chunks-to-make-sorted/)





## 思路：

暴力法。

简单的思路，

从左到右划分chrunk，判断最左边的chrunk最大值，其值+1就是chrunk的size。

依次进行就可以获得多个chrunk的size。<!-- more -->



## 代码：

```c++
class Solution {
public:
    int maxChunksToSorted(vector<int>& arr) {
        int split = -1;
        int num = 0;
        for(int i = 0; i < arr.size(); ++i){
            split = arr[i];
            for(int j = 0; j < split + 1; ++j){
                split = max(split, arr[j]);
            }
            num++;
            i = split;
        }
        return num;
    }
};
```