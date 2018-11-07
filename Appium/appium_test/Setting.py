#coding:utf-8
from appium import webdriver
from time import sleep
import yaml
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from Function import location,Open_app

desired_caps=Open_app('Setting')
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
sleep(1)

# driver.keyevent('4')
location(driver,"语言和输入法")
# target = driver.find_element_by_name("日期和时间")
# driver.execute_script("arguments[0].scrollIntoView();", target)
driver.find_element_by_name("语言").click()
sleep(2)
location(driver,"中文(简体)")
sleep(3)

driver.quit()
