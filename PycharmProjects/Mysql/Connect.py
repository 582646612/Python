#mysql -u root -p
import pymysql.cursors
connection=pymysql.connect(host='localhost',port=3306,user='root',password='123',db='test',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
cursor=connection.cursor()
sql="select * from source"
cursor.execute(sql)
result = cursor.fetchall()
for data in result:
    print(data)
connection.close()