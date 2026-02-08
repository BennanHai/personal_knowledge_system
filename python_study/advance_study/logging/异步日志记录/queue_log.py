# @Author: Benanahai
# @Time  : 2025/3/2 19:49 
# @Desc  :

# 在高并发场景下，同步日志记录可能会影响性能。可以通过QueueHandler和QueueListener实现异步日志记录：

import logging
import logging.handlers
import queue
import threading

# 创建一个队列
log_queue = queue.Queue()

# 创建队列处理器
queue_handler = logging.handlers.QueueHandler(log_queue)

# 创建记录器
logger = logging.getLogger('my_async_logger')
logger.setLevel(logging.DEBUG)
logger.addHandler(queue_handler)

# 创建日志监听器
file_hander = logging.FileHandler('my_async_log.log')
listener = logging.handlers.QueueListener(log_queue, file_hander)

# 启动日志监听器
listener.start()
# 记录日志
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')

# 停止日志监听器
listener.stop()