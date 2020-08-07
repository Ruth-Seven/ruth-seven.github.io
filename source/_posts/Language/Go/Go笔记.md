---
title: Go笔记
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
categories:
  - Language
  - Go
date: 2020-08-07 13:15:47
tags:
---


<!-- more -->

# go学习

> 在一个悲伤的日子打开一个特殊语言的入门学习之路。

Go is expressive, concise, clean, and efficient. Its **concurrency mechanisms** make it easy to write programs that get the most out of multicore and networked machines, while its **novel type** system enables flexible and modular program construction. Go compiles quickly to machine code yet has the convenience of **garbage collection** and the power of **run-time reflection.** It’s a fast, **statically typed**, compiled language that feels like a dynamically typed, interpreted language.

## 安装



去该[页面](https://golang.org/doc/install)寻找安装包入口，安装后把路径加入环境变量。

```
export PATH=$PATH:/usr/local/go/bin
```

## tour

```
package main

import (
	"fmt"
	"time"
)

func main() {
	fmt.Println("Welcome to the playground!")
	fmt.Println("The time is", time.Now())
}
```

### 导入包

有两种方式，一是：

```
import (
	"fmt"
	"math/rand"
)
```

抑或：

```
import "fmt"
import "math"
```

### Exported names

go中包中Capital Word开头的变量都是Exported names，Exported names顾名思义就是可以被暴露给调用者的。应对的Unexported names都是对于调用包的都是unaccessible。

```
package main
/
import (
	"fmt"
	"math/rand"
)

func main() {
	fmt.Println("My favorite number is", rand.Intn(10))
}
```