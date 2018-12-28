import requests
import unittest

login_url = 'http://127.0.0.1:5000/login'
info_url='http://127.0.0.1:5000/info'
username = 'admin'
password = '123456'
data = {
'username': username,
'password': password
}
response = requests.post(login_url, data=data).json()

print(response)
response_cookies = requests.post(login_url, data=data).cookies
session = response_cookies.get('session')
print(response_cookies)
print(session)
info_cookies = {
            'session': session
        }
response = requests.get(info_url, cookies=info_cookies).json()
print(response)

s = requests.session() # 新建一个会话
s.post(url=login_url,cookies=info_cookies) # 发送登录请求
res = s.get(info_url)
print(res)
#
# class TestLogin(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         login_url = 'http://127.0.0.1:5000/login'
#         info_url = 'http://127.0.0.1:5000/info'
#         username = 'admin'
#         password = '123456'
#
#     def test_login(self):
#         """
#         测试登录
#         """
#         data = {
#             'username': username,
#             'password': password
#         }
#
#         response = requests.post(login_url, data=data).json()
#
#         assert response['code'] == 200
#         assert response['msg'] == 'success'
#
#     def test_info(self):
#         """
#         测试info接口
#         """
#
#         data = {
#             'username': username,
#             'password': password
#         }
#
#         response_cookies = requests.post(login_url, data=data).cookies
#         session = response_cookies.get('session')
#         assert session
#
#         info_cookies = {
#             'session': session
#         }
#
#         response = requests.get(info_url, cookies=info_cookies).json()
#         assert response['code'] == 200
#         assert response['msg'] == 'success'
#         assert response['data'] == 'info'