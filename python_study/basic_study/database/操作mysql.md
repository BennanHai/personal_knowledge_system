[第80天：Python 操作 MySQL](https://mp.weixin.qq.com/s?__biz=MzkxNDI3NjcwMw==&mid=2247493388&idx=1&sn=c56910a2610659c51393ddaa44985f05&chksm=c1724f3cf605c62a3d14aacf44724b977512539244db5c5b7d990af1e36ffa01f9021f4782ee&scene=21#wechat_redirect)

本章节Python 操作 MySQL 数据库需要是使用到 PyMySQL 驱动


## 1. 操作流程

1. 安装 MySQL 数据库
2. pymysql 模块安装与使用
3. 获取数据库的连接
4. 执行 sql 语句或存储过程
5. 关闭数据库连接


## pymysql 模块安装与数据库 CURD

### 一、安装

PyMySQL 模块使用 pip命令进行安装：

```
pip3 install PyMySQL
```

### 二、pymysql 连接数据库

1. **pymysql .connect 函数：连接上数据库**

```
# 导入模块
import pymysql


# 打开数据库连接


conn = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="123456",
    database="test_db",
    charset="utf8")


print(conn)
print(type(conn))
 
```

输出结果显示如下：表面数据库连接成功

```
<pymysql.connections.Connection object at 0x00000000022A54A8>
<class 'pymysql.connections.Connection'>
```

2. **conn.cursor():获取游标**

如果要操作数据库，光连接数据是不够的，咱们必须拿到操作数据库的游标，才能进行后续的操作，游标的主要作用是用来接收数据库操作后的返回结果，比如读取数据、添加数据。通过获取到的数据库连接实例 conn 下的 cursor() 方法来创建游标。


3. **完整数据库连接操作实例如下：**

```
# 导入模块
import pymysql


# 打开数据库连接
conn = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="123456",
    database="test_db",
    charset="utf8")
# print(conn)
# print(type(conn))


# 获取连接下的游标
cursor_test = conn.cursor()
print(cursor_test)


# 使用 execute()  方法执行 SQL 查询，查询数据库版本
cursor_test.execute("SELECT VERSION()")


# 使用 fetchone() 方法返回一条数据.
data = cursor_test.fetchone()


print("Database version : %s " % data)


# 关闭数据库连接
conn.close()
```



### 三、CRUD操作

1. 创建表

创建表代码如下：

```
import pymysql


# 打开数据库连接
conn = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="123456",
    database="test_db",
    charset="utf8")


# 获取连接下的游标
cursor_test = conn.cursor()


# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor_test.execute("DROP TABLE IF EXISTS EMPLOYEE")


# 使用预处理语句创建表
sql = """CREATE TABLE user1 (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""


cursor_test.execute(sql)


# 关闭数据库连接
conn.close()
```


2. 插入数据

插入数据实现代码：

```
import pymysql


# 打开数据库连接
conn = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="123456",
    database="test_db",
    charset="utf8")


# 获取连接下的游标
cursor_test = conn.cursor()


# 使用预处理语句创建表
sql = """INSERT INTO user1(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Fei', 'Fei', 20, 'M', 1000)"""


try:
   # 执行sql语句
   cursor_test.execute(sql)
   # 提交到数据库执行
   conn.commit()
except:
   # 如果发生错误则回滚
   conn.rollback()


# 关闭数据库连接
conn.close()
```


3. 查询数据

Python查询Mysql使用 fetchone() 方法获取单条数据, 使用fetchall() 方法获取多条数据。

* fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
* fetchall(): 接收全部的返回结果行.
* rowcount: 这是一个只读属性，并返回执行 execute()方法后影响的行数。

**查询数据代码如下：**

```
import pymysql

# 打开数据库连接
conn = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="123456",
    database="test_db",
    charset="utf8")


# 获取连接下的游标
cursor_test = conn.cursor()


sql = """
    select * from user1"""


try:
    # 执行 sql 语句
    cursor_test.execute(sql)
    # 显示出所有数据
    data_result = cursor_test.fetchall()
    for row in data_result:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        # 打印结果
        print("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
              (fname, lname, age, sex, income))
except:
    print("Error: unable to fetch data")


# 关闭数据库连接
conn.close()
```


4. 更新数据

```
# 导入模块
import pymysql


# 打开数据库连接
conn = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="123456",
    database="test_db",
    charset="utf8")
# print(conn)
# print(type(conn))


# 获取连接下的游标
cursor_test = conn.cursor()


sql = "UPDATE user1 SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')


try:
    # 执行SQL语句
    cursor_test.execute(sql)
    # 提交到数据库执行
    conn.commit()
except:
    # 发生错误时回滚
    conn.rollback()


# 关闭数据库连接
conn.close()
```

5. 删除数据

```
# 导入模块
import pymysql


# 打开数据库连接
conn = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="123456",
    database="test_db",
    charset="utf8")
# print(conn)
# print(type(conn))


# 获取连接下的游标
cursor_test = conn.cursor()


sql = "DELETE * FROM user1"


try:
    # 执行SQL语句
    cursor_test.execute(sql)
    # 提交到数据库执行
    conn.commit()
except:
    # 发生错误时回滚
    conn.rollback()


# 关闭数据库连接
conn.close()
```
