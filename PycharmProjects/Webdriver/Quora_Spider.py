#coding=utf-8
from selenium import webdriver
from time import sleep
driver = webdriver.Firefox()
driver.get("http://www.51zxw.net")
driver.maximize_window()
sleep(3)
driver.get("http://www.baidu.com")
driver.set_window_size(800,800)
sleep(2)
driver.refresh()
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click
sleep(5)
driver.quit()



