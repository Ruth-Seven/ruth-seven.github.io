---
title: 32. Longest Valid Parentheses
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
date: 2021-04-25 16:25:41
tags:
categories:
---


<!-- more -->



## 思路： 

栈验证匹配括号很简单，但是用如何获取多个匹配成功的括号组合长度就很麻烦！

难的是想到，连续的有效括号`()())()()`只需要记录一个最先未匹配的位置。具体做法是，在栈中存储一个最后没有匹配到的右括号下标。





## 代码

```c++
class Solution {
public:
    int longestValidParentheses(string s) {
        int maxlen = 0; 
        stack<int> st;
        
        st.push(-1); // 压入一个最后未匹配的)。
        for(int i = 0; i < s.size(); ++i){
            if(s[i] == ')'){
                st.pop();
                if(!st.empty()){ // 刚刚的）匹配成功，可以计算最长匹配
                    maxlen = max(maxlen, i - st.top()); 
                }else st.push(i); // 说明该)没有匹配到，是新的最后的最右括号
            }else st.push(i);
        }
        return maxlen;
    }
};

```

