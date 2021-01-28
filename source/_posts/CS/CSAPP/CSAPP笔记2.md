---
title: CSAPP笔记2
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
categories:
date: 2020-08-07 12:16:59
tags:
---





# 程序结构和执行过程

本章主要讲解程序在机器级代码上的执行过程以及程序编译翻译过程。

## 信息存储

相比人类熟悉的代表了十指的十进制，二进制的稳定性、表达形态少、对硬件芯片的友好性是建造计算机的更优选择。典型的二进制应用就是记录数值，`float-point encoding` 和 `Unsigned encoding`就是代表。

> 有趣的是，计算机的算术运算过程即使是对溢出运算也会满足结合律(associative)



数值组成的bit有限就造成了数据表达的有限，从而引出的计算溢出，甚至安全问题都是编程者需要考虑的。

------

虚拟空间(virtual memory)是计算机操作系统提供的虚拟空间，以C语言的指针举例，一个C pointer指向的一定是一个数据类型(int, float, or structure)的第一个字节的虚拟地址。C语言本身会组织类型信息(*type* information)以便获取指针指向的数据内容，但是在机器级的代码中所有的程序对象都是一样的bit。(p63)

> C语言在早期计算机语言发展占据重要的位置，比如提供了内存分配器（memory allocator）——the malloc library function。C语言的编译可以对GCC（Gun Compiler Collection）添加参数以控制编译版本
>
> - `gcc -std=c11 prog.c` 指定了C11标准版本
> - `-std=c99`指定了C99版本
> - `-ansi`和`-std=c89`指定了C90版本
> - `-std=gnu11`指定了GNU项目的开发的一个版本，包括了ISO C11的内容
>
> C语言支持向后兼容（backward compliale，“后”就是指过去，而非口语所说的“以后”），那么C语言编译的32bit的程序也可以在64位机子上跑。但是64bit的程序不能在32位的机子上跑。
>
> - `gcc -m32 prog.c` 设置了编译的位数，同理`-m64`设置了64bits

> C的指针有两个方面——值和类型，值指向了指针指向的内容的地址，类型指出了指向的地址的存放的信息的种类。

十六进制计数 （Hexadecimal Notation）

[![image-20200503124826544](http://static.come2rss.xyz/image-20200503124826544.png)](http://static.come2rss.xyz/image-20200503124826544.png)

[image-20200503124826544](http://static.come2rss.xyz/image-20200503124826544.png)



1000多页是时候考虑时间问题了，有更值得去做事情去干，暂时读的话还不读英文版了。

