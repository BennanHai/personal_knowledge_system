[第9天：Python Tupple](https://mp.weixin.qq.com/s?__biz=MzkxNDI3NjcwMw==&mid=2247493306&idx=1&sn=5f312f55b123c6675c2deb8772727c88&chksm=c1724e8af605c79cb92faab2fc6f00c6cc4677d0b77d6dad9013f06171681a1bddaf45e70859&scene=21#wechat_redirect)

* Python 的元组与列表类似，不同之处在于元组的元素不能修改。
* 元组使用小括号()，列表使用方括号[]。


# 1. 元组基本操作

## 1.1 创建元组

元组创建很简单，只需要在括号中添加元素(不需要括号也可以)，并使用逗号隔开即可。

```python

>>> tup1 = ('baidu', 'google', 12, 34); 
>>> tup2 = (1, 2, 3, 4, 5 );
>>> tup3 = "a", "b", "c", "d";

# 创建空元组
>>> tup4 = ()

# 查看tup4和tup3的类型
>>> type(tup4)
<class 'tuple'>
>>> type(tup3)
<class 'tuple'>
```

> 注意:
>
> - 元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用，如下：

```python

>>> TupNum = (34)   
>>> type(TupNum)   # 不加逗号是整型
<class 'int'>
>>> TupNum = (34,)
>>> type(TupNum)  # 加上逗号变元组
<class 'tuple'>
```

## 1.2 访问元组

元组的访问和序列访问元素一样，都是通过下标索引进行访问操作

```python
>>> tup1 = ('baidu', 'google',1,2)
>>> tup2 = (1, 2, 3, 4, 5, 6, 7)
>>> tup1[0:2]
('baidu', 'google')
>>> tup2[1:4]
(2, 3, 4)
```

## 1.3 修改元组


元组不能修改，只能通过索引进行复制和连接操作。

## 1.4 删除元组

由于元组的不可修改性，所以元组中的元素值是不允许删除的，但我们可以使用 del 语句来删除整个元组

```python
tup = ('baidu', 'google',1,2)
 
print (tup)
del tup;
print ("删除后的元组 tup : ")
print (tup)

# 报错信息如下，证明整个元组已经被删除
删除后的元组 tup1 : 
Traceback (most recent call last):
  File "tupple.py", line 29, in <module>
    print(tup1)
NameError: name 'tup' is not defined
```

# 2. 元组运算符

与字符串一样，元组之间可以使用 + 号和 \* 号进行运算。这就意味着他们可以组合和复制，运算后会生成一个新的元组。总而言之对整个元组进行一些运算后就会生成一个新的元组。

## 2.1 元组长度

```python

# 求元组tup1的长度
>>> tup1 = ('baidu', 'google',1,2)
>>> len(tup1)
4
```

## 2.4 判断元素

判断元组中元素是否存在使用关键字 in 进行判断，判断结果返回布尔值

```python

>>> tup1
'abc'
>>> 'a' in tup1
True
```



# 3. 元组内置函数

和列表一样，元组同样也拥有一些内置函数，这些函数用于判元组中的元素大小以及将元组做相应的转换

```python

#计算元组元素个数。
len(tuple)

#返回元组中元素最大值。
max(tuple)

#返回元组中元素最小值。
min(tuple)

#将列表转换为元组。
tuple(seq)
```
