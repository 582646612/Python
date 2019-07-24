from get_csv import get_xls
from get_xml import xml1_rg,xml2_rg
from api import api_rg
if __name__ == '__main__':#发展人不行，结算对象为【渠道】,共I列
    data = get_xls('C:\\Users\LT\Desktop\曲靖.xls')
    success, fail = 0, 0
    sum=1
    for i in data:
        print("总数:",len(data),",正在执行第",sum,'条')
        x=xml1_rg(i)
        y=xml2_rg(i)
        put=api_rg(x,y,i[8],i[2])
        if put['STATUS_CODE']=='0' or put['STATUS_CODE']=='1':
            success+=1
        elif put['STATUS_CODE']=='2':
            print(i)
            print(put)
            fail+=1
        sum+=1
    print("总的条数为：", len(data))
    print("成功条数为：", success)
    print("失败条数为：", fail)