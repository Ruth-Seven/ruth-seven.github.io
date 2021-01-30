---
title: 566. Reshape the Matrix
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
date: 2021-01-30 15:12:10
tags:
categories:
---




## [566. Reshape the Matrix](https://leetcode-cn.com/problems/reshape-the-matrix/)





## 思路：



> 从今天起，有些水题就不写了。浪费时间了。

<!-- more -->



## 代码：

```c++
class Solution {
public:
    class Iter{
        
        int i ,j;
        int n, m;
    public:
        vector<vector<int>> &nums;
        // Iter(vector<vector<int>> &_nums): nums(_nums){
        Iter(vector<vector<int>> &_nums): nums(_nums){
            i =0, j = 0;
            n = nums.size();
            m = (n == 0) ? 0 : nums[0].size();
        }
        bool empty(){
            return i > n - 1 || i == n - 1 && j > m - 1;
        }

        int& next(){
            if(j == m){
                j = 0;
                i = i + 1;
            }
            // cout << nums[i][j] << endl;
            return nums[i][j++];
        }
        
    };
    vector<vector<int>> matrixReshape(vector<vector<int>>& nums, int r, int c) {
        if(nums.size() == 0 || nums.size() * nums[0].size() != r * c)
            return vector<vector<int>>(nums);
        int n = nums.size();
        int m = nums[0].size();

        vector<vector<int>> mat(r, vector<int>(c));
        Iter p1(nums), p2(mat);
        while(!p1.empty()){
            p2.next() = p1.next();
        }
        // cout << p1.nums[0][0] << endl;
        // cout << p2.nums[0][0] << endl;
        return p2.nums;
    }
};
```