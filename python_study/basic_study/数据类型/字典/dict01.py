# @Author: Benanahai
# @Time  : 2024/12/21 23:39 
# @Desc  :
import copy

# 字典
# 字典是一系列键-值对，每个键都与一个值相关联，可以通过键来访问与之相关联的值。
# 字典用{}表示，键-值对用冒号分隔，键值对之间用逗号分隔。
# 字典是无序的，可以通过键来访问值，键可以是数字、字符串等。
# 字典是可变的，可以添加、修改和删除键-值对。
# 字典中的值可以是任意数据类型，包括列表、字典等。
# 字典中的键必须是唯一的，但值可以重复。
# 字典的基本操作
# 创建字典
alien_0 = {'color': 'green', 'points': 5}
# 访问字典中的值
print(alien_0['color'])
print(alien_0['points'])
# 添加键-值对
alien_0['x'] = 0
alien_0['y'] = 25
print(alien_0)
# 修该字典的值
alien_0['points'] = 10
print(alien_0)
# 删除键-值对
del alien_0['x']
print(alien_0)
# 遍历字典
for k, v in alien_0.items():
    print(f"{k}: {v}")
# 遍历字典的键
for k in alien_0.keys():
    print(k)
# 遍历字典的值
for v in alien_0.values():
    print(v)


# 键必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行，如下实例：
dict = {['Name']: 'Fiona', 'Age': 10}

print("dict['Name']: ", dict['Name'])

# 以上实例输出结果：
# Traceback (most recent call last):
# File "D:\Program Files\python\anaconda\Lib\site-packages\IPython\core\interactiveshell.py", line 3577, in run_code
# exec(code_obj, self.user_global_ns, self.user_ns)
# File "<ipython-input-2-e8ef1407f259>", line 1, in <module>
# dict = {['Name']: 'Fiona', 'Age': 10}
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# TypeError: unhashable type: 'list'



dict = {'Name': 'Fiona', 'Age': 10}

print ("字典长度 : %d" %  len(dict))
dict.clear()
print ("字典删除后长度 : %d" %  len(dict))

# 输出结果为：
# 字典长度 : 2
# 字典删除后长度 : 0



dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

dict11 = dict.copy()
print(dict11)
print("新复制的字典为 : ", dict11)


#
import copy
dict1 = {'user': 'runoob', 'num': [1, 2, 3]}

# 浅拷贝: 引用对象  赋值
dict2 = dict1
dict3 = dict1.copy()
dict4 = copy.copy(dict1)

# 深拷贝
dict5 = copy.deepcopy(dict1)

# 修改 data 数据
dict1['user'] = 'root'
dict1['num'].remove(1)

# 输出结果
print(dict1)
print(dict2)
print(dict3)
print(dict4)
print(dict5)

# {'user': 'root', 'num': [2, 3]}
# {'user': 'root', 'num': [2, 3]}
# {'user': 'runoob', 'num': [2, 3]}
# {'user': 'runoob', 'num': [2, 3]}
# {'user': 'runoob', 'num': [1, 2, 3]}



