---
title: 279. Perfect Squares
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-12-10 09:40:13
---




## [279. Perfect Squares](https://leetcode-cn.com/problems/perfect-squares/)

## 思路：



1. dp。均摊复杂度比较低
2. 贪心算法，贪
3. bfs+贪心

<!-- more -->

## 代码：

dp

66%

```c++
class Solution {
public:
    int numSquares(int n) {
        vector<long long> dp(n + 1, INT_MAX);
        dp[0] = 0;
        for(long long i = 1; i <= n; ++i){
            for(long long  j = 1; j * j <= i; ++j){
                long long t = i - j * j;
                dp[i] = min(dp[i], dp[t] + 1);
            }
        }
        return dp[n];
    }
};
```



贪心搜索

70%

```c++
class Solution {
public:
    vector<long long> dp; //数字平方搜索值
    int numSquares(int n) {
        dp.resize(sqrt(n) + 1);
        for(int  i = 1; i < dp.size(); ++i){
            dp[i - 1] = i * i;
        }
        for(int i = 1; i <= n; ++i){
            if(getLevel(n, i)) return i;
        }
        return 0;
    }
    bool getLevel(int n, int ssize){// ssize个平方数的和是否等于n
        if(ssize == 1){ 
            if(count(dp.begin(), dp.end(), n) > 0) return true;        
            return false;
        }
        for(int i = 0; i < dp.size(); ++i){
            if(getLevel(n - dp[i], ssize - 1)) 
                return true;
        }
        return false;
        
    }
};
```



bfs搜索

17%……

unordered_set的的损耗还是太大了吗

```c++
class Solution {
public:
    vector<long long> dp;
    int numSquares(int n) {
        dp.resize(sqrt(n) + 1);
        for(int  i = 1; i < dp.size() + 1; ++i){
            dp[i - 1] = i * i;
        }
        int level = 1;
        unordered_set<int> que, next_que; //8%->17%
        que.insert(n);
        //层序遍历，整层树。
        while(1){
        }
        return 0;
    }
   	void search(unordered_set<int> que, unordered_set<int> next_que){        
            for(auto t : que){                
                for(int i = 0; i < dp.size() && dp[i] <= t ; ++i){
                    // cout << t << " " << dp[i] << endl;                
                    if(dp[i] == t) return level;
                    next_que.insert(t - dp[i]);
                }
            }
            level += 1;
            que = next_que;
            next_que.clear();
    }

};
```

再优化一下28%

```c++
class Solution {
public:
    vector<long long> dp;
    int numSquares(int n) {
        dp.resize(sqrt(n) + 1);
        for(int  i = 1; i < dp.size() + 1; ++i){
            dp[i - 1] = i * i;
        }
        int level = 1;
        unordered_set<int> que1, que2; //8%->17%
        que1.insert(n);
        //层序遍历，整层树。
        while(1){
            if(level & 1){
                if(search(que1, que2)) return level;
            }else{
                if(search(que2, que1)) return level;
            } 
            level++;
        }
        return 0;
    }
   	bool search(unordered_set<int> &que, unordered_set<int> &next_que){        
            for(auto t : que){                
                for(int i = 0; i < dp.size() && dp[i] <= t ; ++i){
                    // cout << t << " " << dp[i] << endl;                
                    if(dp[i] == t) return true;
                    next_que.insert(t - dp[i]);
                }
            }
            que.clear();
            return false;
    }

};
```

