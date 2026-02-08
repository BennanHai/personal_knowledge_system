# @Author: Benanahai
# @Time  : 2025/3/2 23:28 
# @Desc  : 字典读取日志配置

import logging.config


# 如果不想使用外部文件，可以直接在代码中使用 Python 字典定义配置：
config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'simple',
            'stream': 'ext://sys.stdout'
        },
        'file': {
            'class': 'logging.FileHandler',
            'level': 'DEBUG',
            'formatter': 'simple',
            'filename': 'app_dict.log'
        }
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['console', 'file']
        }
    }
}

logging.config.dictConfig(config)
logger = logging.getLogger('my_module')

logger.debug('This is a debug message.')
logger.info('This is an info message.')