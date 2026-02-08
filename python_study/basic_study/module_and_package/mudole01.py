# @Author: Benanahai
# @Time  : 2024/11/3 14:42

"""
模块：
    模块(module)其实就是 py 文件，里面定义了一些函数、类、变量等
包：
    包(package)是多个模块的聚合体形成的文件夹，里面可以是多个 py 文件，也可以嵌套文件夹
库：
    库是参考其他编程语言的说法，是指完成一定功能的代码集合，在 Python 中的形式就是模块和包

模块其实一个 py 文件，用来封装一组功能；包是将一类模块归集到一起，比模块的概念更大一些；库就是由其它程序员封装好的功能组，一般比包的概念更大一些。


导入模块的方法：
"""
# 方法 1：直接导入整个模块
# mudole01.py
def hello():
    print("Hello from module01!")

# 其他文件导入
import mudole01
mudole01.hello()

# 方法 2：导入特定内容
# 只导入 hello 函数
from mudole01 import hello
hello()

# 导入多个内容
from mudole01 import hello

# 方法 3：使用别名
# 给模块起别名
import mudole01 as m1
m1.hello()

# 给函数起别名
from mudole01 import hello as greet
greet()

# 方法 4：导入全部内容（慎用）
# 导入模块所有公开内容
from mudole01 import *
hello()

# 方法 5：包内导入
# 如果模块在包内（有 __init__.py 的目录）：

# 项目结构
# my_package/
# ├── __init__.py
# └── mudole01.py

# 其他文件导入
# from my_package import mudole01
# mudole01.hello()

# 方法 6：相对导入（包内部使用）
# 假设在包内的另一个模块中
from . import mudole01  # 导入同级模块
# from ..sub_package import module02  # 导入上级子包模块

# 方法 7：动态导入
# 运行时按需导入
module_name = "mudole01"
imported_module = __import__(module_name)
imported_module.hello()

# 常见问题解决
# 1. 模块路径问题
# 如果出现 ModuleNotFoundError，可通过以下方式解决：
#
import sys
sys.path.append("/path/to/your/module")  # 添加模块搜索路径
# 2. 循环导入
# 避免模块间相互导入，可通过以下方式：
#
# 将导入语句放在函数内部
# 重构代码结构
# 3. __init__.py 文件作用
# Python 3.3+ 后非必需，但显式声明包依然推荐使用
# 可定义 __all__ 列表控制 from package import * 的行为


# 最佳实践
# 优先使用 绝对导入 保证代码可读性
# 避免 from module import *（容易污染命名空间）
# 使用清晰的模块命名（全小写+下划线）
# 复杂项目推荐使用 包结构 组织代码
# 需要具体调试导入问题可提供完整项目结构截图。


def hi():
    print("hi")
def ok():
    print("ok")

# 如果这里测试，被其他模块调用时也会执行
hi()


# 避免执行测试代码
if __name__ == "__main__":
    hi()
