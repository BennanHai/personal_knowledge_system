# @Author: Benanahai
# @Time  : 2025/3/20 23:48 
# @Desc  :

"""
函数
    函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段

如何定义函数
函数代码块以 def 关键词开头，后接函数标识符名称和圆括号()。
任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数。
函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
函数内容以冒号起始，并且缩进。
return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。

    def functionname( parameters ):
       "函数_文档字符串"
       function_suite
       return [expression]
def 是用于定义函数的关键字，
functionname 是函数的名称，
parameters 是函数的参数，
function_suite 是函数的主体，
return 是用于返回值的关键字，
expression 是返回值的表达式。

"""

def hi():
    print("Hello World!")

# 调用函数（定义之后要调用）
hi()


# 递归函数
# 计算阶乘
def factorial(n):
    """
    计算阶乘
    :param n: 阶乘的数字
    :return: 阶乘的结果
    """
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))