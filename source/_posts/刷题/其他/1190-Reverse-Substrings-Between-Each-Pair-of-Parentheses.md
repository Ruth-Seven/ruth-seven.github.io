---
title: 1190. Reverse Substrings Between Each Pair of Parentheses
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
categories:
date: 2020-08-07 14:14:44
tags:
---


<!-- more -->

[1190.Reverse Substrings Between Each Pair of Parentheses](https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/)

难度MD
这个题一开始思路就错了，首先是括号匹配问题不能使用左右指针选择，其次是字符串翻转完全可以忽略掉括号（或者说连同括号一起翻转）。
一共有两种思路。



## 思路1

将栈匹配+翻转，复杂度O(n2)O(n2)。

```
class Solution {
public:
    // string reverseParentheses(string s) {
    //     string ns = "";
    //     vector<int> idxl, idxr;
    //     int singbrack = 0, calbrack = 0;
    //     for(int i = 0; i < s.size(); i++){
    //         if(s[i] == '(' || s[i] == ')') singbrack ++;
    //         else ns.push_back(s[i]);
    //     }
    //     singbrack /=  2;
    //     for(int i = 0, j = s.size() - 1; i < j;){
    //         while(i < j && s[i] != '(') i++;
    //         while(i < j && s[j] != ')') j--;
    //         idxl.push_back(i - calbrack);
    //         idxr.push_back(j - singbrack - (singbrack - calbrack - 1)); // reverse 翻转的范围是[),这里注意01错误
    //         i++;
    //         j--;
    //         calbrack ++; 
    //     }
    //     if(calbrack == 0) return ns;
        
    //     for(int i = idxl.size() - 1; i >= 0; i--){
    //         reverse(ns.begin() + idxl[i], ns.begin() + idxr[i]);
    //     }
    //     return ns;
    // }


    string reverseParentheses(string s) {
        string ns = "";
        stack<int> sti;      
        for(int i= 0; i < s.size(); i++){
            if( s[i] == '(')
                sti.push(i);
            else if(s[i] == ')'){
                reverse( s.begin() + sti.top(),  s.begin() + i);
                sti.pop();
            }   
        }
        for(int i = 0; i < s.size(); i++){
            if(s[i] == '(' || s[i] == ')' ) continue;
            ns.push_back(s[i]);
        }
        return ns;
    }
};
```

## 思路2

神奇的黑魔法（这个算法局限于这个应用，感觉挺死板）