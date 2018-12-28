import requests
from bs4 import BeautifulSoup

url = 'http://www.zhipin.com/job_detail/?query=Python&scity=101200100&source=2'
headers = {
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Accept-Language':'zh-CN,zh;q=0.8',
	'Host':'www.zhipin.com',
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
}

a = requests.get(url,headers=headers)
soup = BeautifulSoup(a.text,'lxml')
b = soup.find_all("span",class_="red")
print(b)
for i in b:
	c = i.get_text("|", strip=True)
	print(c)