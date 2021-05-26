---
title: 524. Longest Word in Dictionary through Deleting
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
categories:
date: 2020-10-22 09:15:18
tags:
---




#### [524. Longest Word in Dictionary through Deleting](https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting/)

2020.10.22日

这题还是稍微锻炼了一下我、

<!-- more -->

## 思路：

为了尽量降低代码复杂度，我选择了用hash保留地址法存储每个相同字符的位置。在遍历字典中每个字符中，判断每个字符串的字符合理出现位置，二分hash链式表中每个字符的可能位置即可。

代码虽然复杂一点，但是很快，时间复杂度为：$O(logL(s) * L(d[argmax\  len(d[i])] * d.size()))$

## 代码：



其他人的的双指针法：很慢

```

class Solution 
{
private:
    bool isZichuan(string target, string s)
    {   
        //分别从左端开始索引，检测是否为子列
        int i = 0, j = 0;
        while(i < target.size() && j < s.size())
        {
            if(target[i] == s[j])
                i++;
            j++;  
        }
        return i == target.size();
    }

public:

    string findLongestWord(string s, vector<string>& d) 
    {
        string str = "";
        for(int i = 0; i < d.size(); i++)
        {
            int tag = str.length();
            int leng = d[i].length();
            //若字符串更短或者一样长且字母顺序较大的直接舍去
            if(tag > leng || (tag == leng && str.compare(d[i]) < 0))
                continue;
            
            if(isZichuan(d[i], s))
            {
                str = d[i];
            }
        }a
        return str;
    }
};

作者：lu-guo-de-feng-2
链接：https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting/solution/zhi-xing-yong-shi-60-ms-zai-suo-you-c-ti-jiao-zh-3/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

```

击败99.7%

```
class Solution {
public:
    string findLongestWord(string s, vector<string>& d) {
        vector<int> map[26];
        for(int i = 0; i < s.size(); i++){
            map[s[i] - 'a'].push_back(i);
        }
        string maxs = "";
        for(int i = 0; i < d.size(); ++i){
            int s = -1, flag = 1;
            for(int j = 0; j < d[i].size(); ++j){
                int cp = d[i][j] - 'a';
                int l = 0, r = map[cp].size(), mid;
                while(l < r){
                    mid = (l + r) / 2;
                    if(map[cp][mid] > s) r = mid;
                    else l = mid + 1;
                }
                if(l == map[cp].size() || s >= map[cp][l]){
                    flag = 0;
                    break;
                } 
                s = map[cp][l];
            }
            // cout << endl;
            if(flag && ( maxs.size() < d[i].size() || maxs.size() == d[i].size() && maxs > d[i]))
                maxs = d[i]; 
        }
        return maxs;
        
    }
};
```