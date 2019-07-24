import requests
import json
from get_readfile import read_file
def get_address(add,date):
    orc_url = 'http://10.123.0.126:18210/CIS-CHAR/business/com.ailk.uchannel.commmgr.web.AddCommissionAction?action=getChnlNameByChnlId&url_source=AilkPageInteractionManager'
    date = {
        'SETT_CYCLE':date,
        'CHNL_ID':add,
        'MANUAL_TOTAL_AMOUNT':'',
        'SUBSIDY_TOTAL_AMOUNT':'0.00',
        'SUBSIDY_FLAG':'2'
    }
    head = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'JSESSIONID='+read_file('cooks.txt')
    }
    try:
        res = requests.post(url=orc_url,data=date,headers=head).text
        res=json.loads(res)
        return res['chnlName'], res['paychnlname']
    except:
        print("Cookie已失效，请登录浏览器获取Cookie并更新于cooks.txt文件中")

def get_money(add,sum,date):
    orc_url = 'http://10.123.0.126:18210/CIS-CHAR/business/com.ailk.uchannel.commmgr.web.AddCommissionAction?action=getTax&url_source=AilkPageInteractionManager'
    date = {
        'CHNL_ID': add,
        'TOTAL_AMOUNT': sum,
        'SETT_CYCLE': date,
        'PROVINCE_CODE': '86',
        'CenterValue': '86',
        'CenterType': 'commmgr'
    }
    head = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'JSESSIONID='+read_file('cooks.txt')
    }
    try:
        res = requests.post(url=orc_url, data=date, headers=head).text
        res=json.loads(res)
        return res['tax'],res['pureAmount']
    except:
        print("Cookie已失效，请登录浏览器获取Cookie并更新于cooks.txt文件中")


if __name__ == '__main__':
    # adds=get_address('86b24kp','201905')
    # print(adds)
    themoney=get_money('86b0m5x',270,'201906')
    print(themoney)

