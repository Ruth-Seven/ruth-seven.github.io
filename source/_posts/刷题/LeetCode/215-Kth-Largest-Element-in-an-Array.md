---
title: 215. Kth Largest Element in an Array
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
 - sort
categories:
 - 刷题
 - LeetCode
date: 2020-11-14 10:11:48
---




## [215. Kth Largest Element in an Array](https://leetcode-cn.com/problems/kth-largest-element-in-an-array/)



复习一遍第K大算法的三种经典解法

<!-- more -->

## 思路：

1. 暴力排序
2. 快速排序的Partition
3. 建长度为`k`的小顶堆

## 代码：



```c++
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {    
        int pos = -1;
        int s = 0, e = nums.size();
        k = (int)nums.size() - k + 1;
        pos = sortPartVec(nums, s, e);
        while(1){    
            // cout << s << ' ' << e << " " << pos << endl;        
            if(pos + 1 == k) return nums[pos];
            else if(pos + 1 > k){
                s = s;
                e = pos;
                pos = sortPartVec(nums, s, e); 
            } 
            else{
                s = pos + 1;
                e = e;
                pos = sortPartVec(nums, s, e);
            }
        }
    }

    int sortPartVec(vector<int>& nums, int s, int e){
        int len =  min((int)nums.size(), e - s);
        if(len == 1) return s;
        else if(len == 0) return -1;
        // if(nums[len / 2] > nums[0]) swap(nums[0], nums[len / 2]);
        int l = s, r = e - 1, pivot = nums[s];
        while(l  < r){
            while(l < r && nums[r] > pivot) r--;
            nums[l] = nums[r];            
            while(l < r && nums[l] <= pivot) l++;
            nums[r] = nums[l];
        }
        nums[r] = pivot;
        return r;       

    }
};
```

建堆算法



```c++
class Solution {
public:
    vector<int> heap;
    int maxlen;
    int findKthLargest(vector<int>& nums, int k) {    
        maxlen = k + 1;
        heap.push_back(1);
        for(int i = 0; i < nums.size(); ++i)
            insert_heap(nums[i]);
        return heap[1];

    }

    void upAdjust(int p, int len){
        for(int x = p / 2; x >= 1; x /= 2){            
            if(heap[x] < heap[p]) break;
            swap(heap[x], heap[p]);
            p = x;
        }
    }

    void downAdjust(int p, int len){
        for(int x = p * 2; x < len; x += x){
            if(x + 1 < len)
                x = (heap[x] < heap[x + 1]) ? x : x + 1;
            if(heap[x] >= heap[p]) break;
            swap(heap[x], heap[p]);
            p = x;
        }
    }

    void insert_heap(int x){
         int len = heap.size();
         if(len == maxlen){
             if(heap[1] < x){
                 pop_heap();
                 len--;
             }
             else return;
        }
        heap.push_back(x);
        heap[len] = x;
        upAdjust(len, len + 1);         
    }

    void pop_heap(){
        int pos = 1, len = heap.size();
        heap[1] = heap[len - 1];
        len--;
        heap.pop_back();
        downAdjust(1, len);    
    }
};
```

利用STL模板

```c++
class Solution {
public:
 
    priority_queue<int, vector<int>, greater<int> > que;
    int findKthLargest(vector<int>& nums, int k) {    
        for(int i = 0; i < nums.size(); ++i){
            if(que.size() == k && que.top() < nums[i]){
                que.pop();
                que.push(nums[i]);
            }
            else if(que.size() < k) que.push(nums[i]);
        }            
        return que.top();

    }

 

};
```