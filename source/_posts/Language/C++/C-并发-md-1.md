---
title: C++并发
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
date: 2021-03-14 16:01:34
tags:
categories:
---





# C++并发





`volatile`类型修饰符，用它声明的类型变量表示可以被某些编译器未知的因素更改，比如：操作系统、硬件或者其它线程等。遇到这个关键字声明的变量，编译器对访问该变量的代码就不再进行优化，从而可以提供对特殊地址的稳定访问。



<!-- more -->

`volatile int i=10;`。

当要求使用 volatile 声明的变量的值的时候，系统总是重新从它所在的内存读取数据，即使它前面的指令刚刚从该处读取过数据。而且读取的数据立刻被保存。

总之，`volatile`保证的是变量的可见性。











## 经典并发问题



### `i++`安全吗



`i++`不是原子操作，也就是说，它不是单独一条指令，而是3条指令(3条汇编指令)：

1、从内存中把i的值取出来放到CPU的寄存器中

2、CPU寄存器的值+1

3、把CPU寄存器的值写回内存

由于线程共享栈区，不共享堆区和全局区，所以当且仅当 i 位于栈上是安全的，反之不安全(`++i`也同理).   因为如果是全局变量的话，同一进程中的不同线程都有可能访问到。对于读值，`+1`，写值这三步操作，在这三步任何之间都可能会有CPU调度产生，造成i的值被修改，造成脏读脏写。

`volatile`不能解决这个线程安全问题。因为`volatile`只能保证可见性，不能保证原子性。





# 协程



`python3.7`支持了协程异步编程：

```python
import asyncio
async def display(num):
    await asyncio.sleep(1)
    print(num)
```

异步函数不同于普通函数，调用普通函数会得到返回值，而调用异步函数会得到一个协程对象。我们需要将协程对象放到一个事件循环中才能达到与其他协程对象协作的效果，因为事件循环会负责处理子程序切换的操作，简单的说就是让阻塞的子程序让出CPU给可以执行的子程序。

通过下面的代码可以获取事件循环并将协程对象放入事件循环中。

```python
coroutines = [display(num) for num in range(10)] # 协程对象集
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(coroutines))
loop.close()

```