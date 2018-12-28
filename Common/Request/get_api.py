#coding:utf-8
import requests
import json

app_key = 'kPoFYw85FXsnojsy5bB9hu6x'
secret_key = 'l7SuGBkDQHkjiTPU3m6NaNddD6SCvDMC'
img_url = 'http://upload-images.jianshu.io/upload_images/7575721-40c847532432e852.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240'
# 获取token
get_token_url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(app_key,secret_key)
token = requests.get(url=get_token_url).json().get("access_token")  # 从获取token接口的响应中取得token值
# 识别图片文字
orc_url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token={}'.format(token)
data = {"url": img_url}
res = requests.post(url=orc_url, data=data)
print(json.dumps(res.json(), indent=2, ensure_ascii=False)) # 格式化输出

'''session'''
# s = requests.session() # 新建一个会话
# s.post(url="https://demo.fastadmin.net/admin/index/login.html",data={"username":"admin","password":"123456"}) # 发送登录请求
# res = s.get("https://demo.fastadmin.net/admin/dashboard?ref=addtabs") # 使用同一个会话发送get请求，可以保持登录状态
'''cookies'''
# url = "https://demo.fastadmin.net/admin/dashboard?ref=addtabs"
# cookies = {"PHPSESSID":"9bf6b19ddb09938cf73d55a094b36726"}
# res = requests.get(url=url, cookies=cookies) # 携带cookies发送请求

'''
请求参数
url: 字符串格式，参数也可以直接写到url中
params：url参数，字典格式
data: 请求数据，字典或字符串格式
headers: 请求头，字典格式
cookies: 字典格式，可以通过携带cookies绕过登录
files: 字典格式，用于混合表单（form-data）中上传文件
auth: Basic Auth授权，数组格式 auth=(user,password)
timeout: 超时时间（防止请求一直没有响应，最长等待时间），数字格式，单位为秒

响应解析
res.status_code: 响应的HTTP状态码
res.reason: 响应的状态码含义
req.text：响应的文本格式，按req.encoding解码
req.content: 响应的二进制格式
req.encoding: 解码格式，可以通过修改req.encoding='utf-8'来解决一部分中文乱码问题
req.apparent_encoding：真实编码，由chardet库提供的明显编码
req.json(): （注意，有括号），响应的json对象（字典）格式，慎用！如果响应文本不是合法的json文本，或报错
req.headers: 响应头
req.cookies: 响应的cookieJar对象，可以通过req.cookies.get(key)来获取响应cookies中某个key对应的值
'''
