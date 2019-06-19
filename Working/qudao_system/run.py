from get_csv import getcsv
from get_readfile import read_file
from get_xml import xml1,xml2
from api import api
if __name__ == '__main__':
    data=getcsv('qujing.csv')
    for i in data:
        print(i)
        x=xml1(i)
        print(x)
        y=xml2(i)
        print(y)
        # api(x,y,i[7],'',i[2])