---
title: 最大值减去最小值小于或等于num的子数组数量
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
date: 2021-06-17 08:45:14
tags:
categories:
---





## **[最大值减去最小值小于或等于num的子数组数量](https://www.nowcoder.com/practice/5fe02eb175974e18b9a546812a17428e?tpId=101&&tqId=33086&rp=1&ru=/ta/programmer-code-interview-guide&qru=/ta/programmer-code-interview-guide/question-ranking)**

超级复合怪

<!-- more -->

## 思路：

1. n^3解法暴力
2. 尝试用滑动窗口的思路去做。相邻子数组最大最小的值，可用双头队列的最大栈和最小栈进行维护。先扩展右边，根据性质维护左边，即可。发现每个符合性质的子数组都可提取新的(j - i + 1)个以右起点为右端点的新数组。综合计算复杂度$O(N)$。

```c++

#include <vector>
#include <iostream>
#include <map>
#include <deque>
using namespace std;

int res = 0;
int main(){
    int n, num;
    cin >> n >> num;
    vector<int> arr(n);
    for(int i = 0; i < n; ++i) cin >> arr[i];
    
    deque<int> maxv, minv;
    int i = 0, j = -1;
    
    while( ++j < n ){
        
        while(maxv.size() && arr[maxv.back()] <= arr[j]){
            maxv.pop_back();
         }
        while(minv.size() && arr[minv.back()] >= arr[j]){
            minv.pop_back();
         }
        minv.push_back(j);
        maxv.push_back(j);
        while(maxv.size() && minv.size() && arr[maxv.front()] - arr[minv.front()] > num){
            if(maxv.front() == i) maxv.pop_front(); 
            if(minv.front() == i) minv.pop_front();
            ++i;
        }
        res += j - i + 1;
       // cout << i << " " << j << res << endl;
    
    }
    cout << res << endl;
    
    
}
```