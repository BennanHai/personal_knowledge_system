# @Author: Benanahai
# @Time  : 2025/3/2 18:57
# @Desc  : 从配置文件中读取日志配置
"""

>JSON 配置文件通常包含以下部分：
- version：配置版本，必须为 1。
- formatters：定义日志的格式化器。
- handlers：定义日志的处理器（如输出到控制台、文件等）。
- loggers：定义日志记录器及其配置。
- root：根日志记录器的配置（可选）。

logging_config.json 是一个完整的json配置文件，用于配置logging模块的日志记录器、处理器和格式化器。

"""
import json
import logging.config

# 从配置文件中读取日志配置
with open('logging_config.json', 'r') as f:
    config = json.load(f)
logging.config.dictConfig(config)

# 获取日志记录器 - 使用配置文件中的my_module记录器
# logger = logging.getLogger('my_module')
logger = logging.getLogger('my_module.sub_module')

# 测试
logger.debug('This is a debug message.')
logger.info('This is an info message.')
logger.warning('This is a warning message.')
logger.error('This is an error message.')

# 异常捕获
a = 'lsp'
try:
    int(a)
except Exception as e:
    # logger.error(e) # 只会打印错误信息，不会打印错误堆栈信息
    logger.exception(e) # 会打印错误信息，并且会打印错误堆栈信息
