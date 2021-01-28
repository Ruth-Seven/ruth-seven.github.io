---
title: 40. Combination Sum II
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-12-04 09:50:35
---




## [40. Combination Sum II](https://leetcode-cn.com/problems/combination-sum-ii/)





## 思路：

1. 用map记录数字出现次数，转化为普通的dfs
2. 避免在填充`idx`数字的时候，遍历到重复数字，即可。无需map记录数字。是一种成熟的避免重复数字的方法。



<!-- more -->

## 代码：



40%

```c++
class Solution {
public:
    unordered_map<int, int> ct;
    vector<int> arr;
    vector<vector<int>> res;
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end(), less<int>());
        for(auto i : candidates){
            ct[i]++;
            if(ct[i] == 1) arr.push_back(i);    
        }
        vector<int> aim;
        dfs(aim, 0, target);
        return res;
    }
    void dfs(vector<int> &aim, int pos, int target){
        if(target == 0){
            res.push_back(aim);
            return;
        }
        for(int i = pos; i < arr.size(); ++i){        
            if(arr[i] > target) break;
            if(ct[arr[i]] == 0) continue; //ct[arr[i]]必行存在
            aim.push_back(arr[i]);
            ct[arr[i]]--;
            dfs(aim, i, target - arr[i]);
            ct[arr[i]]++;
            aim.pop_back();
        }
    }
};
```



98%

```c++
class Solution {
public:   
    vector<vector<int>> res;
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end(), less<int>());        
        vector<int> aim;
        dfs(candidates,aim, 0, target);
        return res;
    }
    void dfs(vector<int>& candidates, vector<int> &aim, int pos, int target){
        // for(auto i : aim){
        //     cout << i << ' ' ;
        // }
        // cout << endl;
        if(target == 0){
            res.push_back(aim);
            return;
        }
        for(int i = pos; i < candidates.size() && candidates[i] <= target; ++i){
            //在一层的搜索中选择不重复的数字，同时巧妙的维持了可搜索上一层数字的状态
            if(i > 0 && i > pos && candidates[i] == candidates[i - 1]) continue; 
            aim.push_back(candidates[i]);            
            
            dfs(candidates, aim, i + 1, target - candidates[i]);
            aim.pop_back();
        }
    }
};
```