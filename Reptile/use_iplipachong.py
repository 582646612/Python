#coding:utf-8
from selenium import webdriver
import requests
import json
from bs4 import BeautifulSoup
import urllib.request
import re
import time
from fake_useragent import UserAgent
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



def chakd(num):
    orc_url = 'http://scicglobal.com/wp-admin/admin-ajax.php?action=add_foobar&data='+num
    res = requests.get(url=orc_url)
    data=res.text

    data = json.loads(data)
    soup = BeautifulSoup(data['content'], 'lxml')
    wuliu = soup.find("label", class_="act_me")
    x=wuliu.get_text()
    z=x.split('\t')
    dingdan=z[0]
    kuaidi=z[1]
    return dingdan,kuaidi

# driver = webdriver.Chrome()
# driver.get("https://track.trackingmore.com/plugins.php?express=yunda&tracknumber=7700082981288&lang=cn")
# print(driver.get_log('performance'))
def chakuaidi(id,ty):
    url='http://www.kuaidi100.com/query?type='+ty+'&postid='+id
    req = urllib.request.Request(url)
    res = urllib.request.urlopen(req)
    conte = res.read().decode('utf-8')
    data = json.loads(conte)
    data=data['data']
    for i in data:
        print(i['time'],i['location'],i['context'])

def verif_ip(ip,port,id,ty):
    ua = UserAgent()  # 使用随机header，模拟人类
    headers1 = {'User-Agent': ua.random}  # 使用随机header，模拟人类
    proxy={'http':'http://%s:%s'%(ip,port)}
    repx = urllib.request.ProxyHandler(proxy)
    opener = urllib.request.build_opener(repx)
    url = 'http://www.kuaidi100.com/query?type=' + ty + '&postid=' + id
    req=urllib.request.Request(url,headers=headers1)
    try:
        res = opener.open(req)
        conte = res.read().decode('utf-8')
        data = json.loads(conte)
        datas = data['data']
        for i in datas:
            print(i['time'], i['location'], i['context'])
    except urllib.request.URLError as e:
        print(e.reason)

def txt():
    with  open('file.txt','r') as fp:
        lines = fp.readlines()
    return lines

if __name__ == '__main__':
    lines=txt()
    for line in lines:
        ips = line.split(',')[0]
        ports = line.split(',')[1]
        print(ips,ports)
        z='yunda'
        x='7700082981288'
        verif_ip(ips,ports,x,z)
        # chakuaidi(x,z)
