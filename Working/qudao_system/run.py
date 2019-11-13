from Autologin import auto_login
from Working import run
if __name__ == '__main__':#实物不行\共J列
    # ['版纳','保山','楚雄','大理','德宏','迪庆','红河','昆明','丽江','临沧','怒江','普洱','曲靖','文山','玉溪','昭通']
    tity = ['保山', '怒江']
    for i in tity:
        print('****************************************************************')
        print("正在执行地市：", i)
        try:
            local = 'C:\\Users\LT\Desktop\\' + i + '.xlsx'
            auto_login(local,i,'run')
        except:
            print("执行失败，无"+i+"地市文件")
