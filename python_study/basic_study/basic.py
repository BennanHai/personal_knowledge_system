
"""
推导式
"""

import sys


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
    
    # 双重循环
    pairs = [(x, y) for x in range(3) for y in range(3)]
    print(pairs)
    # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

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
    
    # 交换键值对
    original = {"a": 1, "b": 2, "c": 3}
    swapped = {value: key for key, value in original.items()}
    print(swapped)  # {1: 'a', 2: 'b', 3: 'c'}

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
    
def test_tuple_comprehension():
    """
    元组推导式
    """
    # 创建一个元组，将列表中各字符串的长度组成元组
    tuple01 = (len(i) for i in ['Google','Runoob', 'Taobao'])
    print(tuple01)  # <generator object test_tuple_comprehension.<locals>.<genexpr> at 0x000001D1A1B73140>
    print(type(tuple01))  # <class 'generator'>  也是一个生成器对象
    print(tuple(tuple01))  # (6, 6, 6)
    
    # 
    a = (x for x in range(1,10))
    print(a)  # <generator object test_tuple_comprehension.<locals>.<genexpr> at 0x000001D1A1B73140>
    print(tuple(a))  # (1, 2, 3, 4, 5, 6, 7, 8, 9)
    

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



"""
迭代器
"""
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
        

"""
生成器
"""
def test_generator():
    """
    生成器
    """
    # 创建生成器对象
    gen01 = (x for x in range(1,10))  # 生成器对象，也是元组
    print(gen01)  # <generator object test_generator.<locals>.<genexpr> at 0x000001D1A1B73140>
    print(type(gen01))  # <class 'generator'>
    print(next(gen01))  # 1
    print(next(gen01))  # 2

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
          


if __name__ == '__main__':
    # # 测试列表推导式
    # test_list_comprehension()
    # # 测试字典推导式
    # test_dict_comprehension()
    # # 测试集合推导式
    # test_set_comprehension()
    # # 测试元组推导式
    # test_tuple_comprehension()
    # 测试性能
    test_comprehension_time()
    
    
    ## 测试迭代器
    # test_iterator()
    
    # # 测试自定义迭代器
    # my_iter = MyIter(20)
    # for i in my_iter:
    #     print(i)
    
    # 测试生成器
    # test_generator()
    
    # test_generator_function()
    
    # test_generator_fubonacci(7)
    

    