---
title: 1286. Iterator for Combination
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-10-08 09:06:01
---

想了一下全组合的写法，顺便复习了一下全排列(full permutaion)的思想。

<!-- more -->
#### [1286. Iterator for Combination](https://leetcode-cn.com/problems/iterator-for-combination/) 全排列



## 思路：

官方给出了生成法，这种方法比较死板不去学习。

我依据全排列的递归生成方法，扩展到全组合的生成方法，但是需要存储。思路就是：f(s,i,len,str)递归给出已生成i位str，获取s的len及之后的全组合字符串。

大神给出了基于二进制的全组合generatorf方法。由于全组合的排列顺序在二进制看来就是相同数量的`1`和`0`的组合，因此可以由大到小排列。

比如，字典序排序应该是:

```
ab
ac
ad
bc
bd
```

刚好可以对应二进制数，从大到小:

```
1100
1010
1001
0110
0101
0011
```

再利用`n&(n-1)`计算出0bN的1的个数。

## 代码：

全组合写法：

```c++

class CombinationIterator {
public:
    queue<string> que;
    int len = -1;
    CombinationIterator(string characters, int combinationLength) {

        len = combinationLength;
        printCombination(characters, 0, 0, "");
    }
    // 全排列写法，combination只是组合，而非全排列
    void printPer(string a, int depth){
        if(depth > len) return;
        else if(depth == len){
        //    cout << counter++ << ' '  << a.substr(0, len) << endl;
            que.push(a.substr(0, len));
            return;
        }
        for(int i = depth + 1;i < a.size(); i++){
        printPer(a, depth + 1);
            swap(a[i], a[depth]);
        }
        printPer(a, depth + 1);
    }
    // combination写法

    
 
void printCombination(string a, int depth, int idx, string b){
    if(depth > len) return;
    else if(depth == len){
        //cout << counter++ << " " << b << endl;
        que.push(b);
        return;
    }
    for(int i = idx;i < a.size() - len + depth + 1; i++){
       printCombination(a, depth + 1, i + 1, b + a[i]);
    }
 

}


    string next() {
        string res = que.front();
        que.pop();
        return res;
    }
    
    bool hasNext() {
        return !que.empty();
    }
};

/**
 * Your CombinationIterator object will be instantiated and called as such:
 * CombinationIterator* obj = new CombinationIterator(characters, combinationLength);
 * string param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */
```

bit版：

```c++

class CombinationIterator {
private:
    int cur;
    int sz;
    string chars;
public:
    
    CombinationIterator(string characters, int combinationLength) {

        sz = combinationLength;
        chars = characters;
        cur = (1 << chars.size()) - 1;

    }
    //要求输入字符串长度<= 31
    int countone(int n){
        int res = 0;
        while(n){
            n = n & (n - 1);
            res ++;
        }
        return res;
    }
    
    string next() {
        while(cur > 0 && countone(cur) != sz) cur--;
        if(cur <= 0) return "";
        string res = "";
        cout << cur << endl;
        for(int i = 0; i < chars.size(); i++){
            if((cur & (1 << i)) != 0)
                res = chars[chars.size() - 1 - i] + res;
        }
        cur--;
        return res;
    }
    
    bool hasNext() {
        while(cur > 0 && countone(cur) != sz) cur--;
        if(cur > 0) return true;
        else return false;
     }

};

/**
 * Your CombinationIterator object will be instantiated and called as such:
 * CombinationIterator* obj = new CombinationIterator(characters, combinationLength);
 * string param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */
```



