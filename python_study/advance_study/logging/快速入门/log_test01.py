# @Author: Benanahai
# @Time  : 2025/3/2 16:27 
# @Desc  :

import logging

# 创建一个日志记录器 Logger
logger = logging.getLogger(__name__)
# 设置日志级别为 DEBUG
logger.setLevel(logging.DEBUG)

# 创建处理器Hander
str_hander = logging.StreamHandler()
# 设置处理器级别为 DEBUG
str_hander.setLevel(logging.DEBUG)

# 创建格式化器Formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
formatter = logging.Formatter('%(asctime)s - %(pathname)s  - %(funcName)s - %(levelname)s - %(message)s')
# 将格式化器添加到处理器Hander中
str_hander.setFormatter(formatter)

# 将处理器添加到日志记录器Logger中
logger.addHandler(str_hander)


# 测试
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

