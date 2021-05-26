---
title: Coroutine协程简记
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-10-08 13:35:04
---
Coroutine，即协程。虽然名字很像线程进程，但是协程与前两者的相似之处很少。协程，顾名思义为协作合作的多任务程序。

<!-- more -->

# A Simple Overview of Coroutine

### Definition

Wiki百科的定义比较广泛，但是它提出了协程的三个重要特征：

> Coroutines（协程） are computer program components that generalize subroutines for non-preemptive multitasking, by allowing execution to be suspended and resumed. 

+ 运行子程序
+ 完成协作性质任务
+ 运行时可暂停和重新唤醒

这三点已经可以概括了协程的面貌了，为了更深入了解协程的特点，我们可以从其他相似概念，最后从python的`asycio`入手了解协程。

### Analogy

#### Comparison with subroutines

subroutine看似高大上，与routine有着密不可分的关系，就其定义来说就是一个`A set of instructions that performs a specific task for a main routine`，也可以称之为`function`，`procedure`。

子程序是协程的特例，子程序从开头执行到末尾就结束了，仅仅返回一个值而且不保存状态，但是协程不同，它的“结束形式”是调用另一个协程的，同时其内部变量依旧保存，在下次被调用时仍然可以使用。值得注意的，被调用的`coroutine`仍可以调用调用它的`coroutine`，从这个角度说，不似与一般调用方法的`caller-callee`关系，`coroutine`的关系是`symmetric`的。

#### Comparison with threads:

协程与线程很相似，但是协程是合作性质的多任务，而线程是典型的抢占式多任务性质的。

协程是典型的`concurrency`（并发）性质的程序，而非`parallelism`（并发）性质的程序。也就是说协程仅仅创建了一个线程或者说一个进程。

> `parallism`是`concurrency`的真子集。
>
> BTW, `threading`（多线程化）是`concurrency`的一种实现手段，`multprocessing` （多处理器运行）是`paralism`的一种实现手段。
>
> 四者的关系如图：
>
> [![Concurrency versus parallelism](http://static.come2rss.xyz/muiltclip_image001.jpg)](https://files.realpython.com/media/Screen_Shot_2018-10-17_at_3.18.44_PM.c02792872031.jpg)

协程无需进行线程切换的优势让它性能优势远超多线程进程，更加适合`hard-time realtime context`， GO语言的火爆也得力于此。

多线程的缺点在于线程切换涉及到系统调用和调用阻塞，大大减慢了速度；多线程的同步竞争问题也需要信号量和同步锁维护。

#### Comparison with generators:

生成器也称之为半协程，是协程的一个子集。熟知的语言如C++、python都实现了`generator`的机制，可以看出`generator`基本符合协程的三个特征。但是对于`generator`来说，`sysmmetric`还是不太够。

其次，`genenrator`的`yield`关键词定义了`generator`退出和重新执行的`entry`，同上面所述，`generator`并没有主动`yield`(割让控制权)和重新执行的权利，他更像被动生产者，把控制权交给调用`generator`的`caller`。而`coroutie`可以在`yield`之后突然夺回控制权，

#### Comparison with mutual recursion：

 讨论到，控制权在不同`subroutine`之间相互交换的情况，相互调用的函数可以类比`coroutine`。但是有明显的不同，就如一开始`Definition`所说，`coroutine`可以保存状态，变量和`execution point`，而且能`resume execution from execution point` 而不是从头执行。

另外, `mutual recursion`调用的对方函数后，会增加系统函数栈的层数(`stack frame`)。而`coroutine`在传递控制权的时候，可以使用已经存在的`context`，并且仅仅只用一个`jump`来完成。

> 具体实现未曾探究。



## Coroutines in `asyncio`

`asyncio`是python的内置系异步包，其API在3.4~3.7中快速迭代，如果幸运的话，以后可能会稳定下来。

> 更多异步包可以用`pip install --upgrade pip aiohttp aiofiles`安装即可。

`asyncio`就是`Asynchrnous IO`缩写。众所周知，`cpu-bound`(所谓劳动密集型任😂)更需要多线程多处理器完成，`IO-bound`型任务需要多个线程来处理IO堵塞，或者由强大的😈协程完成。重复一遍，`coroutine`编程仅仅是一个单一线程单一进程的风格，他并不是`parallelism`，而是`concurrent`。更详细的说：

+ 异步`coroutine`在等待一个任务完成之时可以，可以停止执行，让其他`coroutines`执行。这个性质非常想进程同步所说的让权等待。

为了支持异步处理，python引入了两个新key words: `async` and `awati`。前者定义异步函数，后者声明可以让权的语句。比如下面这个小程序：

```python 
import asyncio

async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")

async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")

```

三个异步执行的`count()`会在各自阻塞的时候让权给其他`count()`。可以想到，这个程序执行时间大概在1秒，而非同步执行的3秒。



## END

> 接下的内容由于，个人水平和时间都有限，虽然做了更多的学习，但还是打算不发出来误人子弟了。



