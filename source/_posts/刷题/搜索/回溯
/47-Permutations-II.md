---
title: 47. Permutations II
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-12-03 12:58:55
---




## [47. Permutations II](https://leetcode-cn.com/problems/permutations-ii/)2



## 思路：

保证`idx`位的元素不重复即可。

1. 可以用set去重nums[idx]
2. 用set去重res

<!-- more -->

## 代码：



66%

```c++
class Solution {
public:
    
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<vector<int>> permute;
        permuteUniqueCore(permute, nums, 0);
        return permute;
    }

    void permuteUniqueCore(vector<vector<int>> &permute, vector<int>&nums, int pos){
        if(nums.size() == 0 ) return;
        if(pos == nums.size() - 1){
            permute.push_back(nums);
            return;
        }
        // set无脑去重，空间有点大
        unordered_set<int> vis;
        for(int i = pos; i < nums.size(); ++i){
            if(pos != i && vis.count(nums[i])) continue;
            vis.insert(nums[i]);
            swap(nums[pos], nums[i]);
            permuteUniqueCore(permute, nums, pos + 1);
            swap(nums[pos], nums[i]);            
        }
    }
};
```



88%

```c++
class Solution {
public:
    vector<int> temp;vector<vector<int>> res;

    vector<vector<int>> permuteUnique(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        vector<int> vis(nums.size());
        permuteCore(nums, vis, 0);
        return res;
    }

    
    void permuteCore(vector<int>&nums, vector<int> &vis, int pos){
        if(pos == nums.size()){
            res.push_back(temp);
            return;
        }
        for(int i = 0; i < nums.size(); i++){
            if(vis[i] || (i > 0 && nums[i] == nums[i -1] && !vis[i - 1])) continue;
            vis[i] = 1;
            temp.push_back(nums[i]);
            permuteCore(nums, vis, pos + 1);
            temp.pop_back();
            vis[i] = 0;            
        }        
    }
};

```