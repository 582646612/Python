from bs4 import BeautifulSoup
import urllib
import re
import random

base_url="https://baike.baidu.com"
his=["/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711"]
url=base_url+his[-1]
html = urllib.urlopen(url).read().decode('utf-8')
print html
soup = BeautifulSoup(html, features='xml')
print soup.find("h1").get_text(),'url:',  his[-1]


# for i in range(20):
#     html = urllib.urlopen(url).read().decode('utf-8')
#     soup = BeautifulSoup(html, features='xml')
#     print(i, soup.find('h1').get_text(), 'url:', hiss)
#
#     # find valid urls
#     sub_urls = soup.find_all("a", {"target": "_blank", "href": re.compile("/item/(%.{2})+$")})
#
#     if len(sub_urls) != 0:
#         his.append(random.sample(sub_urls, 1)[0]['href'])
#     else:
#         # no valid sub link found
#         his.pop()