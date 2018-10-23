#coding=utf-8
import urllib2
import json
# 1 分析JS源码 找出请求 自己模拟实现 难度比较高 麻烦
# 2 模拟浏览器实现 三方库多 简单 但是效率会慢一点
url = 'http://www.toutiao.com/api/pc/focus/'
wbdata = urllib2.requests.get(url).read().get_text()
print wbdata
data = json.loads(wbdata)
news = data['data']['pc_feed_focus']

for n in news:
  title = n['title']
  img_url = n['image_url']
  url = n['media_url']
  print(url,title,img_url)