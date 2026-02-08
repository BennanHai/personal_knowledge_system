# @Author: Benanahai
# @Time  : 2025/3/23 16:01 
# @Desc  :


"""
官方文档：https://docs.python.org/zh-cn/3.13/library/datetime.html
datetime 模块实现对 日期 的算术运算。
datetime 模块内含有一个同名的 datetime 类，该类中包含多个操作日期的函数，例如：datetime.now()、datetime.fromtimestamp()、datetime.timedelta()等
"""
import datetime
# 获取当前时间
print(datetime.datetime.now())
# 获取当前时间的时间戳
print(datetime.datetime.now().timestamp())
# 时间戳转时间, fromtimestamp()函数可以将时间戳转换成 datetime 对象。
print(datetime.datetime.fromtimestamp(1680000000)) # 2023-03-28 18:40:00
# 时间加减
print(datetime.datetime.now() + datetime.timedelta(days=1))


print(datetime.date(2023, 3, 28))
print(datetime.time(18, 40, 0))
print(datetime.datetime(2023, 3, 28, 18, 40, 0))
print(datetime.datetime.now().date())


"""
https://docs.python.org/zh-cn/3.13/library/time.html#module-time
time模块主要功能是读取系统时钟的当前 时间
time.time() 返回当前时间的时间戳
time.sleep() 休眠
"""
import time

# 获取当前时间的时间戳
# 每个时间戳都以自从 1970 年 1 月 1 日午夜（历元）经过了多长时间来表示。
print(time.time())
# 休眠
time.sleep(2)
print(time.time())

