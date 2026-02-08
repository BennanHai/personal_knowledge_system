[第11天：Python 字典](https://mp.weixin.qq.com/s?__biz=MzkxNDI3NjcwMw==&mid=2247493312&idx=1&sn=5a0fea8a37f0700435f6a640c010805f&chksm=c1724ef0f605c7e65c33ab036eaa02aa557478bab93abf428b0d82568c99e18a0fde6405ff8e&scene=21#wechat_redirect)


Python 中的字典提供了一种灵活的访问和组织数据的方式

* 字典是由很多值组成的集合
* 字典的索引可以是不同的数据类型，同样也不止是整数，也有字符串
* 字典的索引被称为“键”，键及键所关联的值叫键值对（类似于Java中的Map集合）
* 字典是另一种可变容器模型，且可存储任意类型对象。
* 字典的每个键值 key=>value 对用冒号 : 分割，每个键值对之间用逗号 , 分割，整个字典包括在花括号 {} 中 ,格式如下所示：

```
dictionary  = {'url1':'baidu', 'url':'google', 'num1':12, 'num2':34};
```

键一般是唯一的，如果键重复，最后的一个键值对会替换前面的键值对，值没有唯一性要求，如下：

```
dic1 = {'name':'zhangsan','age':23,'address':'BeiJing','name':'lisi'}
# 查看字典值发现重复的键值后面的替换前面的
dic1
{'name': 'lisi', 'age': 23, 'address': 'BeiJing'}


dic1['name']
'lisi'
```

值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组，如下：

```
dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258',('a','b'):(12,43)}
MyCon = {12:'big',0:'white',354:'gentle',1:'good'}
```


# 1. 访问字典数据

访问字典的值通过方括号里面添加键就可以直接访问。

```python

MyDog = {'size':'big','color':'white','character':'gentle'}

# 字典值通过[‘键’]来访问
print(MyDog['size'])
 big   #输出结果

print('My Dog has '+MyDog['color']+' fur.' + ' and it has a ' + MyDog['character']+' character')
My Dog has white fur. and it has a gentle character #输出结果

```

访问字典中不存在的键将导致KeyError出错信息。

```python

dic1 = {'name':'zhangsan','age':23,'address':'BeiJing'}
#找字典中键为 'color' 的值
dic1['color']
Traceback (most recent call last):
  File "<input>", line 1, in <module>
KeyError: 'color'
```

# 2. 修改字典元素

## 2.1 添加和更新字典数据

向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对如下实例:

```python
dict = {'Name': 'Fiona', 'Age': 10, 'Class': 'Three'}
# 更新
dict['Age'] = 8 
# 添加
dict['School'] = "Middle School" 
# 查看字典数据 
dict
{'Name': 'Fiona', 'Age': 8, 'Class': 'Three', 'School': 'Middle School'}
```

## 2.2 删除字典

对字典元素的删除操作能单一删除也能将整个字典清空，显示的删除一个字典使用 del 命令

```python

dict = {'Name': 'Fiona', 'Age': 10, 'Class': 'Three'}

# 删除键是'Name'的条目 
del dict['Name']  

# 清空字典所有条目
dict.clear()  

# 删除整个字典元素
del dict  

# 以下语句将异常，字典不存在
print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])
```

# 3. 字典键的特性


**`字典值`**可以没有限制地取任何python对象，既可以是标准的对象，也可以是用户定义的；

**`字典键`**不行，两个重要点：

1. **不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住（覆盖之前的）**

1. **键必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行，如下实例：**

```python

dict = {['Name']: 'Fiona', 'Age': 10} 
 
print "dict['Name']: ", dict['Name']

# 以上实例输出结果：

Traceback (most recent call last):
  File "test.py", line 3, in <module>
    dict = {['Name']: 'Zara', 'Age': 7} 
TypeError: list objects are unhashable
```

# 4. 字典的函数

```python
# 1. len() 方法计算字段元素的个数

>>> dict = {'Name': 'Fiona', 'Age': 10, 'class': 'Three'} 
>>> len(dict)
     3

# 2. str() 方法输出字典中可以打印的字符串标识

>>> dict = {'Name': 'Runoob', 'Age': 10, 'Class': 'Three'}
>>> str(dict)
"{'Name': 'Runoob', 'Age': 10, 'Class': 'Three'}"

# 3. type() 方法返回输入的变量类型，如果变量是字典就返回字典类型
```


# 5. 字典的方法


## 5.1 删除字典所有元素

删除字典内所有元素，clear() 方法没有任何返回值,实例如下：

```python
dict = {'Name': 'Fiona', 'Age': 10}

print ("字典长度 : %d" %  len(dict))
dict.clear()
print ("字典删除后长度 : %d" %  len(dict))

# 输出结果为：
字典长度 : 2
字典删除后长度 : 0
```

## 5.2 复制字典

copy() 方法对字典进行复制

```python

dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

dict11 = dict.copy()
print(dict11)
print("新复制的字典为 : ", dict11)
```


- 浅拷贝  深拷贝

```python
dict1 = {'user': 'runoob', 'num': [1, 2, 3]}

# 浅拷贝: 引用对象  赋值
dict2 = dict1  
# 拷贝
dict3 = dict1.copy()  

# 修改 data 数据
dict1['user'] = 'root'
dict1['num'].remove(1)

# 输出结果
print(dict1)
print(dict2)
print(dict3)
```

## 5.4 返回字典的值

返回指定键的值，如果值不在字典中返回default值

```python
dict.get(key, default=None)

# 参数
key -- 字典中要查找的键。
default -- 如果指定键的值不存在时，返回该默认值值。

```

## 5.5 key in dict

如果键在字典dict里返回true，否则返回false

```python

dict = {'Name': 'Mary', 'Age': 20,'Address':'BeiJing'}

# 检测键 Age 是否存在
if 'Age' in dict:
    print("键 Age 存在")
else:
    print("键 Age 不存在")

# 检测键 Sex 是否存在
if 'Sex' in dict:
    print("键 Sex 存在")
else:
    print("键 Sex 不存在")

# not in

# 检测键 Name 是否存在
if 'Name' not in dict:
    print("键 Name 不存在")
else:
    print("键 Name 存在")

# 输出：
键 Age 存在
键 Sex 不存在
键 Name 存在
```


## 5.6 dict.items()

item() 方法以列表返回可遍历的(键, 值) 元组数组

```python

dict = {'Name': 'Mary', 'Age': 17}
 
print ("Value : %s" %  dict.items())

# 输出结果为：
Value : dict_items([('Age', 17), ('Name', 'Mary')])
```

**可遍历的元组数组举例：**

```
dict1 = {'老大':'25岁',
        '老二':'20岁',
        '老三':'12岁',
        }
print(dict1.items())
for key,values in dict1.items():
    print(key + '已经' + values + '了')
```



## 5.7 dict..keys()

返回一个迭代器，可以使用 list() 来转换为列表

**keys()方法语法：**

```
dict.keys()
```

**实例：**

```
dict = {'Name': 'Mary', 'Age': 17}


print(dict.keys())
```

**以上结果输出为：**

```
dict_keys(['Name', 'Age'])
```

由结果看出结果返回一个迭代对象，这时候我们可以使用 list 转换为列表：

```
list1 = list(dict.keys())
print ("转换后的结果为 : %s" % list1)


# 输出结果为一个列表，后续可以对其进行相应操作：
转换后的结果为 : ['Name', 'Age']
```


## 5.10 dict.values()

Python 字典 values() 方法返回一个迭代器，可以使用 list() 来转换为列表，列表为字典中的所有值。

```
dict = { 'Name': 'Mary','Sex': 'male', 'Age': 7}


print("字典所有值为 : ", list(dict.values()))
```

**以上结果输出为：**

```
字典所有值为 :  ['Mary', 'male', 7]
```


## 5.9 dict..update(dict2)

Python 字典 update() 函数把字典参数 dict2 的 key/value(键/值) 对更新到字典 dict 里。

**语法：**

```
dict.update(dict2)
# 参数
 dict2 -- 添加到指定字典dict里的字典。
```

**实例：**

```
dict = {'Name': 'Mary', 'Age': 17}
dict2 = {'Sex': 'female' }


# 将 dict2 中的结果添加到字典 dict 中　
dict.update(dict2)
print ("更新字典 dict : ", dict)
```

**以上结果输出为：**

```
更新字典 dict :  {'Name': 'Mary', 'Age': 17, 'Sex': 'female'}
```
