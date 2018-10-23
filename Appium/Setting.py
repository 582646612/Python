#coding:utf-8
from appium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

from Function import location
desired_caps = {}

desired_caps['platformName'] ='Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = '127.0.0.1:4555'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'
# desired_caps['app'] ='C:\\Users\\cs\\Desktop\\app-release.apk'
desired_caps["unicodeKeyboard"] ="True"
desired_caps["resetKeyboard"] ="True"

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
sleep(1)
location(driver,"语言和输入法")
# target = driver.find_element_by_name("日期和时间")
# driver.execute_script("arguments[0].scrollIntoView();", target)
driver.find_element_by_name("语言").click()
sleep(2)

# for i in range(1,5):
#     try :
#         sleep(2)
#         spath="//*[@class='android.widget.LinearLayout'][%d]"%i
#         print spath
#         driver.find_element_by_xpath(spath).click()
#         sleep(2)
#         driver.back()
#     except Exception as e:
#         print e
location(driver,"汉语")
sleep(3)

driver.quit()
