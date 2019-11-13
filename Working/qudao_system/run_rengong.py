from Autologin import auto_login
from get_xls import get_xls

if __name__ == '__main__':#发展人不行，结算对象为【渠道】,共I列
    # ['版纳','保山','楚雄','大理','德宏','迪庆','红河','昆明','丽江','临沧','怒江','普洱','曲靖','文山','玉溪','昭通']
    tity=['版纳','楚雄']
    for i in tity:
        print('****************************************************************')
        print("正在执行地市：", i)
        try:
            local = 'C:\\Users\LT\Desktop\\' + i + '.xlsx'
            data = get_xls(local)
            auto_login(local, i, 'run_rengong')
        except:
            print("执行失败，无"+i+"地市文件")


