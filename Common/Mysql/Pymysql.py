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
    def insert(self):
        sql = "INSERT INTO `tech_courses` (`total`, `price`, `area`, `type`, `local`, `title`, `created_time`) VALUES('235', '18196元/平米', '129.15平米暂无数据', '3室2厅高楼层/共24层', '所在区域五华顺城', '南北通透朝南看金马坊朝北看南屏街，视野开阔阳光充足', '2019-01-03 13:46:34')"
        self.mycursor.execute(sql)
        self.mydb.commit()

if __name__ == '__main__':
    Mysql().insert()
