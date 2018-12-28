#coding:utf-8
import urllib
import urllib.request
import re

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
try:
    request = urllib.request.Request(url,headers = headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    # print(content)
    pattern = re.compile('<div class="content".*?span>(.*?)</span.*?</div>',re.S)
    items = re.findall(pattern,content)
    for x in items:
        x = re.sub('\n', '', x)
        x=re.sub('<br/>', '\n', x)
        print(x,'\n')
except urllib.request as e:
    if hasattr(e, "code"):
        print(e.code)

    if hasattr(e, "reason"):
        print(e.reason)