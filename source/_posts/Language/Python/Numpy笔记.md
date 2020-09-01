---
title: Numpy笔记
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
categories:
  - Language
  - Python
date: 2020-08-07 13:08:45
tags:
---





## 基础概念

## axis

常常用于指定函数的计算方式，如sum(x,axis=0)会得到一个row array,而不是按行计算的column array。

<!-- more -->

[![image-20200503125336529](http://static.come2rss.xyz/image-20200503125336529.png)](http://static.come2rss.xyz/image-20200503125336529.png)

[image-20200503125336529](http://static.come2rss.xyz/image-20200503125336529.png)





## 乘法

首先

| 矩阵乘法            | 符号 | 说明                             | Np                          |
| :------------------ | :--- | :------------------------------- | :-------------------------- |
| `matmul`            | .    | 矩阵乘法                         | np.dot(M1,M2)               |
| `Hadamard product`  | ⊙⊙   | element-wise乘法，逐元素对应相乘 | np.multiply(M1,M2)或者M1*M2 |
| `Kronecker product` | ⊗⊗   | 任意形状矩阵相乘                 | ?                           |

不太明朗的第三个乘法举例：

[![image-20200503125443492](http://static.come2rss.xyz/image-20200503125443492.png)](http://static.come2rss.xyz/image-20200503125443492.png)

[image-20200503125443492](http://static.come2rss.xyz/image-20200503125443492.png)



| 向量乘法                      | 符号 | 说明                     | Np                  |
| :---------------------------- | :--- | :----------------------- | :------------------ |
| `Inner Product`,`dot product` | ..   | 运算结果为标量(A scalar) | np.dot(L1,L2)       |
| `outer product`               | ⊗⊗   | 结果是矩阵               | np.outer(a1,a2)或者 |
| `cross product`               | ××   | 结果是向量               | ?                   |

> 上两表中‘Li’表示**列表**，‘Mi’表示矩阵，‘Ai’表示向量Array
>
> 上表中 `np.multiple`以及`np.outer`都可以接受矩阵（nArray）、向量（nArray)以及列表（LIST），唯有`np.dot`在接受nArray是表现为矩阵乘法，在接受LIST表现为向量内积。

`dot product`，即点积或者内积。

[![image-20200503125432138](http://static.come2rss.xyz/image-20200503125432138.png)](http://static.come2rss.xyz/image-20200503125432138.png)

[image-20200503125432138](http://static.come2rss.xyz/image-20200503125432138.png)



点乘的几何意义：点乘可以用来计算两个向量的夹角

[![image-20200503125425021](http://static.come2rss.xyz/image-20200503125425021.png)](http://static.come2rss.xyz/image-20200503125425021.png)

[image-20200503125425021](http://static.come2rss.xyz/image-20200503125425021.png)



`Outer production`或``，即外积，在线性代数中一般指两个向量的张量积，结果为一个矩阵。可调用`np.outer(x1,x2)`。例子如下：

[![image-20200503125416187](http://static.come2rss.xyz/image-20200503125416187.png)](http://static.come2rss.xyz/image-20200503125416187.png)

[image-20200503125416187](http://static.come2rss.xyz/image-20200503125416187.png)



向量叉积(`Cross product`)：叉乘的结果是一个**向量**，使用符号 [![[公式\]](http://blog.come2rss.xyz/2020/04/26/language/python/Numpy%E7%AC%94%E8%AE%B0/Numpy%E7%AC%94%E8%AE%B0/equation-1581420237739.svg)](http://blog.come2rss.xyz/2020/04/26/language/python/Numpy笔记/Numpy笔记/equation-1581420237739.svg)

[[公式\]](http://blog.come2rss.xyz/2020/04/26/language/python/Numpy笔记/Numpy笔记/equation-1581420237739.svg)

，举例



[![image-20200503125406301](http://static.come2rss.xyz/image-20200503125406301.png)](http://static.come2rss.xyz/image-20200503125406301.png)

[image-20200503125406301](http://static.come2rss.xyz/image-20200503125406301.png)



### 索引

对于一个多维Array,使用单一的数组索引会产生一定意义上的语义模糊。如果索引单个元素，就要写上所有维度的索引。比如

```
c = np.zeors((1,3))
print(c[0,1]) #两个维度
```



# 常用函数

```
np.exp()
```

`np.square()` return the element-wise square of the input.

```
np.sum(a, axis=None, dtype=None, out=None, keepdims=<no value>, initial=<no value>, where=<no value>)
```

> **axis** : None or int or tuple of ints, optional
>
> **Axis or axes along which a sum is performed**. The default, **axis=None**, will sum all of the elements of the input array. If axis is negative it counts from the last to the first axis.
>
> If axis is a tuple of ints, a sum is performed on all of the axes specified in the tuple instead of a single axis or all the axes as before.

```
np.random.randn(a,n）`(‘np.’以下全省略）
`.array(LIST)` 新建一个numpy array。
`.exp()
.reshape()` 类似`array.reshape
```

`.dot(X1,X2)` 矩阵乘法

`.zeros(shape, dtype=float, order='C')` Return a new array of given shape and type, filled with zeros.

> shape: int or tuple of ints
>
>  Shape of the new array, e.g., `(2, 3)` or `2`

`.squeeze()` Remove single-dimensional（单维度条目，即shape=1的条目） entries from the shape of an array.

[![image-20200212162003524](http://blog.come2rss.xyz/2020/04/26/language/python/Numpy%E7%AC%94%E8%AE%B0/Numpy%E7%AC%94%E8%AE%B0/image-20200212162003524.png)](http://blog.come2rss.xyz/2020/04/26/language/python/Numpy笔记/Numpy笔记/image-20200212162003524.png)

[image-20200212162003524](http://blog.come2rss.xyz/2020/04/26/language/python/Numpy笔记/Numpy笔记/image-20200212162003524.png)



`.divide(x1,x2）` returna true division of the input, elelment-wise.

`.copy(a, order='K')` Return an array copy of the given object.(真复制)

`.linspace(start,stop,num=50)` Return evenly spaced numbers over a specified interval. `num` 表示产生的列表的数字个数。

`np.random.shuffle(x)`, 把x本身shuffle一下，注意不返回值。

```
.savetxt('new.csv', my_matrix, delimiter = ',')
```

将数组或者矩阵存储为csv文件

# Array用法

`Array.reshap()`（以下省略`array`）

```
.reshape()
```

`.shape[i]` 访问shape元祖中的第i个数。

## 新建

**np.array(list/tuple)**

```
np.ndarray()
```

`shape`：数组的形状。

`dtype`：数据类型。

`buffer`：对象暴露缓冲区接口。

`offset`：数组数据的偏移量。

`strides`：数据步长。

`order`：`{'C'，'F'}`，以行或列为主排列顺序。

## 初始化

可以使用array对list，或者DF进行初始化。

> 稍稍注意一下， python中的`(3)`是一个INT对象，而`（3，）`是一个tuple对象

In [12]:

```
print(a.shape)
(1, 3)
```

In [13]:

```
a = np.array([1, 2, 3])
print(a.shape)
(3,)
```

In [17]:

```
a = np.array([[1], [2], [3]])
print(a.shape)

(3, 1)
```

In [19]:

```
a = np.array([1,2,3], ndmin =  2)
print(a.shape)
(1, 3)
```

In [22]:

```
a = np.array([1, 2, 3], ndmin = 1)
print(a.shape)
(3,)
```

# 库

## np.linalg

linalg = linear + algebra

`np.linalg.inv()` 矩阵求逆
`np.linalg.det()`矩阵求行列式（标量

`np.linalg.norm` 求范数；

> norm(x, ord=None, axis=None, keepdims=False)
>
> ord表示范数种类
>
> axis: If *axis* is an integer, it specifies **the axis of \*x\*** along which to compute the vector norms.
>
> keepdims: If this is set to True, the axes which are normed over are left in the result as dimensions with size one.(好像是保留大小为1的维度)

Note: 标准化可使用norm，xnormalized=x∥xnorm∥xnormalized=x‖xnorm‖

## np.random

`numpy.random.normal(loc=0.0, scale=1.0, size=None)` Draw random samples from a normal (Gaussian) distribution. `loc` : the meanof the distribution. `scale` Standard deviation (`width`) of the distribution. `size` a int or tuple of ints, optional. If size is none, single value is returned if `loc` and `scale` are both scalars. (也就说 loc 和 scale 支持 array-like 参数)

### numpy的优点

在numpy中矩阵、向量和数值都是numpy array, 不管他是啥。

numpy可以轻松的进行numpy array和数值之间的+-*/甚至np.exp()的高级运算，而list不行。

**其他：**

np.dot(X1, X2)为矩阵乘法

np.sum（x1, axis）为求和, axis = 0 为竖直方向求和，axis=1为水平方向，默认竖直方向

X1.T表示X1的转置

c = np.dot(a,b) #dot是矩阵乘法 *是element-wise product

# 有用的操作

nArray中的True/Flase转化为1/0.

```
C = [0.5, 0.6, 0.1]
c = np.array(C) > 0.5
print(c)
print(c + 0)
```

## 数据筛选

`Df.fillna(value, inplace)` 把NaN数据替换成value。

`Na[~np.isnan(Na)]` 可以通过判判断条件选择数据

`[x+1 for x in list if x < 5]` list可以以列表表达式来生成新列。

## **增加数据维度**

numpy中包含的newaxis可以给原数组增加一个维度

np.newaxis放的位置不同，产生的新数组也不同

一维数组

```
x = np.random.randint(1, 8, size=5)

x
Out[48]: array([4, 6, 6, 6, 5])

x1 = x[np.newaxis, :]

x1
Out[50]: array([[4, 6, 6, 6, 5]])

x2 = x[:, np.newaxis]

x2
Out[52]: 
array([[4],
       [6],
       [6],
       [6],
       [5]])
```