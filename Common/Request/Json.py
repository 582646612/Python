#!/usr/bin/python3

import json

# Python 字典类型转换为 JSON 对象
data = {
    'no': 1,
    'name': 'Runoob',
    'url': 'http://www.runoob.com'
}

json_str = json.dumps(data)
print("Python 原始数据：", repr(data))
print("JSON 对象：", json_str)

# 将 JSON 对象转换为 Python 字典
data2 = json.loads(json_str)
print(data2)
print ("data2['name']: ", data['name'])
# print ("data2['url']: ", data2['url'])

# 文件，可以使用 json.dump() 和 json.load() 来编码和解码JSON数据