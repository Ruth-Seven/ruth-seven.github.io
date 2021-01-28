---
title: 126. Word Ladder II
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-11-29 10:59:06
---




## [126. Word Ladder II](https://leetcode-cn.com/problems/word-ladder-ii/)

## 思路：

> 这次的bugs很少，开心。
>
> 这题核心就是BFS（DFS）的基础上加上剪枝优化。或者TBFS
>
> 



建立搜索树BFS搜索结果即可。

最好用邻接矩阵优化BFS搜索数量，同时显然的，你没法通过绕一个小弯找到最短路，这可以剪枝。



<!-- more -->

![img](D:\个人文件\重要文件\闲书与笔记\MD暂存文件\164a736e22a59a44e7e51e79e2f22f77d392fcd4dc621ea0083a91bd86855884.jpg)



第二种思路就是双头搜索。因为题目给出了起始地点和结束地点的字符串。在搜索的时候控制一下搜索空间，搜索深度就AC了。击败96%！。

## 代码：

```C++
// 26th样例超时
class Solution {
public:
    
    vector<vector<string>> findLadders(string beginWord, string endWord, vector<string>& wordList) {
        vector<vector<string>> ans;
        int n = wordList.size(), flag = 0;
        for(int i = 0; i < n; ++i){
            if(wordList[i] == endWord) flag = 1;
        }
        if(!flag) return ans;
        queue<SN*> que;
        wordList.push_back(beginWord); // size++
        que.push(new SN(n, -1, 0, nullptr));
        int endlevel = -1;
        while(que.size()){
            SN *p = que.front(); 
            que.pop();
            // cout << wordList[p.x] <<"  " << p.l << '#';
            // if(p.plink != nullptr)
            //     cout << p.x << (p.plink)->x << endl;
            // cout << (p.plink == &p) << endl;  // bugs: p.plink == &p
            //search the final points.
            if(endlevel > 0 && p->l > endlevel) continue;
            if(wordList[p->x] == endWord){
                endlevel = p->l;
                vector<string> tmp;
                SN* np = p;
                while(np  != nullptr){
                    tmp.push_back(wordList[np->x]);
                    np = np->plink;      
                    // cout << np->x << " ";              
                }
                // cout << endl;
                reverse(tmp.begin(), tmp.end());
                ans.push_back(tmp);
            }
            
            
            // emplace more points.
            for(int j = 0; j < n; ++j){
                if(islink(wordList[j], wordList[p->x])){                    
                    SN* newp = new SN(j, p->x, p->l + 1, p); //bugs: 这里取的地址是变量p的地址，同时地址指向不变，但是p指向的内容会受暂存变量p赋值而变化。 这可是C++基础啊
                    //解决方法： 给每个变量一个新的地址即可
                    // cout << (&newp == &p) << endl;
                    que.push(newp);
                }
            }
        }

        return ans;
    }

    bool islink(const string &a, const string  &b){
        int len = a.size(), t = 0;
        for(int i = 0; i < len; ++i){
            if(a[i] != b[i]) t++;
            if(t > 1) return false;
        }
        if(t == 0) return false;
        return true;
    }
    class SN{
    public:
        int  x;
        int px;
        int l;
        SN * plink;
        SN(int _x, int _px, int _l, SN* _plink):x(_x), px(_px), l(_l), plink(_plink){}
    };
};
```



AC

```c++

//图优化版本
// 执行用时：
// 644 ms
// , 在所有 C++ 提交中击败了
// 61.99%
// 的用户
// 内存消耗：
// 19.1 MB
// , 在所有 C++ 提交中击败了
// 66.81%
// 的用户
class Solution {
public:

    vector<vector<string>> findLadders(string beginWord, string endWord, vector<string>& wordList) {
        
        vector<vector<string>> ans;
        
        int n = wordList.size(), flag = 0;
        for(int i = 0; i < n; ++i){
            if(wordList[i] == endWord) flag = 1;
        }
        if(!flag) return ans;


        //bulid the map.
        wordList.push_back(beginWord); // size++
        n++;
        vector<vector<int>> edges;
        edges.resize(n + 1);

        for(int i = 0; i < n; ++i){
            for(int j = i + 1; j < n; ++j){
                if(islink(wordList[i], wordList[j])){
                    edges[i].push_back(j);
                    edges[j].push_back(i);
                }
            }
        }
        
        vector<int>  cost(n, n + 1);
        cost[n - 1] = 0;

        //bfs
        queue<SN*> que;        
        que.push(new SN(n - 1, -1, 0, nullptr));
        int endlevel = -1;
        while(que.size()){
            SN *p = que.front(); 
            que.pop();

            if(endlevel > 0 && p->l > endlevel) continue;
            if(wordList[p->x] == endWord){
                endlevel = p->l;
                vector<string> tmp;
                SN* np = p;
                while(np  != nullptr){
                    tmp.push_back(wordList[np->x]);
                    np = np->plink;                          
                }                
                reverse(tmp.begin(), tmp.end());
                ans.push_back(tmp);
            }
                        
            // emplace more points.
            for(auto j : edges[p->x]){            
                if(cost[j] > cost[p->x]){ // 没法绕一个圈子找到最短路
                    cost[j] = cost[p->x] + 1;
                    SN* newp = new SN(j, p->x, p->l + 1, p);
                    que.push(newp);
                }
                
            }
        }

        return ans;
    }

    bool islink(const string &a, const string  &b){
        int len = a.size(), t = 0;
        for(int i = 0; i < len; ++i){
            if(a[i] != b[i]) t++;
            if(t > 1) return false;
        }
        if(t == 0) return false;
        return true;
    }
    class SN{
    public:
        int  x;
        int px;
        int l;
        SN * plink;
        SN(int _x, int _px, int _l, SN* _plink):x(_x), px(_px), l(_l), plink(_plink){} //由于历史原因，px和l有点多余
    };
};
```





双向bfs思路学习；（未完成）

```c++
class Solution {
public:
    vector<vector<string>> findLadders(string beginWord, string endWord, vector<string>& wordList) {
        vector<vector<string>> path;
        unordered_set<string> dict ,q1, q2; //dict：搜索空间 q1q2:双头搜索
        unordered_map<string, vector<string>> next;
        for(const auto &p : wordList){
            dict.insert(p);
        }
        if(!dict.count(endWord))
            return path;

        dict.erase(beginWord);
        dict.erase(endWord);

        q1.insert(beginWord);
        q2.insert(endWord);
        bool reverse = false, found = false;
        while(!q1.empty()){
            unordered_set<string> q;
            for(const auto &w : q1){
                string cw = w;
                for(size_t i = 0 ; i < cw.size(); ++i){
                    char c = cw[i];
                    for(int j = 0; j < 26; ++j){
                        cw[i] = j + 'a';
                        if(q2.count(cw)){
                            reverse ? next[cw].push_back(w) : next[w].push_back(cw);
                            found = true;
                        }
                        if(dict.count(cw)){ //count 比 find好用
                            reverse ? next[cw].push_back(w) : next[w].push_back(cw);
                            q.insert(cw);
                        }
                    }
                    cw[i] = c;
                }
            }
            // for(const auto &w :q)
            //     cout << w << " ";
            // cout << endl;
            //控制搜索层数            
            if(found)  break;
            for(const auto &w : q){
                dict.erase(w);
            }
            //选择扩展范围小的开始搜索，降低搜索数量
            if(q.size() < q2.size()){
                q1 = q;
            }else{
                reverse = !reverse;
                q1 = q2;
                q2 = q;
            }

        }

        vector<string> oneway = {beginWord};
        buildPath(next, path, oneway, beginWord, endWord);
        return path;
        
    }
    
    void buildPath(unordered_map<string, vector<string>>& next, vector<vector<string>>& path, 
                 vector<string> &oneway, string nword, string endWord){
        if(nword == endWord){            
            path.push_back(oneway);
            return;        
        }
        for(const auto &w : next[nword]){
            oneway.push_back(w);
            buildPath(next, path, oneway, w, endWord);
            oneway.pop_back();
        }
    }
};

```