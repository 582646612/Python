#!/usr/bin/python
# -*- coding: utf-8 -*-

from urllib import request
import re
import os,json
import xlwt

book = xlwt.Workbook()
sheet = book.add_sheet('sheet', cell_overwrite_ok=True)
path = 'D:\\'
os.chdir(path)
result11=[]
result21=[]
result31=[]
result41=[]
result51=[]

for k in range(1,75):
    url="https://fe-api.zhaopin.com/c/i/sou?start="+str(k*90)+"&pageSize=90" \
        "&cityId=%E5%85%A8%E5%9B%BD&workExperience=-1&education=-1&companyType=-1&employmentType=" \
        "-1&jobWelfareTag=-1&kw=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B8%88&kt=3&_v=0.64456245&x-" \
        "zp-page-request-id=8f8a864b761e41039e1a51c832f46cc7-1545894272489-303580"
    html=request.urlopen(url).read()    #读取网页源代码内容
    # data = request.urlopen(url).text
    # data = json.loads(data)

    print(html.decode())


    # pat1 = 'onclick="submitLog.*?">(.*?)</a>'
    # pat2 = '<li class="query-others__borders__detail__item"><a href="(.*?)"'
    # pat3 = 'class="zp-query">(.*?)</a>'
    # pat4 = 'class="zp-query">1(.*?)</a>'
    # pat5 = 'target="_blank">(.*?)<'
    # #pat6 = '<span>(.*?)</span>'
    # #pat7 = 'target="_blank">(.*?)</a>'
    #
    # result1 = re.compile(pat1).findall(str(html,"utf-8"))
    # result2 = re.compile(pat2).findall(str(html,"utf-8"))
    # result3 = re.compile(pat3).findall(str(html,"utf-8"))
    # result4 = re.compile(pat4).findall(str(html,"utf-8"))
    # result5 = re.compile(pat5).findall(str(html,"utf-8"))
    # print(result1,result2,result3,result4,result5)
    # result11.extend(result1)
    # result21.extend(result2)
    # result31.extend(result3)
    # result41.extend(result4)
    # result51.extend(result5)


j = 0
for i in range(0,len(result11)):
    try:
        zhiwei = result11[i]
        wangzhi = result21[i]
        gongzi = result31[i]
        gongzuodidian = result41[i]
        gongsimingcheng = result51[i]
        sheet.write(i + 1, j, zhiwei)
        sheet.write(i + 1, j + 1, wangzhi)
        sheet.write(i + 1, j + 2, gongzi)
        sheet.write(i + 1, j + 3, gongzuodidian)
        sheet.write(i + 1, j + 4, gongsimingcheng)

    except Exception as e:
        print('出现异常：' + str(e))
        continue

book.save('d:\\shujufenxishi.xls')
print(book)