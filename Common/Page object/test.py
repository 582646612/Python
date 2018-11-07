#coding:utf-8
# 用page object思想实现百度首页的搜索和登陆功能
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class BaiduPage(object):
    url = 'http://www.baidu.com/'
    username = 'XXXXXX'
    password = '******'

    def __init__(self, driver):
        self.driver = driver

    def search(self, kw='51cto'):
        self.driver.get(self.url)
        time.sleep(2)
        self.driver.find_element_by_id('kw').send_keys(kw)
        self.driver.find_element_by_id('su').click()
        time.sleep(2)

    def login(self, username=None, password=None):

        if username == None:
            username = self.username
        if password == None:
            password = self.password
        self.driver.get(self.url)
        time.sleep(2)
        self.driver.find_element_by_link_text('登录'.decode('utf-8')).click()
        time.sleep(2)
        self.driver.find_element_by_id('TANGRAM__PSP_8__userName').send_keys(self.username)
        self.driver.find_element_by_id('TANGRAM__PSP_8__password').send_keys(self.password)
        self.driver.find_element_by_id('TANGRAM__PSP_8__submit').click()
        time.sleep(2)

    def __del__(self):
        pass
        # self.driver.quit()


driver = webdriver.Chrome()
page = BaiduPage(driver)
page.search()
driver.quit()