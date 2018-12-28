#coding=utf-8
import requests
import urllib.request
import json
# 1 分析JS源码 找出请求 自己模拟实现 难度比较高 麻烦
# 2 模拟浏览器实现 三方库多 简单 但是效率会慢一点
url = 'https://www.toutiao.com/api/pc/focus/'
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
content= response.read().decode('utf-8')
# print (content)
data = json.loads(content)
news = data['data']['pc_feed_focus']
print(news)
for n in news:
  title = n['title']
  img_url = n['image_url']
  print(title,img_url)