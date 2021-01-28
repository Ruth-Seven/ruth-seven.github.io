---
title: 39. Combination Sum
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-12-04 09:50:26
---



## [39. Combination Sum](https://leetcode-cn.com/problems/combination-sum/)

> 在dfs搜索题中，形象化一个dfs搜索树是一个非常有趣的，形象的描述方法。比如下面这个没有剪枝的dfs搜索树。也可以比较一下，下面两种解法的dfs搜索树的不同之处。
>
> ![img](http://static.come2rss.xyz/1598091943-hZjibJ-file_1598091940241)

<!-- more -->

## 思路：

dfs搜索剪枝代码。非常标准的一道搜索题。

> 官方给出的时间复杂度分析
>
> ![image-20201204092517420](http://static.come2rss.xyz/image-20201204092517420.png)

## 代码：



66%

```C++
class Solution {
public:
    vector<vector<int>> res;
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end(), less<int>()); //sort优化顺序 33%->47%
        vector<int> aim;

        dfsCombinate(candidates, aim, target, 0);
        return res;
    }

    void dfsCombinate(vector<int>& candidates, vector<int>& aim, int target, int pos){
        if(pos == candidates.size()) return;
        if(target <=0){
            if(target == 0){
                res.push_back(aim);
            }
            return;
        }
        aim.push_back(candidates[pos]);
        dfsCombinate(candidates, aim, target - candidates[pos], pos);
        aim.pop_back();
        dfsCombinate(candidates, aim, target, pos + 1);
    }
};
```



99%

```c++
class Solution {
public:
    vector<vector<int>> res;
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end(), less<int>()); //sort优化顺序 33%->47%
        vector<int> aim;

        dfsCombinate(candidates, aim, target, 0);
        return res;
    }

    void dfsCombinate(vector<int>& candidates, vector<int>& aim, int target, int pos){        
        
        if(target == 0){
            res.push_back(aim);
            return;
        }                
        for(int i = pos;i < candidates.size(); ++i){ //for循环代替递归寻找，减少函数调用，增加效率
            if(candidates[i] > target) break;
            if(i > pos && candidates[i] == candidates[i - 1]) continue; // 重复数字无需再判断
            aim.push_back(candidates[i]);
            dfsCombinate(candidates, aim, target - candidates[i],i);
            aim.pop_back();
        }            
    }
};
```