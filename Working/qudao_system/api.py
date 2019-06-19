import requests
import pandas as pd
from urllib import parse
from get_readfile import read_file

def api(xm1,xm2,mem1,mem2,date):
    orc_url = 'http://10.123.0.126:18210/CIS-CHAR/business/com.ailk.uchannel.commmgr.web.AddCommissionAction?action=saveCommission&url_source=AilkPageInteractionManage'
    date = {
        'xml1':parse.quote(xm1),
        'xml2':parse.quote(xm2),
        'MEMO1':mem1,
        'MEMO2':mem2,
        'manualflag':'0',
        'subsidyflag':'1',
        'settCycle':date,
        'invoice_type':'1',
        'uploadlist':''	,
        'CenterValue':'86',
        'CenterType':'commmgr'
    }
    head = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'JSESSIONID='+read_file('cook.txt')
    }
    res = requests.post(url=orc_url,data=date,headers=head).text
    print(res)

def api_rg(xm1,xm2,mem1,mem2,date): #人工
    orc_url = 'http://10.123.0.126:18210/CIS-CHAR/business/com.ailk.uchannel.commmgr.web.AddCommissionAction?action=saveCommission&url_source=AilkPageInteractionManage'
    date = {
        'xml1':parse.quote(xm1),
        'xml2':parse.quote(xm2),
        'MEMO1':mem1,
        'MEMO2':mem2,
        'manualflag':'1',
        'subsidyflag':'0',
        'settCycle':date,
        'invoice_type':'1',
        'uploadlist':''	,
        'CenterValue':'86',
        'CenterType':'commmgr'
    }
    head = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'JSESSIONID='+read_file('cook.txt')
    }
    res = requests.post(url=orc_url,data=date,headers=head).text
    print(res)

