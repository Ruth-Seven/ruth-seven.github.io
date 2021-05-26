---
title: 172. Factorial Trailing Zeroes
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2021-01-07 11:36:19
---







## 思路：

通过判断1 ~n所有数字因子5的个数判断尾零的数量。快速判断方法是：整除 5， 25， 125等等5的倍数的数字其商就是5的倍数的因子数量。



<!-- more -->



## 代码：



```c++
class Solution {
public:
    int trailingZeroes(int n) {
        int res = 0;
        while(n){
            n /= 5;
            res += n;
            
        }
        return res;
    }
};
```

