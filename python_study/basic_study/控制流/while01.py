# @Author: Benanahai
# @Time  : 2025/3/20 23:43 
# @Desc  :

"""
while循环
while循环用于重复执行一段代码，直到指定的条件不再满足。
语法：
while 条件:
    执行语句
while循环的执行流程：
1. 初始化条件：在循环开始之前，会初始化一个条件。
2. 条件判断：在每次循环开始时，会判断条件是否为真。如果条件为真，则执行循环体；如果条件为假，则跳出循环。
3. 执行循环体：如果条件为真，则执行循环体中的语句。
4. 更新条件：在循环体执行完毕后，会更新条件的值，以便在下一次循环开始时判断条件。
5. 重复执行：重复执行步骤2到步骤4，直到条件为假。
"""

while True:
    print("hello")
    print('你好')
    break

count = 0
while count < 9:
   print( 'The count is:', count)
   count += 1

print("Good bye!")