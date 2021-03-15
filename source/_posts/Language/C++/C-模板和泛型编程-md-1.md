---
title: C++模板和泛型编程
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
date: 2021-03-14 16:01:39
tags:
categories:
---

<!-- more -->



[toc]
# C++模板和泛型编程

C++模板是泛型编程的基础，为类型编程提供了新选择。模板运作的过程分为：模板编译、模板调用、模板实例化，最后一个过程才能发型类型相关的错误。

# 函数模板和类模板

## 函数模板

函数模板是针对任一版本产生特定的函数版本。`typename`关键词定义了类型模板参数`T`。非类型模板参数是模板中的值，而非类型，可由编译器有表达式中推断出来。非类参考参数可以绑定到一个值，或者是具有**静态生命周期的**指针和引用。

> p400 静态内存

> `T`的功能：指定类型，类型转换以及变量声明

```c++
template<typename T, unsigned N, unsigned M > // typename 等价于 class
inline int  compare(const T (&a)[N], const T (&b)[M]{
	compare(a, b);
    return 0;
}
```

### 模板实参推断

函数模板从调用实参中推断出模板形参的类型。

推断的过程就必然涉及到“不怎么完全匹配的”类型转化：

1. 顶层`const`无视
2. 非`const`可以转化为`const`
3. 若形参非引用，则数组和函数可以被自动转化为指向数组第一个元素的指针和函数指针。

> 注意，模板匹配后起实参类型的转化只有2和3。有限的类型转化是在严格模板匹配的产物。p615

比如：

```c++
template <class T> int compare(const T&, const T&);
(a) compare("hi", "world");
(b) compare("bye", "dad");

* (a) 不合法。`compare(const char [3], const char [6])`, 两个实参类型不一致。
* (b) 合法。`compare(const char [4], const char [4])`. 实参一致
```



如果，类型匹配失败，推断错误。

当然正，正常类型转化可以在普通函数形参上。





### 函数模板显式实参

可以在定义函数模板是直接指定**显式模板实参**，被指定的实参无需推断，而对应的形参可以用于**类型转化**。

> 这点非常重要！`std::max<double>max(1, 2);`才不会出错。

调用方式类似于类模板定义实例。

```c++
template <typename A, typename B> A selfadd(B);
auto c = self<int>selfadd(0.12930);

```

显式模板实参的使用从左到右的顺序与对应的模板参数匹配，所以无法推断的类型放前面哈~

### 避免使用模板参数

有时候，多余的返回类型不如直接从结果推断出来：

```c++
template <typename IT>
// decltype(*beg) func(....)是不合法的，因为beg在形参定义之前不存在
auto func(IT beg, IT, end) -> decltype(*beg) 
{
    return *beg;
}
```

> 这个时候，**类型转化**模板可以改变返回类型，形如`remove_reference<decltype(*beg)>::type` 返回了一个`*beg`去掉引用的对象的类型。 `type_traints.h`
>
> 

## 类模板

**类模板**无法从编译器中的类型推断中直接获取类型参数，必须使用显式模板实参。

类模板对每个类型编译出来的类都分离的。

### 成员函数

定义在类中的成员函数隐式声明为`inline`的。

定义在类外的成员函数需要加上模板参数。而类中和声明了模板实参的函数体中无需重复声明模板实参。







### 友元

模板类声明普通类为友元和普通类把模板类声明为友元的语法都是一样的：

```c++
template<typenmae T> calss Pal;
class C{
	friend class Pal<C>; // 限定用C实例化的 Pal, 需要前置声明
    template <typename T>  friend class pal2; //无需前置声明
}

template<typename T> class C2{
    friend class Pal<T>; // 同上
    template <typename X> frined class Pal2; // 同上
    friend class Pal3; // 普普通通
    friend T; // T
}
```

那么和友好函数呢？

```c++
//以下两个声明都需要前置声明
// 形如template <> friend 不需要前置声明
template<typename T> class C3{
    friend bool compare();
	friend bool operator==<T>(parameter lists);
}
```

### 别名

```C++
//typedef 只能用在实例化类
typedef Blob<string> StrBlob;
// using 可以为类模板定义一个类型别名
template<typename T> using twin = pair<T, T>;
twin<string> authours;
template<typename T> using twin = pair<int, double>; //固定任意个类型参数、
```



### `static`成员

不同类型实例化的类的`static`成员相互独立，而且在实例化的时候才会被初始化。

```c++
//类外定义
size_t Foo<T>::crt = 0;
```





# 模板参数

模板参数可以覆盖外围的变量名，而且在内部无法被重用。

### 使用类的类型成员

`typename T::value_type()`指定访问模板参数`T`中声明的`value_type`是类型。该语句调用返回一个`T::value_type`默认初始化对象。

`T::value_type()`可能是一个`T`的静态成员! 



### 默认实参

`template <typename T, typename F = less<F>> class Compare;` 指定了`F`默认参数为一个函数指针。如此便可以省略，实例化时的类型参数`Compare<int>`。





## 套娃——成员模板

成员模板就是在类中的模板类或者模板函数，同样的模板函数通过传入实参实例化，模板类通过类型实参实例化。

写法和调用都类似上文

## 实例化

函数模板在调用时实例化，类模板被初始化，作为成员函数，或者说需要模板类的某种信息时都会被实体化。

```c++
tempalce <typename T> class GG{
    T a;
}
class C{
	GG a;
}
    
```

### extern

由于模板会在被使用的时候实体化，容易出现多个文件每个文件都存在相同的实例。显示实例化可以避免这种情况。

```c++
// a.cpp
// 实例化声明
extern template declaration; //声明外部文件实例化了该模板
// b.cpp
// 实例化定义
template declaration; //上文的外部文件需要定义函数模板实例

//declaration的一个例子
int compare(const int&, const int&); //直接把所有模板参数替换为类型参数

```

实例化定义需要实例化类的所有成员，那么可能模板成员就有点问题喽。

## 可变模板参数

> p619

C++把可变数量的参数记做参数包，在模板参数列表中的叫模板参数包，在函数参数列表中叫函数参数包。

```c++
template< typename T, typename ... Args> void foo(const T&, const Args& ... rest);  //非常兼容的一种写法
```



`size...(Args)`可以判断函数参数包的元数数量。

### 可变参数模板的拆包？不，是包扩展

一种有趣的处理可变参数的是递归调用：逐步处理——输出参数。

```c++
// 递归结尾：拆包拆到只剩一个参数
template< typename T> ostream& print(ostream& os, const T& t){
	return os << t << endl;
}
// 除了最后一个参数，其余调用都调用自身
template< typename T, typename ... Args> ostream& print(ostream& os, const T& t, const Args& ... rest){
    os <<  t << ", ";
    return print(os, rest...);
}
void test20(){
    print(cout, 0, 1, 2, 3, "js.", "sdk", "opk");    // 模板牛逼	
}
```



上文其实就是包括的应用实例，包扩展包含了两个元素：模式+扩展。扩展是对

```c++
// const Args & 形成了模式，这是对模板参数包元素进行扩展的形式； 
//...给出了参数包扩展的研发
template< typename T, typename ... Args> ostream& print(ostream& os, const T& t, const Args& ... rest){ 
    
//这是对函数参数包rest进行元素扩展， rest本身就是是一个模式
print(os, rest...);
    
//更复杂一点, 对rest每个元素进行模式扩展
print(os, func(rest)...);
```



### 参数包转发

上述的包扩展已经讲述的很清楚了，包转发不过是参数转发的特例罢了

```c++
// Args 是模板参数包， args是函数参数包
alloc.construct(first_free++, std::forward<Args>(args)...);
```

常用于`emplace_back`类似的函数。

# 模板实参推断

## 参数模板和函数指针

> p607

函数模板被赋值给一个函数指针，或者作为函数指针的形参对应的实参时，模板的类型会被推断出来。但是必须保证类型的唯一性。

## 🐱‍👤参数推断和引用

> p608 Important!

两个模板参数推断非常重要的规则：

1. 沿用正常的参数引用绑定规则；
2. `const`是底层的，不是顶层的；

对函数参数是右值引用的情况有特殊规则：

- 类型别名和模板类型参数可以定义别名的别名，引用的引用。形成`折叠`，`int && &`折叠为`int &`。一般来说，折叠结果都是`T &`，除了`int && &&`折叠为`int &&`。所以下标的`f(T &&)`可以接收任意参数，且`T`可以为左值。

  > 这里的左值，容易引发代码错误。



|            | `f(T&)`：引用                                            | `f(const T&)`：接收任意参数                          | `f(T&&)` ；  右值天生不会`const`；移动                       | `f(T)`😓[奇怪的初始化：ex15.44](https://github1s.com/Mooophy/Cpp-Primer/blob/master/ch16/ex16.42.43.44.45.46/main.cpp) ； 赋值初始化 |
| ---------- | -------------------------------------------------------- | ---------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `f(i = 2)` | `f(int &) ; T: int`                                      | `f(const int &)`;`T:int` `const`成为模板参数的一部分 | `f(int & &&)-> f(int &)` ; `T: int&` ; 特殊规则：`T`为左值   | `f(int) ` ; `T: int`                                         |
| `f(ci)`    | `f(const int &)`;`T: const int`                          | `f(const int &)`;`T:int`                             | `f(const int & &&)->f(const int &)` ; `T;const int &`        | `f(int)`;`T:int`.`const`被忽略                               |
| `f(2)`     | `f(int && &)->f(int &); T: int` 💩 只能传递左值，调用错误 | `f(const int &)`;`T:int`                             | `f(int && &&)->f(int &&)` ; `T: int` 本来就是右值，类型为`T` | `f(int) ` ; `T: int` ; 右值被移动给`T`                       |
|            |                                                          |                                                      |                                                              |                                                              |

> `std::move`就是以右值引用和类型转化为基础的写的。
>
> 特别提一下，对是C风格字符串，或者说字符串字面量`f("cho")`实例化为`f(const char[4] &)`

## 转发

> p613⭕

如果一个函数参数是指向模板类型参数的右值引用，那么对应实参的`const`属性和左值/右值将都得到保持。

但是对于模板函数`A`中调用的函数`B`的右值引用形参，难以获得传入`A`的右值引用`args`。因为指向右值的引用变量都是左值！相对的，传入的左值还能好好的绑定。

标准库`forward<T>(arg)`会返回类型为`T&&`的`arg`。`arg`是左值，`forward`返回的是经过折叠的`& &&`，即`&`。`arg`是右值，`forward`返回的是经过折叠的`&& &&`，即`&&`。

而当用于一个指向模板参数类型的右值引用函数参数`T(&&)`时，`forward`会保存的实参类型的所有细节。

```c++
void func(string &a, string &&b)
{
    cout << a << " " << b<< endl;
}
template<typename T1, typename T2, typename F> void filp(F func, T1&& a, T2&& b){
    func(forward<T2>(b), forward<T1>(a));
}


void test19(){
    int i = 1, j = 2;
    string a = "fafsf";
    string b = "kjfse";
    
    filp(func, "dsf", b);
}	
```





# 重载与模板



模板的重载匹配规则更加复杂一点~：

1. 选出所有经过模板参数推断成功的函数，非模板函数

2. 按照类型转换少的函数优先排序

3. 如果只有一个更好的匹配，就选择第一个；如果有多个，则选择**特例化**模板。

   > `const T&` 可以接收任何参数，是最泛化的模板。
   >
   > 而非模板函数比模板函数更特例；

```c++
//a
template <typename T> string debug_rep(const T&);
//b
template <typename T> string debug_rep(T*);

// 对 实参string s
string s = "hi";
debug_rep(s);
//只有a方法是可行的，b：模板实参无法从非指针转化为指针类型

//对string指针
debug_rep(&s);
//a: debug_rep(const string* &) 
//b: debug_rep(string *); //精准匹配,没有类型转化
// 后者无需转化为const，优先级即更高

// 对const string*
const string* sp = &s;
debug_rep(sp);
//a: debug_rep(const string* &)
//b: debug_rep(const string *);
// 两者优先级相同，但是后者的模板函数更特殊，

```

注意，希望被匹配的函数一定要在被调用处的定义域中存在。



> 如果还想讨论一下 C风格字符串查看`p617`。

# 模板特例话



模板特例化（`template specialization`）是为了指定特定类型在模板重载时选定的版本，但本质上是一种**模板实例化**。

比如形参字符数组`const char (&)[20]`，可以接收数组的引用，但是无法直接接收指针`char *p`，所以会被`const char&`模板重载掉。



## 函数特例化

````c++
template<>
{
    int compare(const char* const &p1, const char* const &p2){
        retunr strcmp(p1, p2);
    }
}
````

> 同样的，不要把特例化函数弄丢了。这种错误很难找。

## 类特例化

语法如下：

```c++
template<class T> struct A<int> {
	// class content.
}

```

与函数模板不同的是，类特例化可以进行部分特例化，即成员特例化。在调用成员时，该模板才会对该成员进行特例化。

```c++
template<> 
void Foo<int>::Bar(){
    // function content.
}
```