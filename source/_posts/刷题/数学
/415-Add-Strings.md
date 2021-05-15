---
title: 415. Add Strings
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2021-01-07 11:53:27
---





## [415. Add Strings](https://leetcode-cn.com/problems/add-strings/)

## 思路：

一般的大数相加，不过用高位补零的方法可以大大减少代码复杂度，方便编程。<!-- more -->



## 思路：

```c++
class Solution {
public:
    string addStrings(string num1, string num2) {
        string ans; 
        int add = 0;
        int i = num1.size() - 1, j = num2.size() - 1;
        //低位相加
        while(i >= 0 && j >= 0){
            int sum = add + num1[i--] + num2[j--] - 2 * '0';
            ans = to_string(sum % 10) + ans;
            add = sum / 10;
        }
        
        string c; //剩余高位
        if(i >= 0) c = num1.substr(0, i + 1);
        if(j >= 0) c = num2.substr(0, j + 1);
        string num3; // 高位与add相加
        if(add){
            int k = c.size() - 1;
            while(k >= 0){
                int sum = add + c[k--] - '0';
                num3 = to_string(sum % 10) + num3;//重建一个string太耗时间了
                add = sum / 10;
            }
            if(add) num3 = to_string(add) + num3;
        }else num3 = c;

        return num3 + ans;
    
    }
};
```



优化一下

```c++
class Solution {
public:
    string addStrings(string num1, string num2) {
        string ans; 
        int add = 0;
        int i = num1.size() - 1, j = num2.size() - 1;
        
        while(i >= 0 || j >= 0){
            int a1 = i >= 0 ? num1[i--] - '0' : 0;
            int a2 = j >= 0 ? num2[j--] - '0' : 0;
            int sum = add + a1 + a2;
            ans = to_string(sum % 10) + ans;
            add = sum / 10;
        }
        return (add == 0 ? "" : "1") + ans;
    
    }
};
```

