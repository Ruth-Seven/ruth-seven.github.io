---
title: CSAPP笔记1
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
categories:
date: 2020-08-07 12:16:31
tags:
---



# Programmer’s Perspective )–3th edition

考完了研究生，浪荡了许久，终于肯安下心来钻研提升内功，就从这本书开始吧，抄录两端话送给自己的激励！

> 读完了本书以后你将成为极少数的“牛人”，这些“牛人”知道事情是怎么运作的，也知道当事情出现故障是如何修复。你写的程序将能更好利用操作系统和系统软件提供的功能，对各种操作条件和运行时的参数都能正确操作，运行起来更快，并避免出现使得成型容易受到网络攻击的缺陷。同时你也要做好更深入探究的准备。研究像编译器，计算机体系结构，操作系统，嵌入式系统、网络互连和网络安全这样高级题目。——译者序
>
> We cover data representations, mechine level representations of C programs, processor architecture, program optimizations, the memory hierarchy, exceptional control flow(exceptions, interrupts, processes, and Unix signals), virtual memory and memory management, system-level I/O, basic network programming, and concurrent programming. THes concepts are suppeorted by series of fun and hands-on lab assignments. —— CSAPP online.



正如书籍的题目，此书的编写者考虑到大多数人都不会编写一个OS或者制作一个CPU，那么从一个程序员的角度可以更具体而实用的理解类似于C语言是怎么编译成汇编语言，不同的设置是如何影响计算机性能的，代理是如何工作的计算机**基础内容**。此书着手于x86处理器机器和Linux类系统，并用C作为工具来实操，提供了多个Lab。

# CHAPTER 1 The wonder of computer system

## 伟大的编译器

一个最基本的C源文件是由N个ASCII码组成的数据串，将以文件的形式存储在计算机磁盘中。而每个ASCII都有由8bit组成，或者说是一字节组成，容易忽视的是，文本每一行的末尾都有`\n`符号，其编码为`10`，或者是`00001010`。

> 中文的注释计算机将怎么处理？猜测可能有文件保存读取编码方式有关。

在linux环境下每一个C源文件都会被编译驱动(compiler driver)所编译为machine-language instructions 组成的可执行程序。

[![image-20200503124858005](http://static.come2rss.xyz/image-20200503124858005.png)](http://static.come2rss.xyz/image-20200503124858005.png)

[image-20200503124858005](http://static.come2rss.xyz/image-20200503124858005.png)



> Pre-processor：预处理器
>
> Assembler：汇编器
>
> Linker：链接器

`gcc -o hello hello.c` 运作四个步骤：Preprocessing phase将`#include<stdio.h>`的语句所标记的系统头文件stdio.h内容插入到程序文本中，并形成hello.i；Compilation phase:将hello.i翻译成assembly-language program(汇编程序)；

> 汇编语言作用之处在于给多种高层次语句的不同编译器提供同一个低层次的输出语言。

Assembly phase： 汇编器将汇编程序hello.s翻译成机器及的二进制relocatable object program(可重定位程序)。

> GCC是伟大的自由(free speach的自由)软件思想主导的运动GUN（GUN’s Not Unix, hh递归的）的产物，其功能强大，能够支持多种语言。同样的GUN产物还有GDB debugger，EMACS editor。

Linking phase：linker将预编译好的printf.o文件链接到可重定位文件hello.o形成了最终的可执行文件hello。

## 重视编译器的效率问题

作为现代工具的使用者，我们程序员无需重造一个编译器或者了解其中的构造，但是更有意义的是去了解如何编写代码才能让编译器翻译出更有效率的代码。书中提出了几个例子：`if-else`是否比`switch`更有效？`for`和`while`哪个效率更高？pointer referenes 是否比数组下标更快？为什么简单的重新放置算数表达式参数(arithmetic expression)可以提高效率？

## 处理器读取和接触存储在内存中的指令

commmand-line interpreter ——shell 可以接受指令并运行，如果输入的指令一个word不是built-in shell command，那么shell就会默认该字符为可执行文文件并load和执行,如`./hello`将执行可执行文件hello，shell会等待程序结束(terminate)，之后输出提示符(a prompt)。

## 系统硬件组织

[![image-20200503124915375](http://static.come2rss.xyz/image-20200503124915375.png)](http://static.come2rss.xyz/image-20200503124915375.png)

[image-20200503124915375](http://static.come2rss.xyz/image-20200503124915375.png)



> 一个Inter风格的硬件组织图

### 总线(Buses)

类似人体血管的贯通系统内部传输固定大小电子信息比特的管道(conduits)，通常这个大小的值不固定。

### I/O 设备(I/O Devices)

I/O设备是计算机系统负责接收发送给外部世界的设备，通过控制器(contrlllers)和适配器(adapter)连接到I/O总线。控制器和适配器的目的为了传输信息，但是控制器是由计算机原有的芯片控制的或者说是在母板(motherboard)上的电路印刷而成的，适配器是可以插入母板插槽的芯片卡。常见的外部设备有磁盘、显示器和鼠标键盘。

### 主存(Main Memory)

主存是系统在运行程序时的暂时存放数据和指令的空间。物理上，其一般有动态随机存储芯片(dynamic random access memory, DRAM)芯片组成。逻辑上说内存实际就是一个地址从零开始的线性字节数组。另外系统指令可由多个比特组成，数据项大小随数据类型不同而变化。

> 原句： In general, each of the machine instructions that constitute a program can **consist of** a variable number of bytes

### 处理器(Processor)

中央处理器(central processing unit)是计算机的心脏，负责解释(interpet)和执行(execute)从内存运送到CPU的IR(instrruction register)的指令。简单的说，CPU包括了其运算器部分（如ALU，寄存器等）和控制器部分（如PC，IR等等）。在CPU运行过程中，CPU解释PC指向的指令，根据指令执行操作并更新PC值。

简单来说，指令包括了Load、Store、Operate(数据运算)和Jump类。

## 运行hello程序

从硬件底层在理解一次刚刚的运行过程，在我们打入`./hello`命令指示，shell程序将键盘输入的字符通过寄存器和总线存储到内存中，当输入`Enter1`后shell开始执行shell程序。

> 有趣！

[![image-20200503124936718](http://static.come2rss.xyz/image-20200503124936718.png)](http://static.come2rss.xyz/image-20200503124936718.png)

[image-20200503124936718](http://static.come2rss.xyz/image-20200503124936718.png)



shell将原本存储在Disk中的代码和数据复制到内存中。系统借助了直接存储器存储器(direct memory access, DMA)而无需通过CPU传输数据直达主存。

[![image-20200503124954066](http://static.come2rss.xyz/image-20200503124954066.png)](http://static.come2rss.xyz/image-20200503124954066.png)

[image-20200503124954066](http://static.come2rss.xyz/image-20200503124954066.png)



最后，CPU运行hello程序，执行对应指令，并把数据`hello,world\n`复制到寄存器并打印到屏幕。

[![image-20200503125006147](http://static.come2rss.xyz/image-20200503125006147.png)](http://static.come2rss.xyz/image-20200503125006147.png)

[image-20200503125006147](http://static.come2rss.xyz/image-20200503125006147.png)



> 其中必然包括了中断技术。

## 高速缓存至关重要

从上文的例子看到程序运行过程中存在大量数据和指令移动，而现有的机械结构却造成了存储器速度和容量之间的取舍难题。往往速度快的存储器（比如寄存器）容量却很小，相反的容量大的存储器比如磁盘、光盘存储速度都很慢。为了解决这一难题，现在计算机配备了高速缓存(cache)，甚至是多级高速缓存。其运用了局部性原理(*locality*)。这对程序**性能**有着重要影响。

> *locality*:程序会倾向于使用局部区域的代码和数据

[![image-20200503125016708](http://static.come2rss.xyz/image-20200503125016708.png)](http://static.come2rss.xyz/image-20200503125016708.png)

[image-20200503125016708](http://static.come2rss.xyz/image-20200503125016708.png)



cache的加入让我们有一个更美妙的想法：存储器层次结构(memory hierarchy)，这种结构从上到下，速度逐渐变慢，价格变低，同时容量上升。更有趣的是，上层可以视为相邻下层的缓存，相邻下层可以视为上层的存储，比如分布式系统中的本地磁盘就是远程存储系统的缓存。

## 操作系统管理硬件

hello程序运行中时，外部数据的输入和打印屏幕这些操作硬件的举动都不是源程序或者shell所做的，都是使用了操作系统所提供的接口。操作系统是计算机硬件和应用软件之间的管理层，一方面负责保护硬件不直接受到应用软件的操作，另一方面提供给所有应用软件统一且简单的接口。

[![image-20200503125027579](file:///D:/Blogfile/pic/CSAPP%E9%98%85%E8%AF%BB%E7%AC%94%E8%AE%B0/image-20200503125027579.png)](file:///D:/Blogfile/pic/CSAPP阅读笔记/image-20200503125027579.png)

[image-20200503125027579](file:///D:/Blogfile/pic/CSAPP阅读笔记/image-20200503125027579.png)



操作系统通过几个抽象的功能来实现对计算机资源的管理，如下图。

> 确实抽象，Processes本身带着运行程序的位置信息、进程信息和源程序信息，也就是说Processes是对三者的管理。其他类似

[![image-20200503125035839](http://static.come2rss.xyz/image-20200503125035839.png)](http://static.come2rss.xyz/image-20200503125035839.png)

[image-20200503125035839](http://static.come2rss.xyz/image-20200503125035839.png)



### 进程(Processes)

即使是单核处理器(*uniprocessor*)计算机也可以同时（宏观）运行多个进程，操作系统在记录并控制了所有进程的上下文(*content*)。操作系统通过保存当前的进程上下文，并载入一个新进程的上下文可以实现进程切换。

[![image-20200503125045850](http://static.come2rss.xyz/image-20200503125045850.png)](http://static.come2rss.xyz/image-20200503125045850.png)

[image-20200503125045850](http://static.come2rss.xyz/image-20200503125045850.png)



一个正在运行的进程可以通过系统调用来调用操作系统的功能，比如读写磁盘，执行另一个程序创建新进程。

### 线程(Threads)

线程作为“轻量级”的进程，能快速访问同进程下的共享资源，占有更少的内存空间，运行效率更高，可以充分利用多核计算机的计算效能。

### 虚拟内存（Virutual Memory）

顾名思义，虚拟内存是操作系统在内存的基础上虚拟空间。对于软件来说虚拟内存唯一可以接触到的空间，物理内存对他们是透明的。

[![image-20200503125120329](http://static.come2rss.xyz/image-20200503125120329.png)](http://static.come2rss.xyz/image-20200503125120329.png)

[image-20200503125120329](http://static.come2rss.xyz/image-20200503125120329.png)



从低地址到高地址所存放的内容分别是：

- 程序的代码和数据
- 读写数据
- 堆(heap)：可以由进程通过程序malloca，new动态创建
- 分享库(shared libraries)：比如C++的`math`库
- 栈：在用户调用函数增长，返回函数时减小，
- 内核虚拟内存：保留给内核程序的空间。用户应用程序无法读取这部分内容，也无法直接掉调用。

### 文件(Files)

至少在Unix I/O上，file系统将各式的外设输入输出设备、甚至网络建模成一个文件。统一的文件形式给系统操作员极大的方便。

> linux: a complex, Posix-compliant version of the Unix operating system.
>
> posix，Portable Operating System Interface X——可移植操作系统接口

## 网络：计算机与其他系统的沟通桥梁

> 讲的太粗略，不计

## 重要主题

> This **concludes our initial whirlwind tour** of systems. An important idea to take away from this discussion is that a system is more than just hardware. It is a collection of intertwined hardware and systems software that must cooperate in order to achieve the ultimate goal of running application programs.

### Amdahl’s Law

Amdahl’s Law假设简单系统的各个部件线性工作，提升一个部件的效率其实对整齐来说提升并不明显。

[![image-20200503125132267](http://static.come2rss.xyz/image-20200503125132267.png)](http://static.come2rss.xyz/image-20200503125132267.png)

[image-20200503125132267](http://static.come2rss.xyz/image-20200503125132267.png)



### 并发(Concurrency)和并行(Parallelism)

并发是对计算机同时运行多个事件的广义概念。并行是指？？？

在分时(time-sharing)操作系统上，所谓的并发仅仅只是一种模拟(simulated)，通过不断的切换进程（在进程(Process-Level Concurrency)级别上 ）让电脑同时相应多个用户的操作。而在线程级别(Threa-Level)上，即时在单核对一个单一的进程也有执行的多重控制流。

随着由多个有单独的操作系统内核管理的单个处理器组成的多核处理器(multiple processors)的到来，多核操作系统诞生了，随之而来的是超线程(hyperthreading)！

[![image-20200503125144846](http://static.come2rss.xyz/image-20200503125144846.png)](http://static.come2rss.xyz/image-20200503125144846.png)

[image-20200503125144846](http://static.come2rss.xyz/image-20200503125144846.png)



[![image-20200503125157325](http://static.come2rss.xyz/image-20200503125157325.png)](http://static.come2rss.xyz/image-20200503125157325.png)

[image-20200503125157325](http://static.come2rss.xyz/image-20200503125157325.png)



超线程（也称为*sinultaneous multi-threading*）是一种允许一个核同时执行的多个控制流，涉及了部分硬件的多分设计，比如PC(program countes)，寄存器文件，而其余硬件只设一份，比如浮点数计算。可以说，在并发概念提出50年的铺垫后，多核处理器和超线程的出现才引爆了对多线程编程应用和并行的极大热情。（Eng. P55）

指令级并行通过多核处理的**多核处理**能力，以及**现代流水线架构**来实现。

单指令多数据(*SIMD，single-instruction, multile-data*)并行是通过特殊硬件允许一条指令同时进行多重操作。常常用于处理图像、声音等数据。

### 抽象(abstraction)的重要性

> 计算机最重要的两个概念——抽象和局部性原理

抽象在计算机领域无处不在，提供给调用者的统一的函数接口API(Application program inteface)是函数的抽象，文件本身就是输出输入设备和物理数据的抽象，虚拟内存是内存和文件的抽象，进程是指令和数据的抽象，而计算机本身也是一个运行在硬件上的虚拟机(可见开头图)

> 终于读完了一个综述，开心 :heart: :happy::happy::happy:~~于2020.04.27.10:17