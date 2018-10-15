#coding:utf-8
from appium import webdriver
import time
from auto_test_ecloud import auto_interact
from Function import Scroll_down,Scroll_up


desired_caps = {}

desired_caps['platformName'] ='Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = '127.0.0.1:6555'
desired_caps['appPackage'] = 'com.baidu.browser.apps'
desired_caps['appActivity'] = 'com.baidu.browser.framework.BdBrowserActivity'
# desired_caps['app'] ='C:\\Users\\cs\\Desktop\\app-release.apk'
# desired_caps["unicodeKeyboard"] ="True"
# desired_caps["resetKeyboard"] ="True"

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(3)
Scroll_up(driver)
time.sleep(2)
Scroll_up(driver)
time.sleep(2)
Scroll_down(driver)
time.sleep(2)
driver.quit()