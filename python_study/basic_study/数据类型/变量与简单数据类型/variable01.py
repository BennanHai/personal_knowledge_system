# @Author: Benanahai
# @Time  : 2024/12/21 17:23 
# @Desc  :

# 变量：
# 变量是程序中存储数据的容器，可以通过变量来引用数据，变量的值可以改变

# 变量的命名规则：
# 1. 变量名只能包含字母、数字和下划线，不能以数字开头。
# 2. 变量名不能包含空格。
# 3. 不能使用Python关键字和函数名作为变量名。
# 4. 变量名应该简洁且具有描述性。
# 5. 变量名应该使用小写字母。
# 6. 慎用字母l和O，容易与数字1和0混淆。


# 字符串
# 字符串就是一系列字符。在python中，用引号引起的都是字符串，引号可以是单引号，也可以是双引号。

# 使用方法修改字符串的大小写：
str1 = "Name"
print(str1.title()) # Title()方法将每个单词的首字母都改为大写，其他字母都改为小写
print(str1.upper()) # upper()方法将字符串全部改为大写
print(str1.lower()) # lower()方法将字符串全部改为小写
# 上面的方法都是临时修改字符串的大小写，如果想永久修改字符串的大小写，需要将修改后的字符串赋值给原变量
str2 = str1.title()
print(str2)

# 删除空白
# 在编程中，额外的空白可能会引发错误，如用户输入的额外空白可能会导致程序无法正确识别输入
# 删除字符串末尾的空白：rstrip()方法
str3 = "Name "
print(str3.rstrip()) # 删除字符串末尾的空白
# 删除字符串开头的空白：lstrip()方法
str4 = " Name"
print(str4.lstrip()) # 删除字符串开头的空白
# 删除字符串两端的空白：strip()方法
str5 = " Name "
print(str5.strip()) # 删除字符串两端的空白


# 删除前缀
# removeprefix()方法用于删除字符串的前缀
# removesuffix()方法删除后缀
url = "https://www.baidu.com/"
uri1 = url.removeprefix("https://")
uri2 = url.removesuffix("/")
print(uri1)
print(uri2)


# 注释
# 注释是程序中的一些说明，不会被执行，可以帮助理解代码
# 在python中，单行注释使用#，多行注释使用三个引号
# 例如：
# 这是一个单行注释
'''
这是一个多行注释
'''
"""
这也是一个多行注释
"""

# python之禅
import this
# 该命令会输出python之禅，其中包含了python的设计哲学，可以帮助理解python的设计思想

"""
import this
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""