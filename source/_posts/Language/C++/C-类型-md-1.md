---
title: C++类型
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
date: 2021-03-14 16:01:40
tags:
categories:
---

<!-- more -->



# C++类型










# const 常量修饰符





### `const`与引用

对常量的引用。

```c++
const int a = 10;
const int &r1 = a; // 并非赋值，执行的是绑定动作
```

初始化：引用本身的类型必须与所引用的类型一致，或者能够转化过来，比如引用变量，引用表达式，引用常量。

```c++
int i = 42
const int &r1 = i * 2; // ✔
int &r2 = i * 2 // 非常量引用无法引用常量（年轻人无法改变老头子）

```



### `const`和指针

指向常量的指针的功能和初始化，类似于指向常量的引用。

```c++
const int i = 10;
const int *p = &i; //✔
int *q = &i //✖ 类似对常量的引用
    
*p = 20 //✖ 无法改变常量
    
int c = 1;
const int *k = &c; //✔
```

对常量的引用和对常量的指针的**统一深层含义**都是不能改变指向的变量的值。



`const`指针，指针作为对象是可以为常量的，这是不同于引用的一点。也带来了新的复杂性。它意味着指针本身无法被修改，而指向的值的特性无关。

> **常量指针**：表示const修饰的为所申明的类型。
>
> **指针常量**：表示const修饰的指针。

```c++
int c = 0
int *const p = &c;

const double PI = 3.14414;
const double *q = &PI;
```



### 顶层和底层`const`

描述对象本身是常量的`const`称为顶层`cosnt`，复杂数据结构有的描述其指向的对象是静态，称为底层`const`。

重要的是，在**赋值和绑定**的过程中，两个值如果底层`const`不一样就有麻烦。

一般来说，要么两个值`const`一致，要么把变量转化为常量。

在

```c++
int c  = 9;
const int *p1 = &c;
const int *const p2 = p1;
int *const p3 = p2; //// p指针是顶层const；const int 用同样有底层const的值赋值，成立！
const int &r = c; // 底层const int 绑定到int上，成立！ 

int *p = p1; //✖ 底层const不一样
p2 = p3
```



### `const`与函数

const 修饰**类成员函数**，其目的是防止成员函数修改被调用对象的值，如果我们不想修改一个调用对象的值，所有的成员函数都应当声明为 const 成员函数。`int get_cm()const;`。





## ` constexpr`

在定义常量时，为了在定义就验证变量是否是一个常量表达式，`constexpr`提供了如此一条道路。

字面值类型`literal type`，简单，值也显而易见。比如指针，算数类型和引用。

> `constexpr`指针只能指向非函数体内部的变量（栈外）。



`constexpr`函数是指形参和返回值都是`cosntexpr`的函数，而且除了无动作的语句，只能有一句返回值。

另外， 常量表达是指用常量表达式计算得来的表达式，也就是说`constexper`量和函数都可以是常量表达式的一部分。





# `static`



> [C++ static 关键字详解](https://www.cnblogs.com/youxin/archive/2012/05/17/2506757.html)
>
> [代码中使用const定义的变量，存放在下面哪个段中？（）](https://www.nowcoder.com/questionTerminal/d1622983cfdb47e98908f648f65576df)
>
> [read more](https://www.cnblogs.com/yanqi0124/p/3795547.html) 

其实我们通常声明的不用static修饰的变量，都是auto的，因为它是默认的，就象short和long总是默认为int一样；我们通常声明一个变量：

```C++
int a;
// int 就是 auto int
auto string s;
```

`auto`的含义是由程序自动控制变量的生存周期，通常指的就是变量在进入其作用域的时候被分配，离开其作用域的时候被释放；而`static`就是不`auto`，变量在程序初始化时被分配，直到程序退出前才被释放；也就是`static`是按照程序的生命周期来分配释放变量的，而不是变量自己的生命周期；所以，像这样的例子：



#### 类静态成员

静态数据成员存储在**全局数据区**。静态数据成员定义时要分配空间，所以不能在类声明中定义（放在`.cpp`里面）。

> 因为`static`是声明性关键字(同`friend`，声明时只需在友元的名称前加上关键字`friend`， 也同`extern`）

属于类的“全局变量”，所有实例共用。



```c++
// A.h
class A{
    static int s_value;
    const static int k_value = 1; // const staic 可以在类内声明
}
// A.cpp
A::s_value = 1; //没有 static

```



#### 类的静态函数



类的静态函数是类的范畴的全局函数，只能访问类的静态成员。实际上，它就是增加了类的访问权限的全局函数：

静态成员函数可以继承和覆盖,但无法是虚函数。

```c++
class A{
    static void func(int value); 
}
```



#### 在cpp内有效的静态**全局**变量

在该cpp内有效，但是其他的cpp文件不能访问这个变量；如果有两个cpp文件声明了同名的**全局**静态变量，那么他们实际上是独立的两个变量；

```c++
static int g_value = 0;
```



如果不使用`static`声明全局变量，该变量可能有被多个文件共用的风险，但是如果想要被多个cpp共享，应该声明为`extern`。所以为了明确用法，全局变量要么`extern`的，要么是`static`的。

在头文件中声明`static`变量也是不建议的，因为会生成一组同名不同域的变量。如果需要声明cpp共享的变量：

```c++
//A.h
extern int g_value; //不要初始化，不要定义
//A.cpp
int g_value =  1;
```





#### 在cpp内有效的静态全局函数

这个函数只可在本cpp内使用，函数的实现不需要static修饰，不会同其他cpp中的同名函数引起冲突。

```c++
static void func();
```



和第三点相同的是：

- 不要在头文件中声明static的全局函数
- 不要在cpp内声明非static的全局函数
- 如果你要在多个cpp中复用该函数，就把它的声明提到头文件里去，否则在cpp内部声明需要加上static修饰；在C语言中这点由为重要！



#### 初始化静态变量

static变量只有一次初始化，不管在类中还是在函数中..有这样一个函数：

```c++
void foo(){
    static int s = 0;
    s++;
}
```

只有第一次调用，`s`初始化为零。

 在类中使用非const的static类成员变量。初始化时要使用`typename classname::variablename = value`的形式

```c++
class A{
    static int a;
    cosnt staic int b = 1; //静态常量可以在类中初始化 
	cosnt staic int c; 
}
int A::a = 1; // here initialize
const int c = 20;//静态常量可以在类外初始化 
```

如果是模板中使用非const的static的变量..那需要根据具体类型初始化。

例如 `int myClass<int>::a = 4`;



#### 静态带来了什么

全局变量都是静态存储方式，静态全局变量限制了该变量只能在该源文件中使用。

而局部变量加上`static`只不过改变了她的生存期。

> 把全局变量改为静态变量不过改变了他的作用域

同理的，静态函数在内存中只有一份，而普通函数在每次调用都维持一份拷贝。



#### 静态变量在哪

一个由c/C++编译的程序占用的内存分为以下几个部分

栈区（stack）——由编译器自动分配释放，存放函数的参数值，局部变量的值等。其操作方式类似于数据结构中的栈。

堆区（heap）——一般由程序员分配释放， 若程序员不释放，程序结束时可能由OS回收 。注意它与数据结构中的堆是两回事，分配方式倒是类似于链表。

全局区——（静态区 static segment）：全局变量和静态变量的存储是放在一块的，初始化的全局变量和静态变量在一块区域(.data)，未初始化的全局变量和未初始化的静态变量在相邻的另一块区域(.bss)。 - 程序结束后由系统释放。

COMMON——用于存放未初始化的全局变量，因为在编译过程中，未初始化的全局变量可能在其他文件中已经定义，属于弱全局变量。如果找到一个强符号和一个弱符号，编译器会直接把该变量分给`bss`。静态符号也类似，直接分给`data`或者`bss`。

常量区——只读数据存放区，比如`const`修饰的变量。常量字符串就是放在这里的(.rodata)。 程序结束后由系统释放。

程序代码区——存放函数体的二进制代码(.text)。

```c++
//main.cpp
int a = 0;          // 全局初始化区
char *p1;           // 全局未初始化区
main()
{
  int b;            // 栈区
  char s[] = "abc"; // 栈区
  char *p2;         // 栈区
  char *p3 = "123456";     // "123456\0" 在常量区，p3在栈区
  static int c =0;         // 全局（静态）初始化区
 
  p1 = (char *)malloc(10);
  p2 = (char *)malloc(20); // 分配得来的10和20字节的区域就在堆区
 
  strcpy(p1, "123456");    // "123456\0" 放在常量区，编译器可能会将它
                              // 与p3所指向的"123456"优化成一个地方。
} 
```





#### 其他

[静态构造函数在C++不成立](https://www.huaweicloud.com/articles/c3dfc11b1b3e1b2bfdcab4730305bd24.html)





# extern

`extern` 是 `C/C++` 语言中表明函数和全局变量作用范围（可见性）在其他模块可见的**声明性**关键字。



##  extern "C" 

> [extern "C"详解](https://zhuanlan.zhihu.com/p/123269132)

被 extern "C" 修饰的变量和函数是按照 `C` 语言方式编译和连接的。

```c++
#ifdef __cplusplus
extern "C" {
#endif
//和
#ifdef __cplusplus
}
#endif
```

###  `C++`和`C` 的函数是怎样编译的。

作为一种面向对象的语言， `C++` 支持函数重载，而过程式语言 `C` 则不支持。所以，函数被 `C++` 编译后在符号库中的名字与 `C` 语言的有所不同。例如，假设某个函数的原型为：

```text
void foo( int x, int y );
```

该函数被 `C` 编译器编译后在符号库中的名字为 `_foo` ，而 `C++` 编译器则会产生像 `_foo_int_int` 之类的名字（不同的编译器可能生成的名字不同，但是都采用了相同的机制，生成的新名字称为 `mangled name` ）。 `_foo_int_int` 这样的名字包含了函数名、函数参数数量及类型信息， `C++` 就是靠这种机制来实现函数重载的。 

同样地， `C++` 中的变量除支持局部变量外，还支持类成员变量和全局变量。用户所编写程序的类成员变量可能与全局变量同名，我们以 `.` 来区分。而本质上，编译器在进行编译时，与函数的处理相似，也为类中的变量取了一个独一无二的名字，这个名字与用户程序中同名的全局变量名字不同。

###  extern "C" 的作用

`extern "C"`的目的就是为了在`C++ `里实现与 `C` 及其它语言的混合编程。`extern "C"`修饰的变量和函数将`C`的方式进行编译，可以提供其他`C`程序连接。



# inline

`inline`修饰的函数即为内联函数，**内联函数**就是**编译时期展开函数**。

​	

节省了每次调用函数带来的额外时间开支。尽量用`inline`、`const`、`enum`替换 `define`。尽量用编译器替换预处理。



> `#define`宏预处理阶段进行粗暴替换，不进行语法检查，而`inline`函数是在编译器阶段进行的替换，接受语法，语义的检查。相对更安全。`#define` 的错误一般很难最查到。





类中除了虚函数的所有成员函数，都默认是内联的，但内联只是一个请求，是否内联决定于编译器的选择。

⚡无论何时，使用基类指针或引用来调用虚函数，它都不能为内联函数(因为调用发生在运行时)。但是，无论何时，使用类的对象(不是指针或引用)来调用时，可以当做是内联，因为编译器在编译时确切知道对象是哪个类的。

```c++
class Base
{
    inline virtual void who() {..........}
}
class Derived : public Base
{
    inline void who() {............}
}


// 此处的虚函数who()，是通过类的具体对象来调用的，编译期间就能确定了，所以它可以是内联的。
    Base b;
    b.who();
 
    // 此处的虚函数是通过指针调用的，需要在运行时期间才能确定，所以不能为内联。
    Base *ptr = new Derived();
    ptr->who();
```





# auto



`C++11`引入的类型推导符，可以极大的缩短类型说明，解放程序员。

由于`auto`会自动去掉类型的引用，可能带来性能开销。

另外，`c++14`能在函数定义的返回值里使用`auto`。



## auto和 decltype的区别

### 语法格式

`auto`需要被赋初始值的变量来推断类型，更简洁。

`decltypen`根据`exp`表达式推导出变量的类型的，更灵活。

### 对`const`和`volatile`关键字的统称



「cv 限定符」是 const 和 volatile 关键字的统称：

- const 关键字用来表示数据是只读的，也就是不能被修改；
- volatile 和 const 是相反的，它用来表示数据是可变的、易变的，目的是不让 CPU 将数据缓存到寄存器，而是从原始的内存中读取。

`auto`关键字对表达式是指针或者引用的类型，会保留`cv`限定符。



```c++
//非指针非引用类型
const int n1 = 0;
auto n2 = 10;
n2 = 99;  //赋值不报错
decltype(n1) n3 = 20;
n3 = 5;  //赋值报错
//指针类型
const int *p1 = &n1;
auto p2 = p1;
*p2 = 66;  //赋值报错
decltype(p1) p3 = p1;
*p3 = 19;  //赋值报错

```

### 对引用的处理



decltype 会保留引用类型，而 auto 会抛弃引用类型，直接推导出它的原始类型。

```c++
#include <iostream>
using namespace std;

int main() {
    int n = 10;
    int &r1 = n;

    //auto推导
    auto r2 = r1;
    r2 = 20;
    cout << n << ", " << r1 << ", " << r2 << endl;

    //decltype推导
    decltype(r1) r3 = n;
    r3 = 99;
    cout << n << ", " << r1 << ", " << r3 << endl;

    return 0;
}
//运行结果：10, 10, 20 ;99, 99, 99
```

## 总结

auto 虽然在书写格式上比 decltype 简单，但是它的推导规则复杂，有时候会改变表达式的原始类型；而 decltype 比较纯粹，它一般会坚持保留原始表达式的任何类型，让推导的结果更加原汁原味。

从代码是否健壮的角度考虑，我推荐使用 decltype，它没有那么多是非；但是 decltype 总是显得比较麻烦，尤其是当表达式比较复杂时。





# sizeof

sizeof是一个操作符（operator），作用是返回一个对象或类型所占的内存字节数。

sizeof的东西会被编译器直接替换掉



# cast

## **static_cast**

格式：

```cpp
static_cast<type>(expression)
```

任何明确的类型转换都可以使用static_cast（static_cast不能转换掉底层const，volatile和__unaligned属性）。由于在编译器期间就进行了类型转化，不提供运行时的检查，所以叫static_cast，因此，需要在编写程序时确认转换的安全性。

主要在以下几种场合中使用：

1. 用于类层次结构中，父类和子类之间指针和引用的转换；进行上行转换，把子类对象的指针/引用转换为父类指针/引用，这种转换是安全的；进行下行转换，把父类对象的指针/引用转换成子类指针/引用，这种转换是不安全的，需要编写程序时来确认；
2. 用于基本数据类型之间的转换，例如把int转char，int转enum等，需要编写程序时来确认安全性；
3. 把void指针转换成目标类型的指针（这是极其不安全的）；



## **dynamic_cast**

格式：

```cpp
dynamic_cast<type>(expression)
```

相比static_cast，dynamic_cast会在**运行时**检查类型转换是否合法，具有一定的安全性。由于运行时的检查，所以会额外消耗一些性能。dynamic_cast使用场景与static相似，在类层次结构中使用时，上行转换和static_cast没有区别，都是安全的；下行转换时，dynamic_cast会检查转换的类型，相比static_cast更安全。

**dynamic_cast转换仅适用于指针或引用。**

在转换可能发生的前提下，dynamic_cast会尝试转换，若指针转换失败，则返回空指针，若引用转换失败，则抛出异常。

1.继承中的转换

(1)上行转换：

在继承关系中 ，dynamic_cast由子类向父类的转换与static_cast和隐式转换一样，都是非常安全的。

(2)下行转换

```cpp
class A { virtual void f(){}; };
class B : public A{ };
void main()
{
     A* pA = new B;
     B* pB = dynamic_cast<B*>(pA); 
}
```

注意类A和类B中定义了一个虚函数，这是不可缺少的。因为类中存在虚函数，说明它可能有子类，这样才有类型转换的情况发生，由于运行时类型检查需要运行时类型信息，而这个信息存储在类的虚函数表中，**只有定义了虚函数的类才有虚函数表**。

2.void*的转换

一些情况下，我们需要将指针转换为void*，然后再合适的时候重新将void*转换为目标类型指针。

```cpp
class A { virtual void f(){} };
int main()
{
     A *pA = new A;
     void *pV = dynamic_cast<void *>(pA); 
}
```

3.菱形继承中的上行转换

首先，定义一组菱形继承的类：

```cpp
class A { virtual void f() {}; };
class B :public A { void f() {}; };
class C :public A { void f() {}; };
class D :public B, public C { void f() {}; };
```

继承关系如图：

![img](http://static.come2rss.xyz/v2-485ce8e9bbcc314e48b691f425d935e8_720w.jpg)

多重继承的上行转化必须明确指定继承路径。

```cpp
class A { virtual void f() {}; };
class B :public A { void f() {}; };
class C :public A { void f() {}; };
class D :public B, public C { void f() {}; };

void main()
{
    D *pD = new D;
    B *pB = dynamic_cast<B *>(pD);
    A *pA = dynamic_cast<A *>(pB);
}
```



> 除了`dynamic_cast<>`是运行时处理的，运行时要进行类型检查，其他三种都是编译时完成的。



## **const_cast**

格式：

```cpp
const_cast<type>(expression)
```

const_cast用于移除类型的const、volatile和__unaligned属性。

常量指针被转换成非常量指针，并且仍然指向原来的对象；常量引用被转换成非常量引用，并且仍然引用原来的对象。

```cpp
const char *pc;
char *p = const_cast<char*>(pc);
```

## **reinterpret_cast**

格式：

```cpp
reinterpret_cast<type>(expression)
```

非常激进的指针类型转换，在编译期完成，可以转换任何类型的指针，所以极不安全。非极端情况不要使用。

```cpp
int *ip;
char *pc = reinterpret_cast<char*>(ip);
```

一个实际用途是在哈希函数中，即，通过让两个不同的值几乎不以相同的索引结尾的方式将值映射到索引





# 左值和右值

> p470

左值表示对象的身份，可以赋值，可以获取值。右值是表示对象的值。

**左值引用**只能绑定到变量，而**右值引用**只能绑定到即将销毁的对象上，比如表达式，字面常量，或者返回右值的表达式。两者完全相反。

> `const`的左值引用可以绑定到右值引用绑定的东西上。`const int  = getInt(); `



> ⭕绑定到右值引用的变量是左值！
>
> ```c++
> int &&t = "hello";
> int &&rlvaue = t; //error
> ```

右值引用要求我们被绑定的东西要么被销毁，要么被赋值。它可以自由的使用被引用对象的资源。

显然的，对象是左值。

> `int && a = 2 * 32` 中 `a`就是变量。

 `std::move(a)`可以返回变量的右值引用。结合上文， `a`之后的值无法被使用。



## 右值引用和成员函数

形参的右值和左值可以作为函数重载的的区分。首先函数匹配会根据传入参数是左值还是右值调用对应版本的函数。

```c++
string s = "hello world"
vec.push_back(s); // 左值
vec.push_back("jjklsdf"); // 右值
vec.push_back(string("jjklsdf")); // 右值

```

C++是不会对右值被赋值这种行动作出限制的（`str1 + str2 = "hello"`）。

引用限定符允许设置成员函数中`this`指针是属于右值还是左值。调用对象也会根据**引用限定符的版本来选择重载版本**。

```c++
Class Foo{
    public:
    	Foo &operator=(const Foo &f) const &  { //this 为左值  且 const 必须在 & 前面
            //省略赋值步骤
            return *this;
        }
		Foo sorted() &;		//👈左值foo 调用
    	Foo sorted() &&; 	//右值foo 调用
}


```

而**同名**成员函数的要么全不写引用限定符，要么全写。