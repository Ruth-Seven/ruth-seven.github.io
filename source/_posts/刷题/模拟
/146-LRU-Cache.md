---
title: 146. LRU Cache
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
date: 2021-02-27 11:09:29
tags:
categories:
---






## 思路：

LRU实现中”删除最近最少使用的数据值“表达可能会让人产生误解，更准确的意思是”删除最长时间未使用的数据值“。

硬件的实现可以用每次更新和添加元素`A`，累加除`A`之外的所有元素的计数值。

<!-- more -->

## 代码：



```c++
class LRUCache {
public:
    // 软件实现LRU毕竟和硬件不同，需要考虑元素的放置和组成位置；
    // hash + 双向链表的结构组成能够在O(1)的速度下获取元素位置
    // 双向链表的支持保证了删除和在首位添加元素的速度也在O(1)
    using pairii = pair<int,int>;
    list<pairii> content; 
    unordered_map<int, list<pairii>::iterator> hash;
    int capacity;
    
    LRUCache(int _capacity) : capacity(_capacity) {
        //如果手写 list 添加 虚拟头尾节点更佳
    }
    
    int get(int key) {
        if(hash.find(key) == hash.end()){
            return -1;
        }
        // 如果能够声明一个属于友元的 list 直接对指针进行操作 效率会更好
        pairii node = *hash[key]; //慎用 删除后的iterator
     
        content.erase(hash[key]); 
        content.emplace_front(node);
        hash[key] = content.begin();
        return node.second;
    }
    
    void put(int key, int value) {
        pairii node{key, value};
        if(hash.find(key) != hash.end()){ // 没有找到对应的value
            content.erase(hash[key]);
        }else if(content.size() == capacity){ // cache容量已满, 删除最长时间未使用的数据值
            hash.erase(content.back().first);
            content.pop_back(); //        
        }
        content.emplace_front(node);
        hash[key] = content.begin();
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
```

