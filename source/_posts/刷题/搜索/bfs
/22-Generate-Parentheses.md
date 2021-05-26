---
title: 22. Generate Parentheses
thumbnail: 'http://static.come2rss.xyz/simptab-wallpaper-20201027164551.png'
toc: true
top: 10
date: 2021-04-26 07:41:25
tags:
categories:
---







## 思路：

正确的迭代方式是，从左到右的遍历中，每一个正确序列都有左括号的数量大于等于右括号的数量。而每一处符号要么是左括号，要么是右括号，后者符号都有选择的生成即可。

如何便可以递归生成所有符合题意的括号。

<!-- more -->

## 代码：

```c++
class Solution {
    vector<string> ans;
    set<string> sset;
public:
    vector<string> generateParenthesis(int n) { 
        generateParenthesisCore(0, 0, n, "");
        for(string s : sset) ans.push_back(s);
        return ans;
    }
    void generateParenthesisCore(int left, int right, int n, string str){
        if(left == n){
            ans.push_back(str + string((n - right), ')'));
            return;
        }

        generateParenthesisCore(left + 1, right, n, str + "(");
        if(left > right){
            generateParenthesisCore(left, right + 1, n, str + ")");
        }
        
    }
};
```

