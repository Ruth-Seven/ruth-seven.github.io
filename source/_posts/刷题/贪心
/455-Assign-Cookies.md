---
title: 455. Assign Cookies
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-10-09 08:14:33
---

<!-- more -->

#### [455. Assign Cookies](https://leetcode-cn.com/problems/assign-cookies/)

贪心 + 二分

<!--more-->

## 思路：

贪心

## 代码：

```c++
class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
            sort(g.begin(), g.end(), less<int>());
            sort(s.begin(), s.end(), less<int>());
            vector<bool> vis(s.size(), 0);
            int ans = 0;
            for(int i = 0; i < g.size(); ++i){
                int l = 0, r = s.size(), mid;
                while(l < r){
                    mid = (l + r) / 2;
                    if(s[mid] >= g[i]) r = mid;
                    else l = mid + 1;
                    
                }
                mid = r;
                while(mid < s.size() && vis[mid]) ++mid;
                if(mid < s.size()){
                    vis[mid] = 1;
                    ++ans;

                }
                
            }        
            return ans;
    }
};
```

错误之处：

+ sort的默认按升序拍戏，使用`greater`按降序排序
+ 二分后mid为暂存值，lr才是最后目的地。