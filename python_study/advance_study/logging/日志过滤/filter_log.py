# @Author: Benanahai
# @Time  : 2025/3/2 19:32 
# @Desc  :

"""
logging 模块的日志过滤功能允许根据特定的条件控制哪些日志应该被记录。通过过滤器，可以实现对日志更加精细的日志控制，例如：
    过滤特定级别的日志。
    过滤包含特定关键词的日志。
    过滤来自特定模块或日志记录器的日志。

logging 模块中的日志过滤器需要继承 logging.Filter 类，重写 filter(record) 方法。record 是一个日志对象，包含了日志的所有信息，比如日志级别、消息和模块名等。

重写的 filter(record) 方法返回 True 时，日志会被记录。返回 False 时，日志会被忽略。
"""

# 一个过滤特定级别日志的例子：
import logging

# 自定义过滤器
class MyLevelFilter(logging.Filter):
    def __init__(self, level):
        self.level = level      # 测试1
        self.keyword = 'info'  # 测试2

    def filter(self, record):

        """
        测试1. 如果日志级别大于等于指定的级别，则返回True，否则返回False
        测试2， 包含特定关键词的日志
        """
        # return record.levelno >= self.level # 测试1
        return self.keyword in record.getMessage()  # 测试2
# 创建一个日志记录器
logger = logging.getLogger('my_filter_logger')
logger.setLevel(logging.DEBUG)

# 创建处理器
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

# 添加过滤器
handler.addFilter(MyLevelFilter(logging.ERROR))
# 添加处理器
logger.addHandler(handler)

# 测试1
logger.debug('This is a debug message')  # 不会被记录
logger.info('This is an info message')   # 测试2时会被记录，包含了关键词info
logger.error('This is an error message')  # 测试1时会被记录，大于等于指定的级别error
