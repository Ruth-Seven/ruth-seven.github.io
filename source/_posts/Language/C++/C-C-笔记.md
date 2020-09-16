---
title: C/C++笔记
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
categories:
  - Language
  - C++
date: 2020-08-07 13:04:58
tags:
---

## 基础

**变量范围**

<!-- more -->

[![image-20200507125512740](http://static.come2rss.xyz/image-20200507125512740.png)](http://static.come2rss.xyz/image-20200507125512740.png)

[image-20200507125512740](http://static.come2rss.xyz/image-20200507125512740.png)





**宏定义**替换

```
//定义常量
#define 标识量 常量
//定义语句
#define ADD(a,b) ((a) + (b))

const double eps = 1e-8;
#define Equ(a,b) ((fabs((a) - (b))) < (eps)) //fabs 对double取绝对值 , included math.h
```

**类型别名**

```
//如
typedef long long LL
```

**常量**

```
const 数据类型 变量名 = 常量
```

**位运算**

```
<< //左移
>> //右移
&  //位与
|  //位或
^  //位异或
~  //位取反 如~a
```

**动态申请**

```
//C malloc
//一个int
int *p = (int*)malloc(sizeof(int));
//一维int
int *p = (int*)malloc(1000 * sizeof(int));

//C free 释放内存变量
free(p);

//c++ new
//一个
int *p = new int;
//一维
int *p = new int[10000];

//C++ delete 
delete(p);
```

## 输入输出(C)

对double的输入格式为`%lf`,输出格式为`%f`。

`%d`、`%s`等输入格式都会自动把空格、换行当成结束判断标志的，同时不把空格当做输入量，而`%c`会“吸收”掉空格。

```
scanf("%d%c%s", &b, &c, a);
printf("b=%d,c=%c,s=%s, \n", b, c, a);
//I：123 A hello
//O:b=123,c= ,s=A,
```

**输出格式**

| %md  | 空格补齐不足m位数字的高位 |
| :--- | :------------------------ |
| %0md | 0补齐不足m位数字的高位    |
| %.mf | 保留m位数字的浮点数       |

**字符串**

只有`gets`和`%s`会自动添加`\0`（空字符NULL，ASCII码为0），同样的`puts`和`%s`通过识别`\0`来输出字符串。所以需要在非上述两个字符串输入函数得到的字符串后面加上`\0`。

**其他常用函数**

`getchar`、`putchar`输入输出单个字符。

`gets`（好像不太安全，不推荐使用），`puts`输出字符串 + 换行符。

`sscanf(str, "%d", &n)`将数据从字符串str中输入 。`sprintf(str, "%d", n)`将数据从字符串str中输出 。

**多组输入**

```
while( scanf("%d", &n) != EOF){
    if( condition == True) break;
}
while( T--)
```

## 输入输出（C++）

```
cin>>b>>d
`cout<<b<<d
```

> 控制double精度可用`#include<iomanip>`，
>
> ```
> cout << setiosflags(ios::fixed) << setprecision(2) << 123.45456 << endl;
> ```

`cin.getline(str, 100)` 读入整行字符串到`str[100]`中。

**总结一下**

| 输入一行     | Char a[]                                              | String a         |
| :----------- | :---------------------------------------------------- | :--------------- |
|              | `cin.getline(a,10000）` 10000表输入限制1000个字符以内 | `getline(cin,a)` |
| 输入一个字符 | Char a                                                |                  |
|              | `cin.get(a,10000)`                                    |                  |
|              | `getchar()`                                           |                  |

## Array

**定义**

```
// 静态定义
//  	一维
int a[10] = {1, 2, 3 ,4 }// 数字不足用零补充
char str[20] = { 'a', 'b', 'c'};
char str[20] = 'abc';

//		二维
int a[5][6] = {{1, 3, 4, 5, 6}, {5, 6}, {}, {2, 3, 5 }};
/*
C++函数（包括主函数）定义的变量都是定义在系统栈中，容易溢出。定义为全局变量可以放到静态存储区中。
*/

//new 二维
int** a = new int*[rowCount];
for(int i = 0; i < rowCount; ++i)
    a[i] = new int[colCount];
    
//delete 二维
for(int i = 0; i < rowCount; ++i) {
    delete [] ary[i];
}
delete [] ary;
```

**初始化**

```
// 按字节赋值， value最好只使用0，或者-1（0xFFFFFFFF）
memset( Array, value, sizeof(Array));
//fill
vector<int> arr;
fill(arr.begin(), arr.end(), value) // C++风格的fill
```

**传参**

```
//传址引用
// 一维
int f(int a[]) {} //一维无需数组大小
// 二维
int f(int a[][5]) {} //二维需要第二纬度大小
```

## 字符数组（C风格）

**常用函数**

```
strlen(s)
```

`strcmp(s1,s2)` 按字典序比较，两个字符串相等返回0，前者大于后者返回正整数，否则返回负整数。

`strcpy(s1, s2)` 把s2复制给s1

`strcat(s1, s2)`把s2拼接到s1后面

## 指针

基础

```
//定义和初始化
int *p1, *p2; // 注意变量名是p1, p2,而非*p1,*p2; int作为int*的基类型，p1无法指向int以外的类型元素
int a, *p3 = &a;
//引用
int c = *p1;

// 运算
p1++ // p1自增，自动指向下一个int元素
p1 + i // p1指向下面i个元素

p3 - p1 // 得到的是p3和p1之间的int为单位的距离，但是p3和p1的本身的值是以Byte为计量的
    
  
//数组
int a[5] = {};
a + i //a表示指向a数组首地址
&a[2] // 表示指向数组a的第3个元素的地址
```

C指针的一个优美的写法，常常在函数中面对不从零开始的数组需要加上一个增量数字，但是可以通过`&A[add + i]`来获取`A[add+i]`的地址并传参，就好像传进去了一个从新开始的数组。

```
merge(&A[l], i, i + step - 1, i + step, min(i + 2 * step - 1, n - 1));
```

## 引用（C++）

引用变量相当于给变量增加了一个别名，对引用变量的操作就是对原变量的操作。

> **注意常量无法使用引用**

```
int f(int &c)//引用
int f(int* &c)//指针引用
```

## 结构体

```
//定义
struct Name{
	int a, b, c;
	Name(){} //构造函数1
	Name(int _a, int _b, int _c):a(_a), b(_b), c(_c) {} //构造函数1
}instance1, instanceN[N], *p; //声明变量instance和instance数组以及 Name类型的指针。

//访问
instance.a // 实例
(*p).a //指针
p->a // 指针
```

## sort排序

`sort`包括在`algorithm.h`包中

```
//法1
struct Stu{
	int score, no;

};
//先按score升序排序，再按no升序排序。
bool cmp(Stu a, Stu b){
	if(a.score == b.score) return a.no < b.no;
	return a.screo < b.score;
}
```

## 运算符优先级

| 优先级                | 运算符                                                       | 描述                                                         | 结合性                                                       |
| --------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1                     | `::`                                                         | [作用域解析](https://zh.cppreference.com/w/cpp/language/identifiers#.E6.9C.89.E9.99.90.E5.AE.9A.E7.9A.84.E6.A0.87.E8.AF.86.E7.AC.A6) | 从左到右                                                     |
| 2                     | `a++` `a--`                                                  | 后缀[自增与自减](https://zh.cppreference.com/w/cpp/language/operator_incdec) |                                                              |
| `*type*()` `*type*{}` | [函数风格转型](https://zh.cppreference.com/w/cpp/language/explicit_cast) |                                                              |                                                              |
| `a()`                 | [函数调用](https://zh.cppreference.com/w/cpp/language/operator_other#.E5.86.85.E5.BB.BA.E7.9A.84.E5.87.BD.E6.95.B0.E8.B0.83.E7.94.A8.E8.BF.90.E7.AE.97.E7.AC.A6) |                                                              |                                                              |
| `a[]`                 | [下标](https://zh.cppreference.com/w/cpp/language/operator_member_access#.E5.86.85.E5.BB.BA.E7.9A.84.E4.B8.8B.E6.A0.87.E8.BF.90.E7.AE.97.E7.AC.A6) |                                                              |                                                              |
| `.` `->`              | [成员访问](https://zh.cppreference.com/w/cpp/language/operator_member_access#.E5.86.85.E5.BB.BA.E7.9A.84.E6.88.90.E5.91.98.E8.AE.BF.E9.97.AE.E8.BF.90.E7.AE.97.E7.AC.A6) |                                                              |                                                              |
| 3                     | `++a` `--a`                                                  | 前缀[自增与自减](https://zh.cppreference.com/w/cpp/language/operator_incdec) | 从右到左                                                     |
| `+a` `-a`             | 一元[加与减](https://zh.cppreference.com/w/cpp/language/operator_arithmetic#.E4.B8.80.E5.85.83.E7.AE.97.E6.9C.AF.E8.BF.90.E7.AE.97.E7.AC.A6) |                                                              |                                                              |
| `!` `~`               | [逻辑非](https://zh.cppreference.com/w/cpp/language/operator_logical)和[逐位非](https://zh.cppreference.com/w/cpp/language/operator_arithmetic#.E6.8C.89.E4.BD.8D.E9.80.BB.E8.BE.91.E8.BF.90.E7.AE.97.E7.AC.A6) |                                                              |                                                              |
| `(*type*)`            | [C 风格转型](https://zh.cppreference.com/w/cpp/language/explicit_cast) |                                                              |                                                              |
| `*a`                  | [间接](https://zh.cppreference.com/w/cpp/language/operator_member_access#.E5.86.85.E5.BB.BA.E7.9A.84.E9.97.B4.E6.8E.A5.E8.BF.90.E7.AE.97.E7.AC.A6)（解引用） |                                                              |                                                              |
| `&a`                  | [取址](https://zh.cppreference.com/w/cpp/language/operator_member_access#.E5.86.85.E5.BB.BA.E7.9A.84.E5.8F.96.E5.9C.B0.E5.9D.80.E8.BF.90.E7.AE.97.E7.AC.A6) |                                                              |                                                              |
| `sizeof`              | [取大小](https://zh.cppreference.com/w/cpp/language/sizeof)[[注 1\]](https://zh.cppreference.com/w/cpp/language/operator_precedence#cite_note-1) |                                                              |                                                              |
| `co_await`            | await 表达式 (C++20)                                         |                                                              |                                                              |
| `new` `new[]`         | [动态内存分配](https://zh.cppreference.com/w/cpp/language/new) |                                                              |                                                              |
| `delete` `delete[]`   | [动态内存分配](https://zh.cppreference.com/w/cpp/language/delete) |                                                              |                                                              |
| 4                     | `.*` `->*`                                                   | [成员指针](https://zh.cppreference.com/w/cpp/language/operator_member_access#.E5.86.85.E5.BB.BA.E7.9A.84.E6.88.90.E5.91.98.E6.8C.87.E9.92.88.E8.AE.BF.E9.97.AE.E8.BF.90.E7.AE.97.E7.AC.A6) | 从左到右                                                     |
| 5                     | `a*b` `a/b` `a%b`                                            | [乘法、除法与余数](https://zh.cppreference.com/w/cpp/language/operator_arithmetic#.E4.B9.98.E6.B3.95.E6.80.A7.E8.BF.90.E7.AE.97.E7.AC.A6) |                                                              |
| 6                     | `a+b` `a-b`                                                  | [加法与减法](https://zh.cppreference.com/w/cpp/language/operator_arithmetic#.E5.8A.A0.E6.B3.95.E6.80.A7.E8.BF.90.E7.AE.97.E7.AC.A6) |                                                              |
| 7                     | `<<` `>>`                                                    | 逐位[左移与右移](https://zh.cppreference.com/w/cpp/language/operator_arithmetic#.E7.A7.BB.E4.BD.8D.E8.BF.90.E7.AE.97.E7.AC.A6) |                                                              |
| 8                     | `<=>`                                                        | [三路比较运算符](https://zh.cppreference.com/w/cpp/language/operator_comparison#.E4.B8.89.E8.B7.AF.E6.AF.94.E8.BE.83)(C++20 起) |                                                              |
| 9                     | `<` `<=`                                                     | 分别为 < 与 ≤ 的[关系运算符](https://zh.cppreference.com/w/cpp/language/operator_comparison) |                                                              |
| `>` `>=`              | 分别为 > 与 ≥ 的[关系运算符](https://zh.cppreference.com/w/cpp/language/operator_comparison) |                                                              |                                                              |
| 10                    | `==` `!=`                                                    | 分别为 = 与 ≠ 的[关系运算符](https://zh.cppreference.com/w/cpp/language/operator_comparison) |                                                              |
| 11                    | `a&b`                                                        | [逐位与](https://zh.cppreference.com/w/cpp/language/operator_arithmetic#.E6.8C.89.E4.BD.8D.E9.80.BB.E8.BE.91.E8.BF.90.E7.AE.97.E7.AC.A6) |                                                              |
| 12                    | `^`                                                          | [逐位异或](https://zh.cppreference.com/w/cpp/language/operator_arithmetic#.E6.8C.89.E4.BD.8D.E9.80.BB.E8.BE.91.E8.BF.90.E7.AE.97.E7.AC.A6)（互斥或） |                                                              |
| 13                    | `                                                            | `                                                            | [逐位或](https://zh.cppreference.com/w/cpp/language/operator_arithmetic#.E6.8C.89.E4.BD.8D.E9.80.BB.E8.BE.91.E8.BF.90.E7.AE.97.E7.AC.A6)（可兼或） |
| 14                    | `&&`                                                         | [逻辑与](https://zh.cppreference.com/w/cpp/language/operator_logical) |                                                              |
| 15                    | `                                                            |                                                              | `                                                            |
| 16                    | `a?b:c`                                                      | [三元条件](https://zh.cppreference.com/w/cpp/language/operator_other#.E6.9D.A1.E4.BB.B6.E8.BF.90.E7.AE.97.E7.AC.A6)[[注 2\]](https://zh.cppreference.com/w/cpp/language/operator_precedence#cite_note-2) | 从右到左                                                     |
| `throw`               | [throw 运算符](https://zh.cppreference.com/w/cpp/language/throw) |                                                              |                                                              |
| `co_yield`            | yield 表达式 (C++20)                                         |                                                              |                                                              |
| `=`                   | [直接赋值](https://zh.cppreference.com/w/cpp/language/operator_assignment#.E5.86.85.E5.BB.BA.E7.9A.84.E7.9B.B4.E6.8E.A5.E8.B5.8B.E5.80.BC)（C++ 类默认提供） |                                                              |                                                              |
| `+=` `-=`             | 以和及差[复合赋值](https://zh.cppreference.com/w/cpp/language/operator_assignment#.E5.86.85.E5.BB.BA.E7.9A.84.E5.A4.8D.E5.90.88.E8.B5.8B.E5.80.BC) |                                                              |                                                              |
| `*=` `/=` `%=`        | 以积、商及余数[复合赋值](https://zh.cppreference.com/w/cpp/language/operator_assignment#.E5.86.85.E5.BB.BA.E7.9A.84.E5.A4.8D.E5.90.88.E8.B5.8B.E5.80.BC) |                                                              |                                                              |
| `<<=` `>>=`           | 以逐位左移及右移[复合赋值](https://zh.cppreference.com/w/cpp/language/operator_assignment#.E5.86.85.E5.BB.BA.E7.9A.84.E5.A4.8D.E5.90.88.E8.B5.8B.E5.80.BC) |                                                              |                                                              |
| `&=` `^=` `           | =`                                                           | 以逐位与、异或及或[复合赋值](https://zh.cppreference.com/w/cpp/language/operator_assignment#.E5.86.85.E5.BB.BA.E7.9A.84.E5.A4.8D.E5.90.88.E8.B5.8B.E5.80.BC) |                                                              |
| 17                    | `,`                                                          | [逗号](https://zh.cppreference.com/w/cpp/language/operator_other#.E5.86.85.E5.BB.BA.E7.9A.84.E9.80.97.E5.8F.B7.E8.BF.90.E7.AE.97.E7.AC.A6) | 从左到右                                                     |

> 注意`&`的优先级比`==`小。



## builtin Funciotn



### Function __builtin_clz

This builtin method is provided by GCC to count the number of **leading** zero’s in variable.

The Syntax:

```
int __builtin_clz (unsigned int x)
```

It takes the input parameter as a number for which the the count of leading zero’s is to be determined. It returns the count of leading zero’s as expected.

Taking for example, lets take a number 16. An **int** takes 4 bytes in gcc. Its binary representation is

Code:

```
00000000 00000000 00000000 00010000
```

Counting the number of leading zero’s is 27 which should be our result for this case..



### Function __builtin_ctz




This builtin method by GCC determines the count of trailing zero in the binary representation of a number.

The Syntax:

```
int __builtin_ctz (unsigned int x)
```

The input parameter is the number for which the the count of trailing zero’s is to be determined. It returns the count of trailing zero’s as expected.

Taking for example, lets take the same number 16. Again, an int takes 4 bytes in gcc. Its binary representation is

Code:

```
00000000 00000000 00000000 00010000
```

Counting the number of trailing zero’s is 4 which should be our result for this case..



### Function __builtin_popcount

This builtin method by GCC determines the number of **one’s** in the binary representation of a number.

The Syntax:

Code:

```
int __builtin_popcount (unsigned int x)
```

The input parameter is the number for which the the number of 1’s is to be determined. It returns the count of set bits as expected..

Taking for example, lets take the same number 16. Again, an int takes 4 bytes in gcc. Its binary representation is

Code:

```
00000000 00000000 00000000 00010000
```

Counting the number of one’s is just 1, which should be our result for this case..