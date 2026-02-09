# python学习笔记
# 推导式
python 推导式是一种独特的数据处理方式，它可以从一个数据序列中创建另一个新的数据序列。
Python 推导式是一种强大且简洁的语法，适用于生成列表、字典、集合和生成器。
Python 支持各种数据结构的推导式：
- 列表(list)推导式
- 字典(dict)推导式
- 集合(set)推导式
- 元组(tuple)推导式

## 列表推导式
列表推导式是一种创建列表的简单方法。格式如下：
```python
[表达式 for 变量 in 列表]

# 或者
[表达式 for 循环变量 in 列表 if 条件]
```

```python
def test_list_comprehension():
    """
    列表推导式
    """
    # 过滤掉长度小于或等于3的字符串列表，并将剩下的转换成大写字母：
    names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
    names_new = [name.upper() for name in names if len(name) >= 3]
    print(names_new) # ['BOB', 'TOM', 'ALICE', 'JERRY', 'WENDY', 'SMITH']

    # 30 以内能被3整除的数
    nums = [x for x in range(30) if x % 3 == 0]
    print(f"能能被3整除的数: {nums}")  # 能能被3整除的数: [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

```

## 字典推导式
字典推导式是一种创建字典的简单方法。格式如下：
```python
{key: value for 变量 in 列表}
# 或者
{key: value for 循环变量 in 列表 if 条件}
```

```python
def test_dict_comprehension():
    """
    字典推导式
    """
    # 创建一个字典，键是1到5，值是键的平方
    nums = {x: x ** 2 for x in range(1, 6)}
    print(nums) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

    # 将列表中各字符串值为键，各字符串的长度为值，组成键值对
    listdemo = ['Google','Runoob', 'Taobao']
    newdict = {key:len(key) for key in listdemo}
    print(newdict) # {'Google': 6, 'Runoob': 6, 'Taobao': 6}
```


## 集合推导式
集合推导式是一种创建集合的简单方法。格式如下：
```python
{表达式 for 变量 in 列表}
# 或者
{表达式 for 循环变量 in 列表 if 条件}
```

```python
def test_set_comprehension():
    """
    集合推导式
    """
    # 创建一个集合，平方数
    setnew = {i**2 for i in (1,2,3)}
    print(setnew)  # {1, 4, 9}

    # 创建一个集合，将列表中各字符串长度的值组成集合
    set01 = {len(i) for i in ['Google','Runoob', 'Taobao']}
    print(set01)  # {6}
```

## 元组推导式
元组推导式可以利用 range 区间、元组、列表、字典和集合等数据类型，快速生成一个满足指定需求的元组。
元组推导式是用 () 圆括号将各部分括起来，而列表推导式用的是中括号 []，另外元组推导式返回的结果是一个生成器对象。
格式：
```python
(expression for item in Sequence )
或
(expression for item in Sequence if conditional )
```

```python
def test_tuple_comprehension():
    """
    元组推导式
    """
    # 创建一个元组，将列表中各字符串的长度组成元组
    tuple01 = (len(i) for i in ['Google','Runoob', 'Taobao'])
    print(tuple01)  # <generator object test_tuple_comprehension.<locals>.<genexpr> at 0x000001D1A1B73140>
    print(tuple(tuple01))  # (6, 6, 6)
    
    # 
    a = (x for x in range(1,10))
    print(a)  # <generator object test_tuple_comprehension.<locals>.<genexpr> at 0x000001D1A1B73140>
    print(tuple(a))  # (1, 2, 3, 4, 5, 6, 7, 8, 9)
    
    
```

## 高级用法
```python
# 三元表达式结合
numbers = [-5, 3, -2, 9, 0]
result = ["positive" if x > 0 else "negative" if x < 0 else "zero" for x in numbers]
print(result)  # ['negative', 'positive', 'negative', 'positive', 'zero']

# 同时迭代键值对
dict1 = {'a': 1, 'b': 2, 'c': 3}
new_dict = {k.upper(): v*2 for k, v in dict1.items()}
print(new_dict)  # {'A': 2, 'B': 4, 'C': 6}

```

## 新能对比
列表推导式比循环创建列表更简洁，并且速度更快。
```python
def test_comprehension_time():
    """
    测试性能
    """
    import time

    # 列表推导式 vs 传统循环
    size = 10000000

    # 传统循环
    start = time.time()
    result = []
    for i in range(size):
        result.append(i**2)
    end = time.time()
    print(f"传统循环: {end-start:.4f}秒")

    # 列表推导式
    start = time.time()
    result = [i**2 for i in range(size)]
    end = time.time()
    print(f"列表推导式: {end-start:.4f}秒")

# 传统循环: 6.0415秒
# 列表推导式: 4.5801秒
```
## 注意事项
推导式让代码更简洁，但要注意保持可读性，复杂的逻辑建议使用传统循环。

- 可读性优先：复杂的推导式可能难以理解，应考虑拆分
- 避免过度嵌套：超过两层的嵌套推导式，应考虑拆分
- 内存考虑：列表推导式会生成完整列表，大数据时考虑生成器
- 作用域：Python 3.x中推导式有独立作用域



# 迭代器
迭代是 Python 最强大的功能之一，是访问集合元素的一种方式。
迭代器是一个可以记住遍历的位置的对象。迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能被访问一次，访问结束后，再次访问会重新开始。
迭代器只能往前不会后退。
迭代器有两个基本的方法：iter() 和 next()。字符串，列表或元组对象都可用于创建迭代器：

>可迭代对象 vs 迭代器
```python
# 可迭代对象 (Iterable)：实现了 __iter__() 方法
# 迭代器 (Iterator)：实现了 __iter__() 和 __next__() 方法

my_list = [1, 2, 3]           # 可迭代对象
my_iter = iter(my_list)       # 迭代器

print(hasattr(my_list, '__iter__'))   # True - 可迭代对象
print(hasattr(my_list, '__next__'))   # False - 不是迭代器
print(hasattr(my_iter, '__next__'))   # True - 是迭代器
```


```python
def test_iterator():
    """
    迭代器
    """
    list01 = [1,2,3,4,5,6]
    iter01 = iter(list01) # 创建迭代器对象
    print(next(iter01)) # 1
    print(next(iter01)) # 2
    print(next(iter01)) # 3
    
    # 也可以使用for循环迭代迭代器对象
    iter02 = iter(list01)
    for i in iter02:
        print(i)

    # 也可以使用next()函数
    iter03 = iter(list01)
    while True:
        try:
            print(next(iter03))
        except StopIteration:
            break
```


把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__() 。
如果对象是迭代器，那么它的 __iter__() 方法会返回它自己，__next__() 方法会返回下一个值，如果没有后续值，则抛出 StopIteration 异常。
```python
class MyIter:
    """
    自定义迭代器
    实现自定义迭代器，需要实现__iter__()和__next__()两个方法

    __iter__()方法返回迭代器对象本身
    __next__()方法返回下一个元素，如果没有下一个元素，则抛出StopIteration异常
    StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况，在 __next__() 方法中我们可以设置在完成指定循环次数后触发 StopIteration 异常来结束迭代。
    """
    def __init__(self, num):
        self.num = num # 输入的数字
        self.current = 5 # 初始数值为5

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.num:
            current = self.current
            self.current += 5  # 下一个数加5
            return current
        else:
            print("迭代完成")
            raise StopIteration 
        

class CountDown:
    """倒计时迭代器"""
    def __init__(self, start):
        self.current = start
        self.start = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        else:
            value = self.current
            self.current -= 1
            return value

# 使用自定义迭代器
countdown = CountDown(5)
for number in countdown:
    print(number)  # 5, 4, 3, 2, 1
```


# 生成器
在 Python 中，使用了 yield 的函数被称为生成器（generator）。
yield 是一个关键字，用于定义生成器函数，生成器函数是一种特殊的函数，可以在迭代过程中逐步产生值，而不是一次性返回所有结果。
跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
当在生成器函数中使用 yield 语句时，函数的执行将会暂停，并将 yield 后面的表达式作为当前迭代的值返回。然后，每次调用生成器的 next() 方法或使用 for 循环进行迭代时，函数会从上次暂停的地方继续执行，直到再次遇到 yield 语句。这样，生成器函数可以逐步产生值，而不需要一次性计算并返回所有结果。

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

def test_generator_function():
    """
    生成器函数
    """
    # 创建生成器对象
    gen02 = countdown(5)
    print(gen02)  # <generator object countdown at 0x000001D1A1B73140>
    print(type(gen02))  # <class 'generator'>
    
    # 通过迭代生成器获取值
    print(next(gen02))
    print(next(gen02))
    print(next(gen02))
    print(next(gen02))
    # print(next(gen02))
    # print(next(gen02)) # 如果迭代器没有更多的元素，则抛出StopIteration异常
    

    # 或者通过for循环迭代生成器获取值
    for i in gen02:
        print(f"for循环中{i}")
```

生成器函数的优势是它们可以按需生成值，避免一次性生成大量数据并占用大量内存。此外，生成器还可以与其他迭代工具（如for循环）无缝配合使用，提供简洁和高效的迭代方式。

```python
def fubonacci(n):
    """
    生成斐波那契数列
    """
    a, b, counter = 0, 1, 0
    while True:
        if counter > n: 
            return
        yield a
        a, b = b, a + b
        counter += 1

def test_generator_fubonacci(n):
    # 创建生成器对象
    gen03 = fubonacci(n)
    print(gen03)  # <generator object fubonacci at 0x000001D1A1B73140>
    print(type(gen03))  # <class 'generator'>
    
    # 通过迭代生成器获取值
    while True:
        try:
            print (next(gen03), end=" ")
        except StopIteration:
            sys.exit()
```


# 装饰器
- [详见装饰器](/python_study/basic_study/decorator/decorator装饰器.md)



