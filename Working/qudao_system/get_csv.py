import requests
import csv
import pandas as pd

def getcsv(name):
    df = pd.read_csv(name,encoding='GB18030')
    list_label = df.columns.values
    list_data =df.values.tolist()
    return list_data

if __name__ == '__main__':
    date=getcsv("qujing.csv")
    for i in date:
        print(i)