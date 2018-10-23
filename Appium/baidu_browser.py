#coding:utf-8
import time

from appium import webdriver
from selenium.webdriver.common.by import By
from auto_test_ecloud import auto_interact
from Function import Zoom,Pinch,Scroll_up,Scroll_down
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
desired_caps = {}

desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = '127.0.0.1:6555'
# desired_caps['appPackage'] = 'com.android.browser'
# desired_caps['appActivity'] = '.BrowserActivity'
desired_caps['appPackage'] = 'com.baidu.BaiduMap'
desired_caps['appActivity'] = 'com.baidu.baidumaps.WelcomeScreen'
desired_caps['unicodeKeyboard'] = 'true'
desired_caps['resetKeyboard'] = 'True'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.ID,"com.baidu.BaiduMap:id/rg")))
Pinch(driver)
Pinch(driver)

time.sleep(2)
Zoom(driver)
Zoom(driver)
time.sleep(2)
Scroll_up(driver)
time.sleep(2)
Scroll_down(driver)
time.sleep(2)

driver.quit()