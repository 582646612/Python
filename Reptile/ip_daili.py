import urllib.request
import time
import xml.etree as etree
import re
import requests
from bs4 import BeautifulSoup
def get_url(url):     # 国内高匿代理的链接
    url_list=[]
    for i in range(1,100):
        url_new=url+str(i)
        url_list.append(url_new)
    return url_list

def get_contents(url):
    response = urllib.request.urlopen(url)
    data = response.read().decode('utf-8')

    return data
def get_info(xml):
    pattern = re.compile('<td data-title="IP">(.*?)</td>.*?<td data-title="PORT">(.*?)</td>', re.S)
    items = re.findall(pattern, xml)
    return items

def verif_ip(ip,port):
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}
    proxy={'http':'http://%s:%s'%(ip,port)}
    repx = urllib.request.ProxyHandler(proxy)
    opener = urllib.request.build_opener(repx)
    url='https://www.baidu.com/'
    req=urllib.request.Request(url)

    try:
        res = opener.open(req)
        print(res)
        time.sleep(3)
        content=res.read()
        if content:
            print('this is ok')
        else:
            print('It is not ok')
    except urllib.request.URLError as e:
        print(e.reason)


def write(conten):
    with open("file.txt", "a") as fout:
        fout.write(conten)

if __name__ == '__main__':
    url = 'https://www.kuaidaili.com/free/inha/'
    url_list = get_url(url)

    # x=get_contents(url_list[0])
    # print(x)
    # content = get_contents(url_list[0])
    for i in url_list:
        print(i)
        content=get_contents(i)
        # print(content)
        time.sleep(1)
        datas=get_info(content)

        for data in datas:
            print(data[0],data[1])
            x=str(data[0]+','+data[1]+'\n')
            write(x)
            # print(data.split(u':')[0])
            # verif_ip(data[0],data[1])