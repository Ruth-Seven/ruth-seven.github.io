---
title: 680. Valid Palindrome II
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-10-26 10:01:17
---

#### [680. Valid Palindrome II](https://leetcode-cn.com/problems/valid-palindrome-ii/)

## 思路：

典型的贪心题 + 二指针。这题还蛮不错的。

<!-- more -->

运用题目给出的最多删一个的关键信息，就可以写出一个简单的算法：用两个指针变量遍历`string`两边，如果有不用的字符。尝试删除掉两个中的一个，判断剩下的字符串是否是Palindrome.



## 代码：

```c++
class Solution {
public:

    bool isPartialPalindrome(string &s, int l, int r)
    {
        while(l < r){
            if(s[l] != s[r]) return false;
            ++l;
            --r;
        }
        return true;
    }
    bool validPalindrome(string s) {
        int l = 0, r = s.size() - 1;
        while(l < r){
            if(s[l] != s[r]){                
                return isPartialPalindrome(s, l + 1, r) || isPartialPalindrome(s, l , r - 1);                 
            }
            ++l;
            --r;
        }
        return true;
        
    }
};
```

