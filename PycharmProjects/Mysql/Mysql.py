#!/usr/bin/python3
# coding=utf-8
import pymysql

# 打开数据库连接
db = pymysql.connect(host='localhost',port=3306,user='root',passwd='123',db='test',charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询

cursor.execute("SELECT * FROM source")
# fetchall(self):接收全部的返回结果行.
# fetchmany(self, size=None):接收size条返回结果行.如果size的值大于返回的结果行的数量,则会返回cursor.arraysize条数据.
# fetchone(self):返回一条结果行.
# scroll(self, value, mode='relative'):移动指针到某一行.如果mode='relative',则表示从当前所在行移动value条,如果mode='absolute',则表示从结果集的第一 行移动value条.

data = cursor.fetchall()
# for i in range(0,10):
#     print(data)
print(data)

# 关闭数据库连接
db.close()