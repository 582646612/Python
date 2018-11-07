from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
sleep(3)
driver.find_element_by_class_name("s_ipt").send_keys("test")
sleep(3)
driver.find_element_by_id("su").click()