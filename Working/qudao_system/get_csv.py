import xlrd
import pandas as pd
def getcsv(name):
    df = pd.read_csv(name,encoding='GB18030')
    list_label = df.columns.values
    list_data =df.values.tolist()
    return list_data
def get_xls(name):
    data = xlrd.open_workbook(name) # 所有行
    table = data.sheet_by_name('Sheet1')
    nrows = table.nrows  # 行数
    list=[]
    for i in range(1, nrows):
        list.append(table.row_values(i))
    return list
if __name__ == '__main__':
    # date=getcsv("qujing.xls")
    # for i in date:
    #     print(i)
    date=get_xls("普洱.xls")
    for i in date:
        print(i)