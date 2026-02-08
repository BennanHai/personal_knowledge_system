# @Author: Benanahai
# @Time  : 2025/3/23 4:00 
# @Desc  :

# 完整数据库连接操作实例如下：

# 导入模块
import pymysql

# 打开数据库连接
conn = pymysql.connect(
    host="47.97.44.186",
    port=3306,
    user="mysqluser",
    password="mysqluser",
    database="my_db01",
    charset="utf8")
print(f'conn:{conn}')
print(type(conn))

# 获取连接下的游标
# cursor 返回一个游标实例对象，其中包含了很多操作数据的方法，如执行sql语句，sql 执行命令：execute()和executemany()
cursor_test = conn.cursor()
print(f'cursor_test:{cursor_test}')

# 使用 execute()  方法执行 SQL 查询，查询数据库版本
cursor_test.execute("SELECT VERSION()")

# 使用 fetchone() 方法返回一条数据.
data = cursor_test.fetchone()

print("Database version : %s " % data)

# 关闭数据库连接
conn.close()