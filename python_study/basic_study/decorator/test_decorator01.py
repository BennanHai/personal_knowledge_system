# @Author: Benanahai
# @Time  : 2025/3/22 23:11 
# @Desc  :
import random
import time

# 函数装饰器
def my_wrapper(func):
    """自定义装饰器, 打印函数执行时间"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs) # 执行被装饰的函数
        stop_time = time.time()
        print("函数%s 运行时间为: %s" % (func.__name__, stop_time - start_time))
        return res
    return wrapper

# 调用装饰器
@my_wrapper
def test_task():
    time.sleep(1)
    print("in the func")


# 带参数的装饰器
def my_wrapper2(max_attempts):
    """失败重试装饰器"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    print(f"重试第 {attempts} 次，错误：{e}")
            return None
        return wrapper
    return decorator

@my_wrapper2(3)
def test_task2():
    import random
    if random.random() < 0.8:
        raise ValueError("API 调用失败")
    return "成功"


print(test_task2())


# 类装饰器
# 通过实现 __call__ 方法让类的实例可调用：
class LogContext:
    """记录函数调用上下文的类装饰器"""
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"开始执行 {self.func.__name__}")
        result = self.func(*args, **kwargs)
        print(f"结束执行 {self.func.__name__}")
        return result

@LogContext
def hello(name):
    print(f"Hello, {name}!")

hello("Alice")
# 输出：
# 开始执行 hello
# Hello, Alice!
# 结束执行 hello


#
# 保留原函数的元信息
# 装饰器会覆盖原函数的 __name__、__doc__ 等元信息。使用 functools.wraps 修复：
from functools import wraps

def debug(func):
    @wraps(func)  # 保留原函数元信息
    def wrapper(*args, **kwargs):
        print(f"调试：调用 {func.__name__}()")
        return func(*args, **kwargs)
    return wrapper

@debug
def say_hello():
    """打招呼函数"""
    print("Hello!")

print(say_hello.__name__)  # 输出 "say_hello"
print(say_hello.__doc__)   # 输出 "打招呼函数"
