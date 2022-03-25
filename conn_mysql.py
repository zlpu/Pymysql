#1导入库
import pymysql

#2创建连接
conn=pymysql.connect(
    host='192.168.174.130',
    user='pymysql',
    passwd='pymysql',
)
#3创建游标，传递命令
cursor=conn.cursor()

#4 定义sql语句，执行sql语句
#4.1 创建数据库GDP_2021,查询数据库列表
sql_create_database='create database if not exists GDP_2021 character set utf8 collate utf8_bin;'
cursor.execute(sql_create_database)
sql_show_databases='show databases;'
cursor.execute(sql_show_databases)
show_databases=cursor.fetchall()
print('\033[1;31m数据库列表\033[0m')
for i in range(len(show_databases)):
    print(show_databases[i])
#4.2创建表S1，（top、city、GDP），并插入数据
sql_create_table1='use GDP_2021;'
sql_create_table2='create table if not exists S1(top int primary key auto_increment,City varchar(20),GDP varchar(200) );'
cursor.execute(sql_create_table1)
cursor.execute(sql_create_table2)
sql_insert='insert into S1 (City,GDP) values (%s,%s);'
cursor.execute(sql_insert,['广东',27117])
cursor.execute(sql_insert,['江苏',25800])
cursor.execute(sql_insert,['山东',18800])
#4.3 查表
sql_select='select * from S1;'
cursor.execute(sql_select)
select=cursor.fetchall()
print('\033[1;31m表内容如下：\033[0m')
for j in range(len(select)):
    print(select[j])
#5提交事务
conn.commit()
#6关闭游标
cursor.close()
#7关闭连接
conn.close()