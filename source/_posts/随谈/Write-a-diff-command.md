---
title: Write a diff command
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
date: 2021-08-23 09:09:54
tags:
categories:
---





## 写一个简单的`diff`

晚上在看酷壳的 rsync 核心算法，突然感受到算法光芒的笼罩之中，突然想起之前很好奇的一个问题，`diff`是怎么实现的？

<!-- more -->

### 思路

把文件行代替为字符，把`diff`算法抽象成：比较两个字符串`a`、`b`的异同，或者说最大相同，最小不同。再或者说，我们可以指出`a`、`b`最长公共序列、`a`和`b`上“独有”的字符（不包含在子序列），形式上会联想到“两个字符串至少操作K次才能相等”， “最大公共子序列”等题目。更明显的，我们可以考虑用最大公共子序列算法作为引子。

仔细想一想，我们可以利用 dp 的思想，如果有子问题：已比较完成的子串`a[0~i]`、`b[0~j]`，如何判断`a[i]`、`b[j]`是公共序列串相同字符，还是他们是子串独有的字符？

可以联想我们在最大的公共序列串算法，在状态转移过程中的方程提供了我们答案：

- 在`a[i] == b[i]`时：两者为公共子序列的字符
- 在`a[i] != b[i]` 且`dp[i + 1][j + 1] == dp[i][j + 1]`时：`a[i]`为`a`独有的字符串
- 在`a[i] != b[i]` 且`dp[i + 1][j + 1] == dp[i + 1][j]`时：`b[i]`为`b`独有的字符串
- 根据转移方程，没有额外情况

代码

```c++

#include <iostream>
#include <vector>
#include <fstream>
#include <string>

using namespace std;
vector<vector<int> > dp;
vector<string> a, b;

void fill_dp()
{
    int n = a.size();
    int m = b.size();
    dp.resize(n + 1, vector<int>(m + 1, 0));
    for (int i = 0; i <= n; i++)
    {
        for (int j = 0; j <= m; j++)
        {
            if (i == 0 || j == 0)
                dp[i][j] = 0;
            else if (a[i - 1] == b[j - 1])
                dp[i][j] = dp[i - 1][j - 1] + 1;
            else
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
        }
    }
}

void print_diff()
{
    vector<string> diff;
    int i = 1, j = 1;
    while (i <= a.size() || j <= b.size())
    {
        if (i <= a.size() && j <= b.size() && a[i - 1] == b[j - 1])
        {
            diff.push_back("   " + a[i - 1]);
            i++;
            j++;
        }
        else if (j <= b.size() && (i == 0 || dp[i][j] == dp[i][j - 1]))
        {
            diff.push_back(" + " + b[j - 1]);
            j++;
        }
        else if (i <= a.size() && (j == 0 || dp[i][j] == dp[i - 1][j]))
        {
            diff.push_back(" - " + a[i - 1]);
            i++;
        }
        // else
        // {
        //     printf("%s_%s_\n", a.c_str(), b.c_str());
        //     cout << i << ' ' << j << endl;
        //     for (int i = 0; i < a.size() + 1; i++)
        //     {
        //         for (int j = 0; j < b.size() + 1; j++)
        //         {
        //             cout << dp[i][j] << " ";
        //         }
        //         cout << endl;
        //     }
        //     break;
        // }
        // cout << i << j << endl;
    }
    for (int i = 0; i < diff.size(); i++)
    {
        cout << setw(4) << i + 1;
        cout << diff[i] << endl;
    }
}

void read_file(char *file, vector<string> &lines)
{

    ifstream f(file);
    if (!f.is_open())
    {
        cout << "fail to open file " << file << endl;
        return;
    }
    while (f)
    {
        string line;
        getline(f, line);
        lines.push_back(line);
    }
}

int main(int args, char **argv)
{
    if (args < 3)
    {
        cout << "Please input two filenames to compare." << endl;
        exit(1);
    }
    read_file(argv[1], a);
    read_file(argv[2], b);
    fill_dp();
    print_diff();
    return 0;
}
```





### 效果

完全一致~

```shell
$ diff x.txt y.txt -u 
--- x.txt       2021-08-22 22:55:51.000000000 +0800
+++ y.txt       2021-08-22 23:02:43.000000000 +0800
@@ -6,4 +6,8 @@
 if isinstance(dir_paths, str):
     dir_paths = [dir_paths for _ in (urls if use_url else keys)]
 print(dir_paths)
+use_url = 0
+if isinstance(dir_paths, str):
+    dir_paths = [dir_paths for _ in (urls if use_url else keys)]
+print(dir_paths)
 print(type(urls) == list)
\ No newline at end of file

# bytedance @ C02FQ0RQMD6V in ~/projection/python/uploader [23:02:47] C:1
$ g++ diff.cpp -o diff 

# bytedance @ C02FQ0RQMD6V in ~/projection/python/uploader [23:24:01] 
$ ./diff x.txt y.txt
   1   # url_download = 0
   2   urls = [x for x in range(10)]
   3   keys = [x for x in range(19)]
   4   dir_paths = "1"
   5   use_url = 0
   6   if isinstance(dir_paths, str):
   7       dir_paths = [dir_paths for _ in (urls if use_url else keys)]
   8   print(dir_paths)
   9 + use_url = 0
  10 + if isinstance(dir_paths, str):
  11 +     dir_paths = [dir_paths for _ in (urls if use_url else keys)]
  12 + print(dir_paths)
  13   print(type(urls) == list)
  14   
```