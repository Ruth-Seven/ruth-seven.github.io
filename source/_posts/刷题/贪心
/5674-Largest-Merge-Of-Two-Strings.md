---
title: 5674. Largest Merge Of Two Strings
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
date: 2021-02-07 13:46:28
tags:
categories:
---





周赛的题目3

## 算法：

明显是贪心，但我贪错了！

一开始想着比较两个字符创的开头字符，选择字典序大的字符加入。如果两个字符相等就放着比较下一个，直到有不同的就可以全部加入。然后wa了4发。

正确的思路是：比较剩下的字符串，选择字典序大的字符创的的首个字符加入即可。

<!-- more -->



## 代码：



```c++
class Solution {
public:
    string largestMerge(string word1, string word2) {
        int i, j;
        i = j = 0;
        string res;
        int n = word1.size(), m = word2.size();
        while(i < n && j < m){
            // 贪心算法：
            // 直接比较 剩下子串， 选择字典的序大的子串的第一个字母加入
            if(word1.substr(i) > word2.substr(j)) res += word1[i++];
            else res += word2[j++];

        }
        if(i < n) res += word1.substr(i);
        if(j < m) res += word2.substr(j);           
        return res;
    }
};
```

