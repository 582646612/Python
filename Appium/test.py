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

print driver.current_activity
print driver.find_elements_by_android_uiautomator('new UiSelector().clickable(true)')
print  driver.current_activity
driver.quit()
