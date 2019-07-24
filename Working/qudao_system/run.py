from get_csv import get_xls
from get_xml import xml1,xml2
from api import api
if __name__ == '__main__':#实物不行\共J列
    data=get_xls('补贴-临沧.xls')
    success,success1,fail=0,0,0
    sum=1
    for i in data:
        print("总数:",len(data), ",正在执行第", sum, '条')
        x=xml1(i)
        y=xml2(i)
        put=api(x,y,i[9],i[4])
        if put['STATUS_CODE']=='0' or put['STATUS_CODE']=='1':
            success+=1
        elif put['STATUS_CODE']=='2':
            print(i)
            print(put)
            fail+=1
        sum+=1
    print("总的条数为",len(data))
    print("成功条数为",success)
    print("失败条数为", fail)
