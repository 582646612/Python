import requests
import csv
import pandas as pd
# def read_file():
#     with open("message.csv",'r',encoding="gbk") as f:
#         lines = csv.reader(f)
#         dataset = []
#         for line in lines:
#             dataset.append(line)
#         f.close()
#         print(dataset)
def getcsv(name):
    df = pd.read_csv(name,encoding='GB18030')
    list_label = df.columns.values
    list_data =df.values.tolist()
    return list_data

if __name__ == '__main__':
    # read_file()
    date=getcsv("qujing.csv")
    for i in date:
        print(i)