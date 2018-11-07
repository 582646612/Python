#coding:utf-8

import yaml


# open方法打开直接读出来
f = open("test.yaml", 'r')
cfg = f.read()
# print(cfg)
d = yaml.load(cfg)  # 用load方法转字典
print(d)


# import csv
# '''stu1=Studet('Jack',"Beijing")
# stu1.talk()
# stu1=Studet('Marry',"KunMing")
# stu1.talk()'''
# # csv_file=csv.reader(open('G:\Jmeter\date.csv','r'))
# # print(csv_file)
# # for stu in csv_file:
# #     print(stu[2])
# # r打开  a追加  w写入   模式
# stu=['Marry',25,'changsha']
# stu1=['Snow',23,'logange']
# #打开文件，设定写入模式
# out=open('G:\Jmeter\date.csv','a',newline="")
# csv_write=csv.writer(out,dialect='excel')
# csv_write.writerow(stu)
# csv_write.writerow(stu1)
# print("It'is over")

