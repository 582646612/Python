import requests
import pandas
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
def gethousedetail(url):#定义函数，目标获得子域名里的房屋详细信息
    info={}#构造字典，作为之后的返回内容
    res = requests.get(url, headers=headers1)
    soup = BeautifulSoup(res.text, 'html.parser')

    info['房型']=soup.find('div',class_="mainInfo").get_text()
    info['总价'] = soup.find('span', class_="total").get_text()+'万'
    info['具体地点']=soup.find('a',class_="supplement").get_text()
    info['标题']=soup.find('h1',class_="main").get_text()
    info['单价'] = soup.find('span', class_="unitPriceValue").get_text()



    return info#传回这一个页面的详细信息

ua=UserAgent()#使用随机header，模拟人类
headers1={'User-Agent': 'ua.random'}#使用随机header，模拟人类
houseary=[]#建立空列表放房屋信息
domain='https://sh.lianjia.com/ershoufang/'#为了之后拼接子域名爬取详细信息
for i in range(2,3):#爬取399页，想爬多少页直接修改替换掉400，不要超过总页数就好
    res=requests.get('https://sh.lianjia.com/ershoufang/pg'+str(i),headers=headers1)#爬取拼接域名
    soup = BeautifulSoup(res.text,'html.parser')#使用html筛选器
    # print(soup)
    for j in range(0,3):#网站每页呈现30条数据，循环爬取
        url1=soup.select('.item')[j]['data-houseid'] #选中class=prop-title下的a标签里的第j个元素的href子域名内容
        url=domain+url1+'.html'
        print(url)
        houseary.append(gethousedetail(url))#传入自编函数需要的参数
print(houseary)
df=pandas.DataFrame(houseary)
df.to_excel('lianjia.xlsx')