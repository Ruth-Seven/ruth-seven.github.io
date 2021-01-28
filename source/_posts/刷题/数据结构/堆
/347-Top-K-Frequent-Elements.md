---
title: 347. Top K Frequent Elements
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-11-15 09:32:09
---


<!-- more -->

## 思路:

map记录出现初次，

堆维护前K大

## 代码：

```c++

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        map<int, int> counter;
        map<int, int>::iterator iter;
        priority_queue< pair<int, int>, vector<pair<int, int>>, greater<pair<int,int> > >  pq;
        for(auto i : nums)
            counter[i]++;
        
        iter = counter.begin();
        pair<int, int> tp;
        int s1, s2, e1, e2;
        // cout << counter.size() << endl;
        while(iter != counter.end()){
            s1 = iter->first;
            s2 = iter->second;
            if(pq.size() == k){
                tp = pq.top();
                e2 = tp.first;
                e1 = tp.second;
                if(e2 < s2){
                    pq.pop();
                    pq.push(make_pair(s2, s1));
                }
            }else pq.push(make_pair(s2, s1));            
            iter++;
        }

        vector<int> ans;        
        while(pq.size() > 0){                                    
            ans.push_back(pq.top().second);            
            pq.pop();
        }
        return ans;
    }
};
```