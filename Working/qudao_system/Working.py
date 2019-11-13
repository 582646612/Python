from get_xml import xml1,xml2
from api import api
import time
from get_xls import get_xls
from get_xml import xml1_rg,xml2_rg
from api import api_rg
from get_canshu import get_address
def run_rengong(local,cooks):
    data = get_xls(local)
    success, fail = 0, 0
    sum = 1
    for i in data:
        addre = get_address(i[0], i[2],cooks)
        if addre != 'returnfalse':
            print(time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime()), end=' ')
            print("总数:", len(data), ",正在执行第", sum, '条')
            x = xml1_rg(i, addre)
            y = xml2_rg(i, addre,cooks)
            put = api_rg(x, y, i[8], i[2], addre[3],addre[4],cooks)
            if put['STATUS_INFO'] == '新增成功！':
                success += 1
            else:
                print(i)
                print(put)
                fail += 1
            sum += 1
    print("总的条数为：", len(data))
    print("成功条数为：", success)
    print("失败条数为：", fail)
def run(local,cooks):
    data = get_xls(local)
    success, fail = 0, 0
    sum = 1
    for i in data:
        addre = get_address(i[0], i[4],cooks)
        if addre != 'returnfalse':
            print("总数:", len(data), ",正在执行第", sum, '条')
            x = xml1(i, addre,cooks)
            y = xml2(i, addre)
            put = api(x, y, i[9], i[4], addre[3],cooks)
            if put['STATUS_INFO'] == '新增成功！':
                success += 1
            else:
                print(i)
                print(put)
                fail += 1
            sum += 1
    print("总的条数为", len(data))
    print("成功条数为", success)
    print("失败条数为", fail)


if __name__ == '__main__':
    print('cooks.txt')