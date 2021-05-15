---
title: 3. Longest Substring Without Repeating Characters
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
date: 2021-02-18 13:25:07
tags:
categories:
---



# [3. Longest Substring Without Repeating Characters](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/)



## 思路：

1. 暴力
2. 双指针

> 可以观察到，符合题意的子串在按左端下标从小到大排序时，右端下标也是非严格递增的。
>
> 惊喜的是，双指针便可以派上用场了，`i`，`j`分别指向子串两端，并维护不重复的性质即可。

<!-- more -->

## 代码：

暴力：

```c++
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        
        int ct= 0;
        for(int i = 0; i < s.size(); ++i){
            vector<int> pos(259, -1);
            for(int j = i; j < s.size(); ++j){
                if(pos[s[j]] != -1) break;
                pos[s[j]] = 1;
                ct = max(ct, j - i + 1);
            }
        }
            
        return ct;
    }
};
```



双指针

```c++
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        
        unordered_set<char> hash;
        int i, j, ct, n = s.size(); 
        i = j = ct = 0;
        while(j < n){
            if(!hash.count(s[j])){
                ct = max(ct, j - i + 1);
                hash.insert(s[j++]);
            } 
            else{
                hash.erase(s[i++]);
            }
        }
        return ct;
    }
};
```

