#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

#创建基础类
class BasePage(object):
    #初始化
    def __init__(self, driver):
        self.base_url = 'https://mail.qq.com/'
        self.timeout = 10

    #打开页面
    def _open(self):
        url = self.base_url
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.switch_to.frame('login_frame')  #切换到登录窗口的iframe

    def open(self):
        self._open()

    #定位方法封装
    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    def close(self):
        self.driver.quit()
