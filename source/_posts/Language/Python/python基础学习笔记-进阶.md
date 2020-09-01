---
title: python基础学习笔记-进阶
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
categories:
  - Language
  - Python
date: 2020-08-07 13:12:46
tags:
---





# 速记

## list

`ls`表示一个list函数。

<!-- more -->

`ls.pop(i)` 删除指定下标的内容。（可以用来删除str内容）

```
list_str = list(string)
list_str.pop(1)
#join 可以合并一整个list！
list_str = ''.join(list_str)
```



## dict

`dict.has_key('name')` 若有此键，则返回True，否则返回False。

> 同样的，也可以使用in判断，`print ‘name’ in d.keys()`

## STR函数

`str`表示一个字符串对象。

`str.upper()` 返回一个大写字母的字符串。

`str.atoi()` 别python删掉了

`str.join(str2)`返回两个字符串连接的新字符串 #join 可以合并一整个list！

`str.replace(old, new[, max])` **返回**把str中的old换成new的字符串。在（最多换max次）

> 也可以使用正则表示式中的sub来替换符合正则表达式的子串。
>
> ```
> re.sub(pattern, repl, string, count=0, flags=0)
> ```
>
> repl: 为新字符串
>
> string：为原字符串

`str.strip(str)` 删除头尾指定字符 。参数为空时，默认去除ss字符串中头尾\r, \t, \n, 空格等字符。 `ss.lstrip()`删除ss字符串开头处的指定字符，`ss.rstrip()`删除ss结尾处的指定字符。

## 迭代器和生成器

`Zip(x,y)` 返回一个将两个迭代器或者list，tuple啥的一一对应的组合成新样本的迭代器，其内容长度为最短的一个。

```
>>>c = [1, 3, 4 ]
>>>b = [4, 3 ,2] 
>>>Zip = zip(c,b)
>>>Zip
<zip at 0x1fb0cd1f248>
>>>for x, y in Zip:
>>>print(x, y)
1 4
3 3
4 2
```

利用 *** 号操作符**，可以将二维数据重组为形式等价于转置的数据。

这个[题目](https://leetcode-cn.com/problems/lucky-numbers-in-a-matrix/solution/)就使用了该技巧

```
>>>a = [1,2,3]
>>> b = [4,5,6]
>>> c = [4,5,6,7,8]
>>> zipped = zip(a,b)     # 打包为元组的列表
[(1, 4), (2, 5), (3, 6)]
>>> zip(a,c)              # 元素个数与最短的列表一致
[(1, 4), (2, 5), (3, 6)]
>>> zip(*zipped)          # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
[(1, 2, 3), (4, 5, 6)]
```

`enumerate(thing)` 注意他返回的是一个迭代器

enumerate(thing)`, where thing is either an iterator or a sequence, returns a iterator that will return`(0, thing[0])`,`(1, thing[1])`,`(2, thing[2])`, and so forth.

# for

`enumerate` 可在迭代中得到遍历值和下标`for inx, val in enumerate(['uyy', 'dfdf']):`。

## 类型转化

`list(), str(), float(),int()` 比比皆是。

注意Python没有`char`类型，str字符串也不能和数字相减。

`isinstance(instance, Object)` 判断一个实例是否是一个对象是否是该类型本身，或者位于该类型的父继承链上。

```
>>> isinstance('a', str)
True
>>> isinstance(123, int)
True
>>> isinstance(b'a', bytes)
True
```

`type()` 判断对象的类型，也可判断其他情况如是否是函数、lambda表示式等等。可参见`types`自定义的常量。

```
>>> import types
>>> def fn():
...     pass
...
>>> type(fn)==types.FunctionType
True
>>> type(abs)==types.BuiltinFunctionType
True
>>> type(lambda x: x)==types.LambdaType
True
>>> type((x for x in range(10)))==types.GeneratorType
True
```

`dir()` 如果要获得一个对象的所有属性和方法，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：

```
>>> dir('ABC')
['__add__', '__class__',..., '__subclasshook__', 'capitalize', 'casefold',..., 'zfill']
```

类似`__xxx__`的属性和方法在Python中都是有特殊用途的，比如`__len__`方法返回长度。在Python中，如果你调用`len()`函数试图获取一个对象的长度，实际上，在`len()`函数内部，它自动去调用该对象的`__len__()`方法，所以，下面的代码是等价的：

```
>>> len('ABC')
3
>>> 'ABC'.__len__()
3
```

`getattr()`、`setattr()`以及`hasattr()` 获取属性、设置属性、是否拥有属性。

```
>>> setattr(obj, 'y', 19) # 设置一个属性'y'
>>> hasattr(obj, 'y') # 有属性'y'吗？
True
>>> getattr(obj, 'y') # 获取属性'y'
19
>>> obj.y # 获取属性'y'
19
```

如果试图获取不存在的属性，会抛出AttributeError的错误。

可以传入一个default参数，如果属性不存在，就返回默认值：

```
>>> getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404
404
```

获取对象的方法！

也可以获得对象的方法：

```
>>> hasattr(obj, 'power') # 有属性'power'吗？
True
>>> getattr(obj, 'power') # 获取属性'power'
<bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
>>> fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
>>> fn # fn指向obj.power
<bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
>>> fn() # 调用fn()与调用obj.power()是一样的
81
def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None
```

假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，如果存在，则该对象是一个流，如果不存在，则无法读取。`hasattr()`就派上了用场。

请注意，在Python这类动态语言中，根据鸭子类型，有`read()`方法，不代表该fp对象就是一个文件流，它也可能是网络流，也可能是内存中的一个字节流，但只要`read()`方法返回的是有效的图像数据，就不影响读取图像的功能。

# 奇妙的编程

## 去重并建立索引

```
#使用set 取出corpus_chars 中唯一不重复的部分。
idx_to_char = list(set(corpus_chars))
# 对唯一的数据生成键值对的tuple，并转化为dict
char_to_idx = dict([(char, i) for i, char in enumerate(idx_to_char)])
```

## Max和Lambda

max 函数是 Python 的内置函数

max 有一个 key 参数，指定如何进行值得比较。

下面案例，求出现频次最多的元素：

```
In [13]: def mode(lst):
             if lst is None or len(lst)==0: 
                return None
    ...:     return max(lst, key=lambda v: lst.count(v))
```

出镜最多的元素有多个时，按照以上方法，默认只返回一个。

下面，支持返回多个：

```
In [34]: def mode(lst):
    ...:     if lst is None or len(lst)==0:
    ...:         return None
    ...:     max_freq_elem = max(lst, key=lambda v: lst.count(v))
    ...:     max_freq = lst.count(max_freq_elem) # 出现最多次数
    ...:     ret = []
    ...:     for i in lst:
    ...:         if i not in ret and lst.count(i)==max_freq:
    ...:             ret.append(i)
    ...:     return ret

In [35]: mode([1,1,2,2,3,2,1])
Out[35]: [1, 2]
```

### 多个list

带有一个 `*` 的参数为可变的位置参数，意味着能传入任意多个位置参数。

key 函数定义怎么比较大小：lambda 的参数 v 是 lists 中的一个元素。

```
In [15]: def max_len(*lists):
    ...:     return max(*lists, key=lambda v: len(v))
```

调用 max_len，传入三个列表，正是 v 可能的三个取值。

```
In [17]: r = max_len([1, 2, 3], [4, 5, 6, 7], [8])
    ...: print(f' 更长的列表是 {r}')
更长的列表是 [4, 5, 6, 7]
```

关于 lambda 函数，在此做图形演示。

max_len 函数被传入三个实参，类型为 list，如下图所示，lists 变量指向最下面的 tuple 实例。

[![image-20200219203830985](http://static.come2rss.xyz/80dc83f0-5317-11ea-8128-358088d96de7)](http://static.come2rss.xyz/80dc83f0-5317-11ea-8128-358088d96de7)

[image-20200219203830985](http://static.come2rss.xyz/80dc83f0-5317-11ea-8128-358088d96de7)



程序运行到下一帧，会出现 lambda 函数，它的父函数为 f1，也就是 max_len 函数。

有些读者可能不理解两点，这种用法中：

- 参数 v 取值到底是多少？
- lambda 函数有返回值吗？如果有，返回值是多少？

通过下面图形，非常容易看出，v 指向 tuple 实例的第一个元素，指向的线和箭头能非常直观地反映出来。

[![image-20200219204141898](http://static.come2rss.xyz/91f66a20-5317-11ea-b2e1-7d26d62747f1)](http://static.come2rss.xyz/91f66a20-5317-11ea-b2e1-7d26d62747f1)

[image-20200219204141898](http://static.come2rss.xyz/91f66a20-5317-11ea-b2e1-7d26d62747f1)



下面示意图中，看到返回值为 3，也就是 len(v) 的返回值，其中 v = [1,2,3]。

[![image-20200219204920052](http://static.come2rss.xyz/a078b580-5317-11ea-b2e1-7d26d62747f1)](http://static.come2rss.xyz/a078b580-5317-11ea-b2e1-7d26d62747f1)

[image-20200219204920052](http://static.come2rss.xyz/a078b580-5317-11ea-b2e1-7d26d62747f1)



然后，v 指向 tuple 中的下一个元素，返回值为 4。

[![img](http://static.come2rss.xyz/af1391f0-5317-11ea-b2e1-7d26d62747f1)](http://static.come2rss.xyz/af1391f0-5317-11ea-b2e1-7d26d62747f1)

[img](http://static.come2rss.xyz/af1391f0-5317-11ea-b2e1-7d26d62747f1)



然后，v 指向 tuple 的最后一个元素 [8]，返回值为 1。

[![image-20200219205408391](http://static.come2rss.xyz/bfc5dcb0-5317-11ea-8128-358088d96de7)](http://static.come2rss.xyz/bfc5dcb0-5317-11ea-8128-358088d96de7)

[image-20200219205408391](http://static.come2rss.xyz/bfc5dcb0-5317-11ea-8128-358088d96de7)



根据 key 确定的比较标准，max 函数的返回值为红色字体指向的元素，也就是返回 [4,5,6,7]。

[![img](http://static.come2rss.xyz/ce141fc0-5317-11ea-8bb5-594930f74663)](http://static.come2rss.xyz/ce141fc0-5317-11ea-8bb5-594930f74663)

[img](http://static.come2rss.xyz/ce141fc0-5317-11ea-8bb5-594930f74663)



# 高级篇

## 容器对象

在某些对象中会包含对其它对象的引用，这样的对象被称作**容器**(*containers*)。因此，我们可以把容器视作用于组织各种元素的数据结构。

下面是一些常见的容器对象：

- list, deque, …
- set, frozensets, …
- dict, defaultdict, OrderedDict, Counter, …
- tuple, namedtuple, …
- str

详细内容见[链接](https://www.jianshu.com/p/63af3680c221)

## 切片

对这种经常取指定索引范围的操作，用循环十分繁琐，因此，Python提供了切片（Slice）操作符，能大大简化这种操作。`L[0:3]`表示，从索引`0`开始取，直到索引`3`为止，但不包括索引`3`。

比如：

```
def trim(s):
	whlie s[:1] == ' ':
		s = s[1：]
	whlie s[-1] == ' ':
		s = s[:-1]
```

tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：字符串`'xxx'`也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：

## 迭代

更详细的补充[汗颜](https://www.cnblogs.com/wj-1314/p/8490822.html)

#### 迭代器

定义：
对于list、string、tuple、dict等这些**容器对象**,使用for循环遍历是很方便的。在后台for语句对容器对象调用iter()函数。iter()是python内置函数。
iter()函数会返回一个定义了next()方法的迭代器对象，它在容器中逐个访问容器内的元素。next()也是python内置函数。在没有后续元素时，next()会抛出一个StopIteration异常，通知for语句循环结束。

迭代器是用来帮助我们记录每次迭代访问到的位置，当我们对迭代器使用next()函数的时候，迭代器会向我们返回它所记录位置的下一个位置的数据。实际上，在使用next()函数的时候，调用的就是迭代器对象的_next_方法（Python3中是对象的_next_方法，Python2中是对象的next()方法）。所以，我们要想构造一个迭代器，就要实现它的_next_方法。但这还不够，python要求迭代器本身也是可迭代的，所以我们还要为迭代器实现_iter_方法，而_iter_方法要返回一个迭代器，迭代器自身正是一个迭代器，所以迭代器的_iter_方法返回自身self即可。

**术语解释**

1，**迭代器**协议：对象需要提供next()方法，它要么返回迭代中的下一项，要么就引起一个StopIteration异常，以终止迭代。

2，可迭代对象：实现了迭代器协议对象。list、tuple、dict都是Iterable（可迭代对象），但不是Iterator（迭代器对象）。但可以使用内建函数iter()，把这些都变成Iterable（可迭代器对象）。

3，for item in Iterable 循环的**本质**就是先通过iter()函数获取可迭代对象Iterable的迭代器，然后对获取到的迭代器不断调用next()方法来获取下一个值并将其赋值给item，当遇到StopIteration的异常后循环结束

**容器对象化为迭代器**

```
# 随便定义一个list
listArray=[1,2,3]
# 使用iter()函数
iterName=iter(listArray)
print(iterName)
# 结果如下：是一个列表list的迭代器
# <list_iterator object at 0x0000017B0D984278>

print(next(iterName))
print(next(iterName))
print(next(iterName))
print(next(iterName))#没有迭代到下一个元素，直接抛出异常
# 1
# 2
# 3
# Traceback (most recent call last):
#   File "Test07.py", line 32, in <module>
# StopIteration
```

**自定义迭代器**

```
class Fib(object):
    def __init__(self, max):
        super(Fib, self).__init__()
        self.max = max

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib

# 定义一个main函数，循环遍历每一个菲波那切数
def main():
    # 20以内的数
    fib = Fib(20)
    for i in fib:
        print(i)
```

在本类的实现中，定义了一个*iter*(self)方法，这个方法是在for循环遍历时被iter()调用，返回一个迭代器。因为在遍历的时候，是直接调用的python内置函数iter()，由iter()通过调用*iter*(self)获得对象的迭代器。有了迭代器，就可以逐个遍历元素了。而逐个遍历的时候，也是使用内置的next(）函数通过调用对象的*next*(self)方法对迭代器对象进行遍历。所以要实现*iter*(self)和*next*(self)这两个方法。

而且因为实现了*next*(self)方法，所以在实现*iter*(self)的时候，直接返回self就可以。

总结一句话就是：
在循环遍历自定义容器对象时,会使用python内置函数iter()调用遍历对象的*iter*(self)获得一个迭代器,之后再循环对这个迭代器使用next()调用迭代器对象的*next*(self)。

注意点：*iter*(self)只会被调用一次,而*next*(self)会被调用 n 次，直到出现StopIteration异常。

**判断可迭代**可使用`Iterable`类型来判断。

```
from collections import Iterable
isinstance('abc', Iterable) #判断 'abc' 是否可迭代
# True
```

## 生成器

生成器是一类特殊的迭代器。生成器是只能遍历一次的

延迟操作。也就是在需要的时候才产生结果，不是立即产生结果。

第一类：生成器函数：还是使用 def 定义函数，但是，使用yield而不是return语句返回结果。yield语句一次返回一个结果，在每个结果中间，挂起函数的状态，以便下次从它离开的地方继续执行。

如下案例加以说明：

```
# 菲波那切数列
def Fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return '亲！没有数据了...'
# 调用方法，生成出10个数来
f=Fib(10)
# 使用一个循环捕获最后return 返回的值，保存在异常StopIteration的value中
while  True:
    try:
        x=next(f)
        print("f:",x)
    except StopIteration as e:
        print("生成器最后的返回值是：",e.value)
        break
```

第二类：生成器表达式：类似于列表推导，只不过是把一对大括号[]变换为一对小括号()。但是，生成器表达式是按需产生一个生成器结果对象，要想拿到每一个元素，就需要循环遍历。

如下案例加以说明：

```
# 一个列表
xiaoke=[2,3,4,5]
# 生成器generator，类似于list，但是是把[]改为()
gen=(a for a  in xiaoke)
for  i  in gen:
    print(i)
#结果是：
2
3
4
5
#也可以使用next调用generator
generator_ex = (x*x for x in range(10))
print(next(generator_ex))
print(next(generator_ex))
print(next(generator_ex))
print(next(generator_ex))
print(next(generator_ex))
print(next(generator_ex))
print(next(generator_ex))
0
1
4
9
16
25
36
# 为什么要使用生成器？因为效率。
# 使用生成器表达式取代列表推导式可以同时节省 cpu 和 内存(RAM)。
# 如果你构造一个列表(list)的目的仅仅是传递给别的函数,
# 比如 传递给tuple()或者set(), 那就用生成器表达式替代吧!

# 本案例是直接把列表转化为元组
kk=tuple(a for a in xiaoke)
print(kk)
#结果是：
(2, 3, 4, 5)

# python内置的一些函数，可以识别这是生成器表达式，外面有一对小括号，就是生成器，中括号就列表生成式
result1=sum(a for a in range(3))
print(result1)
# 列表推导式
result2=sum([a for a in range(3)])
print(result2)
```

### 列表生成器

列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。

```
[x * x for x in range(1, 11)]
[x * x for x in range(1, 11) if x % 2 == 0]
```

还可以使用两层循环，可以生成全排列：

```
>>> [m + n for m in 'ABC' for n in 'XYZ']
['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
```

三层和三层以上的循环就很少用到了。

运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：

```
>>> import os # 导入os模块，模块的概念后面讲到
>>> [d for d in os.listdir('.')] # os.listdir可以列出文件和目录
['.emacs.d', '.ssh', '.Trash', 'Adlm', 'Applications', 'Desktop', 'Documents', 'Downloads', 'Library', 'Movies', 'Music', 'Pictures', 'Public', 'VirtualBox VMs', 'Workspace', 'XCode']
```

`for`循环其实可以同时使用两个甚至多个变量，比如`dict`的`items()`可以同时迭代key和value：

```
>>> d = {'x': 'A', 'y': 'B', 'z': 'C' }
>>> [k + '=' + v for k, v in d.items()]
['y=B', 'x=A', 'z=C']
```

**Note：** 在一个列表生成式中，`for`前面的`if ... else`是表达式，而`for`后面的`if`是过滤条件，不能带`else`。也就是说`for`后面不能加`else`，而`for`前面`if`必须加`else`。

## 装饰器

类中的属性可以通过方法的包装来防止外露，但是直接调用方法不如直接写属性简介明白。程序员们想出了装饰器`@property`个东西来修饰方法，是其可以方法可以如同属性一样使用、赋值。当然Python最后会把它转化为等价的方法调用形式？

如

```
class Student(object):
	#定义了一个只读的属性
    @property
    def score(self):
        return self._score
	#定义了一个可读也可写的属性
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
        
    # 仅定义@property的方法是定义了一个只读属性
	@property
	def age(self):
		return self.age
```

## 多重继承

假设在为了每个功能而专门设计一个类并同时作为一个父亲类，那么类数量可能会指数型增长而且类的层次变得更加复杂。

[![image-20200503125546752](http://static.come2rss.xyz/image-20200503125546752.png)](http://static.come2rss.xyz/image-20200503125546752.png)

[image-20200503125546752](http://static.come2rss.xyz/image-20200503125546752.png)



为了解决这一个问题，多重继承的概念就此引出，即一个类可以继承多个类，那么只需要把需要添加的功能写成类，并继承给相应需要的类即可。

```
#比如给Dog添加Runable， Carnivorous 的功能
class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
    pass
```

## 自定义类 magic function的天下

我们先定义一个`Student`类，打印一个实例：

```
>>> class Student(object):
...     def __init__(self, name):
...         self.name = name
...
>>> print(Student('Michael'))
<__main__.Student object at 0x109afb190>
```

看到类似`__slots__`这种形如`__xxx__`的变量或者函数名就要注意，这些在Python中是有特殊用途的。

`__slots__`我们已经知道怎么用了，`__len__()`方法我们也知道是为了能让class作用于`len()`函数。

除此之外，Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类。

#### `__str__()` `__repr__()` `__len__()` `__iter__` `__getitem__` `__setitem__()`

`__str__()`可在`print(class)`时调用，并显示出内容。 如果不定义的话，一般都是这样子的打印出一堆`<__main__.Student object at 0x109afb190>`，不好看。

`__repr__()`在直接敲变量的被调用，同样也可以自定义来输出的好看一点，也可以偷懒一点`__repr__ = __str__`。

`__len__()` 可在`__len__()`时调用。

`__iter__` 该方法返回一个迭代对象以供`for`循环使用。然后，Python的for循环就会不断调用该迭代对象的`__next__()`方法拿到循环的下一个值，直到遇到`StopIteration`错误时退出循环。我们以斐波那契数列为例，写一个Fib类，可以作用于for循环：

```
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值
```

现在，试试把Fib实例作用于for循环：

```
>>> for n in Fib():
...     print(n)
...
1
1
2
3
5
...
46368
75025
```

Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素：

```
>>> Fib()[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'Fib' object does not support indexing
```

`__getitem__` 可以实现按元素寻址。

```
class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a
```

现在，就可以按下标访问数列的任意一项了：

```
>>> f = Fib()
>>> f[0]
1
```

但是list有个神奇的切片方法：

```
>>> list(range(100))[5:10]
[5, 6, 7, 8, 9]
```

对于Fib却报错。原因是`__getitem__()`传入的参数可能是一个int，也可能是一个切片对象`slice`，所以要做判断：

```
class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
```

现在试试Fib的切片：

```
>>> f = Fib()
>>> f[0:5]
[1, 1, 2, 3, 5]
>>> f[:10]
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```

但是没有对step参数作处理：

```
>>> f[:10:2]
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
```

也没有对负数作处理，所以，要正确实现一个`__getitem__()`还是有很多工作要做的。

此外，如果把对象看成`dict`，`__getitem__()`的参数也可能是一个可以作key的object，例如`str`。

与之对应的是`__setitem__()`方法，把对象视作list或dict来对集合赋值。最后，还有一个`__delitem__()`方法，用于删除某个元素。

总之，通过上面的方法，我们自己定义的类表现得和Python自带的list、tuple、dict没什么区别，这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口。

#### `__getattr__`

一般来说，如果调用一个不存在的属性，会爆出错误，提示没有这个`attribute`。要避免这个错误，除了可以加上一个`score`属性外，Python还有另一个机制，那就是写一个`__getattr__()`方法，动态返回一个属性。

```
class Student(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr=='score':
            return 99
         # 返回函数也是完全可以的：    
        if attr=='age':
            return lambda: 25
```

python对于调用的不存在的类的函数和属性会都使用`__getattr__()`

```
>>> s = Student()
>>> s.name
'Michael'
>>> s.score
99
>>> s.age()
25
```

**Note**: 只有在没有找到属性的情况下，才调用`__getattr__`，已有的属性，比如`name`，不会在`__getattr__`中查找。

注意到任意调用`__getattr__`也未定义的属性都会返回`None`，这是因为我们定义的`__getattr__`默认返回就是`None`。要让class只响应特定的几个属性，我们就要按照约定，抛出`AttributeError`的错误：

```
class Student(object):

    def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25
        raise AttributeError('Student object has no attribute %s % attr)
```

这实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。这种完全动态调用的特性有什么实际作用呢？作用就是，可以针对完全动态的情况作调用。

举个例子：

现在很多网站都搞REST API，比如新浪微博、豆瓣啥的，调用API的URL类似：

- http://api.server/user/friends
- http://api.server/user/timeline/list

如果要写SDK，给每个URL对应的API都写一个方法，那得累死，而且，API一旦改动，SDK也要改。

利用完全动态的`__getattr__`，我们可以写出一个链式调用：

```
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
    	#返回一个Chain对象，而且path随着新的对象而动态增长了！
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__
```

试试：

```
#一开始`chain()`的`_path`为空！
>>> Chain().status.user.timeline.list
'/status/user/timeline/list'
```

这样，无论API怎么变，SDK都可以根据URL实现完全动态的调用，而且，不随API的增加而改变！

还有些REST API会把参数放到URL中，比如GitHub的API：

```
GET /users/:user/repos
```

调用时，需要把`:user`替换为实际用户名。如果我们能写出这样的链式调用：

```
Chain().users('michael').repos
```

就可以非常方便地调用API了。有兴趣的童鞋可以试试写出来。

### `__call__`

任何类，只需要定义一个`__call__()`方法，就可以直接对实例进行调用。请看示例：

```
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)
>>> s = Student('Michael')
>>> s() # self参数不要传入
My name is Michael.
```

`__call__()`还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。

如果你把对象看成函数，那么函数本身其实也可以在运行期动态创建出来，因为类的实例都是运行期创建出来的，这么一来，我们就模糊了对象和函数的界限。

那么，怎么判断一个变量是对象还是函数呢？其实，更多的时候，我们需要判断**一个对象是否能被调用**，能被调用的对象就是一个`Callable`对象，比如函数和我们上面定义的带有`__call__()`的类实例.通过`callable()`函数，我们就可以判断一个对象是否是“可调用”对象。

```
>>> callable(Student())
True
>>> callable(max)
True
>>> callable([1, 2, 3])
False
>>> callable(None)
False
>>> callable('str')
False
```

## 枚举类

`Enum`枚举类型定义一个class类型，然后，每个常量都是class的一个唯一实例。

```
from enum import Enum
#返回`Month`类型的枚举类
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
```

可以直接使用`Month.Jan`来引用一个常量，或者枚举它的所有成员：

```
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
```

如果需要更精确地控制枚举类型，可以从`Enum`派生出自定义类：

```
from enum import Enum, unique
#@unique装饰器可以帮助我们检查保证没有重复值。
@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
```

访问枚举类型的方法归纳：

```
#引用
##属性
>>> day1 = Weekday.Mon
>>> print(day1)
Weekday.Mon

##下标
>>> print(Weekday['Tue'])
Weekday.Tue

##方法调用，（必须是int）
>>> print(Weekday(1))
Weekday.Mon

#属性具有值
>>> print(Weekday.Tue.value)
2
#属性之间可以比较
>>> print(day1 == Weekday.Mon)
True
>>> print(day1 == Weekday.Tue)
False
#遍历
>>> for name, member in Weekday.__members__.items():
...     print(name, '=>', member)
...
Sun => Weekday.Sun
Mon => Weekday.Mon
Tue => Weekday.Tue
Wed => Weekday.Wed
Thu => Weekday.Thu
Fri => Weekday.Fri
Sat => Weekday.Sat
```

## Callback函数

在我的理解下，Callback是可以指函数A可以作为参数传入一个函数B并在函数B中调用A，即A是Callbackable的。

```
#callback
def cb(value):
    if  value % 130 == 0:
        return (True, value)
    elif value > 100000:
        return (True, None)
    return (False ,None)

def fibonacci_call(func):
    values = []
    while(True):
        if len(values) < 2:
            values.append(1)
        else:
            values = [values[-1], values[-2] + values[-1]]
        res =  func(values[-1] )
        print(values[-1])
        if res[0]:
            return res[1]
        
fibonacci_call(cb)
```

## Python的对象说明

Python的一切都是一个对象，当传参给函数的时候传的是一个对象的指针！那么在函数内部进行改变变量的指向的时候，原数据是不会受到影响的！如：

```
a = 10
def test(a):
    a = a + 1
    print(a)
test(a)
print(a)


```

11
10
​```

```
所以只能不改变原来的指向，直接改变原来的值！如

​```python
a = [1]
def test(a):
	a[0] = 2
    print(a)
test(a)
print(a)

```

[1]
[1]
​```

```
## 元类MateClass

看不太懂，溜了溜了 https://www.liaoxuefeng.com/wiki/1016959663602400/1017592449371072

## 引用顺序以及关键字

### 命名空间

命名空间(Namespace)是从名称到对象的映射，大部分的命名空间都是通过 Python 字典来实现的。

命名空间提供了在项目中避免名字冲突的一种方法。各个命名空间是独立的，没有任何关系的，所以一个命名空间中不能有重名，但不同的命名空间是可以重名而没有任何影响。

一般有三种命名空间：

- **内置名称（built-in names**）， Python 语言内置的名称，比如函数名 abs、char 和异常名称 BaseException、Exception 等等。
- **全局名称（global names）**，模块中定义的名称，记录了模块的变量，包括函数、类、其它导入的模块、模块级的变量和常量。
- **局部名称（local names）**，函数中定义的名称，记录了函数的变量，包括函数的参数和局部定义的变量。（类中定义的也是）

**命名空间的生命周期**：

命名空间的生命周期取决于对象的作用域，如果对象执行完成，则该命名空间的生命周期就结束。

因此，我们无法从外部命名空间访问内部命名空间的对象。

### 作用域

作用域就是一个 Python 程序可以直接访问命名空间的正文区域。

Python 中，程序的变量并不是在哪个位置都可以访问的，访问权限决定于这个变量是在哪里赋值的。变量的作用域决定了在哪一部分程序可以访问哪个特定的变量名称。Python的作用域一共有4种，分别是：

有四种作用域：

- **L（Local）**：最内层，包含局部变量，比如一个函数/方法内部。
- **E（Enclosing）**：包含了非局部(non-local)也非全局(non-global)的变量。比如两个嵌套函数，一个函数（或类） A 里面又包含了一个函数 B ，那么对于 B 中的名称来说 A 中的作用域就为 nonlocal。
- **G（Global）**：当前脚本的最外层，比如当前模块的全局变量。
- **B（Built-in）**： 包含了内建的变量/关键字等。，最后被搜索



**查找变量的顺序：**

python引用变量的顺序： 当前作用域局部变量（此函数）->外层作用域变量->当前模块中的全局变量->python内置变量

![image-20200503125603390](http://static.come2rss.xyz/image-20200503125603390.png)



**全局变量和局部变量**

定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。

局部变量只能在其被声明的函数内部**访问**，而全局变量可以在整个程序范围内访问。调用函数时，**所有在函数内声明的变量名称都将被加入到作用域中**。





### global 和 nonlocal关键字

当内部作用域想**修改**外部作用域的变量时，就要用到global和nonlocal关键字了。

如果要修改**嵌套**作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字了，如下实例：

​```python
def a():
	var = 1
	def b():
		nonlocal var #注意这里var的nonlocal的声明不可以接后续的东西
		var = 2
```

## 面对对象编程

面向对象最重要的概念就是类（Class）和实例（Instance），必须牢记类是抽象的模板，比如Student类，而实例是根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，但各自的数据可能不同。在Python中，定义类是通过`class`关键字：

`class`后面紧接着是类名，即`Student`，类名通常是**大写开头**的单词，紧接着是`(object)`，表示该类是从哪个类继承下来的，通常，如果没有合适的继承类，就使用`object`类，这是所有类最终都会继承的类。

定义好了`Student`类，就可以根据`Student`类创建出`Student`的实例，创建实例是通过类名()实现的：

面向对象最重要的概念就是类（Class）和实例（Instance），必须牢记类是抽象的模板，比如Student类，而实例是根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，但各自的数据可能不同。

```
>>> bart = Student()
>>> bart
<__main__.Student object at 0x10a67a590>
>>> Student
<class '__main__.Student'>
```

可以看到，变量`bart`指向的就是一个`Student`的实例，后面的`0x10a67a590`是内存地址，每个object的地址都不一样，而`Student`本身则是一个类。

可以**自由地给一个实例变量绑定属性**，比如，给实例`bart`绑定一个`name`属性：

```
>>> bart.name = 'Bart Simpson'
>>> bart.name
'Bart Simpson'
```

由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。通过定义一个特殊的`__init__`方法，在创建实例的时候，就把`name`，`score`等属性绑上去：

```
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score
```

注意：特殊方法“**init**”前后分别有两个下划线！！！

注意到`__init__`方法的第一个参数永远是`self`，表示创建的实例本身，因此，在`__init__`方法内部，就可以把各种属性绑定到`self`，因为`self`就指向创建的实例本身。

有了`__init__`方法，在创建实例的时候，就不能传入空的参数了，必须传入与`__init__`方法匹配的参数，但`self`不需要传，Python解释器自己会把实例变量传进去：

```
>>> bart = Student('Bart Simpson', 59)
>>> bart.name
'Bart Simpson'
>>> bart.score
59
```

和普通的函数相比，在**类中定义的函数只有一点不同**，就是第一个参数永远是实例变量`self`，并且，调用时，不用传递该参数。除此之外，类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数。

### 数据封装

面向对象编程的一个重要特点就是数据封装。在上面的`Student`类中，每个实例就拥有各自的`name`和`score`这些数据。我们可以通过函数来访问这些数据，比如打印一个学生的成绩：

```
>>> def print_score(std):
...     print('%s: %s' % (std.name, std.score))
...
>>> print_score(bart)
Bart Simpson: 59
```

但是，既然`Student`实例本身就拥有这些数据，要访问这些数据，就没有必要从外面的函数去访问，可以直接在`Student`类的内部定义访问数据的函数，这样，就把“数据”给封装起来了。这些封装数据的函数是和`Student`类本身是关联起来的，我们称之为类的方法：

```
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))
```

要定义一个方法，除了第一个参数是`self`外，其他和普通函数一样。要调用一个方法，只需要在实例变量上直接调用，除了`self`不用传递，其他参数正常传入：

```
>>> bart.print_score()
Bart Simpson: 59
```

这样一来，我们从外部看`Student`类，就只需要知道，创建实例需要给出`name`和`score`，而如何打印，都是在`Student`类的内部定义的，这些数据和逻辑被“封装”起来了，调用很容易，但却不用知道内部实现的细节。

封装的另一个好处是可以给`Student`类增加新的方法，比如`get_grade`：

```
class Student(object):
    ...

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'
```

同样的，`get_grade`方法可以直接在实例变量上调用，不需要知道内部实现细节：

### 访问限制

------

在Class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，这样，就隐藏了内部的复杂逻辑。

私有变量（private）是类中属性的名称前加上两个下划线`__`的属性，在Python中，实例的变量名如果以`__`开头，所以，我们把Student类改一改：

```
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
```

这样就确保了外部代码不能随意修改对象内部的状态，这样通过访问限制的保护，代码更加健壮。

但是如果外部代码要获取和修改name和score怎么办？可以给Student类增加`get_name`和`get_score`这样的方法：

```
class Student(object):
    ...

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score
    def set_score(self, score):
        self.__score = score
```

在这种方法中，可以对参数做**检查**，避免传入无效的参数：

需要注意的是，在Python中，变量名类似`__xxx__`的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，**特殊变量是可以直接访问的**，不是private变量，所以，不能用`__name__`、`__score__`这样的变量名。

有些时候，你会看到以一个下划线开头的实例变量名，比如`_name`，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。

**原理：**双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问`__name`是因为Python解释器对外把`__name`变量改成了`_Student__name`，所以，仍然可以通过`_Student__name`来访问`__name`变量：

```
>>> bart._Student__name
'Bart Simpson'
```

但是强烈建议你不要这么干，因为不同版本的Python解释器可能会把`__name`改成不同的变量名。总的来说就是，Python本身没有任何机制阻止你干坏事，一切全靠自觉。

最后注意下面的这种*错误写法*：

```
>>> bart = Student('Bart Simpson', 59)
>>> bart.get_name()
'Bart Simpson'
>>> bart.__name = 'New Name' # 设置__name变量！
>>> bart.__name
'New Name'
```

表面上看，外部代码“成功”地设置了`__name`变量，但实际上这个`__name`变量和class内部的`__name`变量*不是*一个变量！内部的`__name`变量已经被Python解释器自动改成了`_Student__name`，而外部代码给`bart`新增了一个`__name`变量。不信试试：

```
>>> bart.get_name() # get_name()内部返回self.__name
'Bart Simpson'
```

要理解多态的好处，我们还需要再编写一个函数，这个函数接受一个`Animal`类型的变量：

```
def run_twice(animal):
    animal.run()
    animal.run()
```

当我们传入`Animal`的实例时，`run_twice()`就打印出：

```
>>> run_twice(Animal())
Animal is running...
Animal is running...
```

当我们传入`Dog`的实例时，`run_twice()`就打印出：

```
>>> run_twice(Dog())
Dog is running...
Dog is running...
```

当我们传入`Cat`的实例时，`run_twice()`就打印出：

```
>>> run_twice(Cat())
Cat is running...
Cat is running...
```

看上去没啥意思，但是仔细想想，现在，如果我们再定义一个`Tortoise`类型，也从`Animal`派生：

```
class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')
```

当我们调用`run_twice()`时，传入`Tortoise`的实例：

```
>>> run_twice(Tortoise())
Tortoise is running slowly...
Tortoise is running slowly...
```

你会发现，新增一个`Animal`的子类，不必对`run_twice()`做任何修改，实际上，任何依赖`Animal`作为参数的函数或者方法都可以不加修改地正常运行，原因就在于多态。

多态的好处就是，当我们需要传入`Dog`、`Cat`、`Tortoise`……时，我们只需要接收`Animal`类型就可以了，因为`Dog`、`Cat`、`Tortoise`……都是`Animal`类型，然后，按照`Animal`类型进行操作即可。由于`Animal`类型有`run()`方法，因此，传入的任意类型，只要是`Animal`类或者子类，就会自动调用实际类型的`run()`方法，这就是多态的意思：

对于一个变量，我们只需要知道它是`Animal`类型，无需确切地知道它的子类型，就可以放心地调用`run()`方法，而具体调用的`run()`方法是作用在`Animal`、`Dog`、`Cat`还是`Tortoise`对象上，由运行时该对象的确切类型决定，这就是多态真正的威力：调用方只管调用，不管细节，而当我们新增一种`Animal`的子类时，只要确保`run()`方法编写正确，不用管原来的代码是如何调用的。这就是著名的“开闭”原则：

对扩展开放：允许新增`Animal`子类；

对修改封闭：不需要修改依赖`Animal`类型的`run_twice()`等函数。

继承还可以一级一级地继承下来，就好比从爷爷到爸爸、再到儿子这样的关系。而任何类，最终都可以追溯到根类object，这些继承关系看上去就像一颗倒着的树。比如如下的继承树：

```
                ┌───────────────┐
                │    object     │
                └───────────────┘
                        │
           ┌────────────┴────────────┐
           │                         │
           ▼                         ▼
    ┌─────────────┐           ┌─────────────┐
    │   Animal    │           │    Plant    │
    └─────────────┘           └─────────────┘
           │                         │
     ┌─────┴──────┐            ┌─────┴──────┐
     │            │            │            │
     ▼            ▼            ▼            ▼
┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐
│   Dog   │  │   Cat   │  │  Tree   │  │ Flower  │
└─────────┘  └─────────┘  └─────────┘  └─────────┘
```

### 静态语言 vs 动态语言

对于静态语言（例如Java）来说，如果需要传入`Animal`类型，则传入的对象必须是`Animal`类型或者它的子类，否则，将无法调用`run()`方法。

对于Python这样的动态语言来说，则不一定需要传入`Animal`类型。我们只需要保证传入的对象有一个`run()`方法就可以了：

```
class Timer(object):
    def run(self):
        print('Start...')
```

这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一**个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。**

Python的“file-like object“就是一种鸭子类型。对真正的文件对象，它有一个`read()`方法，返回其内容。但是，许多对象，只要有`read()`方法，都被视为“file-like object“。许多函数接收的参数就是“file-like object“，你不一定要传入真正的文件对象，完全可以传入任何实现了`read()`方法的对象。

### 小结

继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。

动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。

### 实例属性和类属性

由于Python是动态语言，根据类创建的实例可以任意绑定属性。

给实例绑定属性的方法是通过实例变量，或者通过`self`变量：

```
class Student(object):
    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.score = 90
```

但是，如果`Student`类本身需要绑定一个属性呢？可以直接在class中定义属性，这种属性是类属性，归`Student`类所有：

```
class Student(object):
    name = 'Student'
```

当我们定义了一个类属性后，这个属性虽然归类所有，但类的所有实例都可以访问到。

```
>>> class Student(object):
...     name = 'Student'
...
>>> s = Student() # 创建实例s
>>> print(s.name) # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
Student
>>> print(Student.name) # 打印类的name属性
Student
>>> s.name = 'Michael' # 给实例绑定name属性
>>> print(s.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
Michael
>>> print(Student.name) # 但是类属性并未消失，用Student.name仍然可以访问
Student
>>> del s.name # 如果删除实例的name属性
>>> print(s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
Student
```

从上面的例子可以看出，在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。

小结：python可以动态绑定实例属性，但是最好别和类属性重合，不然会会覆盖掉类属性。

## Python高级面对对象编程

### 添加对象和属性

Python这种动态类型语言可以在运行过程中动态添加定义给类和实例添加方法和属性。但是给实例添加的属性和方法是无法对新建的实例生效的，或者说无法改变类。

如

```
class Student(object):
    pass
>>> s = Student()
>>> s.name = 'Michael' # 动态给实例绑定一个属性
>>> print(s.name)
Michael   

>>> def set_age(self, age): # 定义一个函数作为实例方法
...     self.age = age
...
>>> from types import MethodType
>>> s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
>>> s.set_age(25) # 调用实例方法
>>> s.age # 测试结果
25


>>> s2 = Student() # 创建新的实例
>>> s2.set_age(25) # 尝试调用方法,
#可以见到给一个实例添加的方法是不对另一个实例起作用的
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'set_age'



>>> def set_score(self, score):
...     self.score = score
...
>>> Student.set_score = set_score # 给类绑定方法
```

##### 使用`__slots__`限制类的属性

可以使用特殊变量`__slots__`来限制类的属性。

```
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
    
>>> s = Student() # 创建新的实例
>>> s.name = 'Michael' # 绑定属性'name'
>>> s.age = 25 # 绑定属性'age'
>>> s.score = 99 # 绑定属性'score'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
```

可以看到`age`由于没有被`__slots__`包括在内，所以不可被绑定。

使用`__slots__`要注意，`__slots__`定义的属性仅对当前类实例起作用，对继承的子类是不起作用的。除非在子类中也定义`__slots__`，这样，子类实例允许定义的属性就是自身的`__slots__`加上父类的`__slots__`。

## 函数式编程 Functional Programming

函数是Python内建支持的一种封装，我们通过把大段代码拆成函数，通过一层一层的函数调用，就可以把复杂任务分解成简单的任务，这种分解可以称之为面向过程的程序设计。函数就是面向过程的程序设计的基本单元。

而函数式编程（请注意多了一个“式”字）——Functional Programming，虽然也可以归结到面向过程的程序设计，但其思想更接近数学计算。

我们首先要搞明白计算机（Computer）和计算（Compute）的概念。

在计算机的层次上，CPU执行的是加减乘除的指令代码，以及各种条件判断和跳转指令，所以，汇编语言是最贴近计算机的语言。

而计算则指数学意义上的计算，越是抽象的计算，离计算机硬件越远。

对应到编程语言，就是越低级的语言，越贴近计算机，抽象程度低，执行效率高，比如C语言；越高级的语言，越贴近计算，抽象程度高，执行效率低，比如Lisp语言。

函数式编程就是一种抽象程度很高的编程范式，纯粹的函数式编程语言编写的函数没有变量，因此，任意一个函数，只要输入是确定的，输出就是确定的，这种纯函数我们称之为**没有副作用**。而允许使用变量的程序设计语言，由于函数内部的变量状态不确定，同样的输入，可能得到不同的输出，因此，这种函数是有副作用的。

函数式编程的一个特点就是，允许把**函数本身作为参数传入另一个函数**，还允许返回一个函数！

Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言。

### 高阶函数

#### 函数名也是变量

函数名其实就是指向函数的变量！对于`abs()`这个函数，完全可以把函数名`abs`看成变量，它指向一个可以计算绝对值的函数！

```
>>> abs = 10
>>> abs(-10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not callable
```

把`abs`指向`10`后，就无法通过`abs(-10)`调用该函数了！因为`abs`这个变量已经不指向求绝对值函数而是指向一个整数`10`！要恢复`abs`函数，请重启Python交互环境。

注：由于`abs`函数实际上是定义在`import builtins`模块中的，所以要让修改`abs`变量的指向在其它模块也生效，要用`import builtins; builtins.abs = 10`。

#### 传入函数

既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。

一个最简单的高阶函数：

```
def add(x, y, f):
    return f(x) + f(y)
```

当我们调用`add(-5, 6, abs)`时，参数`x`，`y`和`f`分别接收`-5`，`6`和`abs`，根据函数定义，我们可以推导计算过程为：

```
x = -5
y = 6
f = abs
f(x) + f(y) ==> abs(-5) + abs(6) ==> 11
return 11
```

### Map/Reduct

Python内建了`map()`和`reduce()`函数。

如果你读过Google的那篇大名鼎鼎的论文“[MapReduce: Simplified Data Processing on Large Clusters](http://research.google.com/archive/mapreduce.html)”，你就能大概明白map/reduce的概念。

我们先看map。`map()`函数接收两个参数，一个是函数，一个是`Iterable`，`map`将传入的函数依次作用到序列的每个元素，并把结果作为新的`Iterator`返回。

```
>>> def f(x):
...     return x * x
...
>>> r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> list(r)
[1, 4, 9, 16, 25, 36, 49, 64, 81]
```

`map()`传入的第一个参数是`f`，即函数对象本身。由于结果`r`是一个`Iterator`，`Iterator`是惰性序列，因此通过`list()`函数让它把整个序列都计算出来并返回一个list。

看`reduce`的用法。`reduce`把一个函数作用在一个序列`[x1, x2, x3, ...]`上，这个函数必须接收两个参数，`reduce`把结果继续和序列的下一个元素做”累积”。其实这么描述并不够详细，

[参考](https://www.cnblogs.com/51kata/p/5438195.html)

> reduce操作是函数式编程中的重要技术之一，其作用是通过对一个集合的操作，可以从中生成一个值。比如最常见的求和，求最大值、最小值等都是reduce操作的典型例子。python通过内置reduce函数对reduce操作提供了很好的支持。
>
> 函数语法： reduce(function, iterable[,initializer])
>
> 函数参数含义如下：
>
> 1、function 需要带两个参数，1个是用于保存操作的结果，另一个是每次迭代的元素。
>
> 2、iterable 待迭代处理的集合
>
> 3、initializer 初始值，可以没有。
>
> reduce函数的运作过程是，当调用reduce方法时：
>
> 1、如果存在initializer参数，会先从iterable中取出第一个元素值，然后initializer和元素值会传给function处理；
>
> 接着再从iterable中取出第二个元素值，与function函数的返回值 再一起传给function处理，以此迭代处理完所有元素。最后一次处理的function返回值就是reduce函数的返回值。
>
> 2、如果不存在initializer参数，会先从iterable中取出第一个元素值作为initializer值，然后以此从iterable取第二个元素及以后的元素进行处理。特殊情况下，如果集合只有一个元素，则无论function如何处理，reduce返回的都是第一个元素的值。
>
> 下面我们通过具体的例子来说明。

```
from functools import reduce
CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
}

def str2float(s):
    nums = map(lambda y: CHAR_TO_FLOAT[y], s)
    point = 0
    def add(sum, x):
        nonlocal point
        if x == -1 :
            point =  1;
            return sum
        elif point == 0:
            return sum* 10 + x
        else:
            point = point * 10
            return sum + x/point            
    return reduce(add, nums)


def str2float_ini(s):
    nums = map(lambda y: CHAR_TO_FLOAT[y], s)
    point = 0
    def add(sum, x):
        nonlocal point
        if x == -1 :
            point =  1;
            return sum
        elif point == 0:
            return sum* 10 + x
        else:
            point = point * 10
            return sum + x/point            
    return reduce(add, nums,999)

t = str2float_ini('2132.213')
print(t)
t = str2float_ini('2132.213')
print(t)

```

2132.213
9992132.213
​```

```
### filter

Python内建的`filter()`函数用于过滤序列。

和`map()`类似，`filter()`也接收一个函数和一个序列。`filter()`把传入的函数依次作用于每个元素，然后根据返回值是`True`还是`False`决定保留还是丢弃该元素。

**注意**到`filter()`函数返回的是一个`Iterator`，也就是一个惰性序列，所以要强迫`filter()`完成计算结果，需要用`list()`函数获得所有结果并返回list。



### sort

Python内置的`sorted()`函数就可以对list进行排序：
```

> > > sorted([36, 5, -12, 9, -21])
> > > [-21, -12, 5, 9, 36]

```
此外，`sorted()`函数也是一个高阶函数，它还可以接收一个`key`函数来实现自定义的排序。key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。对比原始的list和经过`key=abs`处理过的list：

我们再看一个字符串排序的例子：
```

> > > sorted([‘bob’, ‘about’, ‘Zoo’, ‘Credit’])
> > > [‘Credit’, ‘Zoo’, ‘about’, ‘bob’]

```
默认情况下，对字符串排序，是按照ASCII的大小比较的，由于`'Z' < 'a'`，结果，大写字母`Z`会排在小写字母`a`的前面。

现在，我们提出排序应该忽略大小写，按照字母序排序。要实现这个算法，不必对现有代码大加改动，只要我们能用一个key函数把字符串映射为忽略大小写排序即可。忽略大小写来比较两个字符串，实际上就是先把字符串都变成大写（或者都变成小写），再比较。xx

这样，我们给`sorted`传入key函数，即可实现忽略大小写的排序：
```

> > > sorted([‘bob’, ‘about’, ‘Zoo’, ‘Credit’], key=str.lower)
> > > [‘about’, ‘bob’, ‘Credit’, ‘Zoo’]

\```

要进行反向排序，不必改动key函数，可以传入第三个参数`reverse=True`：

## 正则表达式

这个坑以后再填 https://www.runoob.com/regexp/regexp-rule.html