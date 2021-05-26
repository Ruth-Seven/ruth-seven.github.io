---
title: 380. Insert Delete GetRandom O(1)
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
date: 2021-03-03 12:26:20
tags:
categories:
---








## 思路：

要求插入，删除，随机获取元素用$O(1)$

不要求数据有序，也不要要求数据按原序。

`hash + 动态数组`即可。

> 删除的时候，交换待删除元素到动态数组末就行了。

<!-- more -->



## 代码：



```c++

class RandomizedSet {
    vector<int> arr;
    unordered_map<int, int> idx;
public:
    /** Initialize your data structure here. */
    RandomizedSet() {

    }
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    bool insert(int val) {
        if(idx.count(val)){
            return false;
        }
        arr.push_back(val);
        idx[val] = arr.size() - 1;
        return true;
    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    bool remove(int val) {
        if(!idx.count(val)) return false;
        int pos = idx[val];
        idx[arr[arr.size() - 1]] = pos;
        swap(arr[pos], arr[arr.size() - 1]);
        arr.pop_back();
        idx.erase(val);
        return true;
    }
    
    /** Get a random element from the set. */
    int getRandom() {
        return arr[random() % arr.size()];
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */
```

