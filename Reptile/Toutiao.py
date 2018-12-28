#coding:utf-8
import requests
import json

# https://www.toutiao.com/hot_words/ 热词
orc_url = 'https://www.toutiao.com/api/pc/realtime_news/'
data = {'date': 'Wed, 26 Dec 2018 08:16:50 GMT'}
res = requests.post(url=orc_url, data=data)

data=res.text
data=json.loads(data)
data=data['data']

# print(res.text.encoding('utf-8'))
for x in data:
   print('https://www.toutiao.com'+x['open_url'],x['title']) # 格式化输出


