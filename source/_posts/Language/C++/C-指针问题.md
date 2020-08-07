---
title: C++指针问题
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
categories:
  - Language
  - C++
date: 2020-08-07 13:05:44
tags:
---



## a、&a与 &a+1

**1.正确解C语言指针中的 &a+1，假设a为一个数组**

```
int a[5]={1,2,3,4,5};
int p=(int)(&a+1); 
printf("%d",*(p-1));
```

<!-- more -->

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

The double asterisk ***\*** define what is known as a **Pointer to Pointer.**

This is a simple concept, a pointer is an independent entity. It can point to anything i.e it can point to a variable or it can point to a pointer which in-turn points to something else.

This concept is not limited to only a “POINTER TO POINTER”.
You can have a chain of pointers.
In the following case ” **x ”** is a variable having value 23, **“ y ”** contains the address of ” **x ”** , and **“ z ”** contains the address of **“ y “.**

```
int x = 23;
int *y;
int **z;
y = &x;
z = &y;

std::cout<<x<<endl; 		//23
std::cout<<*y<<endl; 		//23
std::cout<<**z<<endl; 	//23
```

The *****(asterisk) is called a de-referencing operator to access the value the pointer points to.

You can check out more at
[C++ Pointer to Pointer (Multiple Indirection)](http://www.tutorialspoint.com/cplusplus/cpp_pointer_to_pointer.htm)

Thanks :-)

