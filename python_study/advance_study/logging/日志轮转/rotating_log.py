# @Author: Benanahai
# @Time  : 2025/3/2 19:19 
# @Desc  : 日志轮转

"""
当日志文件过大时，可以通过文件轮转（Rotating）将日志分割成多个文件。logging提供了两种文件轮转处理器：
    RotatingFileHandler：基于文件大小轮转。
    TimedRotatingFileHandler：基于时间轮转。
"""

import logging
from logging.handlers import RotatingFileHandler

# 创建一个日志记录器，并设置日志级别为DEBUG
logger = logging.getLogger('my_app')
logger.setLevel(logging.DEBUG)

# 1. 基于文件大小轮转
# 创建一个RotatingFileHandler处理器，并设置日志文件名、最大文件大小（字节）和最大备份文件数量
# handler = RotatingFileHandler(
#     filename='my_app.log',       # 日志文件名
#     maxBytes=1 * 1024 * 1024,  # 每个日志文件最大 1MB (为了测试，设置为 1MB)
#     backupCount=5,            # 保留 5 个备份文件
#     encoding='utf8'
# )

# 2. 基于时间轮转
handler = logging.handlers.TimedRotatingFileHandler(
    filename='my_app_time.log',
    when='midnight',  # 每天凌晨
    interval=1,  # 每日一次
    backupCount=7,  # 保留 7 个备份文件
    encoding='utf8'
)

# 创建一个格式化器，并将其添加到处理器中
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# 测试
for i in range(10000):
    logger.info(f'This is a log message {i}')