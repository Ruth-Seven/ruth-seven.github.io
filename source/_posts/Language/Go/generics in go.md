---
layout: generic
title: go
date: 2021-07-30 09:08:21
tags:
---







# go generics came here!

在 go1.17 beta 已经实现了go 泛型，虽然它现实在一个不稳定的版本，我已经心心念了好久了，毕竟不是每个人都喜欢自己写一遍各种类型的`Min`   。

<!--more-->



从 C++起手的老司机应该都忘不了模板的恐怖和复杂之处，作为异常鄙视 C++的 go，一开始并没有急着推出泛型。然而广大人民群众的呼声还是得到了 go 开发者的响应，go 泛型的开发逐步提上日常，测试版本在 1.17 release开放（预计在 2021August），稳定的实现会在 go2 登场！

但知其然必须知其所以然，为什么我们需要泛型？go 机制中的接口编程不够满足功能吗？go 又能带给我们怎样的编程体验？我们又能 怎么使用 go 呢？这是我们需要考虑的点。

## Interfaces and genercs

接口编程作为go 鸭子类型的核心特色，不与类型强制绑定，实现了在静态类型中的动态类型，本质是一种泛型编程的体现。但很明显的，接口编程同时也存在着不少缺点：

- ~~动态检查失去了静态类型的速度~~
- 需要类型显式地把类型特点以方法的形式表征出来，尤其是把 bulit-in 类型重命名类型，再抽象出公共方法
- 难以表现类型之间的组合关系

举一个🌰：经典 `go sort`包使用

```go
package main

import (
 "fmt"
 "sort"
)

type Person struct {
 Name string
 Age  int
}

func (p Person) String() string {
 return fmt.Sprintf("%s: %d", p.Name, p.Age)
}
type ByAge []Person

func (a ByAge) Len() int           { return len(a) }
func (a ByAge) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }
func (a ByAge) Less(i, j int) bool { return a[i].Age < a[j].Age }

func main() {
 people := []Person{
  {"Bob", 31},
  {"John", 42},
  {"Michael", 17},
  {"Jenny", 26},
 }

 fmt.Println(people)
 sort.Sort(ByAge(people))
 fmt.Println(people)

 sort.Slice(people, func(i, j int) bool {
  return people[i].Age > people[j].Age
 })
 fmt.Println(people)

}

```

为了排序`slice of people`不得不定义一个`byage`slice同时声明匹配的方法。这里接口编程体现他的强大，接口类型再套一个接口可以现实`adaper`模式，增加扩展性。但同时，可以窥见，任何一个基础类型的排序都需要重新实现一遍上面的接口，当然标准库也是这么实现的。

> 悄咪咪看了下1.17，sort 并没有改动，这就叫向后兼容啊！

熟悉 C++的朋友，都知道用 C++使用模板实现了排序模板算法，对自定义数据集通过重载运算符来获取`<` 关系。那 go 如果用模板会怎么处理？



## What go can bring to go？

go 的设计者对 go的 泛型要求很高：

- 简单清晰易懂。
- 把对泛型使用的复杂度交给设计代码者，使用代码的用户是感受不到泛型代码带来的差异。这一点，和 C++的模板方法类似，C++模板方法会进行类型推导，但是 C++的模板类是需要强制选取类型的。
- 使用泛型可以设计出丰富的`generic datastruct`。 虽然我们内置的`sclice`和`map`也是泛型的，但内部实现原理不同。
- 用静态类型`genenric data`取代一部分接口



## Draft design

泛型编程重要是对可选类型做出一个约束，比如说大家都有同一个方法，同一个属性，同一个可执行的“动作”，比如赋值。

比如：

```go
// Element 必须可赋值
func Reverse (type Element) (s []Element) {
    first := 0
    last := len(s) - 1
    for first < last {
        s[first], s[last] = s[last], s[first]
        first++
        last--
    }
}


```

go 语法规定`contract`可以说明 类型的上述“特点”

```go
contract Sequence(T) { // 规定可选类型
    T string, []byte
}
 
func Min (type T Ordered) (a, b T) T {  // Ordered（明示元素可用`<`比较） 是预定的contract
    if a < b {
        return a
    }
    return b
}
 

contract Stringer(T) { // 规定方法
    T String() string
}
func ToStrings (type E Stringer) (s []E) []string {
    r := make([]string, len(s))
    for i, v := range s {
        r[i] = v.String()
    }
    return r
}
 
contract G(Node, Edge) { // 规定类型组合关系
    Node Edges() []Edge
    Edge Nodes() (from Node, to Node)
}
func New (type Node, Edge G) (nodes []Node) *Graph(Node, Edge) {
    ...
}

func (g *Graph(Node, Edge)) ShortestPath(from, to Node) []Edge {
    ...
}
```

对于类泛型编程

```go
type Tree (type E) struct {
    root    *node(E)
    compare func(E, E) int
}

type node (type E) struct {
    val         E
    left, right *node(E)
}

func New (type E) (cmp func(E, E) int) *Tree(E) {
    return &Tree(E){compare: cmp}
}


func (t *Tree(E)) find(v E) **node(E) {
    pn := &t.root
    for *pn != nil {
        switch cmp := t.compare(v, (*pn).val); {
        case cmp < 0:
            pn = &(*pn).left
        case cmp > 0:
            pn = &(*pn).right
        default:
            return pn
        }
    }
    return pn
}


func (t *Tree(E)) Contains(v E) bool {
    return *t.find(e) != nil
}
 
func (t *Tree(E)) Insert(v E) bool {
    pn := t.find(v)
    if *pn != nil {
        return false
    }
    *pn = &node(E){val: v}
    return true
}

```

对应的用户编程，与非泛型编程无异：

```go
var intTree = tree.New(func(a, b int) int { return a - b })

func InsertAndCheck(v int) {
    intTree.Insert(v)
    if !intTree.Contains(v) {
        log.Fatalf("%d not found after insertion", v)
    }
}

```

## Conclusion

遗憾的是，已经将至 2021.8，go generic 还是没有released。我没有进行更多深入了解了。

## reference

[Why generic?](https://blog.golang.org/why-generics)

[Generics in Go](https://bitfieldconsulting.com/golang/generics)

[Generics in Go Explained with Code Examples](https://www.freecodecamp.org/news/generics-in-golang/)

[Contracts — Draft Design](https://github.com/golang/proposal/blob/master/design/go2draft-contracts.md)

