#获取标签对应值
from xml.dom import minidom
#打开文件
dom=minidom.parse('Class_info.xml')
#获取文档对象元素
root=dom.documentElement
#获取对象
names=root.getElementsByTagName('name')
ages=root.getElementsByTagName('age')
citys=root.getElementsByTagName('city')

for i in range(4):
    print(names[i].firstChild.data)
    print(ages[i].firstChild.data)
    print(citys[i].firstChild.data)