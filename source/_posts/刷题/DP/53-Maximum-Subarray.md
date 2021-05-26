---
title: 53. Maximum Subarray
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-12-28 15:41:34
---





## [53. Maximum Subarray](https://leetcode-cn.com/problems/maximum-subarray/)



## 思路：

1. dp
2. 线段树区间查询

<!-- more -->

以下的题解，摘录自LeetCode：



![image-20201228154320926](http://static.come2rss.xyz/image-20201228154320926.png)

![image-20201228154336934](http://static.come2rss.xyz/image-20201228154336934.png)

![image-20201228154406542](http://static.come2rss.xyz/image-20201228154406542.png)



> 上面的时间渐进上界大概是$o(2N)$。

## 代码：

```c++
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int n = nums.size();
        if(n <= 0 ) return 0;
        int maxsum = nums[0];
        int adds = 0;
        for(int i = 0;i < n; ++i){
            adds += nums[i];
            maxsum = max(maxsum, adds);
            if(adds < 0){
                adds = 0;
            }
        }
        return maxsum;

    }
};
```

线段树多段查询

```c++
class Solution {
public:
    struct sts{
        
        int msum, isum, lsum, rsum;
    };

    sts pushup(sts l, sts r){
        sts a; 
        a.msum = max(max(l.msum, r.msum), l.rsum + r.lsum);
        a.lsum = max(l.isum + r.lsum, l.lsum);
        a.rsum = max(r.isum + l.rsum, r.rsum);
        a.isum = l.isum + r.isum;
        return (sts){a.msum, a.isum, a.lsum, a.rsum};
    }

    sts get(vector<int> &nums, int l, int r){
        if(r == l){
            return (sts){nums[r], nums[r], nums[r], nums[r]};
        }
        int m = (r + l) >> 1;
        sts a = get(nums, l, m);
        sts b = get(nums, m + 1, r);
        return pushup(a, b);
    }
    int maxSubArray(vector<int>& nums) {
        if(nums.size() == 0) return 0;
        return get(nums, 0, nums.size() - 1).msum;

    }
};
```