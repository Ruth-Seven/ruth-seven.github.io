---
title: 20. Valid Parentheses
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2021-01-23 18:22:12
---





## [20. Valid Parentheses](https://leetcode-cn.com/problems/valid-parentheses/)

## 思路：

用栈判断即可。

<!-- more -->

## 代码：

```c++
class Solution {
    stack<char> sta;
public:
    bool isValid(string s) {
        for(auto c : s){
            if(c == '(' || c == '[' || c == '{'){
                sta.push(c);
                continue;
            }
            
            if(sta.size()){
                char topc = sta.top();
                switch(topc){
                    case '(' : 
                        if(c == ')') sta.pop();
                        else return false;
                        break;
                    
                    case '[' : 
                        if(c == ']') sta.pop();
                        else return false;
                        break;
                    
                    case '{' : 
                        if(c == '}') sta.pop();
                        else return false;
                        break;
                }

            }else return false;
        }

        if(sta.empty()) return true;
        else return false;
    }
};
```



map简洁写法

```c++
class Solution {
    stack<char> sta;
public:
    bool isValid(string s) {
        
        map<char, char> pairs = {
            {'[',']'},
            {'(', ')'},
            {'{', '}'}
        };
        for(auto c : s){
            if(pairs.count(c)){
                sta.push(c);
            }
            else{
                if(sta.empty() || pairs[sta.top()] != c) return false;
                sta.pop();
            }
        }
        return sta.empty();
    }
};
```