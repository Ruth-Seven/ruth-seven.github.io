---
title: 318. Maximum Product of Word Lengths
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2021-01-17 18:22:41
---




## [318. Maximum Product of Word Lengths](https://leetcode-cn.com/problems/maximum-product-of-word-lengths/)



## 思路：



为了避免查询时候的重复比较，可以将比较内容变成一个`标志符`，减少了比较时候的重复计算。

进一步的，可以进一步优化重复标志符的查询次数。

<!-- more -->

## 代码：

```c++

class Solution {
public:
    int aderator(string s){
        int pic = 0;
        for(auto &c : s){
            pic |= (1 << (c - 'a'));
        }
        return pic;
    }
    int maxProduct(vector<string>& words) {
        vector<int> pics;
        for(auto &s : words){
            pics.push_back(aderator(s));
        }
        int maxl = 0;
        for(int i = 0; i < pics.size(); ++i){
            for(int j = i + 1; j < pics.size(); ++j){
                if((pics[i] & pics[j]) == 0){
                    maxl = max(maxl, int(words[i].size() * words[j].size()));
                }
            }
        }
        return maxl;
    }
};
```

在上题基础上，用hashmap记录key相同的长度最长的string，减少查询次数。

```c++
class Solution {
public:
    int aderator(string s){
        int pic = 0;
        for(auto &c : s){
            pic |= (1 << (c - 'a'));
        }
        return pic;
    }
    int maxProduct(vector<string>& words) {
        unordered_map<int, int> map;
        for(auto &s : words){
            int key = aderator(s);
            map[key] = max(map[key], (int)s.size());
        }
        int maxl = 0;
        for(auto &[key1, value1] : map){
            for(auto &[key2, value2] : map){
                if((key1 & key2) == 0){
                    maxl = max(maxl, int(value1 * value2));
                }
            }
        }
        return maxl;
    }
};
```