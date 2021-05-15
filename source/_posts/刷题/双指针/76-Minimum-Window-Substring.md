---
title: 76. Minimum Window Substring
thumbnail: 'http://static.come2rss.xyz/黑色幽默.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-10-23 10:48:10
---




## [76. Minimum Window Substring](https://leetcode-cn.com/problems/minimum-window-substring/)



## 思路1:

经典双指针下的滑动窗口算法。滑动窗口的左右部分分别由两个指针`l`,`r`指向。

<!-- more -->

使用滑动窗口观察可能符号的条件的子串，并用`unordered_map`或者`map`来记录原字符串`s`和滑动窗口`win`中的元素个数。

其算法过程如下：

1. 窗口的右指针向右滑动一次，并检查窗口内是否有足够元素。若是，则左指针向右收缩窗口。重复上述步骤即可。

## 代码：

```c++

class Solution {
public:

    map<char, int> cur, ori;
    //优化: 去除无效字符
    int ahash[800] = {0};
    bool check(){
        for(const auto &p : ori){
            if(cur[p.first] < p.second)
                return false;                
        }
        return true;
    }
    string minWindow(string s, string t) {
        for(int i = 0; i < t.size(); ++i){
            ++ori[t[i]];
            ahash[t[i]] = 1;
        }
        int l = 0, r = -1, maxLen = 0x7fffffff;
        string ans = "" ;
        
        while(r < int(s.size())){            
            while(++r < s.size() && !ahash[s[r]]);
            if(r == s.size()) break;
            ++cur[s[r]];
            
            // cout << l << ' ' << r << endl;
            while(check() && l <= r){                
                if(maxLen > r - l + 1){
                    ans = s.substr(l, r - l + 1);
                    maxLen = r - l + 1;
                }
                //先减再移动……这个bug
                --cur[s[l]];   
                while(++l <= r && !ahash[s[l]]);
                    
            }
        } 
        return ans;
    }
};
```



## 思路2：

更巧妙的方法：

音量模拟：想象一排音量，分别代表着每个t中元素的个数。



![音量图图片大全_uc今日头条新闻网](D:\Blogfile\pic\76-Minimum-Window-Substring\images)

在滑动窗口向`r`指针在`t`向右扩展窗口中， 每遇到一个`s`中的元素就减去对应的音量值。如果滑动窗口中包含了`s`中的各个元素（包括种类和数量），那么就有音量图的每个柱子都在水平下以下或者持平，如果我们记录在水平线之上的数值变动——用`cnt`记录`--yin[s[i]] >=0`的剩余次数即可。

如果`cnt==0`，说明窗口已经包括了所有元素，可以缩小范围，把左指针向👉右滑动。`cnt`的变动也是同理的。

代码如下：

## 代码2：

```c++
class Solution {
public:

    // 音量模拟
    unordered_map<char, int> map;
    string minWindow(string s, string t){
        for(int i = 0; i < t.size(); ++i) ++map[t[i]];
        int cnt = t.size(), l = 0, r = -1, start = l, maxl = s.size() + 1;
        while(r < int(s.size())){
            if(--map[s[++r]] >= 0) --cnt;
            // cout << l << ' ' << r << ' ' << cnt << endl;
            while(l <= r && cnt == 0){
                if(maxl > r - l + 1){
                    start = l;
                    maxl = r - l + 1;
                }
                if(++map[s[l]] > 0) cnt++;
                l++;  
            }
        }
          return maxl == s.size() + 1 ? "" : s.substr(start, maxl);
    }
};

```



## 代码3：（二刷）



```c++
class Solution {
public: 
    // 双指针必定都搜索到所有匹配串的原因是 所有以 g为终点的符合题意的的字符串s1，
    // 其左端点必定可以向左移动，因为移动会包含到更多字符串
    // 反过来想，从起点出发，右端点移动先尽可能包含多直到足够的字符，
    // 再向右移动左端点尽可能减少多余的字符，获取一个尽可能短的字符串
    // 为了尝试其他结果，不断地进行以下活动
    //  移动右端点一次，缩短左端点，可以搜索到其他结果
    
    // 比较细节的是控制过程和循环结束
    // 
    string minWindow(string s, string t) {
        int ct[256] = {0}, allct = t.size();
        string ans; 
        // s += 'A';
        for(int i = 0; i < t.size(); ++i) ++ct[t[i]];
        int p1 = 0, p2 = 0; // [)左闭右开空间，秒在不需要初始化
        int minlen = s.size() + 1, minp1 = 0;
        while(p2 < s.size()){
            // 要么右移p2直到t字符串全部被囊括，要么试探性移动p2一个位置，进行其他位置的探索
            while(p2 < s.size()){ // p2 <= s.size()
                if(ct[s[p2]] > 0) --allct; // allct统计是否当前[p1, p2)是否有t的全部字符
                --ct[s[p2]]; // 更新字符数量
                ++p2;
                if(allct == 0) break; //前进一步
            }
            while(ct[s[p1]] < 0){ // 如果该字符多余了，缩小左端点
                ++ct[s[p1]];
                ++p1;
            }
            if(allct == 0 && p2 - p1 < minlen){
                minp1 = p1;                
                minlen = p2 - p1;
            } 
            // cout << p1 << ' ' << p2 << ' ' <<  allct << endl;
        }
        if(minlen > s.size())ans = "";
        else ans = s.substr(minp1, minlen);
        return ans;
    }
};
```

