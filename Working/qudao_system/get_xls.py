import xlrd

def get_xls(name):
    data = xlrd.open_workbook(name) # 所有行
    table = data.sheet_by_name('Sheet1')
    nrows = table.nrows  # 行数
    list=[]
    for i in range(1, nrows):
        list.append(table.row_values(i))
    return list
if __name__ == '__main__':
    date=get_xls("普洱.xls")
    for i in date:
        print(i)