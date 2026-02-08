# @Author: Benanahai
# @Time  : 2025/3/2 19:55 
# @Desc  :

"""
loguru 是一个 Python 日志记录 第三方开源库，相比与 Python 原生的 logging 模块，loguru 提供了更简单、更强大、更优雅的日志记录方式。
它是对 Python 标准库logging的替代方案，具有开箱即用、功能丰富、配置灵活等特点。
"""
from venv import logger

# 安装loguru
# pip install loguru

# 导入loguru
import loguru
from loguru import logger

# 开箱即用，默认输出到控制台，不需要额外配置
logger.info('loguru Hello, World!')

# 功能丰富，支持多种日志输出方式，如文件、数据库、邮件等
# 通过 add 方法添加配置
logger.add('app.log', format='{time} {level} {message}', level='INFO')
# 支持自定义时间类型
logger.add('app.log', format='{time:YYYY/MM/DD at HH:mm:ss} {level} {message} {extra}', level='DEBUG')
# 若 Loguru 的内置字段不满足要求，还可以使用 bind() 方法绑定额外的上下文信息，然后通过 {extra} 字段显示这些信息。
bind_logger = logger.bind(user='admin')
bind_logger.info('loguru Hello, World!')

# ! 移除
logger.remove()
logger.add('app.log', format='{time} {level} {message}', level='INFO', rotation='1 MB', compression='zip')
logger.info('loguru Hello, World!')

# # 日志轮转
# # 文件过大时自动轮换
# logger.add("file_1.log", rotation="500 MB")
# # 每天中午 12 点创建新文件
# logger.add("file_2.log", rotation="12:00")
# # 文件过期后轮换
# logger.add("file_3.log", rotation="1 week")
# # 一段时间后清理旧日志
# logger.add("file_X.log", retention="10 days")
# # 压缩日志以节省空间
# logger.add("file_Y.log", compression="zip")

# Loguru 还支持根据日志级别或其他条件动态调整日志格式：
# 错误日志显示为红色。其他日志显示为默认格式。
def formatter(record):
    ERROR_LEVEL = "ERROR"

    try:
        if record.get("level") and hasattr(record["level"], "name") and record["level"].name == ERROR_LEVEL:
            return "<red>{time} | {level} | {message}</red>\n"
        return "{time} | {level} | {message}\n"
    except (KeyError, AttributeError):
        return "{time} | {level} | {message}\n"


logger.add('app_formatter.log', format=formatter)
logger.info('info')
logger.error('error')
logger.warning('warning')
logger.success('success')


# 支持使用装饰器捕获异常
logger.remove()

logger.add('catch_log.log', format='{time}|{level}|{file}:{name}|{line}|{message} ')
@logger.catch
def test_catch():
    return 1/0

test_catch()

# enqueue=True：将日志消息放入队列中，确保线程安全、多进程安全以及异步日志记录。日志消息会被后台线程处理，不会阻塞主程序的执行。
logger.add("output.log", enqueue=True)

logger.info("Hello, World!")


# 使用 serialize=True参数，Loguru 会将日志消息转换为 JSON 格式。转换后的格式保留了日志的完整结构化信息，便于后续处理和分析。
logger.add("output.log", serialize=True)
logger.info("This is a serialized log message")
logger.error("An error occurred", details={"code": 500, "message": "Internal Server Error"})
