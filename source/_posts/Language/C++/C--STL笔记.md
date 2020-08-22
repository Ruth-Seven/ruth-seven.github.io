---
title: C++STL笔记
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
categories:
  - Language
  - C++
date: 2020-08-07 13:03:15
tags:
---



> 本篇文章中所指的区间，若无特殊说明，就是指半闭半开区间。

## vector

<!-- more -->

**定义**

```
#include<vector>
// 一维
vector< typename > v1;

// 二维
vector< vector< typename> > v2;
vector< typename> v3[arraySize];

// vector<int>(n, 2)动态生成了一个长度为n，每个元素为2的vector对象
vector<vector<int> > dp(n, vector<int>(n, 2));
```



**访问**

```
//下标
v1.[i];

//迭代器
vector< typename >::iterator it = v1.begin();
for(it; it < v1.end(); it++) // 迭代器实现了加法 和 自加
	printf("%d", *(it));
for(int i = 0; i < v1.size(); i++)
	printf("%d", *(it + i));
```

**常用函数**

```
//添加元素
v1.push_back(2);

//添加元素，而且在vector size不够的时候自动扩充，而push_back不会
v1.emplace_back(100);


//删除末尾元素
v1.pop_back();

// 个数
v1.size(); // return a unsigned value.

//清空
v1.clear();

//插入元素
v1.insert(it, x); //在it处插入一个元素x, O(n)

// 删除
v1.earse(it); // 删除一个在it的元素
v1.earse(v1.begin(), v1.end() ); // 删除一个[beign(), end())范围内的区间所有元素
```

## set

集合，一个内部自动按升序排序且不含重复元素的容器。

**定义**

```
#include<set>
set<typename> s1;
set<typename> s2[arraySize];

```

**访问**

```
c++ //set只能使用迭代器访问 set< typename>::iterator it = s1.begin(); for....
```

**常用函数**

```
//插入元素x，并自动排序，去重 O(logN)
s1.insert(x);

//查找value对应的迭代器 O(logN)
s1.find(value);

// 个数
s1.size();

//清空
s1.clear();

//删除
s1.earse(it); //删除一个it对应的元素
s1.earse(value); //删除一个元素value
s1.earse(s1.begin(), s1.end()); // 删除一个[beign(), end())范围内的区间所有元素

​```c++



## string

**定义**

​```c++
#include<string>
string str;
string str = "hello world";
```

**访问**

```
//下标
str[i];

// 迭代器
string::iterator it = str.begin();
*(it);
```

**输出输入**

```
//标准
cin >> str;
cout << str;

//转为为cstr

printf("%s", str.c_str());
```

**常用操作**

```
// += 自加
str += str;

// + 加法
str2 = str + str;

// compare operator 按字典序比较，比如 ==, !=, <, >,<=等
str == str2;
```

**常用函数**

```
// 个数
str.size();
str.length();

//插入 O(N)
str.insert(pos,  string);
str.insert(itPos, itInsertBegin, itInsertEnd); //在itPos中插入一个区间上的字符串

// 删除
str.erase(it); //删除单个元素
str.erase(itFirst, itEnd); //删除区间元素
str.erase(pos, length); //删除长度为length从pos开始的字符子串

// 清除
str.clear();

//子串
str.substr(pos, len);  //返回长度为length从pos开始的字符子串


//常数
string::npos == -1  ;// 为unsigned_int类型，可大概4e9大小或者说-1

//查找 find 返回子串的第一处出现的位置，或者返回npos（没有这个子串）
str.find(str1);
str.find(str1, pos);// 从pos处开始查找资源

//替换
str.replace(pos, len, str2); //把从pos开始的长为len的str子串替换为str2
str.replace(it1, it2, str2); //把[it1, it2)区间上的子串替换为str2
```

## map

**定义**

```
#include<map>
map<typename, typename> mp; //map不可使用char数组作为键或者值；
```

**访问**

```
//下标访问
mp['c'] = 2 // 访问并赋值

//迭代器
map<char, int>::iterator it = mp.begin();
for(it; it < mp.end(); it++)
	printf("%c %d\n", it->first, it->second); // 使用迭代器访问键和值

​```c++

**查找**

​```c++
map<char, int>::iterator it = mp.find(key); //返回 键为key 的元素的迭代器
```

**删除**

```
mp.erase(it); //删除迭代器指向里的映射  O(1)
mp.erase(key); //删除键对应的映射
mp.erase(mp.begin(), mp.end()) //删除迭代器指向的区间上元素
```

**常用函数**

```
1// 个数
mp.size();

// 清除
mp.clear();
```

更多的类型有`unoderde_map`和`multimap`。

## queue

**定义**

```
#include<queue>
queue<typename> que;
```

**访问**

```
//只能访问队尾和队首
que.back();
que.front();
```

**常用函数**

```
//向队尾插入元素
que.push();

//删除队首元素，无返回队首元素
que.pop();

//判空
que.empty(); // 判断que是否为空

// 个数
que.size();
```

## priority_queue

底层由堆实现。

**定义**

```
#include<queue>
priority_queue<typename> pq;
```

**常用函数**

```
//插入元素
pq.push(value); // O(logN)

//获取队首元素
pq.top(); //若队空，则会导致报错

//队首出队
pq.pop();

//判空
pq.empty();

//个数
pq.size();
```

**优先级设置**

```
//一般数据结构
priority_queue<int> pq; //默认优先级大的在顶部（数字大）
priority_queue<int, vector<int>, less<int> > pq; // 数字逐步减少，优先级大的在顶部
priority_queue<int, vector<int>, greater<int> > pq; // 数字逐步增加，优先级小的在顶部

//结构体 设置1
struct str{
    string name;
    int price;
    //友元函数重载"<"符号，函数判断了两个str的优先级，name字典序大的的优先级高
    //  即name字典序高的排前面
   // 同理可以设置          return s1.name > s2.name; 达到字典序小的优先级高的效果
    frind bool operator < (str s1, str s2){
        return s1.name < s2.name;
    }
}

//结构体 设置2
struct str{
    string name;
    int price;
}
// 效果类似，不过还是移出来
struct cmp{
    bool operator () (str s1, str s2){
        return s1.name < s2.name;
    }
}
```

> 为了提高效率和速度，可以在函数传参的时，添加`const`和`&`符号
>
> ```
> friend bool operator < (const fruit &f1, const fruit &f2){
> 	return f1.price < f2.price;
> }
> friend bool operator () (const fruit &f1, const fruit &f2){
> 	return f1.price < f2.price;
> }
> ```

## stack

**定义**

```
#include<stack>
stack< typename > name;
```

**访问**

```
st.top(); //只能访问顶部数据
```

**常用函数**

```
//入栈
st.push();

//弹出
st.pop();

//空
st.empty();

//个数
st.size();
```

## pair

**定义**

```
#include<utility>
pari<typename1, typename2> name;

//初始化
pair<string, int> p("nihe", 5);

//临时使用
p = pair<string,int>("haha", 5);
p = make_pair("haha", 5);
```

**访问**

```
//结构体方式
p.first; //访问第一个元素
p.second;//访问第二个元素
```

**比较**

```
//先判断pair的first元素，在判断second元素。
p1 < p1 //等等
```

**常见用法**

```
//构造二元结构体, 减少时间
p = make_pair("niha", 34);

//作为map的键值插入
mp.insert(p);
```

## algorithms

`reverse(itBegin, itEnd)` 翻转容器中从[itBegin,itEnd)[itBegin,itEnd)的元素。

`swap(x,y)`交换元素

`next_permutation(BidirectionalIterator itBegin, BidirectionalIterator itEnd)` 把[itBegin,itEnd)[itBegin,itEnd)的元素排列为下一个排列。(指向数组的指针应该也行，了解不深)

`fill(ForwardIterator itBegin, ForwardIterator itEnd, const T& val)` 逐个遍历 并赋值[itBegin,itEnd)[itBegin,itEnd)的元素

```
sort(itBegin, itEnd[, cmp])
//cmp例程， 数据从小到大排序；结构体同理
bool cmp(int a, int b){
    return a < b;    
}
```

`lower_bound(itFirst, itEnd, val)` 返回在有序容器中的第一个大于等于val的元素的位置（迭代器或者指针）。

`upper_bound(itFisrt, itEnd, val)`返回有序容器中第一个大于val的元素的位置（迭代器或者指针）。

> 获取下标：
>
> ```
> //至少对于数组指针来说
> pos = upper_bound(it1, it2, 3);
> index = pos - a' //减去数组首地址可得下标
> ```

\#[STL](http://blog.come2rss.xyz/tags/STL/)