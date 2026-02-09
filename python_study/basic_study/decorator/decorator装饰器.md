[第20天：Python 之装饰器](https://mp.weixin.qq.com/s?__biz=MzkxNDI3NjcwMw==&mid=2247493322&idx=1&sn=7aab5f18a2d643b19b12e133e23fa816&chksm=c1724efaf605c7ec736408874093fc8b414c675a0f6bfffb2dfd5bf28de4612f67e6f7a573f3&scene=21#wechat_redirect)


## 1. 概念介绍

**装饰器**（decorator），又称“装饰函数”，即一种返回值也是函数的函数，可以称之为“函数的函数”。其目的是在不对现有函数进行修改的情况下，实现额外的功能。最基本的理念来自于一种被称为“装饰模式”的设计模式。

装饰器（Decorator）是 Python 的一个重要特性，它可以让程序员在不修改代码的情况下，对函数进行扩展， 动态增强函数的功能。

> 语法糖：指计算机语言中添加的某种语法，这种语法对语言的功能并没有影响，但是更方便程序员使用。通常来说使用语法糖能够增加程序的可读性，从而减少程序代码出错的机会。

本质是一个可调用对象（函数或者类），它接受一个函数作为参数，并返回一个新的函数或类。

装饰器的语法使用 @decorator_name 来应用在函数或方法上。

装饰器的应用场景：
- 日志记录: 装饰器可用于记录函数的调用信息、参数和返回值。
- 性能分析: 可以使用装饰器来测量函数的执行时间。
- 权限控制: 装饰器可用于限制对某些函数的访问权限。
- 缓存: 装饰器可用于实现函数结果的缓存，以提高性能。


## 2.基本语法
解析：decorator 是一个装饰器函数，它接受一个函数 func 作为参数，并返回一个内部函数 wrapper，在 wrapper 函数内部，你可以执行一些额外的操作，然后调用原始函数 func，并返回其结果。

decorator_function 是装饰器，它接收一个函数 original_function 作为参数。
wrapper 是内部函数，它是实际会被调用的新函数，它包裹了原始函数的调用，并在其前后增加了额外的行为。
当我们使用 @decorator_function 前缀在 target_function 定义前，Python会自动将 target_function 作为参数传递给 decorator_function，然后将返回的 wrapper 函数替换掉原来的 target_function。
```python
def decorator_function(original_function):
    def wrapper(*args, **kwargs):
        # 这里是在调用原始函数前添加的新功能
        before_call_code()
        
        result = original_function(*args, **kwargs)
        
        # 这里是在调用原始函数后添加的新功能
        after_call_code()
        
        return result
    return wrapper

# 使用装饰器
@decorator_function
def target_function(arg1, arg2):
    pass  # 原始函数的实现
```

## 3.内置装饰器
Python 提供了一些内置的装饰器，用于常见的场景。

- @staticmethod: 用于定义静态方法，静态方法不依赖于实例，只能通过类名调用。
- @classmethod: 用于定义类方法，类方法第一个参数是类本身，而不是实例。
- @property: 用于定义属性，通过属性可以直接访问类的属性，而不需要调用方法。
- @abstractmethod: 用于定义抽象方法，抽象方法必须在子类中实现。

