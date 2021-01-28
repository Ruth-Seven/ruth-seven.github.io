---
title: 932. Beautiful Array
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2021-01-04 10:17:46
---




## [932. Beautiful Array](https://leetcode-cn.com/problems/beautiful-array/)

## 思路：

这题的难度是怎么想出一个策略来保存漂亮数组的存在。<!-- more -->

将1~N的数字划分为奇数和偶数，并放到数组两边，即可保证。同时可以发现仿射变化对漂亮数组的性质没有影响。
$$
2 *(k *  a[k] + b) =  k *  a[i] + b + k *  a[j] + b
$$


那么就有任意一边的数字都可以通过仿射变化变为`1-(N/2+1/2)`的问题。比如，原本左边有$(n + 1) / 2$个奇数数字，右边有$N/2$个偶数数字。那么左边的奇数数字可以通过仿射变化$a[i]'= a[i]/2 + 1/2$，右边的偶数数字可以通过仿射变化$a[i]'= a[i]/2$，将问题分解成了规模减半的两个子问题。

通过递归分治我们可以解决该问题。

## 代码：

100%

```c++
class Solution {
public:
    vector<int> beautifulArray(int N) {
        vector<int> arr(N);
        for(int i = 0; i < arr.size(); ++i)
            arr[i] = i + 1;
        f(0, N - 1, N, arr);
        return arr;
    }

    void f(int s, int e, int N, vector<int> &arr){
        if(s == e){
            arr[s] =  1;
            return;
        }
        int odd = (N + 1) / 2;
        f(s, s + odd - 1, odd, arr);
        for(int i = s; i < s + odd; i++)
            arr[i] = arr[i] * 2 - 1;
        f(s + odd, e, N - odd, arr);
        for(int i = s + odd; i <= e; ++i)
            arr[i] = arr[i] * 2;
    }
};
```