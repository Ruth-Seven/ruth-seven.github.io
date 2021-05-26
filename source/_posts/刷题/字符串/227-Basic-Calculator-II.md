---
title: 227. Basic Calculator II
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
date: 2021-02-12 20:22:37
tags:
categories:
---



# [227. Basic Calculator II](https://leetcode-cn.com/problems/basic-calculator-ii/)



## 思路

经典的中缀转后缀练手题，但是我偏不。

在遍历字符串把数字和运算符存储到一个数字栈和运算栈中，考虑到运算顺序是乘除>加减，且左边>右边，所以在压入新运算符`op`前把栈中优先级大于等于`op`的运算法弹出，并计算。

遍历完了运算栈可能还有运算符，逆向计算即可。最后数据栈弹出结果就完事。



## 代码

```c++
class Solution {
public:
    using ull = unsigned long long;
    ull func(char c, ull num1, ull num2){
        if(c == '+') return num1 + num2;
        if(c == '-') return num1 - num2;
        if(c == '*') return num1 * num2;
        if(c == '/') return num1 / num2;
        return 0;
    }
    int calculate(string s) {
        s += ']';
        stack<char> op;
        stack<ull> num;
        map<char, int> pri{{'+', 1},{'-', 1},{'*', 2},{'/', 2}};
        ull cal = 0;
        for(auto c : s){
            if(isdigit(c)) cal = cal * 10 + c - '0';
            else{
                if(c == ' ') continue;
                // cout << c << ' ' << cal << endl; 
                num.push(cal); 
                cal = 0;
                if(c == ']') continue;
                
                while(op.size() &&  pri[c] <= pri[op.top()]){
                    int num2 = num.top(); num.pop();
                    int num1 = num.top(); num.pop();
                    num.push( func(op.top(), num1, num2) );
                    op.pop();
                }
                op.push(c);
            }
        }
        // cout << num.size() << ' ' << op.size() << endl;
        while(op.size()){
            int num2 = num.top(); num.pop();
            int num1 = num.top(); num.pop();
            num.push( func(op.top(), num1, num2) );
            op.pop();
        }
        return num.top();


    }
};
```

