---
title: 382. Linked List Random Node
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2021-01-10 10:05:02
---




## [382. Linked List Random Node](https://leetcode-cn.com/problems/linked-list-random-node/)



## 思路：

让我想起来之前来宁大讲座的美国教授的出的抽取车流题目。

我们可以使用蓄水池抽样算法（Reservoir Sampling）:

考虑抽取一个样例的情况：我们从头遍历一个List，并以$1/k$的概率把第k个元素保留下来。

可以由归纳法得：

第k-1个元素的保留概率是$1/(k - 1)$，在第K个元素遍历时，第K-1次遍历是被保留的元素在这次被保留的概率是$\frac{1}{k-1} * \frac{k - 1}{k}= \frac{1}{k}$ 。

这就保证了遍历一遍全部数组后，各个元素被抽取的等概率性质。

<!-- more -->

再考虑k>1的情况，证明更复杂一点：

![1.png](http://static.come2rss.xyz/831bdf1ea840c47b79007f206fb9fe6f1a1effb6c5ceed15509fe0abb23ed2f9.jpg)



实现代码：

```c++

import java.util.Random;

Class Solution{
    public static void main(String[] args){
        int[] nums = new int[]{1, 2, 3, 4, 5};
        Solution s = new Solution();
        int[] ans = s.sample(nums, 3);
        for(int i = 0; i < ans.length; i++){
            System.out.printf("%d ", ans[i]);
        }
    }
    private int[] sample(int[] nums, int n){
        Random rd = new Random();
        int[] ans = new int[n];
        for(int i = 0; i < nums.length; i++){
            if(i < n){
                ans[i] = nums[i];
            } else {
                if(rd.nextInt(i+1) < n){
                    ans[rd.nextInt(n)] = nums[i];
                }
            }
        }
        return ans;
    }
}
```



## 代码

```c++

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
private:
    ListNode* head;
    int ct = 0;
public:
    /** @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node. */
    Solution(ListNode* _head): head(_head) {
        // newp = p = head;
    }
    
    /** Returns a random node's value. */
    int getRandom() {  //蓄水池随机抽取算法
        ListNode *p = head, *newp = head;
        int ct = 0;
        while(newp){
            ++ct;
            if(rand() % ct == 0){
                p = newp;
            }
            newp = newp->next;
        }   
        return p->val;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(head);
 * int param_1 = obj->getRandom();
 */
```