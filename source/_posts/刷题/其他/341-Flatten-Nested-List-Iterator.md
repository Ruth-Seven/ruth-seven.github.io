---
title: 341. Flatten Nested List Iterator
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
categories:
date: 2020-09-25 09:14:36
tags:
---





## [341. Flatten Nested List Iterator](https://leetcode-cn.com/problems/flatten-nested-list-iterator/)

<!-- more -->

## 思路：

缓存lazy法

stack存储遍历空间法



## 代码：

```c++
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */

class NestedIterator {
public:
    int pos = 0;
    queue<int> que;
    vector<NestedInteger> nestedList;
    NestedIterator(vector<NestedInteger> &_nestedList) {
        // que.clear();
        nestedList = _nestedList;
    }
    
    int next() {
        if(hasNext()){
            int nexti = que.front();
            que.pop();
            return nexti;
        }
        return -1;
    }
    
    bool hasNext() {
        if(que.empty()){
            if(nestedList.size() == pos){
                return false;
            }
            //不要忘记pos+
            while(pos != nestedList.size() && que.empty()){
                getInt2que(nestedList[pos++]);
            }
            
        }
        if(que.empty()) return false;
        else return true;
    }

    void getInt2que(NestedInteger ni){
        if(ni.isInteger()){
              que.push(ni.getInteger());
        }else{
            vector<NestedInteger> list = ni.getList();
            for(auto item :list){
                getInt2que(item);
            }
        }
    }
};

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i(nestedList);
 * while (i.hasNext()) cout << i.next();
 */
```



不够机智的实现



```c++
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */

class NestedIterator {
    using nestedVecIt = vector<NestedInteger>::iterator;
    stack<pair<nestedVecIt, nestedVecIt> > nested;
public:

    NestedIterator(vector<NestedInteger> &nestedList) {
        if(nestedList.size() > 0) nested.push({nestedList.begin(), nestedList.end()});
    }
    bool hasNext() { 
        locate();
        return !nested.empty();        
    }

    void locate(){
        if(nested.size() == 0) return;

         while(nested.size()){  
            auto& [itnested, itend]  = nested.top();  
            if(itnested == itend) nested.pop();
            else if(!itnested->isInteger()){
                auto & veclist = itnested->getList();
                ++itnested;
                nested.push({veclist.begin(), veclist.end()});
            }
            else break;            
        }         

    }

    int next() {
        if( hasNext()){ 
            auto& [itnested, itend]  = nested.top();
         
            int nextv = 0;
            if(itnested->isInteger()){
                nextv = itnested->getInteger();
                ++itnested;
                return nextv;
            }
            else{
                auto & nestedList = itnested->getList();
                ++itnested; // 无论是数字还是数组都要向前遍历
                nested.push({nestedList.begin(), nestedList.end()});
                return next();
            }            
        }
        return -1;
    }
};

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i(nestedList);
 * while (i.hasNext()) cout << i.next();
 */
```

更优雅的实现

```c++
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */

class NestedIterator {
    using nestedVecIt = vector<NestedInteger>::iterator;
    stack<pair<nestedVecIt, nestedVecIt> > nested;
public:

    NestedIterator(vector<NestedInteger> &nestedList) {
        if(nestedList.size() > 0) nested.push({nestedList.begin(), nestedList.end()});
    }
    bool hasNext() { 
         while(nested.size()){  
            auto& [itnested, itend]  = nested.top();  
            if(itnested == itend) nested.pop();
            else if(!itnested->isInteger()){
                auto & veclist = itnested++->getList(); // 自增后获取 nestedList                
                nested.push({veclist.begin(), veclist.end()});
            }
            else break;            
        }         
        return !nested.empty();        
    }

    // 保证调用前 指针指向的元素存在且为数字
    int next() {
        return nested.top().first++->getInteger();
    }
};

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i(nestedList);
 * while (i.hasNext()) cout << i.next();
 */
```

