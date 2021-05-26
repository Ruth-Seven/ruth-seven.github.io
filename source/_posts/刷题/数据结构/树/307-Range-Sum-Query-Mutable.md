---
title: 307. Range Sum Query - Mutable
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
date: 2021-02-05 20:38:24
tags:
categories:
---



# [307. Range Sum Query - Mutable](https://leetcode-cn.com/problems/range-sum-query-mutable/)





## 思路

线段树 + lazy操作

<!-- more -->

## 代码







线段树累加操作（代码应该正确，顺手写一写）



```c++
class NumArray {
public:
    int n = 0, m = 0;
    vector<int> d, b, a;
    void build(int l, int r, int no){
        int m = (l + r) / 2;
        if(l == r){
            d[no] = a[l];
            return;
        }
        else {
            build(l, m, no * 2), build(m + 1, r, no * 2 + 1);
            d[no] = d[no * 2] + d[no * 2 + 1];
        }
    }
    
    void update_big(int l, int r, int s, int t, int c, int no){ // [s, t] is updated
        if(s <= l && r <= t){
            d[no] += (r - l + 1) * c;
            b[no] += c;
            return;
        }
        int mid = (l + r) / 2;
        if(b[no] && l != r){
            d[no * 2] += (mid - l + 1) * b[no];
            d[no * 2 + 1] += (r - mid) * b[no];
            b[no * 2] += b[no];
            b[no * 2 + 1] += b[no];
            b[no] = 0;
        }

        if(s < mid + 1) update_big(l, mid, s, t, c, no * 2);
        if(t > mid)update_big(mid + 1, r, s, t, c, no * 2 + 1);
        d[no] = d[no * 2] + d[no * 2 + 1];
    }

    int query_big(int l, int r, int s, int t, int no){  // [s, t] is queried.
        if(s <= l && r <= t){
            return d[no];
        }
        int mid = (l + r) / 2;
        if(b[no] && l != r){
            d[no * 2] += (mid - l + 1) * b[no];
            d[no * 2 + 1] += (r - mid) * b[no];
            b[no * 2] += b[no];
            b[no * 2 + 1] += b[no];
            b[no] = 0;
        }
        int sum = 0;
        if(s < mid + 1) sum += query_big(l, mid, s, t, no * 2);
        if(t > mid) sum += query_big(mid + 1, r, s, t, no * 2 + 1);
        return sum;
    }
    NumArray(vector<int>& nums) {
        m = nums.size();
        n = m * 2 + 10;
        d.resize(n);
        b.resize(n);
        a = nums;
        build(0, m - 1, 1);
    }
    
    void update(int index, int val) {
        update_big(0, m, index, index, val, 1);
    }
    
    int sumRange(int left, int right) {
        return query_big(0, m, left, right, 1);
        // return 0;
    }

    
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * obj->update(index,val);
 * int param_2 = obj->sumRange(left,right);
 */
```





线段树更新为定值（AC ） 17% 



````c++
class NumArray {
public:
    int n = 0, m = 0;
    vector<int> d, b, a, isb;
    void build(int l, int r, int no){
        int m = (l + r) / 2;
        if(l == r){
            d[no] = a[l];
            return;
        }
        else {
            build(l, m, no * 2), build(m + 1, r, no * 2 + 1);
            d[no] = d[no * 2] + d[no * 2 + 1];
        }
    }
    
    void update_big(int l, int r, int s, int t, int c, int no){ // [s, t] is updated
        if(s <= l && r <= t){
            d[no] = (r - l + 1) * c;
            b[no] = c;
            isb[no] = 1;
            return;
        }
        int mid = (l + r) / 2;
        if(l < r && isb[no]){
            d[no * 2] = (mid - l + 1) * b[no];
            d[no * 2 + 1] = (r - mid) * b[no];
            b[no * 2] = b[no];
            b[no * 2 + 1] = b[no];
            isb[no * 2] = isb[no * 2] = 1;
            b[no] = isb[no] = 0;
        }

        if(s < mid + 1) update_big(l, mid, s, t, c, no * 2);
        if(t > mid)update_big(mid + 1, r, s, t, c, no * 2 + 1);
        d[no] = d[no * 2] + d[no * 2 + 1];
    }

    int query_big(int l, int r, int s, int t, int no){  // [s, t] is queried.
        if(s <= l && r <= t){
            return d[no];
        }
        int mid = (l + r) / 2;
        if(l < r && b[no]){
            d[no * 2] = (mid - l + 1) * b[no];
            d[no * 2 + 1] = (r - mid) * b[no];
            b[no * 2] = b[no];
            b[no * 2 + 1] = b[no];
            isb[no * 2] = isb[no * 2] = 1;
            b[no] = isb[no] = 0;
        }
        int sum = 0;
        if(s < mid + 1) sum += query_big(l, mid, s, t, no * 2);
        if(t > mid) sum += query_big(mid + 1, r, s, t, no * 2 + 1);
        return sum;
    }
    NumArray(vector<int>& nums) {
        m = nums.size();
        n = m * 4 + 10; // n * 2 开太小了
        d.resize(n);
        b.resize(n);
        isb.resize(n);
        a = nums;
        build(0, m - 1, 1);
    }
    
    void update(int index, int val) {
        update_big(0, m - 1, index, index, val, 1);
    }
    
    int sumRange(int left, int right) {
        return query_big(0, m - 1, left, right, 1);
        // return 0;
    }

    
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * obj->update(index,val);
 * int param_2 = obj->sumRange(left,right);
 */
````

