import requests
from get_readfile import read_file
import json
orc_url = 'http://10.123.0.126:18210/CIS-CHAR/business/com.ailk.uchannel.commmgr.web.AddCommissionAction?action=saveCommission&url_source=AilkPageInteractionManage'
head = {
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Cookie': 'JSESSIONID='+read_file('cooks.txt')
    }
def api(xm1,xm2,mem1,date):
    date = {
        'xml1':xm1,
        'xml2':xm2,
        'MEMO1':mem1,
        'MEMO2':'',
        'manualflag':'0',
        'subsidyflag':'1',
        'settCycle':date,
        'invoice_type':'1',
        'uploadlist':''	,
        'CenterValue':'86',
        'CenterType':'commmgr'
    }
    res = requests.post(url=orc_url,data=date,headers=head).text
    return json.loads(res)
def api_rg(xm1,xm2,mem1,date): #人工
    date= {
        'xml1':xm1,
        'xml2':xm2,
        'MEMO1':'',
        'MEMO2':mem1,
        'manualflag':'1',
        'subsidyflag':'0',
        'settCycle':date,
        'invoice_type':'1',
        'uploadlist':''	,
        'CenterValue':'86',
        'CenterType':'commmgr'
    }
    res = requests.post(url=orc_url,data=date,headers=head).text
    return json.loads(res)

