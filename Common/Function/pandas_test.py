import pandas
houseary=[{'具体地点': '近3号线金沙江路站', '位置': '大三房，价格实惠，采光无遮挡，有钥匙，看房方便', '总价': '1080', '所在区': '3室2厅'}, {'具体地点': '', '位置': '房子出门公交，小区高层观景房，有钥匙，随时可看', '总价': '203', '所在区': '2室1厅'}, {'具体地点': '近8号线延吉中路站', '位置': '双南户型、房型方正、精装修税费少、近地铁', '总价': '320', '所在区': '2室1厅'}]

# df=pandas.DataFrame(houseary)
# df.to_excel('pandas.xlsx')

iris=pandas.read_excel('pandas.xlsx')
print(iris.head())