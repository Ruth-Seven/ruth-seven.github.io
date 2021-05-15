---
title: 42. Trapping Rain Water
thumbnail: 'http://static.come2rss.xyz/黑色幽默.jpg'
toc: true
top: 10
date: 2021-04-16 17:58:37
tags:
categories:
---





# [42. Trapping Rain Water](https://leetcode-cn.com/problems/trapping-rain-water/)



## 思路：

这题蛮hard的，挺考验思路；

思考一下，下雨的过程，水往低处流，一点一点汇聚起来，逐渐逐渐升高水面。我们是否可以在先求出低水平面的水量，在此之上求出高水平面的水量。

> `43234`中就有两个水沟：`2`上的`1*1`的水沟，和`323`上的`3*1`水沟。

用这种想法，我们只需要遍历得到一个水平面的右边界，记录该水平面的左边界，获取低水平面的高度，填充下新水平面的水量即可。

最小值单调栈`S`可以帮助我们维持左边界的`pos`，记`S`的栈顶元素指向的高度为`a`，`a`之下的元素指向的高度为`b`。其性质必然有`a > b`。遍历到高度`c`，

- 若`c < a`，则对蓄水没有影响。
- 如果`c > b`，则三者形成了一个水沟，计算🦁式子见代码，并且该水沟可能可以继续往上“看看”，在适当条件上看看单调栈，循环填充高水位水沟。
- 如果`c==a`，则显然应该替换掉`a`，因为单调栈维持的是等高水沟的最新端，试想`33323`。

经过上述填充过程，单调栈的性质也要维护一下，详细见代码。

<!-- more -->

## 代码：

```c++

class Solution {
public:
    int trap(vector<int>& height) {
        if(height.size() <= 1) return 0;
        stack<int> sck;
        int amount = 0;
        for(int i = 0; i < height.size(); ++i){
            while(sck.size() >= 2 && height[sck.top()] <= height[i]){
                int lowh = height[sck.top()]; 
                sck.pop();
                amount += (i - sck.top() - 1) * (min(height[i], height[sck.top()]) - lowh);
              //  cout << amount << endl;
            }
            while(!sck.empty() && height[sck.top()] <= height[i]) sck.pop();  // <= 按次序出现的等高的山峰A,B， 明显的有AB填充了水量，下一个被填充的应该是B,所以A必须被pop
            if(sck.empty() || height[i] < height[sck.top()]) sck.push(i);
        }
        return amount;
    }
};
```

