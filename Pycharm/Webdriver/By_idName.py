#coding-utf-8
from selenium import webdriver
from time import sleep
driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
sleep(3)
driver.find_element_by_id("kw").send_keys("我要自学网")
driver.find_element_by_id("wd").send_keys("123456")
sleep(3)
driver.find_element_by_id("su").click()
