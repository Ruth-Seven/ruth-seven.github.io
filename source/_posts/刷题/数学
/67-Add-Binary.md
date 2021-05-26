---
title: 67. Add Binary
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2021-01-12 11:10:02
---




## [67. Add Binary](https://leetcode-cn.com/problems/add-binary/)

<!-- more -->

## 代码：

```c++
class Solution {
public:
    string addBinary(string a, string b) {
        if(a == "" || b == "") return a == "" ? b : a;
        int i = a.size() - 1, j = b.size() - 1, add = 0;
        string ans = "";
        while(i >= 0 || j >= 0){
            int numa = i < 0 ? 0 : a[i] - '0';
            int numb = j < 0 ? 0 : b[j] - '0';
            --i, --j;
            int sum = numa + numb + add;
            add = sum / 2;
            sum %= 2;
            ans.push_back(sum + '0');
        }
        if(add){
            ans.push_back(add + '0');
        }
        reverse(ans.begin(), ans.end());
        return ans;

    }
};
```