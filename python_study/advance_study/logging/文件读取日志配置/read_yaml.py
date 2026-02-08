# @Author: Benanahai
# @Time  : 2025/3/2 23:11 
# @Desc  : 读取yaml文件日志配置

import logging.config
import yaml # 需要安装 pyyaml 库

# 从配置文件中读取日志配置
with open('logging_config.yaml', 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)

logging.config.dictConfig(config)

# 获取日志记录器 - 使用配置文件中的my_module记录器
logger = logging.getLogger('my_module')

# 测试
logger.debug('This is a debug message.')
logger.info('This is an info message.')



