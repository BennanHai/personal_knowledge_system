# @Author: Benanahai
# @Time  : 2024/12/21 23:34 
# @Desc  :

"""
语法：
if 判断条件：
    执行语句……
else：
    执行语句……
"""

x = int(input("请输入一个数字："))
if x < 0:
    x = 0
    print('负数已变为0')
elif x == 0:
    print('0')
elif x == 1:
    print('1')
else:
    print('其他')
