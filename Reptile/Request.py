# -*- coding:utf-8 -*-
import urllib
import re
def get_html(url):
    page = urllib.urlopen(url)#打开网页
    html = page.read()#读取页面源码
    return html
# print htmlcode#在控制台输出
# pageFile=open("pagecode.txt","w")
# pageFile.write(htmlcode)
# pageFile.close()
def get_img(aaa):
    reg=r'src="(.+?\.jpg)" width'
    reg_img=re.compile(reg)
    imglist=reg_img.findall(get_html(aaa))
    x=0
    for img in imglist:
        urllib.urlretrieve(img, '%s.jpg'%x)
        x+=1
print ("输入一个网址")
address=raw_input()
print(address)
get_img(address)