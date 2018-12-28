# coding=utf-8
import http.cookiejar as cookielib
import urllib

def get_cookie():
    #设置保存cookie的文件，同级目录下的cookie.txt
    filename = 'cookie.txt'
    #声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
    cookie = cookielib.MozillaCookieJar(filename)
    #利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器
    handler = urllib.request.HTTPCookieProcessor(cookie)
    #通过handler来构建opener
    opener = urllib.request.build_opener(handler)
    #创建一个请求，原理同urllib.request的urlopen
    response = opener.open("http://www.baidu.com")
    #保存cookie到文件
    cookie.save(ignore_discard=True, ignore_expires=True)
def use_cookie():
    # 创建MozillaCookieJar实例对象
    cookie = cookielib.MozillaCookieJar()
    # 从文件中读取cookie内容到变量
    cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
    # 创建请求的request
    req = urllib.request.Request("http://www.baidu.com")
    # 利用urllib.request的build_opener方法创建一个opener
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
    response = opener.open(req)
    print (response.read())