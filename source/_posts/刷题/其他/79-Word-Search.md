---
title: 79. Word Search
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
categories:
date: 2020-11-26 08:42:40
tags:
---





## [79. Word Search](https://leetcode-cn.com/problems/word-search/)





## 思路：

回溯直接k.o.

<!-- more -->

## 代码：

官方

```C++
class Solution {
public:
    bool check(vector<vector<char>>& board, vector<vector<int>>& visited, int i, int j, string& s, int k) {
        if (board[i][j] != s[k]) {
            return false;
        } else if (k == s.length() - 1) {
            return true;
        }
        visited[i][j] = true;
        vector<pair<int, int>> directions{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        bool result = false;
        for (const auto& dir: directions) {
            int newi = i + dir.first, newj = j + dir.second;
            if (newi >= 0 && newi < board.size() && newj >= 0 && newj < board[0].size()) {
                if (!visited[newi][newj]) {
                    bool flag = check(board, visited, newi, newj, s, k + 1);
                    if (flag) {
                        result = true;
                        break;
                    }
                }
            }
        }
        visited[i][j] = false;
        return result;
    }

    bool exist(vector<vector<char>>& board, string word) {
        int h = board.size(), w = board[0].size();
        vector<vector<int>> visited(h, vector<int>(w));
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                bool flag = check(board, visited, i, j, word, 0);
                if (flag) {
                    return true;
                }
            }
        }
        return false;
    }
};

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/word-search/solution/dan-ci-sou-suo-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```



我滴，不过由于没有把判断条件写在dfs函数入口那，性能显得不太好。

```C++
class Solution {
public:
    int m, n;
    int dx[4] = {-1, 1, 0, 0};
    int dy[4] = {0, 0, -1, 1};
    bool dfs(vector<vector<char>>& board, string word, vector<vector<bool>> &vis, int x, int y, int pos){ //BUGS VECTOR &
        if(x < 0 || y < 0 || x >= m || y >= n || vis[x][y] || pos == word.size()) return false;
        vis[x][y] = true;
        cout << x << ' ' << y << endl;        
        if(board[x][y] == word[pos]){
            if(pos == word.size() - 1) return true;
            for(int i = 0;i < 4; ++i){
                int nx = x + dx[i];
                int ny = y + dy[i];
                if(dfs(board, word, vis, nx, ny, pos + 1))
                    return true;
            }
        }
        return false;
    }   
    bool exist(vector<vector<char>>& board, string word) {
        m = board.size();
        if(m > 0){
            n = board[0].size();
        }
        
        for(int i = 0; i < m; ++i){
            for(int j = 0; j < n; ++j){
                if(word[0] == board[i][j]){
                    cout << "i * j" ;
                    vector<vector<bool>> vis(m, vector<bool>(n, 0));
                    if(dfs(board, word, vis, i, j, 0))
                        return true;
                }                
            }
        }
        return false;
    }
};
```