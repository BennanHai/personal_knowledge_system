[第18天：Python 之迭代器](https://mp.weixin.qq.com/s?__biz=MzkxNDI3NjcwMw==&mid=2247493320&idx=1&sn=3112931b76710ec4799acf58ca149047&chksm=c1724ef8f605c7ee4cc44194d6176c2456efdf138d4a33ed92834e8a66f33a23ef2fb3f14efb&scene=21#wechat_redirect)



对于迭代器对象本身来说，需要具有\`\_\_iter\_\_()\`^[2]^和\`\_\_next\_\_()\`^[3]^两种方法，二者合称为“**迭代器协议**”。也就是说，只要同时具有这两种方法，Python 解释器就会认为该对象是一个迭代器；反之，只具有其中一个方法或者二者都不具有，解释器则认为该对象不是一个迭代器。



在Python中，迭代器是处理可迭代对象的核心机制，支持高效的数据遍历。以下是迭代器的详细解析：

---

### 一、迭代器与可迭代对象

1. **可迭代对象（Iterable）**
   定义：实现了 `__iter__()` 方法或 `__getitem__()` 方法的对象，可以被遍历。
   常见类型：列表、元组、字典、字符串、文件对象等。
   验证方法：

   ```python
   from collections.abc import Iterable
   print(isinstance([1,2,3], Iterable))  # True
   ```
2. **迭代器（Iterator）**定义：实现了 `__iter__()` 和 `__next__()` 方法的对象，用于逐个访问元素。特性：

   - 单向遍历，不能回退。
   - 遍历结束后抛出 `StopIteration` 异常。
     验证方法：

   ```python
   from collections.abc import Iterator
   print(isinstance(iter([1,2,3]), Iterator))  # True
   ```

---

### 二、迭代器协议

迭代器必须满足以下条件：

1. 实现 `__iter__()` 方法，返回自身（即 `self`）。
2. 实现 `__next__()` 方法，返回下一个元素，无元素时抛出 `StopIteration`。


有了上面的讨论，我们就可以自己实现一个简单的迭代器。只要确保这个简单迭代器具有与迭代器定义相符的行为即可。

说人话就是：要定义一个数据类型，具有`__iter__()`方法并且该方法返回一个带有`__next__()`方法的对象，而当该类已经具有`__next__()`方法时则返回其本身。示例代码如下：

```
class Reverse:
    """反向遍历序列对象的迭代器"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)


    def __iter__(self):
        return self


    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
```

验证一下：

```
>>> rev = Reverse('justdopython.com')
>>> next(rev)
'm'
>>> next(rev)
'o'
>>> next(rev)
'c'
>>> next(rev)
'.'
```


**示例2：自定义迭代器**

```python
class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        num = self.current
        self.current -= 1
        return num

# 使用
for num in CountDown(3):
    print(num)  # 输出 3, 2, 1
```

---

### 三、生成器：简化迭代器创建

生成器通过 `yield` 关键字自动实现迭代器协议，无需手动定义 `__iter__()` 和 `__next__()`。

1. **生成器函数**

   ```python
   def fibonacci(max):
       a, b = 0, 1
       while a < max:
           yield a
           a, b = b, a + b

   for num in fibonacci(10):
       print(num)  # 输出 0, 1, 1, 2, 3, 5, 8
   ```
2. **生成器表达式**
   语法类似列表推导式，使用圆括号：

   ```python
   squares = (x**2 for x in range(5))
   print(list(squares))  # [0, 1, 4, 9, 16]
   ```

---

### 四、操作迭代器的内置函数

1. **`iter()`**
   将可迭代对象转换为迭代器。

   ```python
   my_list = [1, 2, 3]
   it = iter(my_list)
   ```
2. **`next()`**
   获取迭代器的下一个元素。

   ```python
   print(next(it))  # 1
   print(next(it))  # 2
   ```

---

### 五、应用场景

1. **处理大型数据集**
   逐行读取文件，避免内存溢出：

   ```python
   with open('large_file.txt') as f:
       for line in f:
           process(line)
   ```
2. **无限序列**
   生成器可表示无限序列（如斐波那契数列、传感器数据流）。
3. **惰性求值**
   按需生成数据，提升效率。

---

### 六、注意事项

- 迭代器是“一次性”的，遍历后需重新创建。
- 避免在迭代过程中修改可迭代对象。
- 使用 `try...except` 处理 `StopIteration`。

---

### 总结

迭代器是Python遍历数据的核心机制，通过 `__iter__` 和 `__next__` 实现协议。生成器简化了迭代器的创建，适用于高效处理大数据和惰性求值场景。理解迭代器可提升代码性能和资源管理能力。
