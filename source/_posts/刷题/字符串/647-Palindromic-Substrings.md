---
title: 647. Palindromic Substrings
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
date: 2021-02-14 21:02:17
tags:
categories:
---





# [647. Palindromic Substrings](https://leetcode-cn.com/problems/palindromic-substrings/)1



## 思路：

`Manacher`算法：

回文字符串的判断方式方式会从中心点从发向外不断扩展，`Manacher`算法给出了缩减了字符串判断回文的重复步骤。其核心思想在于，一段回文`s`上的呈对称状的左右`A`和`B`两点，`B`点的最小回文长度可以通过`A`点的回文长度和`B`到`s`边右边界的长度最小值决定。另外，为了改变回文串长度为偶数和奇数的不同，在每个字符前和后都插入一个`#`，如此插入后的`T`的最长回文串**半径**`d`，与`S`最长回文串**半径**的`k`有， `k = [d / 2]` 。

> `[]`向下取整。

<!-- more -->



## 代码：



```c++
class Solution {
public:
    int countSubstrings(string s) {
        string t = "!#"; // 插入哨兵
        for(char c : s){
            t += c + string("#"); 
        }
        t +="$";
        int amount = 0, n = t.size();
        vector<int> f(n);
        int curmid = 1, right = 1;
        for(int i = 1; i < n; ++i){
            int j = curmid * 2 - i;
            int len = i > right ? 1 : min(f[j], right - i + 1);
            while(t[i + len] == t[i - len]) ++len; //$ !作为哨兵自动控制边界
            f[i] = len;
            if(i + len - 1 > right){
                curmid = i;
                right = i + len - 1;
            }
            amount += f[i] / 2;
            // cout<< f[i] << " ";
        }
        // cout << endl;
        return amount;
    }
};
```

