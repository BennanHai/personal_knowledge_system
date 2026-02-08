[第12天：Python 集合](https://mp.weixin.qq.com/s?__biz=MzkxNDI3NjcwMw==&mid=2247493314&idx=1&sn=cb92c32937dfd1f1bba3a0ae5862b7f4&chksm=c1724ef2f605c7e48460f02819a8c862d8a85ed23ead53e452ebf8467db8f9dd7b5a2e15157e&scene=21#wechat_redirect)

Python也包含有 集合 类型。集合是由**不重复元素**组成的**无序的**集。它的基本用法包括成员检测和消除重复元素。集合对象也支持像 联合，交集，差集，对称差分等数学运算。

# 集合创建

可以使用大括号 { } 或者 set() 函数创建集合

```python
set1 = {'None',11,22,'agg'}
print(set1)
```

创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

```python
# 创建空集合
>>> empty_set = set()
>>> type(empty_set)
  <class 'set'>


# 创建空字典
>>> empty_dict = {}
>>> type(empty_dict)
  <class 'dict'>
```

# 集合的基本操作

## 2.6 集合运算

集合之间的运算符分别是‘-’、‘|’、‘&’、‘^’ ; 下面以两个集合之间的运算为例进行讲解：

* ‘-’：代表前者中包含后者中不包含的元素
* ‘|’：代表两者中全部元素聚在一起去重后的结果
* ‘&’：两者中都包含的元素
* ‘^’：不同时包含于两个集合中的元素

```python

>>> a = set('afqwbracadaagfgbrafg')
>>> b = set('rfgfgfalacazamddg')
>>> a                                
{'r', 'q', 'd', 'b', 'w', 'g', 'f', 'c', 'a'}
>>> b
{'r', 'd', 'g', 'f', 'l', 'z', 'c', 'm', 'a'}
# 集合a中包含而集合b中不包含的元素
>>> a - b                            
{'b', 'w', 'q'}
 # 集合a或b中包含的所有元素
>>> a | b                           
{'d', 'g', 'l', 'c', 'r', 'q', 'b', 'w', 'f', 'z', 'm', 'a'}
# 集合a和b中都包含了的元素
>>> a & b                            
{'r', 'd', 'g', 'f', 'c', 'a'}
# 不同时包含于a和b的元素
>>> a ^ b                            
{'l', 'q', 'b', 'w', 'z', 'm'}
```


# 3. 集合推导式

和列表一样，集合也支持推导式

```python
# 判断元素是否存在
>>> a = {x for x in 'abracadabra' if x not in 'abc'}
>>> a
{'r', 'd'}
```


# 4. 集合内置方法

### 4.1 difference()

difference() 方法用于返回集合的**差集**，即返回的集合元素包含在第一个集合中，但不包含在第二个集合(方法的参数)中，返回一个新的集合。difference() 方法语法：

```
set.difference(set)
```

**实例：** 两个集合的差集返回一个集合，元素包含在集合 x ，但不在集合 y ：

```
# 求两个集合的差集，元素在 x 中不在 y 中
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}


z = x.difference(y)
# z = x - y

print('两个集合的差集是：%s' % z)


# 输出结果为：
{'cherry', 'banana'}
```


### 4.3 intersection()

intersection() 方法用于返回两个或更多集合中都包含的元素，即交集，返回一个新的集合。

**intersection() 方法语法：**

```
set.intersection(set1, set2 ... etc)


**参数：**
set1 -- 必需，要查找相同元素的集合
set2 -- 可选，其他要查找相同元素的集合，可以多个，多个使用逗号 , 隔开
```

**实例：**

```
# 返回两个或者多个集合的交集
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}


z = x.intersection(y)


print(z)


#　返回三个集合的交集
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}


result = x.intersection(y, z)
print('三个集合的差集是：%s' % result)


# 输出结果：


{'apple'}
两个集合的差集是：{'c'}
```


### 4.5 union()

union() 方法返回两个集合的并集，即包含了所有集合的元素，重复的元素只会出现一次，返回值返回一个新的集合

**语法：**

```
union() 方法语法：


set.union(set1, set2...)
参数
set1 -- 必需，合并的目标集合
set2 -- 可选，其他要合并的集合，可以多个，多个使用逗号 , 隔开。
```

**实例：**

```
# 合并两个集合，重复元素只会出现一次：


x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}
 
z = x.union(y) 
 
print(z)
输出结果为：


{'cherry', 'runoob', 'google', 'banana', 'apple'}




# 合并多个集合：


实例 1
x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}
 
result = x.union(y, z) 
 
print(result)
输出结果为：


{'c', 'd', 'f', 'e', 'b', 'a'}
```


```python
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

```
