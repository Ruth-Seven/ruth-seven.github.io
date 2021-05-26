---
title: 字符串hash
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-08-07 12:02:09
---



滚动哈希：O(n+m)时间内完成字符串匹配；
实现：选取两个台适的互素数$b$和h(l<b<h)，假设字符串 C=clc2c3…CmC=clc2c3…Cm，定义哈希函数：
$$
H(C)=(C_1b_{m−1}+C_2b_{m−2}+⋯+C_mb_0)
$$





其中b是基数。

可以得出O(n)的时间复杂度就可以计算得到一个串的Hash值。而由取余性质

$$
(A+B)
$$





以滚动计算hash值，可实现以复杂度O(1)O(1)计算每个母串的长度为nn子串的hash值。最后再O(n+m)时间内完成字符串匹配。在实现时，可以使用64位无符号整数计算哈希值，并取M等于264264，通过自然溢出省去求模运算。



```c++
typedef unsigned long long ull;
const ull b=100000007;//哈希的基数；
//C是否在S中出现
bool contain(string C,string S)
{
     int m = C.length(), n = S.length();
     if(m > n)  return false;
     //计算b的m次方
     ull t=1;
     for(int i = 0;i < m; i++)   t *= b;
 
     //计算C和S长度为m的前缀对应的哈希值
     ull Chash=0, Shash=0;
     for(int i = 0;i < m; i++)   Chash = Chash * b + C[i];
     for(int i = 0; i < m; i++)   Shash = Shash * b + S[i];
 
     //对S不断右移一位，更新哈希值并判断
     for(int i = 0; i + m < n; i++){
          if(Chash == Shash)  return true;//S从位置i开始长度为m的字符串子串等于C；
          Shash = Shash * b - S[i] * t + S[i+m];
      }
      return false;
}
```

