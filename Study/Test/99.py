# -*- coding: UTF-8 -*-


# author by : www.runoob.com

# 九九乘法表
def multi_table():
    result = ''
    for i in range(1, 10):
        for j in range(1, i + 1):
            separator = '\n' if j == i else '\t'
            result += '%d * %d = %-2d' % (j, i, i * j)
            result += separator
    return result

r = multi_table()
print(r)