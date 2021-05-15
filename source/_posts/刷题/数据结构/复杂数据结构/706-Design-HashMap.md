---
title: 706. Design HashMap
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
date: 2021-03-15 11:13:45
tags:
categories:
---



## 思路思路：

 `hash table` 配置 STL强大的API包装完成了。

<!-- more -->



## 代码：

```c++
class MyHashMap {
    vector<list<pair<int, int>>> data;
    static const int base = 1931;
    static int hash(int key){
        return key % base;   
    }
    auto findit(int key, int pos){
        auto iskey = [key](pair<int, int> item){return item.first == key;};
        return find_if(data[pos].begin(), data[pos].end(), iskey);
    }

public:
    /** Initialize your data structure here. */
    MyHashMap() {
        data.resize(1931);
        // erase不会检查尾指针
        // int key = 0,  pos  = 0;
        // auto it = findit(key, pos);
        // cout << "start" << key << endl;
        // data[pos].erase(it);
    }
    
    /** value will always be non-negative. */
    void put(int key, int value) {
        int pos = hash(key);
        auto it = findit(key, pos);
        if(it == data[pos].end())
            data[pos].insert(it, {key, value});
        else 
            it->second = value;
    }
    
    /** Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key */
    int get(int key) {
        int pos = hash(key);
        auto it = findit(key, pos);
        // cout << "find" << key << endl;
        return it == data[pos].end() ? -1 : (*it).second;
    }
    
    /** Removes the mapping of the specified value key if this map contains a mapping for the key */
    void remove(int key) {
        int pos = hash(key);
        auto it = findit(key, pos);
        // cout << "remove" << key << endl;
        if(it != data[pos].end()) data[pos].erase(it);
    }
};

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */
```

