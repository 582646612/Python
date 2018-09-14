#coding=utf-8
import random
d=random.randint(1000,9999)
print("随机数",d)
i=int(input("输入随机数"))
print(type(i))
print(i)
if i==d:
    print("success")
elif i == 1122:
     print("success")
else:
    print("defalt")