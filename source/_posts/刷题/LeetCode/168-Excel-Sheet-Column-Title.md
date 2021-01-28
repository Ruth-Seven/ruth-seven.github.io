---
title: 168. Excel Sheet Column Title
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
  - 数学
categories:
  - 刷题
  - LeetCode
date: 2021-01-12 11:09:54
---





## [168. Excel Sheet Column Title](https://leetcode-cn.com/problems/excel-sheet-column-title/)







从进制的根源出发可以更彻底的探究算法的本源。26进制的的10进制数值计算如下：
$$
s = 26^3*x_3 + 26^2*x_2+ 26^1*x_1 + 26^0*x_0
$$
在该题目条件下，$A-Z$分别代表$1-26$，不符合上述计算公式。一般除数取余法直接除于进制值K，（在本题中$K=26$）即可获取低位$x_i$，但是由于零的缺失，$Z=26$的情况，如下公式，除数取余法失效了。

<!-- more -->
$$
s / 26 = 26^2*x_3 + 26^1*x_2+ 26^0*x_1 + 1, if\ x_0 = 26
$$
修改的话，当我们发现当前位是 26 的时候，我们应该在等式两边减去一个 1 。就可以把
$$
s - 1 =  26^3*x_3 + 26^2*x_2+ 26^1*x_1 + 26^0*(x_0 -1), if\ x_0 = 26
$$


这样两边再同时除以 26 的时候，就可以把 x1 去掉了。

这种思路的代码：

```c++
class Solution {
public:
    string convertToTitle(int n) {
        string ans;
        
        while(n){
            int c = n % 26;
            if(c == 0){ //更深层次	的说，我们从商借了一个1给余数！
                c = 26;
                --n;
            }
            ans += c - 1 + 'A';
            n /=  26;
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }
};
```



换一种想法，举个🌰有:
$$
\begin{split}
54  &= 26 * 2 + 2 \\
27  &= 26 * 1 + 1
\end{split}
$$
54有个位数2，十位数2，分别对应B和B，27有个数为1，十位数1，分别对应A,A。所以有

```c++
class Solution {
public:
    string convertToTitle(int n) {
        string ans;
        
        while(n){
            // 注意这里为什么不是 ans = (n - 1) % 26 + 'A'， 而是让 n--;
            // 实际上经过取余过后，后续受影响的结果只有 n % 26 == 0的情况
            // 也就是说 本质上 n-- 也是为了向商了借一个数字
            n--; 
            ans += n % 26 +  'A';
            n /=  26;
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }
};
```

感觉好简单粗暴有效啊！