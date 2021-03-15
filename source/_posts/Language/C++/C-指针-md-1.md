---
title: C++指针
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
date: 2021-03-14 16:01:34
tags:
categories:
---




<!-- more -->

[toc]

# C++指针



## 指针和数组

数组要么在静态存储区被创建（如全局数组），要么在栈上被创建。数组名对应着（而不是指向）一块内存，其地址与容量在生命期内保持不变；数组实际上就是一个常量指针，例如：

```c++
char ar[10];  //就相当于char * const ar;  即数组名对应一块空间， 该数组名不能指向其他空间。
```
> 指针可以随时指向任意类型的内存块，它的特征是“可变”，所以我们常用指针来操作动态内存。指针远比数组灵活，但也更危险。
>
> 数组是可以退化为指针的，比如作为参数。

数组也可以可以被引用。

```c++
char s[10] = "dsjflk";
void f(char (&s)[10]); //形参为 10个int的数组的引用

void f(char (&s)[10]); //✖ 形参为 10个int引用的数组
```





### 指针和数组的区别：

1.数组和指针与内存空间的关系：

   数组一般在栈区开辟空间，也可以在静态区开辟空间（全局数组、静态数组），空间的开辟与回收都由编译器或操作系统来完成，不需要程序员手动执行，不会产生内存泄露。

   指针首先是一个变量，是变量就要有存储空间，所以指针变量一般在栈区存储，如果说指针变量指向一个已存在的变量，则不需开辟空间；如果说指针指向一块动态开辟的空间，需要使用malloc或new开辟，指针变量的值保存的是在堆上开辟空间的首地址，不再使用指针时，需使用free或delete手动释放内存，否则会造成内存泄露。

2.修改内容：
数组和指针虽然都可以用一个字符串来初始化，尽管看上去一样，但底层机制却不同。例如：

```c++
void main()
{
    char ar[] = "hello";
    cout<<ar<<endl;
    ar[1] = 'E';    // Ok "hEllo\0"

    char *p = "hello";
    cout<<p<<endl;
    p[1] = 'E';     // Error
}
```
       数组ar的实际存储应该是在栈上分配6个（注意不是5个）空间，用来存储‘h’,‘e’,‘l’,‘l’,‘o’,‘\0’，

  ar（一个常量指针）可以看成是‘h’的首地址，这6个字节的空间是可以改变的，即ar[i]可以作为左值；
  指针p,首先在栈上开辟4个字节的空间（与编译器和平台有关），"hello"是一个常量字符串，**位于静态区**，常量字符串属于只读区，不可改变，所以p[1] = ‘E’出错。

3.赋值与比较：

```c++
void main()
{
    char ar[] = "hello";
    char br[10];
    //br = ar;     // Error
    if(ar == br)  // Error 
    {}

    char *p;
    p = ar;   //只是把ar的首元素的地址赋给p
    p = new char[strlen(ar)+1];
    strcpy(p, ar);  //可以把ar的内容拷贝到p
}
```
 不能对数组名进行直接复制与比较。示例2中，若想把数组ar的内容复制给数组br，不能用语句 br = ar ，否则将产生编译错误。应该用标准库函数strcpy进行复制。同理，比较br和ar的内容是否相同，不能用if(br==ar) 来判断，应该用标准库函数strcmp进行比较。

语句p = ar 并不能把a的内容复制指针p，而是把a的地址赋给了p。要想复制ar的内容，可以先用库函数malloc为p申请一块容量为strlen(a)+1个字符的内存，再用strcpy进行字符串复制。同理，语句if(p==ar) 比较的不是内容而是地址，应该用库函数strcmp来比较。

4.计算内存容量：

```c++
void fun(char ar[]) //数组类型退化为指针
{
    cout<<sizeof(ar)<<endl;    // 4
}
```

        用运算符`sizeof`可以计算出数组的容量（字节数）。示例2中，`sizeof(ar)`的值是6（注意别忘了’\0’）。
    指针p指向ar，但是`sizeof(p)`的值却是4。这是因为`sizeof(p)`得到的是一个指针变量的字节数，相当于`sizeof(char*)`，而不是p所指的内存容量。`C++/C`语言没有办法知道指针所指的内存容量，可以把数组长度作为一个参数传入函数。
注意当**数组作为函数的参数进行传递**时，该数组自动退化为同类型的指针。示例中，不论数组ar的容量是多少，`sizeof(ar)`始终等于`sizeof(char *)`。



### 数组指针和指针数组的区别

> 指针的定义要从内到外，从优先级高到优先级低来理解。
>
> 优先级：`()>[]>*`

数组指针（也称行指针）定义 `int (*p)[n]`;
`()`优先级高，首先说明p是一个指针，指向一个整型的一维数组，这个一维数组的长度是n，也可以说是p的步长。也就是说执行p+1时，p要跨过n个整型数据的长度。

如要将二维数组赋给一指针，应这样赋值：

```c++
int a[3][4];
int (*p)[4]; //该语句是定义一个数组指针，指向含4个元素的一维数组。
 p=a;    //将该二维数组的首地址赋给p，也就是a[0]或&a[0][0]
 p++;    //该语句执行过后，也就是p=p+1;p跨过行a[0][]指向了行a[1][]
```

所以数组指针也称指向一维数组的指针，亦称行指针。

**指针数组**定义 `int *p[n]`;
`[]`优先级高，先与p结合成为一个数组，再由`int*`说明这是一个整型指针数组，它有n个指针类型的数组元素。这里执行p+1是错误的，这样赋值也是错误的：`p=a`；因为p是个不可知的表示，只存在p[0]、p[1]、p[2]...p[n-1]，而且它们分别是指针变量可以用来存放变量地址。但可以这样 `*p=a`; 这里*p表示指针数组第一个元素的值，a的首地址的值。
如要将二维数组赋给一指针数组:

```c++
int *p[3];
int a[3][4];
for(i=0;i<3;i++)
p[i]=a[i];
//这里int *p[3] 表示一个一维数组内存放着三个指针变量，分别是p[0]、p[1]、p[2]
// 所以要分别赋值。
```

这样两者的区别就豁然开朗了，数组指针只是一个指针变量，似乎是C语言里专门用来指向二维数组的，它占有内存中一个指针的存储空间。指针数组是多个指针变量，以数组形式存在内存当中，占有多个指针的存储空间。
还需要说明的一点就是，同时用来指向二维数组时，其引用和用数组名引用都是一样的。
比如要表示数组中i行j列一个元素：
`*(p[i]+j)、*(*(p+i)+j)、(*(p+i))[j]、p[i][j]`

 





# 指针

指针类型的大小是固定的（无论该指针指向哪种数据类型），在32位系统中为4字节；在64位系统中为8字节。

## 野指针

#### 野指针产生的原因：

> [参考](https://www.cnblogs.com/asking/p/9460965.html#:~:text=%E9%87%8E%E6%8C%87%E9%92%88%E7%9A%84%E5%8D%B1%E5%AE%B3%EF%BC%9A,%E9%9C%80%E8%A6%81%E5%BE%88%E9%95%BF%E7%9A%84%E6%97%B6%E9%97%B4%E3%80%82)

1、指针定义时未被初始化：指针在被定义的时候，如果程序不对其进行初始化的话，它会指向随机区域，因为任何指针变量（除了static修饰的指针变量）在被定义的时候是不会被置空的，它的默认值是随机的。

2、指针被释放时没有被置空：我们在用malloc开辟内存空间时，要检查返回值是否为空，如果为空，则开辟失败；如果不为空，则指针指向的是开辟的内存空间的首地址。指针指向的内存空间在用free()或者delete（注意delete只是一个操作符，而free()是一个函数）释放后，如果程序员没有对其置空或者其他的赋值操作，就会使其成为一个野指针。

3、指针操作超越变量作用域：不要返回指向栈内存的指针或引用，因为栈内存在函数结束的时候会被释放。

### 野指针的危害：

野指针的问题在于，指针指向的内存已经无效了，而指针没有被置空，解引用一个非空的无效指针是一个**未被定义**的行为，也就是说不一定导致段错误，野指针很难定位到是哪里出现的问题，在哪里这个指针就失效了，不好查找出错的原因。所以调试起来会很麻烦，有时候会需要很长的时间。



#### 规避方法

初始化指针时将其置为NULL，之后再对其进行操作。

释放指针时将其置为NULL，最好在编写代码时将free()函数封装一下，在调用free()后就将指针置为NULL。

要想彻底地避免野指针，最好的办法就是养成一个良好的编程习惯。







## 指针定义

### 指针和常量


![image-20201017083000794](D:\个人文件\重要文件\闲书与笔记\MD暂存文件\image-20201017083000794.png)

### 	指针函数和函数指针



```c++
int *addition(int a, int b){
    int * sum = new int(a + b);
    return sum;
}

int subtraction(int a, int b){
    return  a - b;    
}

int operation(int x, int y, int (*func)(int ,int )){
    return (*func)(x, y);
}

int (*minus)(int, int) = subtraction;
int *m =  addition(1, 2);
int n = operation(3, *m, minus));
```

## a、&a与 &a+1

**1.正确解C语言指针中的 &a+1，假设a为一个数组**

```
int a[5]={1,2,3,4,5};
int p=(int)(&a+1); 
printf("%d",*(p-1));
```



答案为什么是5？这个问题的关键是理解 &a。a是一个数组名，也就是数组的首地址。对a进行取地址运算符，得到的是一个指向数组的指针！！！！这句话尤为重要！也就相当于`int (*p) [5] = &a;`

p 是一个指向数组的指针，它指向的是一个包含 5 个 int 元素的数组！！

那么执行 &a+1 后，p 移动了一个数组的距离，p 的偏移量相当于 `p + sizeof(int) * 5`，指向 a 数组最后一个元素的后一位 ！！

而程序中强制将指针`p`转换成一个`int*`，那么 `p -1` 其实就是 `p - sizeof(int)`所以，`p -1` 指向了数组中的最后一个元素，也就是 5

1. **以下输出分别是多少？**

```
#include <stdio.h>
int main()
{
	int a[5] = {1,2,3,4,5};
	int *ptr = (int *)( &a + 1);
	printf("%d, %d, \n", *(a+1), *(ptr-1) );
	return 0;
}
```

答案：2, 5
解释： a 为大小为5的数组，a表示数组的首地址，`&a`表示数组`a`的地址，`&a+1`表示移动了一个a数组的大小的距离，`ptr + sizeof(int) * 5`, 因此 ptr是一个指向a的最后一个元素的后一位的指针（ptr跨过了a的所有元素）。
因此，

> （1）(a+1) 表示 a 的首地址之后的一个元素，即 a[1]=2; C 语言和 Python都是 0-index;
> （2）(ptr-1) 表示指针 ptr 移动了一位，`ptr - sizeof(int)`, 因此指向a的最后一个元素`a[4]=5`;
> （3）因此输出为2和5。

这里的关键在于区分 a + 1 和 &a + 1中移动的“1”是不同的，前者只移动 `sizeof(int)`，后者移动`sizeof(int) * sizeof(a)`。

数组名 a 的特殊之处：
`&a` ： 代指 数组的整体 的地址，这里的 `a`是数组整体
`a`： 代指 数组的第一个成员，这里的 `a`是数组首地址

3.**已知语句 `int a=6`, 则执行了语句 `a+=a-=a\*a` 后，变量`a` 的值为多少？**
解：只有C语言才会有可读性这么神奇的表述。
程序是从右到左执行的，a的初始值为6：
（1）第一步：`a=a-a*a=6-6*6=-30`，此时 a=-30；
（2）第二步：`a=a+（a-a*a)=(-30)+(-30)=-60`，此时 a=-60。

注意：在开发过程中，写这种语句的程序员是要被枪击的（手动滑稽）~

## `**`, a Pointer to Pointer

`int ** p = nulll`定义了一个指针的指针。



# 引用



指针从本质上来讲就是一个变量，其中所存储的就是其他变量的地址。引用可以狭义地认为是某一个变量的别名，它本身是并不存在的。

在机器码层面，也不存在指针，只存在地址（指针其实还隐含了类型信息）。变量这个概念也是不存在的，只有“无格式数据”，被带格式的指令操作而已。所以你看到引用和指针的效果一样，是因为在机器码层面，没有多余的信息去表明他们的区别了。
而在语言层面，引用的确可以理解为const指针

另外引用把地址复制一遍也是很正常的，编译器也的确没法在编译期完全分析出引用的具体指向。引用只不过因为`const`所以不能被重置，但具体指向什么，是可以运行期决定的。

```c++
int a=0,b=1; int& c = flag ? a : b;
```



引用的主要功能就是作为函数的参数和返回值，当你需要指向某个东西，而且一定专一，绝不会让其指向其它东西，使用引用而非指针。





# `new`和`delete`

作为传统的C++动态内存管理语句，它们非常容易出错。忘记释放内存，使用已经被释放的内存的指针都是致命的。



`new`的初始化方法有：

```c++
//默认构造： 
//内置类型用默认初始化， 其值未知
//类调用默认构造函数
int *p = new int;

//传统构造方法
int *p = new int(a)
// 值初始化
int *p = new int(a)

//列表初始化
int *p = new vector<int>{1, 2, 3, 4};

//值初始化
// 但是，类总是调用构造函数来初始化
int *p = new int(); // *p == 0

```

> 知识点补充：
>
> **拷贝初始化：** 通过值拷贝赋值新变量`int a = 3`。
>
> **直接初始化**：不使用`=`， `string s("ni hao!")`.

另外，创建`const`的数据类型也是合理的 , `const string *pcs =  new const string`。



`delete p`无法分别`p`指向的静态创建的变量，还是动态创建的变量，也无法判断`p`是否已经被释放。



### 运作机理

> [more](https://www.jianshu.com/p/a07ba8f384da)

`new operator`:

1. 调用`operator new` 或者`operator new []`来分配一块足够大的内存空间来保存对象。
2. 编译器调用的对应的构造函数进行构造，并传入初始值
3. 返回指向该对象的指针

`delete operator` :

1. 编译器调用对应对象或者数组中元素的析构函数
2. 调用标准库中的`operator delete`或者`operator delete []`释放内存空间。

> `operator delete`或者`operator delete []`仅仅只是函数，而非重载了`new`和`delete`。
>
> 

如果需要，我们可以全局或者类中自定义，`operator new`和`operator delete`。编译器调用查找顺序是从类到全局环境下的。

`::new` 和`::delete` 在将直接使用全局作用域下的函数。



### `delete []`

`delete`处理单个类类型，先会调用析构函数，释放它所占资源，然后释放它所占内存空间。

`delete []`处理数组类类型的时候，会对每一个数组对象都调用它们的析构函数，然后再释放它们所占用的内存空间。所以对于类类型的数组如果不调用`delete[]`，那就只调用了**下标为0**的对象的析构函数，可能会产生问题。

如果对于单个类对象，`delete`和`delete[]`都可以，因为`delete`是知道它要释放多大空间的，加不加[]括号的区别是对不对每个对象调用析构函数，如果只有一个的话，它就调用一次，所以没有关系。





## 动态数组非数组`vector`

> p424

C++可以使用`new int[N]`在堆中创建动态数组，使用`delete [] p`销毁动态数组。

> `delete []`中的`[]`暗指`p`指向数组的第一个元素。

```c++
int *p = new int[21020];
//值初始化
int *p = new int[21020]();
// 列表初始化
int *p = new int[21020]{1, 2, 3, 4};;

delete []p;
```

动态分配一个`size==0`的数组是合法的，但是该指针无法被解引用。

## 智能指针和动态数组

智能指针来管理动态数组不太方便，无法直接引用数据。

同时，对`shared_ptr`需要提供删除器。

```c++
// unique_ptr可直接调用
unique_ptr<int []> up(new int[]);

// shared_ptr需要提供删除器
unique_ptr<int> up(new int[], [] (int *p) {delete[] p;});

```






## malloc

`malloc`申请的空间在虚拟空间是连续的，但在物理空间可能是不连续的。

> linux页大小为4KB。





### new和 malloc 的区别

> [详细内容](https://www.cnblogs.com/QG-whz/p/5140930.html)

![image-20210313161707679](D:\个人文件\重要文件\闲书与笔记\MD暂存文件\image-20210313161707679.png)

1.申请内存位置

new操作符从**自由存储区（free store）**上为对象动态分配内存空间，而malloc函数从**堆**上动态分配内存。



2.返回类型安全性

new操作符内存分配成功时，返回的是对象类型的指针，类型严格与对象匹配，无须进行类型转换，故new是符合**类型安全**性的操作符。而malloc内存分配成功则是返回void * ，需要通过强制类型转换将void*指针转换成我们需要的类型。



3.内存分配失败时的返回值

new内存分配失败时，会抛出bac_alloc异常，它**不会返回NULL**；malloc分配内存失败时返回NULL。



4.是否需要指定内存大小

使用new操作符申请内存分配时无须指定内存块的大小，编译器会根据类型信息自行计算，而malloc则需要显式地指出所需内存的尺寸。



5.是否调用构造函数/析构函数

使用new操作符来分配对象内存时会经历三个步骤：

- 第一步：调用operator new 函数（对于数组是operator new[]）分配一块足够大的，**原始**的，未命名的内存空间以便存储特定类型的对象。
- 第二步：编译器运行相应的**构造函数**以构造对象，并为其传入初值。
- 第三部：对象构造完成后，返回一个指向该对象的指针。

使用delete操作符来释放对象内存时会经历两个步骤：

- 第一步：调用对象的析构函数。
- 第二步：编译器调用operator delete(或operator delete[])函数释放内存空间。





6.对数组的处理

C++提供了new[]与delete[]来专门处理数组类型:



8.是否可以被重载

opeartor new /operator delete可以被重载。标准库是定义了operator new函数和operator delete函数的8个重载版本：




# allocator类

> p 427

C++提供了将内存分配和对象构造初始化分离开来的`allocator`，提供了更高效的选择。

类型感知的`allocator`会针对给出的类型进行位置对齐和内存大小分配。

```c++
allocator<string> allo;
auto p = allo.allocate(n); //分配内存
while(cin >> s >> t)
a.construct(p, s + t); // args构造string对象

auto q = p + n;
while(p != q) // 按构造顺序逆向销毁对象
	a.destroy(q--); // 销毁q指向的一个对象
a.deallocate(p, n); //释放内存
```

`uninitialized_copy(b, e, b2)`之类的模板库函数可以提供对`allocator`创建的内存提供拷贝初始化工作。





# 函数指针

> p221 也算简单中复杂的内容了

函数指针就是指向函数的指针，其定义方式比较复杂，我们可以用`auto`和`decltype`减少定义的编码复杂度。

```C++
// ff的函数指针
void ff(unsigned);
void (*p)(unsigned int) = &ff // `&` 是可选的
// 调用 
p(22); 
(*p)(22); //等价调用
ff(22); // 再等价
```



使用类型别名，类型推断和自动推导：

```c++
// 声明
bool compare(const string&, const string&);

//别名和decltype取一个函数类型的别名
typedef bool Func(const string&, const string&);
typedef decltype(compare) Func2;
using F = bool(const string&, const string&);

//别名和decltype取一个函数指针的别名
typedef bool (*FuncP)(const string&, const string&);
typedef decltype(compare) *FuncP2;
using Fp = bool (*)(const string&, const string&);
//使用
FuncP2 p = compare; // Func *p = compare 显式的转化p为函数指针也是可以的
sort(vec.begin(), vec.end(), p);
//形参
void bigger(string, string, Fp);
```



函数指针会根据指针**定义类型**精准的找到被重载的函数。

函数指针本身可以作为函数形参，调用时直接把函数传入即可。



返回函数是C++所不能做到的，函数最多只能返回函数指针。

```c++
// 声明一个返回 函数指针 的函数
using PF = int (*)(int *, int);
PF f1(int); 

//或者
using F = int (int *, int);
F *f1(int); //必须显式地转化函数为函数指针

// 用一用 decltype
int func(int *, int);
decltype (func) * f1(int);  // decltype返回的是函数，而是函数指针， 必须加 *


// 再或者
int (*f1(int))(int *, int); // 从内往外读，更容易懂
// ()优先级 > * 
// 1. 函数；2. 返回一个指针； 3.指针类型包含了形参列表。 

// 再或者
auto f1(int) -> int (*)(int *, int);
```

> 上面的内容，啃一遍函数指针就差不多了。



# 智能指针

> p400

C++内置指针只能通过`new`和`delete`进行指针的创建和删除，智能指针可以自动计数**元素被智能指针引用的个数**，并在指针引用为零的时候，调用析构函数，自动释放被管理的内存。

## `shared_ptr`类

智能指针都是模板类。多个智能指针`shared_ptr`可以指向同一个实例，其创建、赋值和拷贝都会产生一份新的引用。

```c++
string s = "hello";
shared_ptr<string> p1(s);
shared_ptr<string> p2(p1); //拷贝
shared_ptr<string> p3("world"); // args：创建，调用构造函数 

shared_ptr<string> p4 = make_share<string>("world"); // 最安全的方法:make_share 构造方法
```



把指针转化为智能指针(**explicit显式转化**)总是伴随着危险，因为智能指针可能因为引用为零就提前释放内存，导致指针失效，或者指针*背后*的智能指针失效。

补充一种情况，一份指针来初始化多个智能指针也是必然出现错误。

```C++

//1 指针隐式转化为智能指针是不行滴
int *p = new int(3);
shared_ptr<int> sp = p; //error!

```





```C++
//2. 错误调用智能指针，释放了内存 
int solve(int *p){
    share_ptr<int> np(p) //构造函数
}

// 另一种错误形式
int *p = new int(2);
void process(shared_ptr<int> sp);
process(p); // 错误：无法隐式转化
process(share_ptr<int>(p)); // 错误：虽然能转化，但是内存被错误释放
```

在上面的基础上，`sp.get()` 返回的指针也不能被删除，也不能用于初始化另一个智能指针。原因同上。

> `get()`返回被管理内存的内置指针，用于适配无法使用标准库的代码。



### 删除器

如果对象没有创建好析构函数，或者我们需要对删除对象有更多的操作，比如*被删除的对象不是动态对象*，传递一个**删除器**是最安全的，也是保证释放操作一定会被执行的。

> p416

```c++
void end_connection(Person *p){
    // do something important.
}
Person 
shared_ptr<Person> p(&c, end_connection);
```

### `share_ptr`的线程安全性

首先`share_ptr`对`use_count`更新操作是原子的，一定程度上保证了线程安全。但是由于拷贝对象和更新`use_count`不是原子的，这带来了隐患。比如，标准库的实现是先拷贝智能指针，再拷贝引用计数对象，拷贝引用计数对象的时候，会使use_count加一。

![img](D:\个人文件\重要文件\闲书与笔记\MD暂存文件\20180501163944631)

![img](D:\个人文件\重要文件\闲书与笔记\MD暂存文件\20180501164233241)

所以，对`share_ptr`对的赋值操作要加锁。如果你能保证不会有多个线程同时修改或替换指针指向的对象，不用加锁是完全没有问题的，或者说指针指向的对象本身已经是线程安全。





### 设计一个简单的`share_ptr`

[参照](https://cloud.tencent.com/developer/article/1688444)网址或者印象笔记保存的笔记。





### 现在为什么用shared_ptr而不用auto_ptr。

> [参考](https://www.zhihu.com/question/37351146)

去翻了一下auto_ptr的源码, 看到operator =的代码这样写的:

```cpp
223       operator=(auto_ptr& __a) throw()
224       {
225            reset(__a.release());
226            return *this;
227        }
```



多个auto_ptr不能管理同一片内存， 执行=的时候，就把原来的auto_ptr给干掉。



其实从逻辑上来讲，如果多个auto_ptr管理同一块内存肯定有问题。

第一个auto_ptr析构的时候就应该把内存释放掉了,

第二个auto_ptr再析构的时候，就要去释放已经被释放的内存了， 程序肯定挂掉。





## `unique_ptr`

单独占有对象的指针`unique_ptr`无法被拷贝和赋值，只能被移动。所以它只能使用`new`返回的指针构造。同样的，它也可以传入删除器。

> `*pi = &ix`此类指针是不如`unique_ptr`法眼的，

```c++
unique_ptr<T, D> u2;
unique_ptr<string> u(new string("hello world"));
u.release()
u.reset()
```





### `unique_ptr`和`share_ptr`区别

1. 共享对象；智能指针是否能赋值拷贝；
2. 语法格式不同；



## `weak_ptr`

不改变`shared_ptr`指针引用计数的弱智能指针`weak_ptr`，适合用作辅助`unique_ptr`。`wptr.lock()`判断指针的有效性，如果有效，则返回指向管理同一对象的`shared_ptr`，否则就指向空。



`weak_ptr`的出现就是为了避免`share_ptr`的[循环引用问题](https://blog.csdn.net/lijinqi1987/article/details/79005738)：

````c++


class Node {
  int value;
 public:
  std::shared_ptr<Node> leftPtr;
  std::shared_ptr<Node> rightPtr;
  std::shared_ptr<Node> parentPtr;
  Node(int val) : value(val) {
    std::cout << "Constructor" << std::endl;
  }
  ~Node() {
    std::cout << "Destructor" << std::endl;
  }



    
````

改进后：

```c++

class Node {
  int value;
 public:
  std::shared_ptr<Node> leftPtr;
  std::shared_ptr<Node> rightPtr;
  //只需要把shared_ptr改为weak_ptr;
  std::weak_ptr<Node> parentPtr;
  Node(int val) : value(val) {
    std::cout << "Constructor" << std::endl;
  }
  ~Node() {
    std::cout << "Destructor" << std::endl;
}
int main(){
    std::shared_ptr<Node> ptr = std::make_share<Node>(4);
    ptr->leftPtr = std::make_share<Node>(2);
    ptr->rightPtr = std::make_share<Node>(2);
    ptr->rightPtr->parentPtr = ptr; //weak_ptr initailization
    //如果weak_ptr指向的内容失效，则返回空指针，
    if(auto ptr = ptr->rightPtr->parentPtr.lock()){
        cout << ptr->value << endl;
    }
    
}
```







# 其他



## 复制

`memcpy`是从负责把内存中的数据复制到另一处，但无法处理内存重叠问题，`mmemove`就是`memcpy`的高级版，解决了内存重叠问题。

```c++
void* my_memmove(void* dst, const void* src, size_t n)
{
    char* s_dst;
    char* s_src;
    s_dst = (char*)dst;
    s_src = (char*)src;
    if(s_dst>s_src && (s_src+n>s_dst)) {      //-------------------------第二种内存覆盖的情形。
        s_dst = s_dst+n-1;
        s_src = s_src+n-1;
        while(n--) {
            *s_dst-- = *s_src--;
        }
    }else {
        while(n--) {
            *s_dst++ = *s_src++;
        }
    }
    return dst;
}
```

`strcpy`就是简单的复制字符串。