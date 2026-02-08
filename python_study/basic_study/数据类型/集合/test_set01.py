# @Author: Benanahai
# @Time  : 2025/3/22 20:14 
# @Desc  :


set1 = {'None',11, 22, 11, 22,'agg'}
print(set1)


# 1. 添加元素

s = set(('hello','world'))
print(s)

# 向集合 s 中添加元素
s.add('!')
print('添加元素后的集合是：%s' % s) # {'world', '!', 'hello'}

# 除了 add() 方法可以添加元素外，还有一个方法，也可以添加元素，并且参数可以是列表，元组，字典等，语法格式如下：
#　1）添加列表
s.update([1,3],[2,4])
print('添加元素后的集合是：%s' % s)

# 2）添加元组
s.update(('h', 'j'))
print('添加元素后的集合是：%s' % s)



# 判断元素是否在集合中存在
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)


# 集合内置函数

x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}
# 并集
z = x.union(y)
print(z)
# 交集
z = x.intersection(y)
print(z)
# 差集
z = x.difference(y)
print(z)
# 对称差集
z = x.symmetric_difference(y)
print(z)
#isdisjoint() 方法用于判断两个集合是否包含相同的元素，==如果没有返回 True，否则返回 False
z = x.isdisjoint(y)
print(z)
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
# issubset() 方法用于判断集合的所有元素是否都包含在指定集合中，如果是则返回 True，否则返回 False。
z = x.issubset(y)
print(z)
