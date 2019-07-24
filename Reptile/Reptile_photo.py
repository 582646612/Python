#coding:utf-8
import re
import urllib
import os
def read():
    fin = open("D:\\autodate\\123.txt", "r")
    ct = fin.read()
    fin.close()
    return ct
# page = urllib.urlopen('http://tieba.baidu.com/p/4721099001')
# #read（）返回的结果是二进制的需要转换成字符串
# html =page.read()

reg=r'"imgUrl":"(.+?\.jpg)"'
imgre=re.compile(reg)
print (imgre)
imglist=re.findall(imgre,read())

x=0
os.chdir(os.path.join(os.getcwd(), 'picture'))
for i in imglist:
    urllib.urlretrieve(i,'%s.jpg' %x)
    print (i)
    x+=1



