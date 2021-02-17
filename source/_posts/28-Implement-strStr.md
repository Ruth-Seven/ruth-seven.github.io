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

### KMP算法

KMP算法的核心在于`next`数组，其`next[i]`记录了字符串`str[0...i]`的最长相同前后缀子串（不包括子串本身）的前缀尾下标。如此，我们在母子串在匹配`i`（母串`Sa`），`j`（子串`Sb`）失败时，子串的`k = next[j - 1]`记录了保证了最长`Sa`与`Sb[0, k]`可匹配成功（`k`不断减小，但`i`没有减小），重新判断`Sa[i]==?Sb[k+1]`即可。重复这个步骤，直到`k`无法缩小，或者匹配成功。若成功，`++i`，`++j`；若失败，则`++i`，`j=0`。

但在此之前，还有构造`next`数组。神奇的是，`next[i]`构造与匹配的过程极其类似。首先`next[0] = -1`。记`k = next[i - 1]`，比较`Sb[k + 1] == ? Sb[i]`，若成功，则`Sb[i]= k + 1`；若失败，则寻找更小的公共前后缀（为了寻找最长的公共前缀长度，利用了`Sb[0,..,i-1]`子串的最长前缀后子串，以及更短的前后缀子串！（后两者的性质保证了属于前者的后缀子串✨✨）），缩小`k`为`next[k]`，再次比较。其中`k>-1`。如果还是失败了，明显的不存在相同的前后缀子串`next[i] = -1`。





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





```c++
class Solution {
public:
    //KMP     100% 

    int strStr(string haystack, string needle) {

        int n = haystack.size(), m = needle.size();
        if(m == 0 ) return 0;
        vector<int> next(m, -1); //next[i] 为needle[0,...., i]相同最长前后缀的前缀末下标
        
        for(int i = 1; i < m; ++i){
            int k = next[i - 1]; // needle[0,...., i - 1]相同最长前后缀的前缀末下标
            while(k != -1 && needle[k + 1] != needle[i]){ // 尝试扩展前后缀 needle[0, k + 1], needle[,..,i-1,i]
                k = next[k]; //匹配失败，缩短前后缀
            }
            if(needle[k + 1] != needle[i]) next[i] = -1;
            else next[i] = k + 1;
            // cout << next[i] << endl;
        }

        int i = 0, j = 0;
        for(; i < n; ++i ){ // i, j 为当前匹配的下标字符
            while(haystack[i] != needle[j] && j > 0){  // 两串匹配失败，且j可压缩
                j = next[j - 1] + 1; // 压缩needle串的最长相等前后缀长度， 最小为0
            }
            if(haystack[i] == needle[j]){
                ++j;
                if(j == m) return i - j + 1;
            }

        }
        return -1;
    }
};






```

