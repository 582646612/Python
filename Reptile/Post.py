import urllib
import urllib2
import re

values = {"username": "825096095@qq.com", "password": "cs774411"}
data = urllib.urlencode(values)
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib2.Request(url, data)
response = urllib2.urlopen(request)
# print response.read()
reg=r'"href="="(.+?\"  class)"'
imgre=re.compile(reg)
print imgre
aaa=re.findall(imgre,response)
for i in aaa:
    print i