---
title: 76. Minimum Window Substring
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
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



## 