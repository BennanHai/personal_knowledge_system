# @Author: Benanahai
# @Time  : 2025/3/23 16:20 
# @Desc  :

import os


# 获取当前操作系统
# 目前有效名称为以下三个：posix，nt，java。
# 其中posix是 Portable Operating System Interface of UNIX（可移植操作系统接口）的缩写。Linux 和 Mac OS 均会返回该值；nt全称应为“Microsoft Windows NT”，大体可以等同于 Windows 操作系统，因此 Windows 环境下会返回该值；java则是 Java 虚拟机环境下的返回值。
print(os.name)

# linux 上执行
# ➜  ~ python3
# Python 3.10.6 (main, Mar 20 2025, 16:56:24) [GCC 4.8.5 20150623 (Red Hat 4.8.5-44)] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# >>>
# >>> import os
# >>> print(os.name)
# posix
# >>>

# windows 上执行
# os.environ["HOMEPATH"]

# linux 上执行
os.environ["HOME"]

# 该函数的返回值就是当前目录下所有文件而非文件夹的名称列表。
def get_filelists(file_dir='.'):
    list_directory = os.listdir(file_dir)
    filelists = []
    for directory in list_directory:
        # os.path 模块稍后会讲到
        if(os.path.isfile(directory)):
            filelists.append(directory)

    return filelists

get_filelists()
