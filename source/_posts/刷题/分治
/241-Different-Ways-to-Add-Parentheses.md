---
title: 241. Different Ways to Add Parentheses
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2021-01-02 21:53:55
---




## [241. 为运算表达式设计优先级](https://leetcode-cn.com/problems/different-ways-to-add-parentheses/)



## 思路：



分解算术式子，分开计算即可。

1. 分治法自上而下求取答案，当然可以用上记忆化的技巧。
2. DP自下而上求取答案，速度和内存消耗更少。



<!-- more -->

## 代码：



```c++
class Solution {
public:
    vector<int> diffWaysToCompute(string input) {
        vector<int> nums;
        vector<char> ops;
        int a = 0;
        char op = ' ';
        input = input + '+';
        for(int i = 0; i < input.size(); ++i){
            if(input[i] == '+' || input[i] == '-' || input[i] == '*'){
                nums.push_back(a);
                cout << a;
                a = 0;
                op = input[i];
                
            }
            else{
                a *= 10;
                a += input[i] - '0';
                if(op != ' '){
                    ops.push_back(op);
                    op = ' ';
                }
            }
        }
        
        set<int> res = getDivide(nums, ops, 0, nums.size() - 1);
        vector<int> ans = {};
        for(auto it = res.begin(); it != res.end(); it++)
            ans.push_back(*it);
        return ans;
    }

    set<int> getDivide( vector<int> &nums, vector<char> &ops, int s, int e){
        set<int> temp;
        if(s == e){
            temp.insert(nums[s]);
            return temp;
        }
        for(int i = s; i < e; ++i){            
            set<int> res1 = getDivide( nums, ops, s, i);
            set<int> res2 = getDivide( nums, ops, i + 1, e);

            for(auto it1 = res1.begin(); it1 != res1.end(); it1++){
                for(auto it2 = res2.begin(); it2 != res2.end(); it2++){
                    if(ops[i] == '+') temp.insert(*it1 + *it2);
                    else if(ops[i] == '-') temp.insert(*it1 - *it2);
                    else if(ops[i] == '*') temp.insert(*it1 * *it2);            
                }
            }
        }

        return temp;
    }
};
```





AC80%

```c++
class Solution {
public:
    vector<int> diffWaysToCompute(string input) {
        vector<int> nums;
        vector<char> ops;
        int a = 0;
        char op = ' ';
        input = input + '+';
        for(int i = 0; i < input.size(); ++i){
            if(input[i] == '+' || input[i] == '-' || input[i] == '*'){
                nums.push_back(a);
                // cout << a;
                a = 0;
                op = input[i];
                
            }
            else{
                a *= 10;
                a += input[i] - '0';
                if(op != ' '){
                    ops.push_back(op);
                    op = ' ';
                }
            }
        }
        
         
        return getDivide(nums, ops, 0, nums.size() - 1);
    }

    vector<int> getDivide( vector<int> &nums, vector<char> &ops, int s, int e){
        vector<int> temp;
        if(s == e){
            temp.push_back(nums[s]);
            return temp;
        }
        for(int i = s; i < e; ++i){            
            vector<int> res1 = getDivide( nums, ops, s, i);
            vector<int> res2 = getDivide( nums, ops, i + 1, e);

            for(auto it1 = res1.begin(); it1 != res1.end(); it1++){
                for(auto it2 = res2.begin(); it2 != res2.end(); it2++){
                    if(ops[i] == '+') temp.push_back(*it1 + *it2);
                    else if(ops[i] == '-') temp.push_back(*it1 - *it2);
                    else if(ops[i] == '*') temp.push_back(*it1 * *it2);            
                }
            }
        }

        return temp;
    }
};
```



DP记忆化方法 100%

```c++
class Solution {
public:
    vector<int> diffWaysToCompute(string input) {
        vector<int> nums;
        vector<char> ops;
        int num;
        char op; 
        istringstream ss(input + "+"); //! istringstream
        while(ss >> num && ss >> op){
            nums.push_back(num);
            ops.push_back(op);
        }
        int n = nums.size();
        vector<vector<vector<int>>> dp(n, vector<vector<int>>(n, vector<int>()));
        for(int i = 0; i < n; ++i){
            for(int j = i; j >=0; j--){
                if(i == j){
                    dp[j][i].push_back(nums[i]);
                }else{
                    for(int k = j; k < i; k++){
                        for(auto l : dp[j][k]){
                            for(auto r : dp[k+1][i]){
                                int val = 0;
                                switch(ops[k]){
                                    case '+': val = l + r; break;
                                    case '-': val = l - r; break;
                                    case '*': val = l * r; break;
                                }
                                dp[j][i].push_back(val);
                            }
                        }
                    }
                }
            }
        }
         
        return dp[0][n - 1];
    }
};
```

