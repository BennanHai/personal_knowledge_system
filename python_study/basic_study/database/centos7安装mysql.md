# 安装mysql

[Linux系统centos7安装、配置、远程连接mysql8.0.35、开机自启动（究级无敌宇宙第一详细）](https://blog.csdn.net/zaixiaqin/article/details/134619062)

## 1. 准备工作

### 1.1 查看是否安装 libaio

yum list installed | grep libaio

没有安装则执行安装命令

yum install -y libaio

### 1.2 确定操作系统版本，确定需要下载的mysql版本

```bash
> uname -m # 查看系统是64位还是32位

> ldd --version # 确定glib版本：
ldd (GNU libc) 2.17
```

## 2. 下载mysql

> 官方下载地址：[MySQL :: Download MySQL Community Server](https://dev.mysql.com/downloads/mysql/ "MySQL :: Download MySQL Community Server")

根据上面操作系统确定需要下载的是：64位，glibc2.17版本的：

## 3. 上传文件解压并安装

1. 下载后上传到服务器的/usr/local目录下并解压：

```bash
➜  /local ll
total 885M
drwx--x--x  4 root root 4.0K Mar 20 13:44 containerd
-rw-r--r--  1 root root 860M Mar 23 01:24 mysql-8.4.4-linux-glibc2.17-x86_64.tar.xz
drwxr-xr-x 17 1000 1000 4.0K Mar 20 17:54 Python-3.10.6
-rw-r--r--  1 root root  25M Aug  2  2022 Python-3.10.6.tgz
➜  /opt

```

这里需要 -Jxvf ，不能使用 -zxvf.

```bash
cd /usr/local
tar -Jxvf mysql-8.4.4-linux-glibc2.17-x86_64.tar.xz
```

2. 重命名文件夹:

```bash
mv mysql-8.4.4-linux-glibc2.17-x86_64 mysql8  # 文件夹重命名
```

3. 添加path环境变量

```bash
# 临时添加
export PATH=$PATH:/usr/local/mysql8/bin  # 临时添加path变量，系统重启后失效

# 永久添加
echo "export PATH=$PATH:/usr/local/mysql8/bin" >>/etc/profile  # 编辑 /etc/profile 文件
source /etc/profile    # 使更改生效
```

4. 验证安装结果

```bash
➜  local vim /etc/profile
➜  local source /etc/profile
➜  local
➜  local mysql --version
mysql  Ver 8.4.4 for Linux on x86_64 (MySQL Community Server - GPL)

```

## 4. 创建用户及数据目录

1. 创建用户及组

```bash
groupadd mysql  # 创建用户组mysql
useradd -r -g mysql mysql  # 创建用户mysq（-r 创建系统用户  -g 分组）
```

2. 创建数据目录

```bash
mkdir -p /data/mysql8/datas  # 数据目录
mkdir -p /data/mysql8/logs  # 日志目录
```

3. 更改目录用户组及权限

```bash
chown -R mysql:mysql /data/mysql8
chmod -R 750 /data/mysql8/datas
chmod -R 750 /data/mysql8/logs

```

## 5. 创建配置文件

```bash
vim /etc/my.cnf  # 编辑 /etc/my.cnf
# 没有这个文件不要紧，编辑后保存即可
```

内容如下：

```bash
[mysql]
#默认字符集
default-character-set=utf8mb4
#[client]
port       = 3306
socket     = /tmp/mysql.sock

#[mysqld]
port       = 3306
server-id  = 3306
socket     = /tmp/mysql.sock
## 安装目录
basedir    = /usr/local/mysql8
## 数据存放目录
datadir    = /data/mysql8/datas/mysql
log-bin    = /data/mysql8/datas/mysql/mysql-bin
innodb_data_home_dir      =/data/mysql8/datas/mysql
innodb_log_group_home_dir =/data/mysql8/datas/mysql
##日志及进程数据的存放目录
log-error =/data/mysql8/logs/mysql.log
pid-my_file  =/data/mysql8/logs/mysql.pid
## 服务端使用的字符集默认为8比特编码
character-set-server=utf8mb4
lower_case_table_names=1
autocommit =1
## 创建新表时将使用的默认存储引擎
default_storage_engine = InnoDB
```

**验证配置文件语法**

```
/usr/local/mysql8/bin/mysqld --defaults-file=/etc/my.cnf --validate-config
```

若无错误输出，表示配置文件合法。


### 6. 初始化并启动mysql

1. 指定配置文件初始化mysql：

```bash
mysqld --defaults-my_file=/etc/my.cnf --basedir=/usr/local/mysql8 --datadir=/data/mysql8/datas/mysql --user=mysql --initialize-insecure
```

```bash
➜  local mysqld --defaults-my_file=/etc/my.cnf --basedir=/usr/local/mysql8 --datadir=/data/mysql8/datas/mysql --user=mysql --initialize-insecure
2025-03-22T17:51:53.671533Z 0 [System] [MY-015017] [Server] MySQL Server Initialization - start.
2025-03-22T17:51:53.673478Z 0 [System] [MY-013169] [Server] /usr/local/mysql8/bin/mysqld (mysqld 8.4.4) initializing of server in progress as process 4662
2025-03-22T17:51:53.808111Z 1 [System] [MY-013576] [InnoDB] InnoDB initialization has started.
2025-03-22T17:51:54.946354Z 1 [System] [MY-013577] [InnoDB] InnoDB initialization has ended.
2025-03-22T17:51:57.305834Z 6 [Warning] [MY-010453] [Server] root@localhost is created with an empty password ! Please consider switching off the --initialize-insecure option.
2025-03-22T17:51:59.923365Z 0 [System] [MY-015018] [Server] MySQL Server Initialization - end.
➜  local

```

- 各参数意义：
  --defaults-file: 指定配置文件 （放在--initialize-insecure前）
  --user: 指定用户
  --basedir: 指定安装目录
  --datadir: 指定初始化数据目录
  --initialize-insecure: 初始化不设置密码（若无该参数，则随机生成密码，需在 /data/mysql8/logs/mysql.log 查看）

2. 启动mysql

若没有配置环境变量，即没有执行第四步，则执行该命令：/usr/local/mysql8/bin/mysqld_safe --defaults-file=/usr/local/mysql8/my.cnf &
已经配置好了环境变量，则执行：mysqld_safe --defaults-file=/etc/my.cnf &

```bash
# 前台启动（观察错误）
sudo -u mysql /usr/local/mysql8/bin/mysqld --defaults-my_file=/etc/my.cnf --console

# 或后台启动
sudo -u mysql /usr/local/mysql8/bin/mysqld_safe --defaults-my_file=/etc/my.cnf &
```

4. 验证是否启动

`ps -ef | grep mysql`

```bash
bash
➜  mysql sudo -u mysql /usr/local/mysql8/bin/mysqld_safe --defaults-my_file=/etc/my.cnf &
[1] 5990
➜  mysql 2025-03-22T18:38:23.709416Z mysqld_safe Logging to '/data/mysql8/logs/mysql.log'.
2025-03-22T18:38:23.750508Z mysqld_safe Starting mysqld daemon with databases from /data/mysql8/datas/mysql

➜  mysql
➜  mysql cd ..
➜  datas ps -ef | grep mysql
root      5431  3996  0 02:20 pts/0    00:00:00 su - mysql
mysql     5432  5431  0 02:20 pts/0    00:00:00 -bash
mysql     5455  5432  0 02:23 pts/0    00:00:00 zsh
root      5990  5466  0 02:38 pts/0    00:00:00 sudo -u mysql /usr/local/mysql8/bin/mysqld_safe --defaults-my_file=/etc/my.cnf
mysql     5997  5990  0 02:38 pts/0    00:00:00 /bin/sh /usr/local/mysql8/bin/mysqld_safe --defaults-my_file=/etc/my.cnf
mysql     6234  5997  1 02:38 pts/0    00:00:01 /usr/local/mysql8/bin/mysqld --defaults-my_file=/etc/my.cnf --basedir=/usr/local/mysql8 --datadir=/data/mysql8/datas/mysql --plugin-dir=/usr/local/mysql8/lib/plugin --log-error=/data/mysql8/logs/mysql.log --pid-my_file=/data/mysql8/logs/mysql.pid --socket=/tmp/mysql.sock --port=3306
➜  datas
```


## 7. （远程）登录mysql

1. 登录mysql，修改root用户密码

```bash
➜  datas mysql -uroot
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 8
Server version: 8.4.4 MySQL Community Server - GPL

Copyright (c) 2000, 2025, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY '密码';
Query OK, 0 rows affected (0.01 sec)

mysql>
mysql> FLUSH PRIVILEGES;
Query OK, 0 rows affected (0.00 sec)

mysql>

```

2. 创建远程连接用户

```bash
mysql> use mysql;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql>
mysql> SELECT user,host,plugin,authentication_string FROM user;
+------------------+-----------+-----------------------+------------------------------------------------------------------------+
| user             | host      | plugin                | authentication_string                                                  |
+------------------+-----------+-----------------------+------------------------------------------------------------------------+
| mysql.infoschema | localhost | caching_sha2_password | $A$005$THISISACOMBINATIONOFINVALIDSALTANDPASSWORDTHATMUSTNEVERBRBEUSED |
| mysql.session    | localhost | caching_sha2_password | $A$005$THISISACOMBINATIONOFINVALIDSALTANDPASSWORDTHATMUSTNEVERBRBEUSED |
| mysql.sys        | localhost | caching_sha2_password | $A$005$THISISACOMBINATIONOFINVALIDSALTANDPASSWORDTHATMUSTNEVERBRBEUSED |
| root             | localhost | caching_sha2_password | $A$005$8LFLU`V5`4r%ik8LkQPOuAJsqsGR1ixMAmP8r1q/gIDP2uXE5HLy9o/ |
+------------------+-----------+-----------------------+------------------------------------------------------------------------+
4 rows in set (0.00 sec)

mysql> create user 'mysqluser' @'%' identified by '密码';
Query OK, 0 rows affected (0.01 sec)

mysql>
mysql>
mysql> GRANT ALL PRIVILEGES ON mydb.* TO 'mysqluser'@'%';
Query OK, 0 rows affected (0.00 sec)

mysql> FLUSH PRIVILEGES;
Query OK, 0 rows affected (0.00 sec)

mysql>
mysql> SELECT user,host,plugin,authentication_string FROM user;
+------------------+-----------+-----------------------+------------------------------------------------------------------------+
| user             | host      | plugin                | authentication_string                                                  |
+------------------+-----------+-----------------------+------------------------------------------------------------------------+
| mysqluser        | %         | caching_sha2_password | $A$005$n++GK%wgnA|b Eg7&gt1dXKqYNoY1KF9DDrJ/LMkhGy6ynvbIiUogWXGg8gA |
| mysql.infoschema | localhost | caching_sha2_password | $A$005$THISISACOMBINATIONOFINVALIDSALTANDPASSWORDTHATMUSTNEVERBRBEUSED |
| mysql.session    | localhost | caching_sha2_password | $A$005$THISISACOMBINATIONOFINVALIDSALTANDPASSWORDTHATMUSTNEVERBRBEUSED |
| mysql.sys        | localhost | caching_sha2_password | $A$005$THISISACOMBINATIONOFINVALIDSALTANDPASSWORDTHATMUSTNEVERBRBEUSED |
| root             | localhost | caching_sha2_password | $A$005$8LFLU`V5`4r%ik8LkQPOuAJsqsGR1ixMAmP8r1q/gIDP2uXE5HLy9o/ |
+------------------+-----------+-----------------------+------------------------------------------------------------------------+
5 rows in set (0.00 sec)

mysql>

```

3. 远程连接

8.0+的mysql，需要修改认证方式：caching_sha2_password

mysql>  ALTER USER 'mysqluser'@'%' IDENTIFIED WITH caching_sha2_password BY '密码';
Query OK, 0 rows affected (0.01 sec)

mysql>
mysql> FLUSH PRIVILEGES;
Query OK, 0 rows affected (0.01 sec)

4. 测试

```sql
show databases;

CREATE DATABASE my_db01;

USE my_db01;
CREATE TABLE my_table01(
    id INT,
    name VARCHAR(10)
);
DESC my_table01;
INSERT INTO my_table01 VALUES(1, '老色批');
INSERT INTO my_table01 VALUES(2, '孙悟空');
INSERT INTO my_table01 VALUES(3, '강감찬');

SELECT * FROM my_table01;

```


## **8. 创建 Systemd 服务（推荐）**

创建服务文件 `/etc/systemd/system/mysql.service`：

```ini
[Unit]
Description=MySQL Server
After=network.target

[Service]
User=mysql
Group=mysql
ExecStart=/usr/local/mysql8/bin/mysqld --defaults-file=/etc/my.cnf
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

启用服务：

```bash
sudo systemctl daemon-reload
sudo systemctl start mysql

sudo systemctl enable mysql
```
