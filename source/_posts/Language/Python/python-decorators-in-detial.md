---
title: python decorators in detial
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
categories:
date: 2020-10-21 13:42:12
tags:
---


简单介绍一下python装饰器的写法，妙处和应用。[原文英文链接](https://realpython.com/primer-on-python-decorators/#stateful-decorators)

<!-- more -->


首先要知道：Python’s functions are first-class objects.



```python
def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def greet_bob(greeter_func):
    return greeter_func("Bob")

>>> greet_bob(be_awesome)
'Yo Bob, together we are the awesomest!'
```

### Inner Functions

It’s possible to [define functions](https://realpython.com/defining-your-own-python-function/) *inside other functions*. Such functions are called [inner functions](https://realpython.com/inner-functions-what-are-they-good-for/).

```python
def parent():
    print("Printing from the parent() function")
    def first_child():
        print("Printing from the first_child() function")

    first_child()
```

`inner function` 调用顺序如同 `parent()`所做的效果，同时`inner function`只有在`parent()`被调用之后才会被定义成一个local variable in parent local scope。

### Returning Functions From Functions

Python also allows you to use functions as return values.

```python
# 当然这里的 fisrt_child也可以被传入
def parent():
	def first_child():
        return "Hi, I am Emma"
    # return a reference to the function.
    return first_child
>>> first = parent()
>>> first
<function parent.<locals>.first_child at 0x7f599f1e2e18>
>>>first()
'Hi, I am Emma'
```

### Introspection

一个好的函数需要有know  about its own attributes at runtime.

```python
>>> print
<built-in function print>

>>> print.__name__
'print'

>>> help(print)
Help on built-in function print in module builtins:

print(...)
    <full help message>
```

## decorator 

> 本质上还是一种 syntactic sugar

Simply, decorator wrap a function, modifying its behavior.

```python
def my_decorator(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
		return func(*args, **kwargs)
    return wrapper_do_twice

@my_decorator
def say_whee(args):
    print("whell!")
  	return f"This is My {args}"

>>> say_whee("Adam")
whell
whell
This is My Adam
```

这种**等价**的声明方式，代替了：

```python
say_wapper = my_decorator(say_whee)
```

这种说明方式虽然方便，但是减少了一定程度的代码灵活性。同时，`import`对于该语法糖定义的函数也是有效的。

> 这就是语法糖吗？

注意`say_whee`函数接受参数的情况下同样需要`wrapper_do_twice`传递参数。

### Introspection





```python
import functools

# 显示消耗时间
def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer


# 显示输入输出信息
def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           # 4
        return value
    return wrapper_debug
```



```python
# 经过装饰的函数，的help信息显示的是装饰函数的inner function
>>> say_whee
<function do_twice.<locals>.wrapper_do_twice at 0x7f43700e52f0>

>>> say_whee.__name__
'wrapper_do_twice'



>>> help(say_whee)
Help on function wrapper_do_twice in module decorators:

wrapper_do_twice()

# decorators 采用functools.wraps decorator 保存关于原来函数的信息

import functools

def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice

>>> say_whee
<function say_whee at 0x7ff79a60f2f0>

>>> say_whee.__name__
'say_whee'

>>> help(say_whee)
Help on function say_whee in module whee:

say_whee()
```

**Technical Detail:** The `@functools.wraps` decorator [uses](https://github.com/python/cpython/blob/5d4cb54800966947db2e86f65fb109c5067076be/Lib/functools.py#L34) the function `functools.update_wrapper()` to update special attributes like `__name__` and `__doc__` that are used in the introspection.



### examples

倒计时

```python
import functools
import time

def slow_down(func):
    """Sleep 1 second before calling the function"""
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down

@slow_down
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)
        

>>> countdown(3)
3
2
1
Liftoff!
```



注册者

```python
import random
PLUGINS = dict()

def register(func):
    """Register a function as a plug-in"""
    PLUGINS[func.__name__] = func
    return func

@register
def say_hello(name):
    return f"Hello {name}"

@register
def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def randomly_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f"Using {greeter!r}")
    return greeter_func(name)
```

用户登录

```python
from flask import Flask, g, request, redirect, url_for
import functools
app = Flask(__name__)

def login_required(func):
    """Make sure user is logged in before proceeding"""
    @functools.wraps(func)
    def wrapper_login_required(*args, **kwargs):
        if g.user is None:
            return redirect(url_for("login", next=request.url))
        return func(*args, **kwargs)
    return wrapper_login_required

@app.route("/secret")
@login_required
def secret():
    ...
```

## Decorating Classes

有两种方法可以在classes使用装饰器，一种对methods使用，另一种对class使用。





### method



```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    # 不可修改的属性
    @property
    def radius(self):
        """Get value of radius"""
        return self._radius

    #可设置的属性
    @radius.setter
    def radius(self, value):
        """Set radius, raise error if negative"""
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")

            
	# 无需实例调用，常用于工厂方法
    @classmethod
    def unit_circle(cls):
        """Factory method creating a circle with radius 1"""
        return cls(1)

    # 可在实例或者类中使用，可直接调用
    @staticmethod
    def pi():
        """Value of π, could use math.pi instead though"""
        return 3.1415926535
    
    
## exmaple 2
# 也可以从之前的代码库中调用 方法来decorate
from decorators import debug, timer
class TimeWaster:
    @debug
    def __init__(self, max_num):
        self.max_num = max_num

    @timer
    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_num)])
            
            
```

### class

decorator用在class上面的语法和方法装饰器一样，可以注意到上面方法`@timer`装饰器在class上的作用等同于`timer = warpper_time(TimeWaster)`，也就是返回一个`Timewaster`对象地同时计算`init()`花费时间。

```python

@timer
class TimeWaster:
    def __init__(self, max_num):
        self.max_num = max_num

    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_num)])
```

当然可以把`callable function`当成`decorator`装饰给函数。

```python
import functools

class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)

@CountCalls
def say_whee():
    print("Whee!")
    
    

```

`sya_whee()`等价于`func = CountCalls(say_whee)`，`func`就是调用`CountCalls.__call___()`。这就实现了`class decorator`的功能，同时由于class属性，自动完成了状态存储的功能。

## Nest Decorators

神经的装饰器居然还可以Nesting的，这可比函数调用方便多了！

```python

from decorators import debug, do_twice

@debug
@do_twice
def greet(name):
    print(f"Hello {name}")
    
>>> greet("Eva")
Calling greet('Eva')
Hello Eva
Hello Eva
'greet' returned None
```



Think about this as the decorators being executed in the order they are listed. In other words, `@debug` calls `@do_twice`, which calls `greet()`, or `debug(do_twice(greet()))`:



## Decorators with argument

带着参数的`decorateor`要求对装饰器理解要更上一层楼了：

`@method`指向是一个返回装饰器函数对象的函数，`@method(arsg=args)`指向是的一个带着参数的返回*返回装饰器函数对象*的函数对象。

```python
#!/usr/bin/python3
import functools 

def repeat(times):
    def decorate_repeate(func):
        @functools.wraps(func)
        def inner_repeat(*args, **kwargs):
            for _ in range(times):
                value = func(*args, **kwargs)
            return value
        return inner_repeat
    return decorate_repeat

@repeat(times=4)
def print_whee():
    print("whee!")


print_whee()
print:
whee!
whee!
whee!
whee!
```

对比以下：

```python
def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
		for x in args:
			print("This args of func is:"x)
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice
```

我认为之前的带参数的`decorator`的语法糖等价形式可以写成这样：

```python
#!/usr/bin/python3
import functools 

def repeat(times):
    def decorate_repeat(func):
        @functools.wraps(func)
        def inner_repeat(*args, **kwargs):        
            for x in args:
                print("This args of func is:", x)
            for _ in range(times):
                value = func(*args, **kwargs)
            return value
        return inner_repeat
    return decorate_repeat


def print_whee(*args, **kwargs):
    print("whee!")

# 对调用的函数返回的函数对象进行调用！
# fisrt class NB!
repeat_print_whee = repeat(times=4)(print_whee)
print(repeat_print_whee)
# print(inner_repeat)
print(print_whee)
print(repeat(times=4))
repeat_print_whee(*['hello', 'world'])
```

也就说，装饰器首先调用了`repeat(time)`，返回一个`decorate_repeat(print_whee)`的装饰器函数！接下来的步骤和之前相同。

### optional argument 

本质上来说，`repeat(time)`只不过是套了层调用的`decoreate_repeat(func)`，也就是说

```python
def repeat(_func, *, times=times):
    def decorate_repeat(func):
        @functools.wraps(func)
        def inner_repeat(*args, **kwargs):        
            for x in args:
                print("This args of func is:", x)
            for _ in range(times):
                value = func(*args, **kwargs)
            return value
        return inner_repeat
   	#调用函数
    return decorate_repeat(_func)

```

这就可以引入 可以带参数或者不带参数的`decorator`：

```python
# * 表示后面的 following parameters are keyword-only.
def repeat(_func=None, *, num_times=2):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat

    # 如果decorator带非函数参数，语法糖就会写成
    # repeat(num_time)(func)(*args……)
    # =  wrapper_repeat(*ars ……)
    if _func is None:
        return decorator_repeat
   	# 如果decorator不带参数，decorator会直接调用warpped的函数
    # 返回 wrapper_repeat函数
    else:
        return decorator_repeat(_func)
```

## Stateful decorators

有状态的`decorator`与之前所述的`decorator`的输出依赖于输入的情况，恰恰相反，它依赖于当前的状态。这也于函数式编程的理念不同。不过这里简单运用了`function attributs`

```python
#!/usr/bin/python3
import functools

def count_calls(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
        return func(*args, **kwargs)
    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls

@count_calls
def say_whee():
    print("Whee!")

say_whee()
say_whee()
say_whee()
say_whee()
print(say_whee.num_calls))

print:
Call 1 of 'say_whee'
Whee!
Call 2 of 'say_whee'
Whee!
Call 3 of 'say_whee'
Whee!
Call 4 of 'say_whee'
Whee!
4
```

更好的方式就是使用`class`作为装饰器来修饰方法，他保存状态更加方便！

上文有相关内容。









## 更多真实例子



### delay

```python
import functools
import time

def slow_down(_func=None, *, rate=1):
    """Sleep given amount of seconds before calling the function"""
    def decorator_slow_down(func):
        @functools.wraps(func)
        def wrapper_slow_down(*args, **kwargs):
            time.sleep(rate)
            return func(*args, **kwargs)
        return wrapper_slow_down

    if _func is None:
        return decorator_slow_down
    else:
        return decorator_slow_down(_func)
    
@slow_down(rate=2)
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)
```

### Singleton



用装饰器实现单例模式！用了`stateful decorator`的知识点

> A singleton is a class with only one instance. There are several singletons in Python that you use frequently, including `None`, `True`, and `False`. It is the fact that `None` is a singleton that allows you to compare for `None` using the [`is` keyword](https://realpython.com/python-is-identity-vs-equality/), like you saw in the [Both Please](https://realpython.com/primer-on-python-decorators/#both-please-but-never-mind-the-bread) section:
>
> Using `is` returns `True` only for objects that are the exact same instance.

```python
#!/usr/bin/python3
import functools


def singlenton(cls):
    @functools.wraps(cls)
    def wrap_function(*args, **kwargs):
        if not wrap_function.instance:
            wrap_function.instance = cls(*args, **kwargs)
        return wrap_function.instance
        
    # 设置是必要的
    wrap_function.instance = None
    return wrap_function

@singlenton
class iden(object):
    ...
    
singlenton.instance = "a"
print(singlenton.instance)

cls1 = iden()
cls2 = iden()
print(id(cls1))
print(id(cls2))
```

### Caching Return Value

当然也可以使用`stateful decorator`来计数、甚至cache！

```python
#!/usr/bin/python3
import functools


def count_calls(func):
    @functools.wraps(func)
    def wrap_timers(*args, **kwargs):        
        wrap_timers.times += 1
        print("This is {:^5} times when the function excuted.".format(wrap_timers.times))    
        return func(*args, **kwargs)
    wrap_timers.times = 0
    return wrap_timers


def cache(func):
    @functools.wraps(func)
    def wrap_fibonacci(*args, **kwargs):
        dic = wrap_fibonacci.cache        
        for arg in args:     
            if dic.get(arg) == None:
                dic[arg] = func(*args, **kwargs)
        return dic[arg]
            
    wrap_fibonacci.cache = {}
    return wrap_fibonacci

# @cache
@count_calls
def fibonacci(nums):
    if nums == 1 or nums == 0:
        return nums
    else :
        return fibonacci(nums - 1) + fibonacci(nums - 2)


print(fibonacci(5))
```

注意，如果去掉`@cache`，调用次数不同的哦.

### 对象转化

我们可以方便地添加function的attri，甚至直接把返回值替换成一个其他对象，减少操作的步骤。比如与和`pint`python库就是。

```python 
#!/usr/bin/python3
import math
import functools

import pint


# 设置 unit function
def set_unit(entity):
    def get_add_unit(func):
        func.unit = entity
        # @functools.wraps()
        # def wrap_unit(*args, **kwargs):
        #     func.unit = entity
            # return func(*args, **kwargs)
        return func
    return get_add_unit


# 利用修饰符 设置unit
@set_unit("m^2")
def calM(radius):
    return math.pi * radius ** 2

print(calM(3))
print(calM.unit)


# 单位转化过程
ureg = pint.UnitRegistry()
vol = calM(4) * ureg(calM.unit)
print(vol)
print(vol.to("inches ^2 "))  # Magnitude


# 利用decarotor设置unit, 返回 Quantity 对象！减少转化步骤
def use_unit(unit):
    use_unit.unit = pint.UnitRegistry()

    def decorate_use_unit(func):
        @functools.wraps(func)
        def wrap_use_unit(*args, **kwargs):
            
            return func(*args, **kwargs) * use_unit.unit(unit)

        return wrap_use_unit
    return decorate_use_unit

@use_unit("meters per hour")
def average_speed(dis, time):
    return dis / time

speed = average_speed(10, 29)
print(speed.to("km per hour"))
```

###  Validating JSON

检验JSON请求中是否有某些字段.

```python
# 原始
@app.route("/grade", methods=["POST"])
def update_grade():
    json_data = request.get_json()
    if "student_id" not in json_data:
        abort(400)
    # Update database
    return "success!"

from flask import Flask, request, abort
import functools
app = Flask(__name__)


# 验证decorator
def validate_json(*expected_args):                  # 1
    def decorator_validate_json(func):
        @functools.wraps(func)
        def wrapper_validate_json(*args, **kwargs):
            json_object = request.get_json()
            for expected_arg in expected_args:      # 2
                if expected_arg not in json_object:
                    abort(400)
            return func(*args, **kwargs)
        return wrapper_validate_json
    return decorator_validate_json

@app.route("/grade", methods=["POST"])
@validate_json("student_id")
def update_grade():
    json_data = request.get_json()
    # Update database.
    return "success!"
```

`wrappper function` 把验证部分从原代码中抽离出来，交给了验证`decorator`，而剩下的功能更加纯粹。

