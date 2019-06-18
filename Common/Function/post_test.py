import requests
orc_url = 'http://10.123.0.126:18210/CIS-CHAR/business/com.ailk.uchannel.commmgr.web.AddCommissionAction?action=getChnlNameByChnlId&url_source=AilkPageInteractionManager'
date = {
    'SETT_CYCLE':'201905',
    'CHNL_ID':'86a1924',
    'MANUAL_TOTAL_AMOUNT':'',
    'SUBSIDY_TOTAL_AMOUNT':'0.00',
    'SUBSIDY_FLAG':'2'
}
head = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'JSESSIONID=357a9ae9c510af6fbd033a86ea09'
}
res = requests.post(url=orc_url,data=date,headers=head).text
print(res)