# @Author: Benanahai
# @Time  : 2025/3/20 23:38 
# @Desc  :

"""
for循环
for循环用于遍历序列（如列表、元组、字符串等）或其他可迭代对象中的元素。
语法：
for 变量 in 序列:
    执行语句

for循环的执行流程：
1. 初始化变量：在循环开始之前，会初始化一个变量，通常用于控制循环的次数。
2. 条件判断：在每次循环开始时，会判断条件是否为真。如果条件为真，则执行循环体；如果条件为假，则跳出循环。
3. 执行循环体：如果条件为真，则执行循环体中的语句。
4. 更新变量：在循环体执行完毕后，会更新变量的值，以便在下一次循环开始时判断条件。
5. 重复执行：重复执行步骤2到步骤4，直到条件为假。
"""

for d in 'Python':
    print('当前字母 :', d)


list = ['Google', 'Runoob', 'Taobao']
for i in list:
    print(i)


fruits = ['banana', 'apple',  'mango']
for i in range(len(fruits)):
    print(f'当前水果：{fruits[i]}')