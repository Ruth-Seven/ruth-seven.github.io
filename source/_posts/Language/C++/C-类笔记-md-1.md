---
title: C++ 类笔记
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
date: 2021-03-14 16:01:34
tags:
categories:
---








# C++ 类笔记

> 个人非常喜欢对知识进行概括性的总结，减少记忆负担，舍去无用的语法细节，保留C++设计思路。这是C++系列笔记存在意义。
>
> 所以这类笔记不适用第一次学习的同学，只适合用作第二份参考资料，即学习基础知识之中或者之后进行总结。

<!-- more -->



## 构造函数

默认构造函数默认“候补”，控制成员的默认初始化过程。

```c++
struct Person{
    Person() = defautl;  //让编译器构造出默认构造函数
    s [san]Person(int info){}
}
```

初始化顺序，按照定义的顺序来，与构造函数的初始值列表无关。

```c++
class Person{
    int i ;
    int j;
    Person(int i, int j): age(i), height(j){}
}
```

在重载的基础上，委托构造函数能调用另一个构造函数。

```c++
Person();
Person(int j): Person(){}
Person(double i, int j): Person(i){}
```

调用如下：

```c++
Person p1; //调用了默认构造函数
Person obj(); //这是声明了一个函数
```



### 不要构造函数和析构函数中调用虚函数

虚函数始终仅仅调用基类的虚函数（如果是基类调用虚函数），不能达到多态的效果，所以放在构造函数中是没有意义的，而且往往不能达到本来想要的效果。

> 参见《Effective C++》 条款09：绝不在构造函数或析构函数中调用虚函数



### 构造函数和析构函数的注意事项

构造函数：

1. 构造函数可以被重载。
2. 必须使用初始化列表进行初始化的 ：
   （1）`const`修饰的类成员或初始化的引用成员数据；
   （2）对象的情况（包含继承情况下，通过显示调用父类的构造函数对父类数据成员进行初始化）；
   （3）子类初始化父类的私有成员。

析构函数：

1. 没有返回值，没有参数；
2. 析构函数不能进行重载；
3. 析构函数无需主动调用，如果主动调用析构函数，只会执行析构函数里的内容，不会释放内存。
4. 析构函数一般必须是虚函数，不然在多态情况下无法删除掉派生类的部分内容。



还有，不要在构造函数和析构函数里调用虚函数，`BuyTransaction`在构造过程中调用`Transaction`的构造函数，同时调用的`logTransaction`虚函数并不能调用到派生类的重写方法。因为在构造期间，对象的类型是`base class`而不是`Derived classs`。



```c++
class Transaction{
public:
   Transaction();
   virture void logTransaction() const;
};
 
Transaction::Transaction(){
   ......
   logTransaction();
}
 
class BuyTransaction: public Transaction{
   virture void logTransaction() const;
   ......
};
BuyTransaction b;
```

一种解决方法是取消`virture`类型，同时在派生类构造函数中传入底层函数的信息。

```c++
class Transaction{
public:
   Transaction(const std::string& info);
   void logTransaction(const std::string& info) const;
};
 
class BuyTransaction: public Transaction{
public:
   BuyTransaction(parameters): Transaction(createLogString(parameters)){
   ......
}
private:
   static std::string createLogString(parameters);  
};
```







## this

this是指向该对象的指针。成员函数在运行时会自动传入this指针（编译器），相当于`Screen call(&this);`



```c++
// 返回该对象作为左值
inline Screen & Screen::set(char c){
    return *this; //解引用
}
```







## 特殊类型

### mutable data member  可变数据类型·

即使是`const`函数也能改变mutable类型数据。

```c++
mutable size_t access_str
```

### inline 内敛函数



### `const` 成员函数

把传入函数的this的类型转化为`const`指针，比如`const Sales_data *const `。所以该成员函数无法修改this指向的对象的内容。

这是因为，由于**this的类型是指向常量的指针，this无法绑定（指向）到常量对象上**。进一步的，常量对象无法调用非常量成员函数。反过来，非常量对象可以调用常量和非常量成员函数。

> 这里需要对指针的`const`初始化有彻底的了解。

因此，C++根据对函数是否是`const`的来重载。



### `static`

静态成员生命独立于类之外。

注意，类外定义成员和成员函数不要重复定义`static`关键词。

`static`成员可以作为默认实参。



## 类的定义域

类的定义域自然的在括号内。在类外定义成员和方法是自然需要添加类的名字。

记住，从函数名前的类名开始，该函数就属于类的定义域了。

````c++
class Person{
	using indx = std::strigng::size_type;
	
}

Person::idx //返回值不在函数的定义域中
Person::call(idx a); 
````



### 名字查找

一般的名字查找都是考虑代码之前的声明，从内定义域找到外定义域。

类不同，它先处理声明（成员声明， 函数返回值，函数签名等等），再处理函数定义。在查找过程中，查找完类内还会查找类外的定义域和类的成员和成员函数。



# 重载运算符



重载运算符函数可以改变原有运算符的运算性质，我们有两个问题需要考虑：

1. 重载什么运算符？怎么重载？

> 重载功能应当与原来运算符的性质保持方向一致。比如IO操作，判断`==`和`!=`，赋值和复合赋值，而且同时重载相关联的运算符是更受推荐的。
>
> 另外，具有运算顺序性质规定的运算符，如`&&`和`||`，不推荐重载，因为无法保留该性质。
>
> 通用的符号`()`| `[]` |`=`| `->` 必须是成员。
>
> 以及，内置类型的运算符无法被重载。

2. 重载函数是否应该是成员函数？

>首先，非成员函数的重载函数，比如`Person operator+ (Person &a, Person&b) {return ……} `其调用`c = a + b`的等价形式为`c = operator+(a, b);`。这隐式的利用了`Person`的转化规则，即使`a`或者`b`存在一个非`person`类，但可以隐式转化为`person`数据就可以调用。
>
>作为对比，`Person Person::operator+(Person &a, Person& b){}` 的调用`c = 22 + a`的等价调用形式就是`c = 22.operator+(a)`。`22`作为**左侧运算对象**，被当做`operator+`中传入的`this`指针指向的对象。这显然是错误的。
>
>具有对称性的运算符号 `+`, `<<` 应该作为非成员函数。



## 重载运算符的建议

+  输出不控制格式
+  输入完成后检查内容，而不是输入中检查内容
+  关系运算比较的项目要相同， 如`<` 和`==`；相反的关系运算要同时定义，比如`==`和`!=`；定义一个关系运算符而不是重新定义一个函数，这有利于使用记忆，这能更好的适应标准库。 
+  接受花括号的元素列表的赋值方法：

```c++
vec = {"a", "b", "c"};
Person &operator=(initializer_list<string> il){
    ----
    return P;
}
```

+ `[]`定义返回一个`const`或者非`const`

的元素引用。

+ 前置和后置自增自减运算符的区分方法是

```c++
Person operator++(int){} //后置
Person operator++(){} //前置
```

+ `->`的工作可以委托给`*`。
+ `()`必须是成员函数，可以直接对实例如同调用函数一样调用实例，甚至可以把一个临时对象传入标准库算法中当函数对象用。

## 类型转化的两种方式

C++支持把一步类类型转换，调用只有一个形参的构造函数把一个形参类型的参数转化为该类.

````c++
class Person{
   Person(string s){}
   Person static add(Person a){return a;}
}
string  a = 'xiaoming'

Person.add(a);
Person.add("xiaoming")//执行了两步转换，先把“xiaoming”转化为string


````

`explicit Person(string s)` 可以禁止这种转化。



C++可以重载**类类型转换符**将实例转化任何可以被函数返回的类型。

这一般被隐式的自动转化，而且在仅仅用一次的标准内置转换之前或者之后使用。

```c++
Person{
   public:
    int c;
    Person(int _c):c(_c){}
    operator int(){return c;} //无返回值，无参数
}

si = 4； // 隐式构造 + 拷贝赋值
si + 3;  // 隐式转化为int, 整数加法
```

定义为`bool`以外的类型不太常见，也容易出现bug，因为用户不常使用。

C++引入了显式的类型转换运算符，可以避免大多数问题，但是还是会在`while`| `for` | `&&` | `||` | `！` 和`? :`处，**显式转化还是会被隐式执行**。

```c++
class SmallInt{
    int val;
    public:
    explicit operator int() const {return val;}
}
SmallInt si;
static_cast<int>(si) + 3;
```



### 二义性转化

> 这部分学深了，吃力不讨好。浅尝则止，学会如何避免出现二义性问题即可，

二义性转化就是存在两个以上转化路径：

1. 两个类提供相同类型转化，例子1
2. 类定义了多个类型转化规则，例子2。

```c++
//例子1
struct A{
    A(const B&);
}
struct B{
    operator A() const;
}
A f(const A&);
B b;
A a = f(b); // 1. 构造函数 2. 类型转换
A a=  f(b.operator A() ); //显式调用类型转化

//例子2
struct A{
    A(int = 0);
    A(double);
    operator int() const;
    operator double() const;
}
void f2(long double);
A a;
//无法精准匹配到long double
f2(a); // operator定义的类型转化路径不唯一
long lg;
// 构造函数无法精准匹配
A a2(lg); // 两个构造函数中类型转化不唯一

// 上述问题还可以和函数重载结合在一起，更复杂

//例子3
struct C{
	C(int);
  	C operator+(const C, const C);
    operator int() const;
}
C l, k, g;
g = l + k; //调用重载运算符
int i = g + 0; //二义性问题： 1. 0变C，调用重载运算符； 2. g变int，调用内置运算符
```

通用的建议：

1. 两个类不设置相同的类型转化
2. 避免转化目标是内置类型的类型转化
   - 如果定义了一个算术类型转化，就不要定义接受该转化类型的重载运算符了。如此，对象可以被类型转化，再使用内置运算符；
   - 不要定义多个算术类型的类型转化，让标准类型完成想其他算术类型转化的工作。

> 如果调用重载函数中需要构造函数和类型转化来避免二义性问题，则说明设计不合理。







# 拷贝控制

> p440

## 拷贝其实是一种初始化

拷贝初始化不同于直接初始化，直接初始化利用函数匹配调用对应的构造函数，拷贝初始化在调用`=`下，调用编译器默认生成的或者自定义的**拷贝构造函数**。

> 编译器默认构造的拷贝构造函数叫做，*合成构造函数*，其他同理。

```c++
class Person{
    int age;
public:
    Person()=default;
    Person(int _age): age(_age){};
    Person(const Person &a){};// 第一个参数必须为 类的引用，之后的参数必须有默认值
    // 等价形式
   	//    Person(Person &a):age(a.age)
    int get(){return age;}
};
void test14(){

    
    Person a; //直接初始化
    Person b = a; //拷贝初始化
    Person c = Person(100); // 拷贝初始化
    Person d = 100; // 隐式转化 -> 拷贝初始化
    cout << a.get() << endl;
    cout << b.get() << endl;
    cout << c.get() << endl;
    cout << d.get() << endl;
}

```

拷贝初始化发生在*初始化赋值*的过程中，如上问的`=`，传递值给非引用形参，函数返回值以及列表初始化。

## 赋值是声明之后的事情

类可以控制它的**初始化**过程，也可以控制它的**赋值**过程。`=`拷贝赋值运算符，由编译器默认合成。我们可以通过自定义来重载运算符来控制拷贝的动作，比如禁止拷贝。

```c++
class Foo{
    public: //如果是 private 就无法调用拷贝操作了
    Foo& operator=(const Foo& foo){}; 
    // Foo a = b;
    // a 传入 重载Foo的 `=` 方法的 this 指针
    // b 为 重载Foo的 `=` 方法的 参数foo
    // 重载函数会把foo中非静态成员赋值给 this指向的对象
}
```



## 析构，是对动态分配的终结

析构函数并不负责，释放成员！

析构函数`~Foo()`类似于构造函数，无返回值，但是无参数，所以不可重载。类被销毁的时候，先执行析构函数函数体，在按成员定义的逆序释放非静态成员资源，会对非内置类型调用析构函数，内置成员也不需要析构。

> 这顺序与构造成员完全相反。

注意，动态分配的`new`实例无法因为指针被销毁而被释放，必须对指针使用`delete`运算符才行。这也是析构函数的任务之一。







## 控制拷贝

类可以通过添加`=delete`，或者定义函数为`private`且不声明函数来控制类的行为。

比如，

```c++
class Person(){
public:
	Person()=default;
    Person(const Person& a)=delete; // 阻止拷贝初始化
    Person& operater=(Person &a)=delete; // 阻止赋值
    
}

class Person(){
private:

    Person(const Person& a); // 阻止拷贝初始化
    Person& operater=(Person &a); // 阻止赋值
public:
    Person()=default;
}
```

上面第二例子里，成员函数和友元还是可以拷贝和赋值，但是会因为没有定义，而爆出**链接时错误**



深层和浅层拷贝常常被其他语言说道。C++提出了类值型拷贝和类指针型拷贝，前者对指针资源是创建出独立的内存副本，来保存指针指向的对象，这样拷贝备份独立于原值。后者相反，它直接拷贝指针。这类似于浅层拷贝，两个对象都指向同一份动态分配的资源。

啰嗦一点，类值型拷贝是上述拷贝初始化，拷贝赋值和析构所需要的操作目的。



### 类值的拷贝

```c++

#include <iostream>
#include <string>
using namespace std;

class HasPtrP
{
    std::string *ps;
    int i;
public:
    HasPtrP()
    {
        ps = new std::string("12389123");
        i = 0;
    }

    HasPtrP(const std::string& s )
    {
        ps = new std::string(s);
        i = 0;
    }

    HasPtrP(const HasPtrP& a)
    {
        
        ps  = new std::string(*a.ps); // 拷贝初始化不需要释放ps
        i = a.i + 1;
    }

    HasPtrP& operator=(const HasPtrP& a)
    {
        std::string *p = a.ps; // 缓存ad对象的指针，这是一种好模式，防止`a = a`的赋值产生错误
        delete ps;
        ps  = new std::string(*p);
        i = a.i + 1;
        return *this;
    }
    ~HasPtrP(){
        delete ps;
    };

    void print(){
        cout << *ps << " " << i << endl;
    }
};


int main()
{
    HasPtrP a("nihc"), b = a, c = b;
    a.print();
    b.print();
    c.print();
    
}
```





### 类指针的拷贝

类似指针的拷贝，一个非常好的实现就是`shared_ptr`，直接指出指向共享对象的个数。



````c++

#include <iostream>
#include <string>
#include <vector>
using namespace std;

class HasPtrP
{
    std::string *ps = nullptr; // 指向共享资源的point    
    int *count = nullptr; // 计数器
public:

    HasPtrP(const std::string& s )
    {
        ps = new std::string(s);        
        count = new int(1);
    }

    HasPtrP(const HasPtrP& a)
    {
        
        ps = a.ps;
        count = a.count;
        ++*count;        
    }

    HasPtrP& operator=(const HasPtrP& a)
    {
        if(a.ps == ps) return *this; //防止 `a = a`
        std::string *np = a.ps; // 缓存ad对象的指针，这是一种好模式，防止`a = a`的赋值产生错误
        int *ct = a.count;
        --*count;
        if(*count == 0){
            delete ps;
            delete count;
        }
            
        ps = np;
        count = ct;
        ++*count;
        return *this;
    }
    ~HasPtrP(){
        --*count;
        if(count == 0){
            delete ps;
            delete count;
        }

    };

    void print(){
        cout << *ps << " " << *count << endl;
    }
};


int main()
{
    HasPtrP a("nihc"), b = a, c = b;
    a.print();
    b.print();
    c.print();
    vector<HasPtrP> vec;
    for(int i = 0; i < 5    ; ++i){
        vec.push_back(a);    
        vec[i].print(); 
    }
    a.print();
    vec.clear();
    a.print();
    a = a;
    a.print();
    HasPtrP g("88");
    g = g;
    g.print();
}
````



## 高级swap操作



标准库提供了`swap`操作，但是其标准操作对**类值**型类性能不够优化，因此自定义一个`swap`代替，可以优化性能.

```c++
class HashPtrP{
    friend void swap(const HashPtrP&, const HashPtrP&);
};
void swap(const HashPtrP& lhs, const HashPtrP& rhs){
    using std::swap;
    swap(lhs.ps, rhs.ps);
    swap(lhs.i, rhs.i);
}
```



更优秀的是，如果在赋值操作用`swap`，可以简化代码，同时保证代码的安全性。

```c++
// 注意，这里没有使用引用，就是这里用了拷贝初始化
HashPtrP& operator=(const HashPtrP rhs){
    swap(*this, rhs);
 	this->print();
    return *this; // rhs被销毁
}
```





## 移动构造和移动赋值

> `./cplusplusprimer/cpp_source/ch13/w13.2.reference.cpp`

移动构造函数和移动赋值函数类似于拷贝构造和移动赋值，有类似的函数形式，移动赋值也得出了自赋值问题。

不同是的，移动操作必须传参右值。

```c++
//构造
HasPtrP(HasPtrP &&p) noexcept: ps(p.ps), count(p.count){
        p.ps = nullptr;
        p.count = nullptr;
        cout << "被移动构造" << endl;
    }

//赋值
HasPtrP &operator=(HasPtrP &&p) noexcept{
    if(this != &p){ //避免自身被移动
        if(ps != nullptr){    
            delete ps;
            delete count;
        }
        ps = p.ps;
        count = p.count;
        p.ps = nullptr;
        p.count = nullptr;
    }
    cout << "被移动赋值" << endl;
    return *this;
}
//更好的写法，拷贝交换并赋值：对于左值和右值都可以使用
HasPtrP &operator=(HasPtrP p){ //传入实参首先使用拷贝初始化：左值被拷贝，右值被移动；
    swap(*this, p);
    cout << "被移动 | 拷贝  赋值" << endl;
    return *this;
}// p值自动销毁

```

移动操作是拷贝操作上面性能更好的补充品，但也容易出错——移动数据一半就有错误爆出是难以恢复的。如果需要标准库采用移动操作函数，必须声明为`noexcept`。所以编译器在大部分情况下也不会自动生成移动操作函数，而如果在调用时用右值而没有移动函数，也会用拷贝函数代替。

> 当一个类没有定义自己任何版本的拷贝控制成员，且类中每个非`static`成员都可移动时，编译器才会合成移动构造和移动赋值。
>
> 可移动：内置成员天生可以移动，有移动操作的类也可移动。

移动源对象必须保持可析构，比如指向动态资源的指针为`nullptr`；移动源在移动后的值是无规范意义上的值的；



### 移动迭代器

标准库并没有算法可以直接使用右值，但是提供了移动迭代器**适配器**，`make_move_interator()`把迭代器的解引用符号重载为返回一个指向元素的右值。如此便可以传入正常算法，如`uninitialized_copy()`。但标标准库不会保证，算法会移动后就不会访问原元素，安全性是个小问题。

## 右值引用和成员函数

右值的引用在函数匹配上也不同的，比如标准库中`push_back(const X&)`为一定为左值，`push_back(X&&)`使用右值。

右值和左值一样能调用成员函数，也甚至能进行赋值。后者通常毫无意义，**引用限定符**可以限定函数中`this`指向的对象是右值还是左值。

```C++
class Foo
{
    Foo &operator(Foo &&x) const &{ //限定 如Foo a = b;中 a只能是左值
		//赋值操作
        return *this;
    }
}
```

而限定引用符也导致函数重载，而且限定重载符必须同时出现或者不出现在所有同名成员函数。



## 三五法则

析构函数的需求在于`delete`释放动态内存，所以一般拷贝初始化和拷贝赋值是必须配套析构的。

但是，拷贝赋值和拷贝初始化两者常常同时出现，因为需要相同创建和赋值特性。此时，析构反而不是必须的。

移动操作仍然是为了弥补性能上的差距而生的。



## 继承与拷贝控制

> p553

C++类不继承构造、析构、拷贝和移动操作函数，因为它会自动创建对应的函数。那么虚函数在这几类函数上也有了价值。

👹**合成的**构造、拷贝和析构操作仍会调用基类的，可访问且未删除的，合成或者自定义的拷贝操作来赋值基类部分。

被删除的情况：

| 基类               | 派生类               |      |
| ------------------ | -------------------- | ---- |
| 成员函数删除       | 对应的成员函数被删除 |      |
| 析构不可访问或删除 | 构造函数被删除       |      |
|                    |                      |      |





# 继承

> p526



C++的继承相比与java更加复杂，涉及到更多的底层细节问题。

派生类会把从基类继承过来的部分和派生类自己创建的部分，拼接在一起。





一般来说，派生类构造函数使用基类的构造方法是更合理的，否则只是简单默认初始化。

`static`成员即使在派生类体系中也是只存在一个。

`final`可以防止继承发生。

```c++
class Quote{ // 定义且声明
    
}

class Bulk_quote final : public Quote{// 继承 
    
}
```

## 虚函数

只有`virtual`虚函数才能在C++中执行动态绑定（运行时绑定）强大作用，被派生类继承的虚函数会在被动态绑定到基类部分上。而不存在的动态绑定的函数会在编译器编译过程中绑定到派生类部分上。

> 覆盖虚函数的函数也是虚函数。

这种特性要求虚函数必须实现自身。

动态绑定的特性，让我可以把基类的指针和引用绑定到派生类上，这称之为**派生类到基类的类型转换**。

明显的是，**只有**指针或者引用才能触发动态绑定机制。相对的，非虚函数和对象的调用都在编译时唯一的确定了。





C++引入了**静态类型**描述程序在编译时推断出来的类型，而**动态类型**是在C++运行过程中才能确定的，变量或者表达式在内存中的对象的类型。

  

但是不存在从基类到派生类的类型转化，可以想象派生类的引用是无法使用基类没有的方法的。同样也没有对象之间的类型转化，但是我们可以使用初始化和赋值来赋值对象。

> 基类到派生类的类型转换只能使用强制类型转化。

C++的类的初始化和赋值（移动）都是调用方法的：构造函数和赋值运算符！它们会自动切除掉传递进参数的派生类上多余的部分。



```c++
// 派生类到基类的类型转换
Bulk_quote bulk;
Quote *basep = &bulk;
Quote &basep = bulk;


// 基类到派生类的类型转化, ✖
Quote base;
Bulk_quote *bulkp = &base;
Bulk_quote &bulkp = base;

//强制类型转化
Quote base;
Bulk_quote item = stati_cast<Bulk_quote>(base);

// 初始化和赋值
Bulk_quote bulk;
Quote base(bulk);
Quote base = bulk;


```

### 什么函数不能声明为虚函数

1. 普通函数
2. 内联函数：内联函数是在编译期就被展开，而虚函数运用的是运行时的多态机制。这是有本质的区别的。
3. 构造函数：构造函数用来生成对象，而只有当对象生成后，多态机制才能使用。
4. 静态函数
5. 友元函数



### 纯虚函数

无法在类中定义，只能在类中声明的纯虚函数代表的是一种理念，一种共同接口必须需要继承者完成的设计理念。这注定了抽象基类无法被实例化。



### 小小细节



调用虚函数的默认实参是由其调用的静态类型决定的，比如指针的类型。所以最好基类和派生类的默认实参都是一致的，

作用域运算符可以避免动态绑定，直接指定指向的对象。

`basep->Quote::net_price()`。这通常在派生类方法覆盖基类方法非常有用。



`final`关键字可以修饰方法，避免被覆盖。

`override`（覆盖）关键词显示的提示出该方法需要被覆盖，如果没有就会报错。这是一种良好的区分出**重载和覆盖**的编程习惯。

> 重载是分身，覆盖是父子局`(*^▽^*)`

> 再次说明，只有虚函数才能被覆盖，所以`override`修饰的方法在基类必须是虚函数。

注意，覆盖需要考虑方法是否`const`，函数签名一致性



派生类的构造函数通过递归的调用基类的构造函数来初始化类中数据。

## 访问控制和继承

>  p542

定义成员中，`private`关键字保护了成员不被任何其他类以任何方式访问。`protected`让派生类和友元可以访问**派生类中基类部分**的成员，**而对基类成员是无法访问特权**。

> `protected`权限保证了基类在使用时对任何其他类与`private`一致的表现，而在继承中体现了`public`的特点。
>
> ```c++
> class Base{
> protect:
> void func(){}
> }
> class Drive: publc Base{
> public:
> void func(Base &c){
>   c.func(); //✖ 对对象没有访问特权
> }
> }
> ```
>
> 



定义派生类中，**类派生列表的派生访问说明符**部分定义了**派生类基类部分的成员**的权限。

> 书上讲的比较复杂，我总结一下，其实很简单：本质上就是将派生类中从基类继承来的成员的权限提到最高，比如`pirvate`和`protected`当然取`private`。
>
> 有继承链 `A<- private -B<- protected - C`，`B`从`A`中继承来的成员都是以`private`等级保护起来的，也就是说`B`和`B`的友元都能访问从`A`继承的部分成员，但是`B b`无法直接访问保护和私有内容，那么`C`也无法访问从`B`中`private`的内容。



如果需要改变继承成员的权限，`using`语句可以改变该类可访问成员的权限。

```c++
class B: private A{
    protected:
    using A::size; //从private 改变为protected
}
```





`class`和`sturct`的唯二不同之处就是默认成员访问说明符和默认派生访问说明符，`class`都是`private`而`struct`都是`public`。

### 类型转化的可访问性

讨论一下派生类到基类的转化方式的可行性受到派生访问说明符的影响：

> 这种权限限制方式，**非常像访问接口的权限**。分别考虑：类的用户，类以及类的派生类

+ 用户代码，即实例的转化，只能在`public`继承才行
+ 派生类的成员和友元，在三种派生权限都可进行
+ 派生类的派生类的成员和友元，只能在`protected`和`public`才能进行转化



## 继承的类作用域

> p547

派生类的作用嵌套在基类的作用域中，所有派生域的实体（函数或者变量）可以隐藏基类中的变量和函数。

> 不同作用域的函数无法相互重载，而是会直接隐藏。因为编译器只查找最“靠内”的一个。

这就引出了虚函数和非虚函数在基类和派生类中定义后到底调用哪个的玄学问题⭐⭐⭐：

+ 调用着`p`和`obj`的静态类型决定了必须在该静态类型下查找实体，并且不断查找直到到达继承链的顶端。
+ 找到以后，进行类型检查：
  + 如果调用对象是对象`obj`或者成员不是虚函数，那么就产生一个常规的函数调用。
  + 否则，根据`p`或者引用进行动态绑定，产生一个虚调用。

> 上面的判断规则非常重要。 





## 虚析构函数

> p552

虚析构函数对于动态绑定是必须的。



继承和do [duo]





## 虚函数和构造函数

构造函数和析构函数在负责构造类和销毁类的内容，在继承中可以理解是逐步构建类的内容，而且“改变”了对象的类型。

所以构造函数和析构函数在调用虚函数时，只会调用当前构造函数的所在类的虚函数版本。



## "继承"的构造函数

构造函数式不允许继承的，C++11允许一特别的方式直接直接“继承”基类构造函数。

```c++
class A{
    A(string book, double price);
    
};
class B{
    using A::A;
    //等价于
    //B(string book, double price): A(book, price);
}
```

如此继承的构造函数，其`explicit`和`constexpr`都一致。

但是实参会被省略。

## 容器和继承

容器不支持直接存放继承树上的多个类，无论把容器的`T`定义为基类还是派生类。

但是存放指针就避免这种情况。C++提供了指针的灵活性，也承受了更多安全性和复杂性问题。

## 赋值兼容问题



派生类赋值或者绑定到基类的指针，引用，或者变量上。其内部数据变量一一用派生类初始化。



其中基类的指针无法指向私有继承的派生类，另外派生类的指针也不能指向基类。







# 多重继承

多重继承的构造、析构、赋值和拷贝函数的执行过程都和单继承的过程类似。指针和引用的静态类型对可引用成员的效果，也差不多。

但是，多继承带了来潜在的二义性问题：如果**名字**在多条继承链中找到，调用该名字就是暴露出二义性问题。

> 先查找名字，后进行类型检查。名字包括**类名**，成员名！

```C++
class Base{};
class D1: public Base{int a};
class D2: public Base{int a};
class W: public D1, public D2{};
```

这里有两条继承链：`Base<-D1`和`Base<-D2`，如果成员没有在`w`找到就会同时在所有基类上查找。

```c++
Base *pb = new W; //✖ W有两个Base，二义性问题，无法绑定到特定Base部分
W w;
w.a; // 即使a是private的，也会产生二义性问题
```

通过在派生类中重新定义一个名字，或者在调用是指明作用域，可以避免二义性问题。

```c++
class Base{};
class D1: public virtual Base{public: int a; int b;};
class D2: virtual public Base{public: int a; int b;};
class W: public D1, public D2{public: int b;};

Base *pb = new W; 
W w;
w.D1::a;
w.b;
```



## 虚继承 | 虚派生

虚继承为了保证多重继承链中共同部分只只出现一次，避免**部分**二义性问题，也保证了成员的共享。只需要在继承中把被共享的类声明为`virtual`即可。

> 部分的原因：若在虚基类之下有两个派生类有相同的名字，还是会产生二义性问题。

虚基类必须被第一个初始化，如果有多个虚对象，则按派生列表中出现的顺序从左往右依次构造。虚基类构造完成后，按一般的构造函数调用顺序构造其他对象部分。

> 合成的拷贝、赋值顺序与初始化顺序相同。而析构与其正好相反。

虚基类构造函数如果没有在构造函数的初始化值列表中调用，则会*默认*调用。





# 虚函数表



## 虚函数表、虚指针

 当一个类在实现的时候，如果存在一个或以上的虚函数时，那么这个类便会包含一张虚函数表。而当一个子类继承并重载了基类的虚函数时，它也会有自己的一张虚函数表，言外之意，虚函数表可以让没有重载虚函数的派生类共用。另外，虚函数表对于没有重载的函数可以直接指向基类的方法。

类在内存中的存放形式，对象保存这虚函数表指针，指针指向在编译阶段建构的虚函数表，虚函数表存放着所有继承的自定义的虚函数。在内存结构中它一般都会放在类最开始的地方，而对于普通函数则不需要通过查表操作。

以下例子包含了继承关系：

```cpp
class A {
public:
    virtual void vfunc1();
    virtual void vfunc2();
            void func1();
            void func2();
private:
    int m_data1, m_data2;
};

class B : public A {
public:
    virtual void vfunc1();
            void func2();
private:
    int m_data3;
};

class C : public B {
public:
    virtual void vfunc1();
            void func2();
private:
    int m_data1, m_data4;
};
```

以上三个类在内存中的排布关系如下图所示：

![img](D:\个人文件\重要文件\闲书与笔记\MD暂存文件\v2-e2f479ca9b1c56ac33dfae896ce56f49_r.jpg)

1. 对于非虚函数，如*func2*，互不关联，各自独立的，不存在重载一说，在调用的时候也不需要进行查表的操作，直接调用即可。
2. 由于子类B和子类C都是继承于基类A，因此他们都会存在一个虚指针用于指向虚函数表。**注意**，假如子类B和子类C中不存在虚函数，那么这时他们将共用基类A的一张虚函数表，在B和C中用虚指针指向该虚函数表即可。但是，上面的代码设计时子类B和子类C中都有一个虚函数 *vfunc1*，因此他们就需要各自产生一张虚函数表，并用各自的虚指针指向该表。
3. 对于虚函数 *vfunc2*，两个子类都没有进行重载操作，所以基类A、子类B和子类C将共用一个 *vfunc2*，该虚函数的地址会分别保存在三个类的虚函数表中。
4. 从上图可以发现，在类对象的头部存放着一个虚指针，该虚指针指向了各自类所维护的虚函数表，再通过查找虚函数表中的地址来找到对应的虚函数。
5. 对于类中的数据而言，子类中都会包含父类的信息。如上例中的子类C，它自己拥有一个变量 *m_data1*，似乎是和基类中的 *m_data1* 重名了，但其实他们并不存在联系，从存放的位置便可知晓。

> 在`C`中，*m_data1* 默认为`C`的变量，而非从`A`继承的变量。



再欣赏一个[例子](https://blog.popkx.com/How-are-C-base-classes-and-derived-classes-stored-in-memory-c-how-to-handle-virtual-functions-virtual-table-and-virtual-pointer/)：

![内存模型](D:\个人文件\重要文件\闲书与笔记\MD暂存文件\4260343380.png)

可以看出非虚函数是每个类独立存储的。

而非虚函数不占**实例**空间的，虚表和非虚函数都是在编译期间都生成的。对象里只有虚表指针、变量。



```c++
class A {
public:
    void foo1()  {
        printf("A::prv_i1 \t addr: %p\n", &prv_i1);
        printf("A::prv_i2 \t addr: %p\n", &prv_i2);
    }
    void foo2() {}
    virtual void vfoo1() {}
    virtual void vfoo2() {}

    int pub_i1;
private:
    int prv_i1;
    int prv_i2;
};

class B : public A {
public:
    void foo1() {
        printf("B::prv_i1 \t addr: %p\n", &prv_i1);
        printf("B::prv_i2 \t addr: %p\n", &prv_i2);
    }
    void foo2() {}
    virtual void vfoo1() {}
    //void vfoo2() {}
private:
    int prv_i1;
    int prv_i2;
public:
    int pub_i1;
};


```



### 虚函数表指针和虚函数表创建时机

虚函数表指针(`vptr`)：

`vptr`跟着对象走，所以对象什么时候创建出来，`vptr`就什么时候创建出来，也就是运行的时候。
当程序在编译期间，编译器会为构造函数中增加为`vptr`赋值的代码(这是编译器的行为)，当程序在运行时，遇到创建对象的代码，执行对象的构造函数，那么这个构造函数里有为这个对象的`vptr`赋值的语句。

虚函数表：

虚函数表创建时机是在编译期间。编译期间编译器就为每个**类**确定好了对应的虚函数表里的内容。所以在程序运行时，编译器会把虚函数表的首地址赋值给虚函数表指针，所以，这个虚函数表指针就有值了。



### 虚函数表和虚函数地址

c/c++程序所占用的内存一共分为五种:

栈区,堆区,程序代码区,全局数据区(静态区),文字常量区.

显而易见,虚函数表存放在全局数据区.



虚函数表vtable在Linux/Unix中存放在可执行文件的只读数据段(`rodata`)，这与微软的编译器将虚函数表存放在常量段存在一些差别。

> [参考](https://www.cnblogs.com/chenhuan001/p/6485233.html#:~:text=%E6%A0%88%E5%8C%BA%2C%E5%A0%86%E5%8C%BA%2C%E7%A8%8B%E5%BA%8F,%E5%AD%98%E6%94%BE%E5%9C%A8%E5%85%A8%E5%B1%80%E6%95%B0%E6%8D%AE%E5%8C%BA.&text=%E8%99%9A%E5%87%BD%E6%95%B0%E8%A1%A8%E6%98%AFclass,%E7%B1%BB%E6%89%80%E6%9C%89%E5%AF%B9%E8%B1%A1%E5%85%B1%E6%9C%89%E7%9A%84%E3%80%82)








## 动态绑定

在设计了以上三个类之后，我们就要开始对它们进行使用。

```cpp
int main() 
{
    B b;
    b.vfunc1(); // 自然地调用B的虚函数

    A a = (A)b;
    a.vfunc1(); // 强制转化的b现在属于A类，所以调用的是A的虚函数
}
```

 

```cpp
int main() 
{
    A* pa = new B;
    pa->vfunc1(); //寻找B对象化的虚表指针

    B b;
    pa = &b;
    pa->vfunc1();
}
```

>  访问虚指针方式：**(\* p->vptr[n] )(p)** 或者 **(\* (p->vptr)[n] )(p)**，

它的解读是：通过类对象指针p找到虚指针vptr，再查找到虚函数表中的第n个内容，并将他作为函数指针进行调用，调用时的入参是p(式子中的第二个p)，而这个p就是隐藏的this指针，这里的n也是在编译的时候确定的。

**动态绑定**有以下三项条件要符合：

1. 使用指针进行调用
2. 指针属于up-cast后的 

> 上行转换

3. 调用的是虚函数

与动态绑定相对应的是静态绑定，它属于编译的时候就确定下来的，如上文的非虚函数，他们是类对象直接可调用的，而不需要任何查表操作，因此调用的速度也快于虚函数。

## 静态绑定

综上所述，明确一下：

- 静态类型：对象在声明时采用的类型，在编译期既已确定；
- 动态类型：通常是指一个指针或引用目前所指对象的类型，是在运行期决定的；
- 静态绑定：绑定的是静态类型，所对应的函数或属性依赖于对象的静态类型，发生在编译期；
- 动态绑定：绑定的是动态类型，所对应的函数或属性依赖于对象的动态类型，发生在运行期；



静态类型在编译器期间已经确定了能够使用的函数和属性，即使是空指针也不例外。

```c++
A *pc = new C; //pc静态类型为A*，动态类型为C*
B *pnull = NULL; //pnull静态类型为B*，没有动态类型

pa->func2(); //调用静态类型A*指向的func2()
pnull->func2(); //调用静态类型B*指向的func2() 
```









# 友元





友元声明仅仅声明了友元关系。友元函数和类可以访问类中private方法和变量。更详细的，友元类和友元方法可以自由在他们方法里使用**被友元**的所有属性和方法。

注意，在声明，使用各个方法和类之前要先声明该方法和类。如下：

```c++
//先声明clear
void ScreeN::clear();

class Person{
    friend void Screen::clear(); //友元声明 
	int age;
}

//友元使用
class Screen{
	Person p=  Person();
    void clear(){
        p.age = 0;
    }
    
}
```



友元关系无法被传递，也无法被继承。也就是说友元类无法访问被声明友元的类的基类私有成员。

> p545





# 其他

## 空类

类空大小为1，虽然里面没有虚函数表，没有非静态变量。

`sizeof(A) > 0 `是因为标准规定完整对象的大小为正数。

有很多这样的宏`#define ARRAY_SIZE(x) sizeof(x)/sizeof(x[0])` 如果对象大小是0 这个宏会发生除0错误。



#### 函数的生成时机

- C++98/03

  - 如果用户未声明默认构造函数，编译器将生成一个默认构造函数。（**default constructor**）
  - 如果用户未声明拷贝构造函数，编译器将生成一个拷贝构造函数。（**copy** **constructor**）
  - 如果用户未声明赋值运算符，编译器将生成一个赋值运算符。（**copy** **assignment operator**）
  - 如果用户未声明析构函数，编译器将生成一个析构函数。（**destructor**）

  以上函数仅在需要的时候由编译器生成，如果用户不需要，则不生成。

- C++11（C++14也成立）

  - 如果发生以下情况，编译器将生成移动构造函数（move constructor）
    - 用户未声明拷贝构造函数（**copy** **constructor**）
    - 用户未声明拷贝赋值运算符（**copy** **assignment operator**）
    - 用户未声明移动赋值运算符（**move** **assignment operator**）
    - 用户未声明析构函数（**destructor**）
    - 该类未被标记为已删除（delete）
    - 所有成员均为可移动的（**moveable**）
  - 如果发生以下情况，编译器将生成移动赋值运算符（move assignment operator）
    - 用户未声明拷贝构造函数（**copy** **constructor**）
    - 用户未声明拷贝赋值运算符（**copy** **assignment operator**）
    - 用户未声明移动构造函数（**move** **constructor**）
    - 用户未声明析构函数（**destructor**）
    - 该类未被标记为已删除（delete）
    - 所有成员均为可移动的（**moveable**）

- 举例

  ```C++
  class Thing {
  public:
      Thing();                        // default constructor
      Thing(const Thing&);            // copy c'tor
      Thing& operator=(const Thing&); // copy-assign
      ~Thing();                       // d'tor
      // C++11:
      Thing(Thing&&);                 // move c'tor
      Thing& operator=(Thing&&);      // move-assign
  };
  ```





## union

`union`数据结构能够存储不同的数据结构，但同时只能存储其中一种类型。

```c++

union one4all
{
int int_val;
char s[2];
};
//a.int_val = 15;
a.s[0] = 1;
a.s[2] = 2;
```

`union`的内存存放方式是多个数据类型保存在一起的，程序可以从整数，也可以从字符串数组才角度解释。

​	