#!/usr/bin/python3

import pymysql
import re
import string
# 打开数据库连接
db = pymysql.connect("192.168.0.167", "root", "123456", "3cinter")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询

cursor.execute("SELECT `jichaTotal`, `gongyingTotal`, `chaoyueTotal`, `dayReleaseTotal`, `bvTotal`, `otherTotal` FROM `zyx_member_revenue` WHERE member_id=(SELECT id FROM `zyx_member` WHERE username=542001)")
# fetchall(self):接收全部的返回结果行.
# fetchmany(self, size=None):接收size条返回结果行.如果size的值大于返回的结果行的数量,则会返回cursor.arraysize条数据.
# fetchone(self):返回一条结果行.
# scroll(self, value, mode='relative'):移动指针到某一行.如果mode='relative',则表示从当前所在行移动value条,如果mode='absolute',则表示从结果集的第一 行移动value条.

data = cursor.fetchall()
print(data)

# if data<15000:
#     print(3)
# elif data<50000 and data>15000:
#     print(6)
# elif data<150000 and data>50000:
#     print(9)
# elif data<500000 and data>150000:
#     print(11)
# elif data<1500000 and data>500000:
#     print(13)
# else:
#     print(15)
# for i in range(0,10):
#     print(data)


# 关闭数据库连接
db.close()