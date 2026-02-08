# @Author: Benanahai
# @Time  : 2024/12/21 18:03 
# @Desc  :
import time

# 列表：
# 列表是一系列按特定顺序排列的元素组成，可以包含任意数量的元素，可以是数字、字符串、列表等。
# 列表用[]表示，元素之间用逗号分隔。
# 列表是有序集合，列表的元素可以通过索引访问，索引从0开始。
# 列表是可变的，可以修改、添加和删除元素。

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1])

# 修改列表元素
bicycles[0] = 'yamaha'
print(bicycles)
# 添加列表元素
# 1. 在列表末尾添加元素
bicycles.append('suzuki')
# 2. 在列表中插入元素， 可以在任意位置插入元素
bicycles.insert(2, 'honda')
bicycles.insert(55, 'honda')
print(bicycles)
print(len(bicycles))

# 删除列表元素
# 1. 使用del语句删除元素, 只需要知道元素的索引即可， 删除后无法再访问
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
del bicycles[0]
print(bicycles)
print(bicycles[0])
# print(bicycles['trek']) # TypeError: list indices must be integers or slices, not str

# 2. 使用方法pop()删除元素, 删除列表末尾的元素，并返回该元素
# pop弹出后，元素就不在列表中了
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
pop_bicycle = bicycles.pop()
print(pop_bicycle)
print(bicycles)

# 3. 弹出列表中任意位置的元素, pop()方法可以接受一个索引作为参数，弹出任意位置的元素
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
pop_any_bicycle = bicycles.pop(2)
print(pop_any_bicycle)

# 4. 根据值删除元素, remove()方法只删除第一个指定的值，如果要删除的值在列表中出现多次，需要使用循环来判断
bicycles = ['trek', 'cannondale', 'trek', 'specialized']
bicycles.remove('trek')
print(bicycles)

for i in range(len(bicycles) - 1):
    if bicycles[i] == 'trek':
        # 会返回删除的元素
        del_bicycle = bicycles.remove('trek')
        print(del_bicycle)
print(bicycles)


# 管理列表元素
# 永久排序
# 1. 使用sort()方法对列表进行永久性排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() # 按字母顺序排序
print(cars)

# 2. 使用sort()方法对列表进行永久性排序，按字母顺序相反的顺序排列 -- 添加reverse=True参数
cars.sort(reverse=True) # 按字母顺序相反的顺序排列
print(cars)

# # 临时排序 - 已没有sorted()方法
# # 1. 使用sorted()函数对列表进行临时排序
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sorted() # 按字母顺序排序
# print(cars)

# 3. reverse()反转列表元素（不是按字母），会永久性修改列表元素的排列顺序，但是再次调用reverse()方法会恢复到原来的顺序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)
cars.reverse()
print(cars)

# 4. len()函数获取列表长度
print(len(cars))




# 第四章 操作列表
# 1. 遍历整个列表
cars = ['bmw', 'audi', 'toyota', 'subaru']
for car in cars:
    print(car)

# 2. 创建数值列表
# 1. 使用range()函数生成一系列数字
for value in range(1, 5): # 不包含5
    print(value)

for value in range(5): # 默认从0开始
    print(value)

# 2. 使用list()函数将range()函数生成的数字转换为列表
numbers = list(range(1, 6))
print(numbers)
for number in numbers:
    print(number)

# 3. 使用range()函数生成一系列数字，可以指定步长
numb = list(range(2, 11, 2)) # 打印1-10的偶数
print(numb)

# 4. 创建一个列表，包含1-10的平方
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)

# 5. 列表简单统计
ages = [1, 2, 3, 4, 5,8 ,9, 10]
print(min(ages))
print(max(ages))
print(sum(ages))


# 列表推导式
# 重新计算上面4的平方
squares = [value ** 2 for value in range(1, 11)]
print(squares)

# 练习
values = list(range(1, 21))
print(values)

nums = list(range(1, 1000001))
print(min(nums))
print(max(nums))
start_time = time.time()
print(sum(nums))
end_time = time.time()
print(end_time - start_time)

nums = list(range(1, 21, 2))
print(nums)

nums = list(range(3, 31, 3))
print(nums)

nums = [value ** 3 for value in range(1, 11)]
print(nums)


# 切片是指从列表中提取出指定的元素，可以提取任意长度的子序列
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) # 从0开始到3，但不包含3
print(players[:4]) # 从0开始到4，但不包含4
print(players[1:]) # 从1开始到最后
print(players[-3:]) # 从倒数第3个开始到最后
print(players[:]) # 复制整个列表

# 遍历切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
pls = players[:3]
for pl in pls:
    print(pl)
# 或者
for p in players[:3]:
    print(p)

# 打印列表中间的三个元素
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])


# 元组
# 不可变的列表称为元组，使用圆括号表示
tuple01 = (200, 50)
print(tuple01[0])
print(tuple01[1])
# 元组元素不可修改 - 不可变
# tuple01[3] = 100 # TypeError: 'tuple' object does not support item assignment
# tuple01[1] = 999 # TypeError: 'tuple' object does not support item assignment
# 元组元素不可添加 - 不可变
# tuple01.append(100) # AttributeError: 'tuple' object has no attribute 'append'
# 元组元素不可删除 - 不可变
# del tuple01[1] # TypeError: 'tuple' object doesn't support item deletion
print(tuple01)

tuple02 = (1,) # 只有一个元素的元组，需要在元素后面加逗号
print(tuple02)

# 修改元组变量。虽然不能修改元组的元素，但可以给存储元组的变量赋值
tuple01 = (200, 50, 55, 88)
print(tuple01)

# 遍历元组 - 与列表遍历一样，使用for循环
dim = (200, 50, 66, 888)
for d in dim:
    print(d)


