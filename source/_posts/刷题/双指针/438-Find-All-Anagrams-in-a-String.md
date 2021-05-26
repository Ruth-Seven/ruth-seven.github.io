---
title: 438. Find All Anagrams in a String
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
date: 2021-04-30 13:15:01
tags:
categories:
---








## 思路：

双指针，指向模式串`str`的子串首位`s`和末尾+1`e`。

遍历思路：

1. 不断添加`e`位置上的字符`c`
2. 如果`c`不属于`p`，则双指针跳过`c`
3. 如果`c`属于`p`，则更新。
   1. 但是如果包括的`c`字符太多了，则移动`s`直至数量符合条件
   2. 如果所有字符数量都添加完全一致，则添加结果。移动`s`一位，更新即可。





看了其他题解，发现有一个条件我忽略了，指针之间的距离是相等的，也就是说这是一个滑动窗口问题~草了。

那这很简单，维护一下窗口值就行了。

> 可以说滑动窗口就是一个简单的双指针。

<!-- more -->

## 代码：



```c++

class Solution {
    map<char, int> group, times;// group: [s, e) 之间的字符出现次数， time: p字符出现次数
public:
    vector<int> findAnagrams(string str, string p) {
        int s = 0, e = 0;
        for(auto c : p) ++times[c];
        int groopsize = p.size();
        vector<int> indexes;

        while( s < str.size() && e < str.size()){
            
            if(times[str[e]] == 0) {
                s = e + 1;
                group.clear();
                groopsize = p.size();
            }else{
                ++group[str[e]];
                --groopsize;  
                // 出现次数过多， 向前收缩s
                while( group[str[e]] > times[str[e]]){    
                    --group[str[s]];
                    ++s;
                    ++groopsize;                       
                }
                // [s, e)内是p的anagram
                if(groopsize == 0){
                    indexes.push_back(s);                
                    --group[str[s]];
                    ++s;
                    ++groopsize;                    
                }
            }

            ++e;
            // cout << s << ' ' << e << " " << groopsize << endl;
        }
        // cout << endl;
        return indexes;
    }
};
```





```c++
class Solution {    
public:
    vector<int> findAnagrams(string str, string p) {
        int s = 0, e = 0;
        vector<int> indexes, window, need;
        if(p.size()>str.size()) return {};
        window.resize(128);
        need.resize(128);
        for(int i = 0; i < p.size(); ++i){
            ++window[str[i]];
            ++need[p[i]];
        } 
        e = p.size();    
        while(e <= str.size()){
            if(window == need) indexes.push_back(s);
            if(str.size() == e) break;
            window[str[e++]]++;
        
            window[str[s++]]--;
            
        }  
          
        return indexes;
    }
};
```

