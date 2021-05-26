---
title: python字符编码简记
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
  - 总结
categories:
date: 2020-10-10 12:05:48
---




## python字符集编码简记

不讨论python2的情况下，python3将string分为两种类型，一种是`str`,另一种是`bytes`。前者存储unicode编码的字符串，负责存储unicode code point，后者负责按bytes存储字符串，也是就ACSII编码的code point存储。

<!-- more -->

`str.encode()`默认把str的unicode code point翻译成bytes编码。

`bytes.decode()`默认把bytes的byte code point翻译成utf-8编码。

![image-20201010115840274](http://static.come2rss.xyz/image-20201010115840274.png)

举个例子：

![image-20201010115856720](http://static.come2rss.xyz/image-20201010115856720.png)

### 特性

两者不等价不可运算。

### 文件



经典的文件字符处理方式是使用The unicode sandwich模型，模型通过接受外部字符并decode解码成unicode,最后str通过encode编码为bype。这就保证了程序内部的字符集的统一，但是外部文件的编码方式难以确定。如果使用错误的编码方式去解码，就是出现明显的乱码`Mojibake`。

![image-20201010115937641](http://static.come2rss.xyz/image-20201010115937641.png)



python3的`flie.read(textname, read_mode)`选定了特定解码编码方式，如下图：`encoding=locale.getgpreferredencoding()`作为默认解码方式。

![Reading files](http://static.come2rss.xyz/032.png)