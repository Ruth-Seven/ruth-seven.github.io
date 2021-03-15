---
title: C++标准库
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
date: 2021-03-14 16:01:40
tags:
categories:
---



<!-- more -->



# C++标准库





# IO库



`iostream`包含的`istream`，`ostream`和`iostream`是`iofstream`和`iosstream`所包含的继承类的范例。（`w`宽字符系列类先不讨论。）这极大方便了对不同输入输出的编程工作！

常见的`cin`就是一个`istream`实例。

 

IO对象无靠拷贝和赋值，所以一般调用都是用引用。IO对象。

IO对象有效才能工作，出错有专门的状态位表示，也可以使用函数查询和置位。

## 文件流对象

文件IO对象需要打开文件，其销毁时会自动销毁，也可以手动关闭。

文件流对象的新创建或者每次打开文件，都会改变其文件模式。默认模式一般是`out`和`trunc`，写的同时截断所有内容（消除）。

> 文件流读写要注意权限，尤其是Linux编程！

```c++
// 默认模式
ofstream out("file") ;
// 输出 + 添加
ofstream out("file"， ofstream::out | ofstream::app);

//open 也是一样
ofstream out;
out.open("file", ofsteam::app)
```

## 字符串流

`stringstream`、`istringstream`和`ostringstream`的工作同上。`ostringstream.str()`可获取最后输出的结果。

-----



# 顺序容器



## 序列容器



序列容器`strign`| `vector`| `deque` | `list` | `forward_list` | `array`，支持几乎统一的接口，比如迭代器（正向和反向），插入，初始化等等。比较特殊用的少的，`array`初始化还需要指定固定大小。



>  值初始化是容器没有指定初始化值对各个元素进行的默认初始化过程。



各种类型的容器因为其特性的限制，经常有一些API无法使用。比如`vector`和`string`没有`pop_front`，`forward_list`没有`psuh_back`，

**容器的拷贝和赋值**方法很多，一般来说都是要求元素和容器类型相同，拷贝中`contain(other.begin(), other.end())`允许支持不同但是兼容的元素类型，因为他们可以相互转换。赋值有`container.assign(oldstyle.begin(), oldstyle.end())`，也支持元素转化，比如`*char`到`string`。

 

插入相关的方法还是非常多。`emplace`族方法会在直接在容器管理的内存空间中构建元素，调用时要符合被压入元素的构造方法：

````c++
// 两者结果等价
c.emplace_back("info", 20, 20.0);
c.emplace_back({"info", 20, 20.0});

// 使用默认构造函数
c.emplace_back();
````



访问对象的出乎意料的有`front()`和`back()`，返回了引用的数据（可`const`）。



对于`vector`，`string`和`deque`，插入，删除操作定位会是容器的迭代器失效。当然也有不失效的时候，当容器内存空间没重构，或者改变的部分没有波及到迭代器指向的元素，就不会有事。但维护迭代器的有效性是非常重要的。



需要“内存管理”的容器，`string`，`vector`和`deque`都有内存管理函数，`size()`，`capacity()`、`reserve()`和`shrink_to_fit()`。容器可以提前分配内存，以提供后续元素置入，也可以在添加元素时自动扩容。



`string`容器具有特殊`s(str, pos, len)`等多个构造方法，其`str`可以`string`或者`const *char`（不过按照转化规则，`*char`也是可以的）。常用的有`insert()`、`erase()`、`assign()`、`replace()`、`find()`、`find_first_of()`、`stod()`、`to_string()`。

> 光光，记住所有API和其他们的繁杂的函数签名是性价比不高的，但是记住存在这么一个API并且在应用时能够快速检索到是非常有效的，如果说记住三两种常用的也是可取的 。



`list`和`forward_list`具有类似于通用泛型算法的专属算法，但是略有不同的是，`list.merge()`和`list.unique()`都会直接改变输入参数`list`的内存值，前者会销毁合并的两条链，后者会删除掉多余元素。

## vector



### 扩容原理概述

新增元素：Vector通过一个连续的数组存放元素，如果集合已满，在新增数据的时候，就要分配一块更大的内存，将原来的数据复制过来，释放之前的内存，在插入新增的元素；
对vector的任何操作，一旦引起空间重新配置，指向原vector的所有迭代器就都失效了 ；
初始时刻vector的capacity为0，塞入第一个元素后capacity增加为1；
不同的编译器实现的扩容方式不一样，VS2015中以1.5倍扩容，GCC以2倍扩容。



### `resize`和`reverse`



reserve是容器预留空间，但并不真正创建元素对象，在创建对象之前，不能引用容器内的元素，因此当加入新的元素时，需要用`push_back()/insert()`函数。

resize是改变容器的大小，并且创建对象，因此，调用这个函数之后，就可以引用容器内的对象了，因此当加入新的元素时，用operator[]操作符，或者用迭代器来引用元素对象。







## `stack`适配器



#### pop()返回类型：

为什么pop（）返回viod，而不是类型T呢？也就是说，为什么先用top（），然后用pop（）来访问和删除站定的元素，而不是把它们合并一个返回类型T的成员函数。

这种设计有很好的理由。如果pop（）返回栈顶元素，则必须按值返回，而不是按引用返回。按引用返回是不可行的，因为元素

在栈中已经不存在，必须在按引用返回之前现将其存储到某个地方。如果选用动态内存，除非动态内存最终被删除，否则将导致内存泄露。

按照**数值返回效率很差**，因为它包含对类型T的复制构造函数的调用。让pop（）返回数值将会导致潜在的内存问题或效率很低下，



## `deque`

`deque`的内部结构就是这么简单，一个`map`，加上`map`中元素指向的固定大小的数组空间。

> 我当初怎么没想到，草

![deque容器的底层存储机制](D:\个人文件\重要文件\闲书与笔记\MD暂存文件\2-191213161305R5.gif)

如果`map`数组满了就搬运，这点性能损失还是承受到起。



### `deque`迭代器

维护当前遍历数组的首尾空间的，当前元素的，指向当前数组的指针的指针。

这种调用方式就比较简单~

![deque容器的底层实现](D:\个人文件\重要文件\闲书与笔记\MD暂存文件\2-19121316430U40.gif)



## 顺序容器优缺点

| 顺序容器       | 优点                         | 缺点                   |
| -------------- | ---------------------------- | ---------------------- |
| `vector`       | 动态扩容，随机访问           | 插入费时               |
| `string`       | 随机访问                     | 无法原地修改           |
| `list`         | 插入很快                     | 无法随机访问           |
| `forward_list` | 速度快，同上                 | 同上，没有`size`       |
| `deque`        | 随机访问，头尾可插入且速度快 | 中间插入费时           |
| `array`        |                              | 固定大小，无法添加删除 |





## 容器适配器

顾名思义，就是容器的适配器。`queue` | `priority_quueu`属于队列适配器，`stack`属于栈适配器。两者各自一套的API。

容器适配器建立的其被“包裹”的容器之上，但对其类型有能力的限制。比如`stack`操作比较简单，除了`array`和`forward_list`的序列容器都可以构造，它和`queue`默认用`deque`。`prority_queue`不能用`list`系列的，默认用`vector`。



----



# 泛型算法（generic）

泛型算法是建立在迭代器之上，对`容器`进行操作的。它本身并不调用容器的API，也就是说与容器无关。它不负责检查迭代器的有效值，这是程序员的事。

几个有趣的泛型算法：

|          |                |                  |
| -------- | -------------- | ---------------- |
|          | `find()`       |                  |
|          | `accumulate()` |                  |
|          | `equal()`      |                  |
|          | `fill()`       | `fill_n()`       |
|          | `copy()`       |                  |
|          | `replace()`    | `replace_copy()` |
| 支持谓词 | `sort()`       | `stable_sort()`  |
|          | `unique()`     | `unique_copy()`  |
|          | `for_each()`   |                  |
|          | `find_if()`    |                  |

> `_if` : 表示谓词输入
>
> `_copy` : 表示不改变原输入，将变化内容输出
>
> 算法常常用谓词来重载算法

为了支持元素在容器末端插入元素，`back_inserter()`通过接受一个容器会创建一个写入就调用容器`push_back()`的`back_iterator`。



## 谓词 

> p346

所谓谓词就是可调用的表达式，其结果能判断出正确或错误。`n`元谓词接受`n`个参数。

>  C++中可调用对象只有：函数、函数指针、重载`()`的类和`lambda`表达式。







## 迭代器"适配器"

> p357

`<iterator>`定了其他几种高级迭代器。

### `Insert Iterator`

插入迭代器不同于迭代器，它通过获取迭代器产生一个只能“赋值”操作的适配迭代器，从而对容器进行操作。

- `back_iterator(Container)`会创建一个使用`push_back()`的迭代器，每次赋值都在末尾插入元素
- `front_iterator(C)`会创建一个使用`push_front()`的迭代器，每次赋值都在首部插入元素
- `inserter(C, iter)`会创建一个使用`C.insert(iter)`的迭代器，每次赋值都在`iter`指向的元素之前插入元素。

> 注意 `front`和`inserter`两者插入方式的不同。



### `iostream`迭代器

`iostream`迭代器能够为任何一个输入输出标准流，创建“容器的表现形式”的迭代器。如此，我们就可以通过流迭代器使用泛型算法，甚至用它创建容器。

要求，`istream_iterator`和`ostream_iterator`具有统一的对象，同时对象必须重载了`<<`和`>>`运算符。

> 这很河里。

```c++
#include <iterator>
#include <string>
#include <fstream>    
std::ifstream ffin(argv[1]);
std::istream_iterator<std::string> filein(ffin), string_eof; //默认初始化的string_eof，可以作为流异常或者流读取结束的标志
// std::vector<std::string> doc( , string_eof);
// print(doc);    
std::ofstream ffout(argv[2], std::ofstream::app);
std::ostream_iterator<std::string> fileout(ffout, "\n");
for_each(filein, string_eof, [&](std::string g){ *fileout++ = g;});
```



注意， 流迭代和`insert iterator`的迭代器运算形式都是`iter = val`,`*iter`和`iter++`都是返回`iter`自身，上述程序写成那样是为了保持和其他迭代器的统一形式。



### `reverse iterator`反向迭代器

这个迭代器最简单，直接把迭代器反过来用就行。



## 泛型算法结构

> p365

### 迭代器

迭代器按照其功能按层次分类， 高级层次包含了低级层村的所有功能。

`input iterator`只有判等，自加，解引用，支持箭头运算，支持读元素。

`output iterator`，不能读，只能写。

`forward interator` 可读写，还是只能向前移动

`bidirectional iterator` 多了对双向移动的支持；

`random-access iterator`功能最多，多了支持比较，数字自加自减和加法，迭代器减法，下标访问。而且序列容器大部分直接提供`random-access iterator`。

不同的泛型算法对其迭代器所提供的功能有其要求，比如`unique()`需要随机访问迭代器，`copy()`需要两个输入迭代器和一个输出迭代器。

# 关联容器

> p419

关联容器把键和值联系起来，取消了顺序容器对于位置相关的操作，比如`push_back()`。`unordered_`、`mutil`、`map`和`set`从三个维度上描述了8个容器的特点。

容器的初始化在新标准下，可以在进行值初始化了，只要类型转化成立就行。比如：

```c++
map<string, string> authors = 
{
    {"Jporure", "James"},
    {"Austhem", "Jane"},
    {"Dichens", "CHarles"}
    
}
```



## 关键字

有序容器使用关键词类型的`<`运算符来比较元素：

+ 若`k1 < k2`，则 `k2 < k1` 不成立
+ `<`具有传递性
+ 若`k1 < k2` 和`k2 < k1` 都不成立，则`k1 == k2`。

关联容器所绑定的关键词如果没有重载`<`操作符，必须指针关键容器中的关键词的操作类型。

```c++
bool compare(const Person& a, csont Person & b){
    return Person.a < Person.b;
}

map<Person, vector<Person>, decltype(compare)*> record(compare); // 用类型推导快捷的写出 方法指针的类型

```





无序容器使用`hash`算法和`==`组织元素。他可以帮助我们省下维护容器有序的代价。

**pair**

## 关联容器迭代器

使用关联容器的迭代器，可以用`while(iter != C.end())`控制循环。

通过迭代器解引用获取容器元素, `set`获取的`set_type`,即`const value_type`类型的元素。`map`获取的是`mapped_type`,即`pair<const key_type, value_type>`的元素。

这种返回的元素的特性，注定了无法改变关联容器的键，也没有办法在上面使用写的泛型算法，比如`sort`，而读算法又通常不如内置算法效率高。







## 关联容器API



关联容器的插入，除了直接插入元素，也可以构造成员`map.insert({a, b})`，也可以直接插入迭代器`map.insert(p1, p2)`。不重复键值的容器插入后，返回插入元素的迭代器和插入是否成功的指标，比如，返回值`++rest.first->second`先获取元素，再自增迭代器。而重复键值的容器一定会插入成功，所以只返回插入元素的迭代器。

它的`emplace(args)`可以直接接受可以构造为元素的参数列表。

删除也是老生常谈，`map.erase(k)`（值）、`map.erase(iter)`和`map.erase(p1, p2)`。



特殊的是，在不存在的键使用下标操作，`map`和`unordered_map`会直接创建出值为`0`的单位。这非常有利于写出简洁的代码。但如果需要区分存在是否，`count()`和`find()`就有用很多了。



对于`set`下标是无意义的，因为被映射的值。对于多重键的容器，是无法用键搜索到的。



容器还提供了查找元素的`c.lower_bound(k)`（`*iter<= k`），`c.uppper_bound(k)`(`*iter< k`)和`c.equal_range()`(`*iter1<= k, iter2<k`)。可以看到，第三个方法返回前两个函数的下标的`pair`,正好可以查找到值为`k`的所有元素。

> 特别适用于多重键值的容器。

而多重键的容器其相同键值的元素都相邻，所以可以直接用`for`和`equal_range()`遍历所有相同元素。





## 无序容器

 无序容器以`hash`和重载`==`操作为支持，把元素映射到各个桶。标准库为内置类型设计了`hash`模板。

创建自定义键值的无序容器需要提供`hash`模板和重载`==`。

```C++
size_t hasher(const Person &per){
    return hash<string>()(per.isbn());
}

bool epOp(const Person& aPer, const Person& bPer){
    return aPer.info() == bPer.info();
}
using Per_multiset = unordered_multiset<Person, decltype(hasher)*, decltype<epOp>*>;
//桶大小， hash函数, 相等性判断函数指针
Per_multiset PersonInfo(40, hahser, epOp);

```





## 关联容器优缺点



| 顺序容器        | 优点                 | 缺点           |
| --------------- | -------------------- | -------------- |
| `map`           | 有序；查找时间平衡   |                |
| `unordered_mpa` | `o(1)`查找，不稳定   | 无序；需要扩容 |
| `set`           | 有序；查找时间平衡   |                |
| `mutilset`      | 允许多个相同的值插入 |                |
|                 |                      |                |





# 标准库特殊设施

## tuple

> p636



`tuple<T1, T2, ....., Tn> t(v1, v2, .... , vn)`可以方便的容纳不同类型的数据，常见于函数返回和数据存储。

```c++
make_tuple(v1, v3,.... vn);
auto item = get<i>(t); //模板方法：返回一个对象的引用
```

>  静态程序的痛楚就需要打非常多的类型名称！

## bitset

具有固定的位大小，可以方便的操纵`N`位二进制的。

```c++
bitset<N> b(u); //unsigned long long 初始化
bitset<N> b("1001020101"); //stirng of 0 and 1 初始化

b.any()
b.all()
b.test()
b.flip()

b.to_ulong()
b.to_string()

os >> b //从 0 1 字符流读入数据
is << b;
//等等等等
```



## 正则表达式



> p645 有点复杂，而且不如python的好用，等等再看





## 随机数生成

> 659

C++的随机数生成引擎和众多随机数分布配合起来，作为可调用对象，产出随机数。



## IO格式化

> p666





## 迭代器失效



### 序列容器

`vector`失效情况：

1. `erase`元素`a`导致`a`后面的迭代器全部失效
2. 扩容导致迭代器失效
3. 使用过时的`end`迭代器



`list`失效：

1. `erase`只会导致指向被删除的元素的迭代器失效





`deque`迭代器失效:

- 在deque容器首部或者尾部插入元素，不会使得任何迭代器失效；

- 在deque容器的首部或者尾部删除元素，只会使指向被删元素的迭代器失效；
- 在deque容器的任何其他位置进行`插入`或`删除`操作都将使指向该容器元素的所有迭代器失效；

### 关联容器

`set`和`map`迭代器失效

与list相同，当对其进行`insert`或者`erase`操作时，操作之前的所有迭代器，在操作完成之后都依然有效，但被删除元素的迭代器失效。