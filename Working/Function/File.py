#coding=utf-8
'''
* r 只读模式(默认)
* w 只写模式(不可读，不存在则新创建；存在则重写新内容；)
* a 追加模式(可读，不存在则新创建；存在则只追加内容；)
"+" 表示同时读写某个文件:
r+ 可读写文件(可读；可写；可追加)
w+ 写读
 a+ 同a'''
import csv
def read():
    fin = open("D:\\autodate\\yonghu.txt", "r")
    ct = fin.read()
    # ct = fin.readline()
    fin.close()
    print(ct)
def write():
    conten ="中文 Beautiful is better than ugly."
    fout = open("file.txt", "w")
    fout.write(conten)
    fout.close()
def html():
    fin = open(r'D:\python\Working\Unittest\HtmlReport.html', 'r')
    ht = fin.read()
    # ct = fin.readline()
    fin.close()
    print(ht)

def txt():
    fp = open('D:\\autodate\\yonghu.txt','r')
    lines = fp.readlines()
    fp.close()
    for line in lines:
        username = line.split(',')[0]
        print username
        password = line.split(',')[1]
        print password
def csv():

    date =open('D:\\autodate\\yonghu.csv', 'r')
    lines=date.readlines()
    date.close()
    for line in lines:
        username = line.split(',')[0]
        print username
        password = line.split(',')[1]
        print password
csv()