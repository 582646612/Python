#coding:utf-8
import urllib
import requests
import urllib.request
import re

def geturl(url):
    try:
        request = urllib.request.Request(url)
        # 模拟Mozilla浏览器进行爬虫
        request.add_header("user-agent", "Mozilla/5.0")
        response = urllib.request.urlopen(request)
        content=response.read().decode('gbk')
        pattern = re.compile('<li><span>下一篇：</span><a href="(.*?)" target',re.S)
        items = re.findall(pattern,content)
        pattern1 = re.compile('申论热点</a></div>(.*?)</div>',re.S)
        items1 = re.findall(pattern1,content)
        if items1:
            print(items1)
        else:
            pattern1 = re.compile('单位招聘</a></div>(.*?)</div>', re.S)
            items1 = re.findall(pattern1, content)
            if items1:
                print(items1)
            else:
                pattern1 = re.compile('<p>【导读】</p>.*?</p>(.*?)</div>', re.S)
                items1 = re.findall(pattern1, content)
        return items,items1
    except Exception as e:
        print(e)
def write(conten):
    fout = open("C:\\Users\\\cs\\\Desktop\\computer.txt", "a")
    fout.write(conten)
    fout.close()
if __name__ == '__main__':
    url = 'http://www.zgsydw.com/kaoshitiku/20160530/188416_1.html'
    for i in range(1,1000):
        x=geturl(url)
        url=x[0][0]
        write(x[1][0])
        print(x[0][0])
        print(x[1][0])
