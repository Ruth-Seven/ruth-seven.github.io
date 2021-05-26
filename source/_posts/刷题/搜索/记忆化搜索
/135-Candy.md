---
title: 135. Candy
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-10-10 08:02:10
---

这题还行吧，一般一般。

<!-- more -->

#### [135. Candy](https://leetcode-cn.com/problems/candy/)

### 思路：

简单思路：记忆化搜索candy[i]。

更有技巧性：从左到右遍历更新candy[i],再从右到左遍历更新candy.

更大的脑洞：按峰值和谷值计算机总值。

![image.png](http://static.come2rss.xyz/df2bada8d7abe1d0550ebee880b5bf7b00cb38d553f008a9eb25491ddc356533-image.png)

### 代码：

```c++
class Solution {
public:
    vector<int> candys;
    int len;
    int getcandys(int pos, vector<int>& ratings){
        if(candys[pos] == -1){
            if(pos == 0 && ratings[pos] > ratings[pos + 1])
                candys[pos] = getcandys(pos + 1, ratings) + 1;
            else if(pos == len - 1 &&  ratings[pos] > ratings[pos - 1])
                candys[pos] = getcandys(pos - 1, ratings) + 1;
            else if(pos < len - 1 && pos > 0 && ratings[pos] > min(ratings[pos -1], ratings[pos + 1])){
                if(ratings[pos] > ratings[pos - 1])
                    candys[pos] = getcandys(pos - 1, ratings) + 1;
                if(ratings[pos] >  ratings[pos + 1])
                    candys[pos] =  max(getcandys(pos + 1, ratings) + 1, candys[pos]);
            }
             
            else candys[pos] = 1;
        }
        cout << pos << candys[pos] << endl;
        return candys[pos];

    }
    int candy(vector<int>& ratings) {
        len = ratings.size();
        candys.resize(len, -1);
        int res = 0;
        if(len > 1)
        for(int i = 0;i < len; i++){
            res += getcandys(i, ratings);
        }
        else return 1;
        return res;
    }
};
```

