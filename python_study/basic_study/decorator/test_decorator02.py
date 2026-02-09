# -*- coding: utf-8 -*-
"""
@Author: wangzs22
@Time: 2026/02/09 17:47:26
@Desc: python 装饰器学习
"""
import time
import pandas as pd


#! 1. 函数装饰器
# 不带参数的装饰器
def my_wrapper(func):
    """自定义装饰器, 打印函数执行时间"""
    def wrapper(*args, **kwargs):
        st = time.time()
        res = func(*args, **kwargs) # 执行被装饰的函数
        et = time.time()
        print("函数%s 运行时间为: %s" % (func.__name__, et - st))
        return res
    return wrapper

# 调用装饰器
@my_wrapper
def test_my_wrapper():
    time.sleep(2)
    print("in the func")


# 带参数的装饰器
def my_wrapper02(max_attempts):
    """失败重试装饰器"""
    #! 装饰器的参数 max_attempts 是外部参数，用于指定最大重试次数。
    #! 内部函数 decorator 是装饰器的核心，它接收被装饰的函数 func 作为参数。
    #! 内部函数 wrapper 是实际执行装饰逻辑的函数，它在每次调用 func 前检查是否需要重试。
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

# 调用装饰器
@my_wrapper02(3)
def test_my_wrapper02():
    import random
    if random.random() < 0.8:
        raise ValueError("API 调用失败")
    return "成功"

def to_execl(file_path: str):
    """将 DataFrame 写入 Excel 文件"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            if isinstance(res, pd.DataFrame) and not res.empty:
                res.to_excel(file_path, index=False)
                print(f"DataFrame 已成功写入 {file_path}")
            return res
        return wrapper
    return decorator

# 调用装饰器
@to_execl(file_path="test.xlsx")
def test_to_execl():
    import pandas as pd
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    return df


if __name__ == "__main__":
    # test_my_wrapper()
    # print(test_my_wrapper02())
    test_to_execl()

    