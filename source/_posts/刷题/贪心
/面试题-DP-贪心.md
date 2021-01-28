---
title: 面试题 DP 贪心
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
categories:
date: 2020-08-07 14:14:08
tags:
---


<!-- more -->

收集贪心、DP面试题



## 面14：剪绳子

### 题面：

将一串长为`K`的绳子剪成`m`（`m>=2`，各段长度取整数值）段，各段的长度大于`0`，求出最大的各段绳子长度之积。

### 思路1：

由乘法交换律可知绳子的乘积可以分解，提取出来。所以有`f(m+n)=f(n)*f(m)`，其中`f(n)`是长度`n`的绳子的最大乘积。分析具体问题可以了解到初始条件比较特殊，它对于小数字来说，分解还不如其本身大，所以定义边界条件`f(1) = 1, f(2) = 2, f(3) = 3`。同时在DP表示式为：

f(n)=maxif(n−i)∗f(i)f(n)=maxif(n−i)∗f(i)


所以时间复杂度为O(N2)O(N2)，空间复杂度为O(N)O(N)。



### 思路2：

另一种就是贪心，对于长度`m`大于5的绳子尽可能的剪成长度为3的绳子，同时如果`m%3==1`，那么就少剪一段绳子，剪成两段长为2的绳子。证明如下:
$$
if \ n \geq 5
\
3*(n-3) \geq n
\
2*(n-2) \geq n
\
3*(n -3 ) \geq 2*(n-2)
$$

### 测试：

```
2
2
,
3
2
,
5
6
,
6
9
```

### 代码：

**DP**

```
int maxProduct_DP(int length){
    if(length < 2) return 0;
	if(length == 2) return 1;
    if(length == 3) return 2;
    int* products = new int[length + 1];
    //初试条件比较特殊，小于4的大于1的数的分段乘积不如其本身大
    products[0] = 0;
    products[1] = 1;
    products[2] = 2;
    products[3] = 3;
    for(int i = 4; i <= length; i++){
        int mavV = 0;
        for(int j = 1; j <= i / 2; j++){
            maxV = max(maxV, products[i - j] * products[j]);
        }
        products[i] = maxv;
    }
    int res = products[length];
    //防止内存泄漏
    del[] products;
    return res;
}
```

**贪心**

```
int maxProduct_greedy(int length){
 if(length < 2) return 0;
	if(length == 2) return 1;
    if(length == 3) return 2;
    int timesOf3 = length / 3;
    if(legnth % 3 == 1) timesOf3 -= 1;
    int timesOf2 = (length - timesOf3 * 3) / 2;
    return (int)pow(3, timeOf3) * (int)pow(2, timesOf2);
}
```

## 面42：最大子数组和

### 题面：

如题

### 思路：

DP思想。数组之间的选择与历史无关，可以采取DP的方法。记`f(i)`为以`A[i]`为结尾的最大数组和。转移方程为：

f(i)={A[i],if f(i-1)<0 A[i]+f(i−1),if f(i-1)>0f(i)={A[i],if f(i-1)<0 A[i]+f(i−1),if f(i-1)>0



当然也可以直接从数据的角度理解，代码都是相同的。

### 代码：

```
int MaxSumOfSubArray(int A[], int length){
    int dp[] = new int(length);
	int maxSum = A[0];
    dp[0] = A[0];   
    for(int i = 1; i < length; i++){
        dp[i] = max(A[i], A[i] + dp[i-1]);
        maxSum = max(dp[i], maxSum);
    }
    delete[] dp;
    return maxSum;
    
}
```

> 当然这里的dp数组也可以不要。

## 面45：把数字排成最小的数字

### 题目：

给定一串数字，组合成的一个数字。求出组合后最小数字的

### 思路：

可以直接贪心+反证。按字典序排序数字即可。

### 代码：

就不写了，直接string排序输出即可。

## 面46：数字翻译成字符串

### 题目：

把一串数字翻译成数字对应的字母，并按原顺序组成字符串。由于数字分裂的不同，翻译方法有许多，求出翻译的方法的个数。

### 思路：

第一种就是直接递归分割字符串。显然有子问题重叠的现象，可以考虑使用DP。

第二种用DP思想，考虑`dp[i]`为从`0`到`i`的字符串翻译方法。状态转移方程为：

dp[i]={dp[i−1],if 10<=S[i-1] *10 + S[i] <26 dp[i−1]+dp[i−2],else dp[i]={dp[i−1],if 10<=S[i-1] *10 + S[i] <26 dp[i−1]+dp[i−2],else 



### 代码：

```
int GetTranslateCount(int A[], int length){
    if(A == nullptr || length <= 0) return 0;
    int dp[] = new int(length);
    dp[0] = 1;
    for(int i = 1; i < length; i++){
		int add = A[i - 1] * 10 + A[i];
        if( add > 9 && add < 26){
            if(i < 2) dp = dp[i - 1] + 1;
            else dp[i] = dp[i - 1] + dp[i - 2];
        } 
        else dp[i] = dp[i - 1];
    }
    delete[] dp;
    return dp[length - 1];    
}
```

## 面47：礼物的最大价值

### 题目：

从一在格子上装满礼物的`m*n`的矩形棋盘上，从左上角向下或者向右移动一格到右下角，求出路径上礼物价值的最大值。

### 思路：

明显就是DP

### 代码：

不写了。

## 面48：最长不含重复字符的子字符串

### 题目：

如题

### 思路：

暴力不可取。

采用用DP思想，考虑`dp[i]`为以`S[i]`为结尾的最长不重复字符串。一个不含重复字符的字符串可以在由另一个不同的字符组成另一个不含重复字符的字符串。可以在dp过程中，记录下最新的字符的位置POS，判断`S[i]`的前一个相同字符是否在上一个`S[i-1]`为结尾的最长不重复字符串之内。记上一个字符与`S[i-1]`的长度`d`为`i - POS`。

状态转移方程为：

dp[i]={dp[i−1]+1,if d > dp[i - 1] d,else dp[i]={dp[i−1]+1,if d > dp[i - 1] d,else 



### 代码：

```
int MaxSubStr(String s){
    int dp[] = new int(s.length());
    int pos[26];
    for(int i = 0; i < 26; i++) pos[[i] = -1;
	
	int maxL = 1;
	dp[0] = 1;
	for(int i = 1; i < s.length(); i++){
		int d = i - pos[s[i] - 'a'];
        if(dp[i - 1] < d){
            dp[i] = dp[i - 1] + 1;
        }else dp[i] = d;
        maxL = max(maxL, dp[i]);
        pos[s[i] - 'a'] = i;
    }
	delete[] dp;    
   return maxL;            
    
}
```