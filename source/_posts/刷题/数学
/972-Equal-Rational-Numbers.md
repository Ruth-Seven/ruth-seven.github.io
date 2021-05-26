---
title: 972.Equal Rational Numbers
thumbnail: 'http://static.come2rss.xyz/紫色石楠.jpg'
toc: true
top: 5
tags:
categories:
date: 2020-09-21 09:59:40
---





#### [972. Equal Rational Numbers](https://leetcode-cn.com/problems/equal-rational-numbers/)

思路不止一种，老老实实敲敲代码但不想优化方法的人是没有前途的。

<!-- more -->

## 思路：

第一种：按字符匹配模式分类讨论

+ 两个字符串都没有重复字符串：直接去尾零比较相等值。
+ 只有一个字符串有重复字符串：只有一种情况可以相等，就是题目中无限接近的情况，比如“0.9(9)==1.0”。当然可以用数学证明的，两者相等。用语言描述比较麻烦，意会吧。
+ 两个字符串都有重复字符串：将重复字符串展开多次，尽可能比较相同长度内容即可。

第二种：化为数值法！

重复模式串的数值部分可以计算,比如：
$$
0.00(66)=\frac{1}{100} + \frac{66}{100} + \frac{66}{10000}\cdots
$$
那么一般就有
$$
0.(s) = \frac{s}{10^k }+ \frac{s}{10^{2k} \cdots} \\\\
= s*(\frac{1}{10^k} + \frac{1}{10^{2k}} \cdots)\\\\
= s * (limt_{ \ n\rightarrow\infty}\frac{\frac{1}{10^k}-\frac{1}{(10^k)^n}}{1-\frac{1}{10^k}})\\\\\
= s * \frac{\frac{1}{10^k}}{1-\frac{1}{10^k}}\\\\
which\ k \ is \ the\ len\ of\ s.
$$
非重复部分更容易计算。

那么之后用分数类来计算结果即可。



## 代码：

老实人代码

```c++
class Solution {
public:


//  if find() cant find the char or string, it will retunr str::string::npos;
// static const size_t npos = -1;  the size_t is unsigned int type. 

    
    void getNum(string input, string &integerS, string &nonreS, string &reS){
        int pointPos = input.find(".");
        if(pointPos != string::npos)
            integerS = input.substr(0, pointPos);
        else{
            integerS = input;
            nonreS = reS = "";
            return;
        } 

        int parPos = input.find("(");
        if(parPos != string::npos){
            nonreS = input.substr(pointPos + 1, parPos - pointPos - 1);
            reS = input.substr(parPos + 1, input.size() - 1 - parPos - 1);
        }else{
            nonreS = input.substr(pointPos + 1, input.size() - pointPos - 1);
            reS = ""; 
        }

        if( reS == "" || stol(reS) == 0){
            reS = "";
            int pos =  nonreS.size() - 1;
            while(pos >= 0 && nonreS[pos] == '0') pos--;
            if(pos >= 0) nonreS = nonreS.substr(0, pos + 1);
            else nonreS = "";
            if(integerS == "" || stol(integerS) == 0) integerS = "0";
        } 
    }
    
    bool isNineNum(string S){
        for(int i = 0; i < S.size(); i++)
        {
            if(S[i] != '9') return false;
        }
        return true;
    }   


    string strmul(string s, int time){
        string res = "";
        for(int i = 0; i < time; i++){
            res += s;
        }
        return res;
    }
    //must comfire reS2 == ""
    bool isfiniteEqual(string integerS1, string nonreS1, string reS1, string integerS2, string nonreS2, string reS2){    
        if(!isNineNum(reS1) || reS2.size() != 0) return false;

        int pos = nonreS1.size() - 1;
        for(;pos >= 0; pos --){
            if(nonreS1[pos] != '9') break;
        }
        if(nonreS2.size() != pos + 1) return false;

        int num1 = stol(integerS1 + nonreS1.substr(0, pos + 1));
        int num2 = stol(integerS2 + nonreS2);
        if(num1 + 1 != num2) return false;
        return true;
    }

    bool ispartEqual(string s1, string s2){
        //
        cout << s1 << endl << s2 << endl;
        if(s1.size() > s2.size()) return false;
        if(s2.substr(0, s1.size()) == s1) return true;
        return false;
    }


    bool isRationalEqual(string S, string T) {
        string integerS1 , integerS2, nonreS1, nonreS2, reS1, reS2;
        getNum(S, integerS1, nonreS1, reS1);
        getNum(T, integerS2, nonreS2, reS2);
        if(reS1.size() == 0 && reS2.size() == 0){
            if(integerS1 == integerS2 && nonreS1 == nonreS2) return true;
        }
        else if(reS1.size() == 0 || reS2.size() == 0){
            if(isfiniteEqual(integerS1, nonreS1, reS1, integerS2, nonreS2, reS2) 
            || isfiniteEqual(integerS2, nonreS2, reS2, integerS1, nonreS1, reS1))
                 return true;
        }
        else{
            int l1 = reS1.size(), l2= reS2.size();
            string str1 = integerS1 + nonreS1 + strmul(reS1, reS2.size() + 2);
            string str2 = integerS2 + nonreS2 + strmul(reS2, reS1.size() + 2);
            if(ispartEqual(str1, str2) || ispartEqual(str2, str1)) return true;
        }
        return false;
    }
};
```

数值计算



弱鸡的代码

```c++
typedef long long ll;
class fraction{
public:
    ll n, d;
    fraction(ll _n, ll _d){
        n = _n;
        d = _d;
        if(_d  == 0) d = 1;
      }

    void add(fraction s){
        n = n * s.d + d * s.n;
        d *= s.d;
         clear();
        print(fraction(n, d));
        print(s);
    }

    bool equal(fraction s){            
        if(s.d == d && s.n == n) return true;
        return false;
    }

private:
    ll gcd(ll a, ll b){
        return b?gcd(b, a%b):a;
    }
    void clear(){
        int gcdN = 1;
        if(n == 0)   
            gcdN = 1;
        else   
            gcdN = gcd(d , n);
        n /= gcdN;
        d /= gcdN;
        if(n == 0) d = 1;
    }

};


// 
class Solution {
public:

    void getNum(string input, string &integerS, string &nonreS, string &reS){
        int pointPos = input.find(".");
        if(pointPos != string::npos)
            integerS = input.substr(0, pointPos);
        else{
            integerS = input;
            nonreS = reS = "";
            return;
        } 

        int parPos = input.find("(");
        if(parPos != string::npos){
            nonreS = input.substr(pointPos + 1, parPos - pointPos - 1);
            reS = input.substr(parPos + 1, input.size() - 1 - parPos - 1);
        }else{
            nonreS = input.substr(pointPos + 1, input.size() - pointPos - 1);
            reS = ""; 
        }

    }
    
    ll pow10(ll l){
        ll ans = 1;
        while(l > 0){
            ans *= 10;
            l--;
        }
        return ans;
    }

    ll mystol(string s){
        if(s == "") return 0;
        else return stol(s);
    }

    fraction getFraction(string integer, string nonreS, string reS){
        
        fraction no1 = fraction(mystol(integer), 1);
        int nonreLen = nonreS.size();
        int reLen = reS.size();
        fraction no2 = fraction(mystol(nonreS), pow10(nonreLen));
        fraction no3 = fraction(mystol(reS), pow10(nonreLen) * (pow10(reLen) - 1) );

        no1.add(no2);
        no1.add(no3);
        return no1;
    }

    bool isRationalEqual(string S, string T) {
        string integerS1 , integerS2, nonreS1, nonreS2, reS1, reS2;
        getNum(S, integerS1, nonreS1, reS1);
        getNum(T, integerS2, nonreS2, reS2);
        
        fraction frac1 = getFraction(integerS1, nonreS1, reS1);
        fraction frac2 = getFraction(integerS2, nonreS2, reS2);
        if(frac1.equal(frac2)) return true;
        return false;
    }
};
```

