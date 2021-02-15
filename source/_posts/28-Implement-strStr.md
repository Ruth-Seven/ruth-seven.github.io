---
title: 28. Implement strStr()
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
date: 2021-02-15 10:18:48
tags:
categories:
---





## 思路：

经典的字符子串匹配问题：

1. 暴力匹配，$O(mn)$
2. Rabin Karp $O(n)$
3. [KMP算法](https://leetcode-cn.com/problems/implement-strstr/solution/shi-xian-strstr-by-leetcode/)

<!-- more -->

## 代码：



```c++
class Solution {
public:
    //暴力
    int strStr(string haystack, string needle) {
        int m = haystack.size(), n = needle.size();
        if(n == 0) return 0;

        int k = 0, j = 0;
        //aaaaaf
        //-----fs
        while(k <= m - n){ 
            while(j < n && haystack[k] == needle[j]) ++k, ++j;
            if(j == n) return k - j;
            k = k - j + 1;
            j = 0;
        }
        return -1;
    }
};
```





```c++
class Solution {
public:
    //暴力
    

    int strStr(string haystack, string needle) {
        auto tonum = [](char a){return a -  'a';};
        int m = haystack.size(), n = needle.size();
        if(n == 0) return 0;
        using ktype =  long long;
        ktype base = 26, key = 0; //MOD 超过上限自然溢出?
        ktype point = 0, hpow = 1, MOD = 1e9 + 7;

        for(int i = 0; i < n; ++i){ // 字符串前位权重高
            key = (key * base + tonum(needle[i])) % MOD;
            hpow = (hpow * base) % MOD; // bugs
            point = (point * base + tonum(haystack[i])) % MOD;
        }
        // if(point < 0 || key < 0) cout << "+";
        if(key == point) return 0;
        for(int j = n; j < m; ++j){    
            point = (((point * base  - tonum(haystack[j - n]) * hpow) % MOD + MOD) + tonum(haystack[j])) % MOD; //疯狂使用运算符限制和e取余运算防止溢出
            // if(point < 0 ) cout << '-';
            if(key == point){
                return j - n + 1;
            }
        }

        return -1;
    }
};
```

