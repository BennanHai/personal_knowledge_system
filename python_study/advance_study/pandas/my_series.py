# @Author: Benanahai
# @Time  : 2024/11/9 20:18

"""
Series 特点：
一维数组：Series是一维的，这意味着它只有一个轴（或维度），类似于 Python 中的列表。
索引： 每个 Series 都有一个索引，它可以是整数、字符串、日期等类型。如果不指定索引，Pandas 将默认创建一个从 0 开始的整数索引。
数据类型： Series 可以容纳不同数据类型的元素，包括整数、浮点数、字符串、Python 对象等。
大小不变性：Series 的大小在创建后是不变的，但可以通过某些操作（如 append 或 delete）来改变。
操作：Series 支持各种操作，如数学运算、统计分析、字符串处理等。
缺失数据：Series 可以包含缺失数据，Pandas 使用NaN（Not a Number）来表示缺失或无值。


创建 Series
可以使用 pd.Series() 构造函数创建一个 Series 对象，传递一个数据数组（可以是列表、NumPy 数组等）和一个可选的索引数组。
my_pandas.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)

参数说明：
data：Series 的数据部分，可以是列表、数组、字典、标量值等。如果不提供此参数，则创建一个空的 Series。
index：Series 的索引部分，用于对数据进行标记。可以是列表、数组、索引对象等。如果不提供此参数，则创建一个默认的整数索引。
dtype：指定 Series 的数据类型。可以是 NumPy 的数据类型，例如 np.int64、np.float64 等。如果不提供此参数，则根据数据自动推断数据类型。
name：Series 的名称，用于标识 Series 对象。如果提供了此参数，则创建的 Series 对象将具有指定的名称。
copy：是否复制数据。默认为 False，表示不复制数据。如果设置为 True，则复制输入的数据。
fastpath：是否启用快速路径。默认为 False。启用快速路径可能会在某些情况下提高性能。



"""
import pandas as pd

a = [1, 2, 3]
s = pd.Series(a)
print(s)


str = ["Google", "Runoob", "Wiki"]
myvar = pd.Series(str, index = ["x", "y", "z"])
print(myvar)


