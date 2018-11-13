# coding:utf-8
#mysql -u root -p

import mysql.connector
class Mysql():
    def __init__(self):
        self.mydb = mysql.connector.connect(
        host="localhost",  # 数据库主机地址
        user="root",  # 数据库用户名
        passwd="123",  # 数据库密码
        database="test"
        )
        self.mycursor = self.mydb.cursor()

    def Select(self):
        sql = "SELECT * FROM source"
        self.mycursor.execute(sql)
        data = self.mycursor.fetchall()
        for x in data:
            print(x)
        return data


    def Update(self):
        sql = "UPDATE source SET source_name = %s WHERE source_name = %s"
        val = ("bluetooth80117945172", "bluetooth80117945112")
        self.mycursor.execute(sql, val)
        self.mydb.commit()
        print(self.mycursor.rowcount, " 条记录被修改")

    def Delect(self):
        sql = "DELETE FROM source WHERE source_name = %s"
        na = ("bluetooth80155659698",)
        self.mycursor.execute(sql,na)
        self.mydb.commit()
        print(self.mycursor.rowcount, " 条记录删除")

if __name__ == '__main__':
    Mysql().Select()
