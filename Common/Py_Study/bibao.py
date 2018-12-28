def func(str1):
    print('your computer info is :')
    def func_in(str2):
        print(str1+str2)
    return func_in
a=func('16G RAM ')
a('1T ROM')