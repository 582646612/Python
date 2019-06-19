from get_csv import getcsv
from get_readfile import read_file

from get_xml import xml1_rg,xml2_rg
from api import api_rg
if __name__ == '__main__':
    data=getcsv('昭通.csv')
    for i in data:
        x=xml1_rg(i)
        print(x)
        y=xml2_rg(i)
        print(y)

        # api_rg(x,y,'',i[8],i[2])