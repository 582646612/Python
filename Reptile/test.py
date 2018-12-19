#coding:utf-8
import time
from selenium import webdriver

driver = webdriver.Firefox()
# driver.maximize_window()
# driver.implicitly_wait(6)
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("python")
driver.find_element_by_id("su").click()
time.sleep(3)
assert driver.title == 'python_百度搜索'
driver.close()
