# @Author: Benanahai
# @Time  : 2024/11/2 12:35

"""
迭代器
迭代是 Python 最强大的功能之一，是访问集合元素的一种方式。

迭代器是一个可以记住遍历的位置的对象。

迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。

迭代器有两个基本的方法：iter() 和 next()。

字符串，列表或元组对象都可用于创建迭代器：
"""


list1 = [1, 2, 3, 4, 5]
it = iter(list1)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# print(next(it))  # Traceback (most recent call last


list1 = [1, 2, 3, 4, 5, 89, 78]
it = iter(list1)
# 使用for遍历
for x in it:
    print(x, end=" ")

print()


# StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况，
# 在 __next__() 方法中我们可以设置在完成指定循环次数后触发 StopIteration 异常来结束迭代。
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        # 在 20 次迭代后停止执行
        if self.a < 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)
for x in myiter:
    print(x)

"""
使用了 yield 的函数被称为生成器（generator）。

yield 是一个关键字，用于定义生成器函数，生成器函数是一种特殊的函数，可以在迭代过程中逐步产生值，而不是一次性返回所有结果。

跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。

当在生成器函数中使用 yield 语句时，函数的执行将会暂停，并将 yield 后面的表达式作为当前迭代的值返回。

然后，每次调用生成器的 next() 方法或使用 for 循环进行迭代时，函数会从上次暂停的地方继续执行，直到再次遇到 yield 语句。这样，生成器函数可以逐步产生值，而不需要一次性计算并返回所有结果。

调用一个生成器函数，返回的是一个迭代器对象。

下面是一个简单的示例，展示了生成器函数的使用：
"""


def countdown(n):
    while n > 0:
        yield n
        n -= 1


# 创建生成器对象
generator01 = countdown(5)
print(next(generator01))
print(next(generator01))
# 继续for循环输出
for x in generator01:
    print(x)


# 定义函数
def cry():
    print("小猫，喵喵喵")


# 调用函数
cry()
# 函数没有return时，默认返回None
result = cry()
print(result)


def cal01():
    sum = 0
    for i in range(1, 1001):
        sum += i
    print(sum)


cal01()


def cal02(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    print(sum)


cal02(88)


def get_sum(a, b):
    return a + b


print(get_sum(2, 3))


# 1 1 2 3 5 8 。。。
def rec(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return rec(n - 1) + rec(n - 2)


print(rec(8))


# 猴子吃桃
def rec02(day):
    total = 0
    if day == 10:
        total = 1
    else:
        total = (rec02(day + 1) + 1) * 2
    return total


print(rec02(1))


def rec03(n):
    if n == 1:
        return 3
    else:
        return rec03(n - 1) * 2 + 1


print(rec03(2))

sum = lambda arg1, arg2: arg1 + arg2
print(sum(10, 20))


# 汉诺塔




