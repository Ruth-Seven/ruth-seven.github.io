---
title: 763. Partition Labels
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-10-14 08:26:06
---

<!-- more -->

## 思路：

题目不错，贪心到最晚出现的字符就行了。

## 代码：

```c++

class Solution {
public:
    vector<int> partitionLabels(string S) {
        int vis[26] = {0}, num[26] = {0};
        vector<int> par;
        int k = 0, n = S.size(), last = -1;
        
        for(int i = 0; i < n; ++i)
            num[S[i] - 'a']++;

        while(k < n){
            memset(vis, 0, sizeof(vis));
            for(k; k < n; ++k){                
                int idx = S[k] - 'a';
                vis[idx]++;
                int flag = 0;
                if(vis[idx] == num[idx] ){
                    for(int j = 0; j < 26; ++j){                        
                        if(vis[j] && vis[j] != num[j]){
                            flag = 1;
                            break;
                        }
                    }
                    if(!flag){
                        break;
                    }
                }
            }
            par.push_back(k - last);
            last = k;
            k++;
        }
        return par;
    }
};
```





py版：实现更优雅

```python

class Solution(object):
    def partitionLabels(self, S):
        last = {c: i for i, c in enumerate(S)}
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1
            
        return ans

作者：LeetCode
链接：https://leetcode-cn.com/problems/partition-labels/solution/hua-fen-zi-mu-qu-jian-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```

