---
title: z字变换
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
date: 2021-09-23 09:19:10
tags:
categories:
---




#### [6. Z 字形变换](https://leetcode-cn.com/problems/zigzag-conversion/)

## 思路

1. 按行排序（桶排）
2. 按排遍历

<!-- more -->



## 代码

```c++

class Solution {
    int nextCharGap;
public:
    string convert(string s, int numRows) {
        if(numRows == 1) return s;
        nextCharGap = numRows * 2 - 2;
        string res;

        res += getBoundString(s , 0);
        for(int i = 1; i < numRows - 1; i++) {
           res += getMidiumString(s, i, nextCharGap - i);
        }
        res += getBoundString(s, numRows - 1);
        return res;
    }


    int next(string &s, int pos, char &c) {
        int nextPos = pos + nextCharGap;
        if(s.size() <= nextPos) return -1;
        c = s[nextPos];
        return nextPos;
    }

    string getBoundString(string s, int pos) {
        if(pos >= s.size()) return "";
        char c = s[pos];
        string res = string(1, c);

        while(pos >= 0) {
            pos = next(s, pos, c);
            if(pos < 0) break;
            res += c;
        }
        return res;
    }

    string getMidiumString(string s, int pos1, int pos2) {
        if(pos1 > pos2) return ("pos1 <= pos2");
        
        if(pos1 >= s.size()) return "";
        char c1 = s[pos1];
        string res = string(1, c1);
        if(pos2 >= s.size()) return res;
        char c2 = s[pos2];
        res += string(1, c2);
        
        while(pos1 >= 0 || pos2 >= 0) {
            pos1 = next(s, pos1, c1);
            if(pos1 < 0) break;
            res += c1;

            pos2 = next(s, pos2, c2);
            if(pos2 < 0) break;
            res += c2;
        }
        return res;
    }

}; 
//
// p r
// aii
// yhn
// psg
// ai
// l

```

> 想把相同的过程写成一个函数，结果反而写成了一个大麻花。



```c++
class Solution {
public:
    string convert(string s, int numRows) {
        if(numRows == 1 || s.size() == 0) return s;
        int nextCharGap = numRows * 2 - 2;
        string res;

        for(int i = 0; i < numRows; i++) {
            for(int j = i; j < s.size(); j += nextCharGap) {
                res += s[j];
                int bindingPos = (j - j % nextCharGap + nextCharGap) - (j % nextCharGap);
                if((i != 0 && i != numRows - 1) && bindingPos < s.size()) {
                    res += s[bindingPos];
                }
            }
        }
        return res;
    }

}; 
//
// p r
// aii
// yhn
// psg
// ai
// l

```