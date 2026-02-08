# @Author: Benanahai
# @Time  : 2024/11/10 19:33
import json

import pandas as pd
import numpy as np

'''
DataFrame 是 Pandas 中的另一个核心数据结构，用于表示二维表格型数据。

DataFrame 是一个表格型的数据结构，它含有一组有序的列，每列可以是不同的值类型（数值、字符串、布尔型值）。

DataFrame 既有行索引也有列索引，它可以被看做由 Series 组成的字典（共同用一个索引）。

DataFrame 提供了各种功能来进行数据访问、筛选、分割、合并、重塑、聚合以及转换等操作。

DataFrame 特点：

二维结构： DataFrame 是一个二维表格，可以被看作是一个 Excel 电子表格或 SQL 表，具有行和列。可以将其视为多个 Series 对象组成的字典。

列的数据类型： 不同的列可以包含不同的数据类型，例如整数、浮点数、字符串或 Python 对象等。

索引：DataFrame 可以拥有行索引和列索引，类似于 Excel 中的行号和列标。

大小可变：可以添加和删除列，类似于 Python 中的字典。

自动对齐：在进行算术运算或数据对齐操作时，DataFrame 会自动对齐索引。

处理缺失数据：DataFrame 可以包含缺失数据，Pandas 使用 NaN（Not a Number）来表示。

数据操作：支持数据切片、索引、子集分割等操作。

时间序列支持：DataFrame 对时间序列数据有特别的支持，可以轻松地进行时间数据的切片、索引和操作。

丰富的数据访问功能：通过 .loc、.iloc 和 .query() 方法，可以灵活地访问和筛选数据。

灵活的数据处理功能：包括数据合并、重塑、透视、分组和聚合等。

数据可视化：虽然 DataFrame 本身不是可视化工具，但它可以与 Matplotlib 或 Seaborn 等可视化库结合使用，进行数据可视化。

高效的数据输入输出：可以方便地读取和写入数据，支持多种格式，如 CSV、Excel、SQL 数据库和 HDF5 格式。

描述性统计：提供了一系列方法来计算描述性统计数据，如 .describe()、.mean()、.sum() 等。

灵活的数据对齐和集成：可以轻松地与其他 DataFrame 或 Series 对象进行合并、连接或更新操作。

转换功能：可以对数据集中的值进行转换，例如使用 .apply() 方法应用自定义函数。

滚动窗口和时间序列分析：支持对数据集进行滚动窗口统计和时间序列分析。


DataFrame 构造方法如下：
pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)
参数说明：

data：DataFrame 的数据部分，可以是字典、二维数组、Series、DataFrame 或其他可转换为 DataFrame 的对象。如果不提供此参数，则创建一个空的 DataFrame。
index：DataFrame 的行索引，用于标识每行数据。可以是列表、数组、索引对象等。如果不提供此参数，则创建一个默认的整数索引。
columns：DataFrame 的列索引，用于标识每列数据。可以是列表、数组、索引对象等。如果不提供此参数，则创建一个默认的整数索引。
dtype：指定 DataFrame 的数据类型。可以是 NumPy 的数据类型，例如 np.int64、np.float64 等。如果不提供此参数，则根据数据自动推断数据类型。
copy：是否复制数据。默认为 False，表示不复制数据。如果设置为 True，则复制输入的数据。
'''

print("1. 使用列表的列表创建")
data = [['google', 10], ['runoob', 23], ['wiki', 13]]
df01 = pd.DataFrame(data)
'''
        0   1
0  google  10
1  runoob  23
2    wiki  13
'''
print(df01)

df02 = pd.DataFrame(data, columns=['Site', 'Age'])
"""
     Site  Age
0  google   10
1  runoob   23
2    wiki   13
"""
print(df02)

print("2. 使用字典创建 从字典创建：字典的键成为列名，值成为列数据。")
data02 = {'Site': ['google', 'runoob', 'wiki'], 'Age': [10, 23, 13]}
pd03 = pd.DataFrame(data02)
print(pd03)
print()

data03 = [{'Site': 'google', 'Age': 10}, {'Site': 'runoob', 'Age': 23}, {'Site': 'wiki', 'Age': 13}]
df04 = pd.DataFrame(data03)
print(df04)
print()

# key 为列名
data04 = [{'a': 22, 'b': 55}, {'a': 33, 'b': 66, 'c': 77}, {'a': 33, 'b': 66, 'c': 77, 'd': 77}]
df05 = pd.DataFrame(data04)
print(df05)
"""没有对应的部分数据为 NaN。
    a   b     c     d
0  22  55   NaN   NaN
1  33  66  77.0   NaN
2  33  66  77.0  77.0
"""

print()
print("3. 使用 ndarrays 创建")
ndarray_data = np.array([
    ['google', 10],
    ['runoob', 23],
    ['wiki', 13]
])
# print(ndarray_data)
df04 = pd.DataFrame(ndarray_data, columns=['Site', 'Age'])
print(df04)

print(" 使用series 创建DataFrame")
s1 = pd.Series(['Alice', 'Bob', 'Charlie'])
s2 = pd.Series([25, 30, 35])
s3 = pd.Series(['New York', 'Los Angeles', 'Chicago'])
df06 = pd.DataFrame({'Name': s1, 'Age': s2, 'City': s3})
print(df06)
"""
      Name  Age         City
0    Alice   25     New York
1      Bob   30  Los Angeles
2  Charlie   35      Chicago
"""

print(" 使用loc属性返回指定行的数据")
print(df05.loc[0])
"""
注意：返回结果其实就是一个 Pandas Series 数据。
a    22.0
b    55.0
c     NaN
d     NaN
"""
print(df04.loc[0])

# 也可以返回多行数据，使用 [[ ... ]] 格式，... 为各行的索引，以逗号隔开：
print(df05.loc[[0, 2]])
"""
Name: 0, dtype: object
    a   b     c     d
0  22  55   NaN   NaN
2  33  66  77.0  77.0
"""

print("*" * 23)
"""
DataFrame 的属性和方法:DataFrame 对象有许多属性和方法，用于数据操作、索引和处理，
例如：shape、columns、index、head()、tail()、info()、describe()、mean()、sum() 等。
"""

# DataFrame 的属性和方法
print(df04.shape)  # 形状
print(df04.columns)  # 列名
print(df04.index)  # 索引
print(df04.head())  # 前几行数据，默认是前 5 行
print(df04.tail())  # 后几行数据，默认是后 5 行
print(df04.info())  # 数据信息
print(df04.describe())  # 描述统计信息
# print(df04.mean())    # 求平均值
# print(df04.sum())     # 求和


print("修改列数据：直接对列进行赋值。" * 23)
print(df05)

df05['a'] = [99, 88, 77]
print(df05)

# 添加新列：给新列赋值。
df05['newcolumn'] = [22, 22, 22]
print(df05)

# ·添加新行：使用 loc、append 或 concat 方法。
# 使用 loc 为特定索引添加新行
df05.loc[55] = [88, 88, 88, 88, 88]
print(df05)

#
df07 = pd.read_json("sites.json")
print(df07)
print(df07.to_string())

# 读取 JSON 转为 DataFrame
s = {
    "col1": {"row1": 1, "row2": 2, "row3": 3},
    "col2": {"row1": "x", "row2": "y", "row3": "z"},
}
df08 = pd.DataFrame(s)
print(df08)


df09 = pd.read_json("nested_list.json")
print(df09)
# 这时我们就需要使用到 json_normalize() 方法将内嵌的数据完整的解析出来：
with open("nested_list.json", "r") as f:
    data = json.loads(f.read())
df_nested = pd.json_normalize(data, record_path=["students"])
print(df_nested)
"""
          school_name  ...                                           students
0  ABC primary school  ...  {'id': 'A001', 'name': 'Tom', 'math': 60, 'phy...
1  ABC primary school  ...  {'id': 'A002', 'name': 'James', 'math': 89, 'p...
2  ABC primary school  ...  {'id': 'A003', 'name': 'Jenny', 'math': 79, 'p...

[3 rows x 3 columns]
     id   name  math  physics  chemistry
0  A001    Tom    60       66         61
1  A002  James    89       76         51
2  A003  Jenny    79       90         78
"""


# 让我们尝试读取更复杂的 JSON 数据，该数据嵌套了列表和字典，数据文件 nested_mix.json
with open("nested_mix.json", "r") as f:
    data = json.loads(f.read())

df_nested_mix = pd.json_normalize(
    data,
    record_path=["students"],
    meta=[
        "class",
        "school_name",
        ["info", "president"],
        ["info", "contacts", "tel"]
    ]
)
print(df_nested_mix)

