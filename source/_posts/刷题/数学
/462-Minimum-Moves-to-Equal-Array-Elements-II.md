---
title: 462. Minimum Moves to Equal Array Elements II
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:

categories:
date: 2021-01-14 11:04:09
---




## [462. Minimum Moves to Equal Array Elements II](https://leetcode-cn.com/problems/minimum-moves-to-equal-array-elements-ii/)  第K大





## 思路：



1. 第一次做，看看数据的形式似乎具有凹函数的性质，于是用三分法搜索数值。菜鸡如我，没有总结过三分，有些地方写错了，wa了一次，int超范围了一次。这题好坏啊。算法复杂度$o(nlogn)$。

   <!-- more -->

2. 还有一种思路是排序后，依照凹函数性质二分搜索也可以！复杂度$o(nlogn + nlogn)$ ，还是我快，不过我的n不是他的n。

3. 看题解，发现寻找中位数的方法，更好更容易证明，

可以发现，奇数个数组的中位数容易的，如果在偶数个数字的数组中，中位数公式：
$$
mid\_element = \frac{Arr[size / 2] + Arr[size / 2 + 1]}{2}
$$
幸运的是，在该题意下，直接使用$Arr[size / 2]$的计算值和使用$min\_element$效果一致。题意可以化简。

4. 上题的代码，还可是使用第$k$大数字题目使用的算法来求解。

## 代码：

1



```c++

class Solution {
public:
    using ll = long long; //这题太坏了
    ll gap(vector<int> & nums, ll g){
        ll res = 0;
        for(auto k : nums){
            res += abs(k - g);
        }
        return res;
    }
    ll minMoves2(vector<int>& nums) {
        if(nums.size() == 0) return 0;
        int maxv = *max_element(nums.begin(), nums.end());
        int minv = *min_element(nums.begin(), nums.end());

        while(minv < maxv){
            int mid1 = (maxv - minv) / 3 + minv;
            int mid2 = (maxv - minv)  * 2 / 3  + minv;
            if(mid1 == mid2) ++mid2; //[minv, maxv] = [0, 1]
            ll r1 =gap(nums, mid1), r2 = gap(nums, mid2);
            if(r1 > r2){
                minv = mid1 + 1;
            }else if(r2 > r1){
                maxv = mid2 - 1;
            }else{
                if(mid1 == mid2){
                    minv = maxv = mid1;
                    break;
                }
                minv = mid1  + 1;
                maxv = mid2 - 1;
            }
            // cout << minv << ' ' << maxv << endl;
        }
        return gap(nums, minv);
    }
};
```



2

```c++

class Solution {
public:
    int minMoves2(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int l=0,r=nums.size()-1,mid;
        while(l<r){
            mid=(l+r)>>1;
            if(sumof(nums[mid],nums)<sumof(nums[mid]+1,nums)) r=mid; //利用了凹函数的特性
            else l=mid+1;
        }
        return sumof(nums[l],nums);
    }
    long sumof(int n,vector<int>& nums){
        long sum=0;
        for(int i=0;i<nums.size();i++){
            sum+=abs(nums[i]-n);
        }
        return sum;
    }
};
```



3

```c++
class Solution {
public:
    using ll = long long;
    long minMoves2(vector<int>& nums){
        sort(nums.begin(), nums.end());
        ll sum = 0;
        for(auto k : nums){
            sum+=abs(k - nums[nums.size() / 2]);
        }
        return sum;
    }
};
```

4

```c++
class Solution {
public:
    using ll = long long;
    long minMoves2(vector<int>& nums){
        nth_element(nums.begin(), nums.begin() + nums.size() / 2, nums.end());//偷懒
        ll sum = 0;
        for(auto k : nums){
            sum+=abs(k - nums[nums.size() / 2]);
        }
        return sum;
    }
};
```



我的实现：效率巨低

```c++
class Solution {
public:
    using ll = long long;
    long minMoves2(vector<int>& nums){
        my_nth_element(nums, 0, nums.size(), nums.size() / 2);
        ll sum = 0;
        for(auto k : nums){
            sum+= abs(k - nums[nums.size() / 2]);
        }
        return sum;
    }
    
    int partition(vector<int> &nums, int s, int e){        
        int l = s, r = e - 1, temp = nums[s];
        while(l < r){
            while(l < r && nums[r] >= temp) --r;
            swap(nums[r], nums[l]);
            while(l < r && nums[l] <= temp) ++l;
            swap(nums[r], nums[l]);
        }
        // nums[l] = temp;
        return l;
    }

    void my_nth_element(vector<int> &nums, int s, int e, int k){
        if(s == e) return;
        int idx = partition(nums, s, e);
        if(idx == k) return;
        else if(idx < k) my_nth_element(nums, idx + 1, e, k);
        else my_nth_element(nums, s, idx, k); // bugs, e 是边界， 所以不能取 s - 1
    }
};
```

第K大算法中另一种patition算法。

```c++
class Solution {
public:
    using ll = long long;
    long minMoves2(vector<int>& nums){
        my_nth_element(nums, 0, nums.size(), nums.size() / 2);
        ll sum = 0;
        for(auto k : nums){
            sum+= abs(k - nums[nums.size() / 2]);
        }
        return sum;
    }
    
    // int partition(vector<int> &nums, int s, int e){        
    //     int l = s, r = e - 1, temp = nums[s];
    //     while(l < r){
    //         while(l < r && nums[r] >= temp) --r;
    //         swap(nums[r], nums[l]);
    //         while(l < r && nums[l] <= temp) ++l;
    //         swap(nums[r], nums[l]);
    //     }
    //     // nums[l] = temp;
    //     return l;
    // }

    // 该算法基于一种朴素的想法：把小的前面，大的放后面
    int partition(vector<int> &nums, int s, int e){     
        int i = s, pivot = nums[e - 1];
        for(int j = s; j < e; ++j){
            if(nums[j] < pivot){
                swap(nums[i], nums[j]);
                ++i;
            }
        }
        swap(nums[i], nums[e - 1]);
        return i;
    }
    void my_nth_element(vector<int> &nums, int s, int e, int k){
        if(s == e) return;
        int idx = partition(nums, s, e);
        if(idx == k) return;
        else if(idx < k) my_nth_element(nums, idx + 1, e, k);
        else my_nth_element(nums, s, idx, k); // bugs, e 是边界， 所以不能取 s - 1
    }
};
```