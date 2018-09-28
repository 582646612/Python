#coding=utf-8
from  selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
cookie=driver.get_cookies()
print(cookie)
driver.quit()