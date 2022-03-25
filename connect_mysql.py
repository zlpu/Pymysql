#1.导入库
import pymysql
#2.创建连接，定义主机、用户、密码等连接信息
conn=pymysql.connect(
    host='192.168.174.130',
    user='pymysql',
    passwd='pymysql'

)
#3.创建游标，传递命令
cursor=conn.cursor()
#4.定义sql语句、执行命令
#4.1创建数据库
sql_cretae_database='create database if not exists GDP character set utf8 collate utf8_bin;'
cursor.execute(sql_cretae_database)
#4.2查询数据库并输出
sql_show_databases='show databases;'
cursor.execute(sql_show_databases)
show_databases=cursor.fetchall()
print("\033[1;31m数据库列表：\033[0m")
for i in range(len(show_databases)):
    print(show_databases[i][0])
#4.3数据库GDP中创建表GDP2021_S1
sql_create_table1='use GDP;'
sql_create_table2='create table if not exists GDP2021_S1(TOP int(11) not null primary key AUTO_INCREMENT,City varchar(200),GDP2021_S1 varchar(250));'
cursor.execute(sql_create_table1)
cursor.execute(sql_create_table2)
#4.4查看表结构
sql_desc_table='desc GDP2021_S1;'
cursor.execute(sql_desc_table)
desc_table=cursor.fetchall()
print('\033[1;31m表结构：\033[0m')
for j in range(len(desc_table)):
    print(desc_table[j])

#4.5插入数据
sql_insert='insert into GDP2021_S1 (City,GDP2021_S1) values (%s,%s);'
cursor.execute(sql_insert,['广东',27117])
cursor.execute(sql_insert,['江苏',25800])
cursor.execute(sql_insert,['山东',18800])
#4.6查询表
sql_select='select * from GDP2021_S1'
cursor.execute(sql_select)
select=cursor.fetchall()
print("\033[1;31m表内容：\033[0m")
for k in range(len(select)):
   print(select[k])

#5提交事务
conn.commit()
#6关闭游标
cursor.close()
#7关闭连接
conn.cursor()