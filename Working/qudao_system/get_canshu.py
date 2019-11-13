import requests
import json
def get_address(add,date,cooks):
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
        'Cookie': 'JSESSIONID='+cooks
    }
    try:
        res = requests.post(url=orc_url,data=date,headers=head).text
        res=json.loads(res)
        if res['STATUS_INFO']=='处理成功':
            return res['chnlName'], res['paychnlname'],res['paychnlid'],res['mngdeptid'],res['agentdepttype']
        else:
            print(res)
            return 'returnfalse'
    except Exception as e:
        print("Cookie已失效，请登录浏览器获取Cookie并更新于cooks.txt文件中")

def get_money(add,sum,date,cooks):
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
        'Cookie': 'JSESSIONID='+cooks
    }
    try:
        res = requests.post(url=orc_url, data=date, headers=head).text
        res=json.loads(res)
        return res['tax'],res['pureAmount']
    except:
        print("Cookie已失效，请登录浏览器获取Cookie并更新于cooks.txt文件中")


if __name__ == '__main__':
    adds=get_address('86a0277','201909','f9b8bf3c678c7b5214823a57f164')
    print(adds)
    # themoney=get_money('86b0r37',270,'201908')
    # print(themoney)

