# -*- coding:utf-8 -*-
import urllib.request

import re
from bs4 import BeautifulSoup
page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}

request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read()
# print content
soup = BeautifulSoup(content, "html.parser", from_encoding="utf-8")
links = soup.find_all('span')
print ("所有的链接")
for link in links:
    print (link.get_text())