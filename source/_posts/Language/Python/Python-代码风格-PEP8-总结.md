---
title: Python 代码风格 PEP8 总结
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
categories:
date: 2020-10-31 22:44:09
tags:
---





# [Python 代码风格 PEP8 总结](https://pep8.org/#descriptive-naming-styles)



首先，要保持整个项目的代码风格一致，这一点甚至比遵循PEP8代码风格更加重要。

花在阅读代码的时间远远比比写代码的时间要长，提升代码的可读性`readability`，让整个代码风格的一致，非常重要。

总体来说：

<!-- more -->

+ 提升代码可读性
+ 避免对其他人写的、以前写的、支持过去的特性的的代码进行重构、或者修改

## Code Lay-out

### Indentation

Use 4 spaces per indentation level.

Continuation lines should align wrapped elements either **vertically using Python’s implicit line** joining inside parentheses, brackets and braces, or using a ***hanging indent*** [3](https://pep8.org/#fn3). When using a hanging indent the following should be considered; there should be **no arguments on the first line** and **further indentation** should be used to clearly distinguish itself as a continuation line.

> 应当有两种书写跨行代码的方式：
>
> + 第一行带参数，并保持第二行与第一行垂直对齐
> + 第一行不带参数，剩下的行数保持对齐
>   + 需要有更多的缩进来保持与其他代码的不同

```python

# Aligned with opening delimiter.
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# More indentation included to distinguish this from the rest.
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# Hanging indents should add a level.
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)

# Add some extra indentation on the conditional continuation line.
if (this_is_one_thing
        and that_is_another_thing):
    do_something()
    

result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
)


```



### Tap?

Python 3 disallows mixing the use of tabs and spaces for indentation.

### Maximum Line Length



Limit all lines to a maximum of 79 characters.

这么做有利于：

+ 在编辑器中可以快速浏览水平排列的多个程序文件
+ 保持一行代码的的简洁性



### Break a line from binary operator 



```python

# No: operators sit far away from their operands
income = (gross_wages +
          taxable_interest +
          (dividends - qualified_dividends) -
          ira_deduction -
          student_loan_interest)
```

通常的二元操作符的分割方法如上所示，但是这样破环了操作符和操作数的连续性，更好的方法是把`operator`放在前面。

```python
# Binary operation

## Yes: easy to match operators with operands
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)
```



### Blank Lines

Surround top-level function and class **definitions** with two blank lines.

Method **definitions** inside a class are surrounded by a single blank line.

### Source File Encoding

Code in the core Python3 distribution should always use UTF-8.



### Import*



Imports should usually be on separate lines, e.g.:

Yes:

```python
import os
import sys
#It’s okay to say this though:

from subprocess import Popen, PIPE
```

Imports are always put **at the top of the file**, just after any module comments and docstrings, and before module globals and constants.

Imports should be grouped in the following order:

1. standard library imports
2. related third party imports
3. local application/library specific imports

You should put a blank line between each group of imports.

**Absolute imports** are recommended, as they are usually more readable and tend to be better behaved.

```python
import mypkg.sibling
from mypkg import sibling
from mypkg.sibling import example
```

However, explicit relative imports are an **acceptable alternative** to absolute imports, especially when dealing with complex package layouts where using absolute imports would be unnecessarily verbose:

```python
from . import sibling
from .sibling import example
```





### Whitespace in Expressions and Statements

Immediately **inside** parentheses, brackets or braces:

Yes:

```python
spam(ham[1], {eggs: 2})
```

No:

```python
spam( ham[ 1 ], { eggs: 2 } )
```

Between a **trailing comma** and a following close parenthesis:

Yes:

```python
foo = (0,)
```

No:

```python
bar = (0, )
```

Immediately before a comma, semicolon, or colon:

Yes:

```python
if x == 4: print x, y; x, y = y, x
```

No:

```python
if x == 4 : print x , y ; x , y = y , x
```

However, in a slice the colon acts like a binary operator, and should have equal amounts on either side (treating it as the operator with the lowest priority). In an extended slice, both colons must have the same amount of spacing applied. Exception: when a slice parameter is omitted, the space is omitted.

> 注意下面实例中最后一个例子

Yes:

```python
ham[1:9], ham[1:9:3], ham[:9:3], ham[1::3], ham[1:9:]
ham[lower:upper], ham[lower:upper:], ham[lower::step]
# 和最后一个对比一下，似乎带有某种运算优先级的暗示
ham[lower+offset : upper+offset]
ham[: upper_fn(x) : step_fn(x)], ham[:: step_fn(x)]
# 
ham[lower + offset : upper + offset]
```

No:

```python
ham[lower + offset:upper + offset]
ham[1: 9], ham[1 :9], ham[1:9 :3]
ham[lower : : upper]
ham[ : upper]
```

Immediately before the open parenthesis that starts the argument list of a function call:

Yes:

```python
spam(1)
```

No:

```python
spam (1)
```

Immediately before the open parenthesis that starts an indexing or slicing:

Yes:

```python
dct['key'] = lst[index]
```

No:

```python
dct ['key'] = lst [index]
```

More than one space around an assignment (or other) operator to align it with another.

Yes:

```python
x = 1
y = 2
long_variable = 3
```

No:

```python
x             = 1
y             = 2
long_variable = 3
```

### Other Recommendations

**Avoid trailing whitespace** anywhere. Because it’s usually invisible, it can be confusing: e. g. a backslash followed by a space and a newline does not count as a line continuation marker. Some editors don’t preserve it and many projects (like CPython itself) have pre-commit hooks that reject it.

Always **surround these binary operators with a single space** on either side: assignment (`=`), augmented assignment (`+=`, `-=` etc.), comparisons (`==`, `<`, `>`, `!=`, `<>`, `<=`, `>=`, `in`, `not in`, `is`, `is not`), Booleans (`and`, `or`, `not`).

If operators with different **priorities** are used, consider a**dding whitespace around the operators with the lowest priority(ies)**. Use your own judgment; however, never use more than one space, and always have the same amount of whitespace on both sides of a binary operator.



**Don’t** use spaces around the `=` sign when used to indicate a **keyword argument** or a default parameter value.

> 与下面第二条不同

Yes:

```python
def complex(real, imag=0.0):
    return magic(r=real, i=imag)
```

No:

```python
def complex(real, imag = 0.0):
    return magic(r = real, i = imag)
```

**Function annotations** should use the normal rules for colons and always have spaces around the `->` arrow if present. (See [Function Annotations](https://pep8.org/#function-annotations) below for more about function annotations.)

Yes:

```python
def munge(input: AnyStr): ...
def munge() -> AnyStr: ...
```

No:

```python
def munge(input:AnyStr): ...
def munge()->PosInt: ...
```

When combining an **argument annotation with a default value**, use spaces around the `=` sign (but only for those arguments that have both an annotation and a default).

Yes:

```python
def munge(sep: AnyStr = None): ...
def munge(input: AnyStr, sep: AnyStr = None, limit=1000): ...
```

No:

```python
def munge(input: AnyStr=None): ...
def munge(input: AnyStr, limit = 1000): ...
```

**Compound statements** (multiple statements on the same line) are generally discouraged.

> 简洁还是简洁

Yes:

```python
if foo == 'blah':
    do_blah_thing()
do_one()
do_two()
do_three()
```

Rather not:

```python
if foo == 'blah': do_blah_thing()
do_one(); do_two(); do_three()
```



Trailing Commas 

> commas: `,`

Trailing commas常常用在tuple中的数据分割，我们常常推荐使用圆括号来包含数据和逗号。

```python

FILES = ('setup.cfg',)
```

在List中每一项划分为一行，并把括号分割在下一行中。

```python

FILES = [
    'setup.cfg',
    'tox.ini',
    ]

initialize(FILES,
           error=True,
           )
```



## Comments

Tips:

+ update comments when code is changed
+ never alter the **case of identifiers**
+ be complete sentence
+ write in English

### Block Comments

+ are intended to the same level as that code 
+ starts with a # and a single space.

### Inline Comments

+ Use inline comments **sparingly**(简洁的)
+ Inline comments should be separated by at least two spaces from the statement. They should start with a # and a single space.

### Documentation Strings

Write docstrings for all public modules, functions, classes, and methods. Docstrings are not necessary for non-public methods, but you should have a comment that describes what the method does. This comment should appear after the `def` line.

the `"""` that ends a multiline docstring should be on a line by itself, e.g.:

```python
"""Return a foobang

Optional plotz says to frobnicate the bizbaz first.
"""
```



## Naming Conventions 

### Overriding Principle

Names that are visible to the user as public parts of the API should follow conventions that reflect usage rather than implementation.

> 面向外部的命名其含义远大于实施意义。

### Naming Style3

命名的方式多种多样。

有一种独特的命名方式，是在函数和变量前加一个`short unique prefix` 去聚合相关的名字函数，但是Python用对象名代替了这种功能。

### Leading or trailing undrescores 下划线添加规则

- `_single_leading_underscore`: weak “internal use” indicator. E.g. `from M import *` does **not import** objects whose name starts with an underscore.

- 

- `single_trailing_underscore_`: used by convention to **avoid conflicts** with Python keyword, e.g.:

  ```python
  Tkinter.Toplevel(master, class_='ClassName')
  ```

- `__double_leading_underscore`: when naming a class attribute, i**nvokes name mangling** (inside class FooBar, `__boo` becomes `_FooBar__boo`; see below).

  > To avoid name clashes with subclasses, use two leading underscores to invoke Python’s name mangling rules.
  >
  > Python mangles these names with the class name: if class Foo has an attribute named `__a`, it cannot be accessed by `Foo.__a`. (An insistent user could still gain access by calling `Foo._Foo__a`.) Generally, double leading underscores should be used only to avoid name conflicts with attributes in classes designed to be subclassed.

  

- `__double_leading_and_trailing_underscore__`: “**magic” objects or attributes** that live in user-controlled namespaces. E.g. `__init__`, `__import__` or `__file__`. Never invent such names; only use them as documented.

### Never use indistinguishable name

 Never use the characters ‘l’ (lowercase letter el), ‘O’ (uppercase letter oh), or ‘I’ (uppercase letter eye) as single character variable names.

### Package and Module Names

Modules should have short, all-lowercase names. Underscores can be used in the module name if it improves readability. 

>  the C/C++ module has a leading underscore 

### Class Names

Class names should normally use the CapWords convention.

### Type variable names

> 没懂？？？

Names of type variables introduced in PEP 484 should normally use CapWords preferring short names: `T`, `AnyStr`, `Num`. It is recommended to add suffixes `_co` or `_contra` to the variables used to declare covariant or contravariant behavior correspondingly. Examples

```python
from typing import TypeVar

  VT_co = TypeVar('VT_co', covariant=True)
  KT_contra = TypeVar('KT_contra', contravariant=True)
```

### Exception Names

Because exceptions should be classes, the class naming convention applies here. However, you should use the **suffix “Error”** on your exception names (if the exception actually is an error).

### Global Variable Names

> 对于不想被其他文件导入的变量和函数，使用`__all__ mechdanism或者使用prefixing an undersocre.

(Let’s hope that these variables are meant for use inside one module only.) The conventions are about the same as those for functions.

Modules that are designed for use via `from M import *` should use the `__all__` mechanism to prevent exporting globals, or use the older convention of prefixing such globals with an underscore (which you might want to do to indicate these globals are **“module non-public”**).



### Function Names

Function names should be **lowercase**, with words separated by **underscores** as necessary to improve readability.



### Function and method arguments

Always use `self` for the first argument to instance methods.

Always use `cls` for the first argument to class methods.

If a function argument’s name clashes with a reserved keyword, it is generally better to append a single trailing underscore rather than use an abbreviation or spelling corruption. Thus `class_` is better than `clss`. (Perhaps better is to avoid such clashes by using a synonym.)

> The difference between `cls` and `self`
>
> `cls` implies that method belongs to the class while self implies that the method is related to instance of the class,therefore member with `cls` is accessed by class name where as the one with self is accessed by instance of the class...it is the same concept as `static member` and `non-static members` in java if you are from java background.

### Constants

Constants are **usually defined on a module level** and written in **all capital letters** **with underscores separating** words. Examples include `MAX_OVERFLOW` and `TOTAL`.



## Designing for inheritance



Always decide whether a class’s methods and instance variables (collectively: “attributes”) should be public or non-public. If in doubt, choose non-public; it’s easier to make it public later than to make a public attribute non-public.

如果需要暴露公共属性，必须保证向后兼容性（后来的代码），尽量设置属性为私有。

特别对于父类，需要仔细考虑代码的

### Public and internal interfaces

所有没有被文档记载的属性和方法都应该是私有的，也就是说文档记载的属性可以是私有的或者是公共的。

To better support **introspection**, modules should explicitly declare the names in their public API using the `__all__` attribute. Setting `__all__` to an **empty** list indicates that the module has no public API.



### Programming Recommendation



**少用的lambda表达式:**

Yes:

```python
def f(x): return 2*x
```

No:

```python
f = lambda x: 2*x
```

The first form means that the name of the resulting function object is specifically ‘f’ instead of the generic ‘<lambda>’. This is more useful for **tracebacks** and string representations in general. The use of the assignment statement eliminates the sole benefit a lambda expression can offer over an explicit def statement (i.e. that it can be embedded inside a larger expression).



### 在`try`语句中尽量少用的语句。

### 坚持在函数末尾返回`None`或者应该有的表达式

### Use `''.startswith()` and `''.endswith()` instead of string slicing to check for prefixes or suffixes

> 更快

### Object type comparisons should always use `isinstance()` instead of comparing types directly:

Yes:

```python
if isinstance(obj, int):
```



### For sequences, (strings, lists, tuples), use the fact that empty sequences are false:

Yes:

```python
if not seq:
if seq:
```

### Don’t compare boolean values to True or False using `==`:

Yes:

```python
if greeting:
```

Worse:

```python
if greeting is True:
```