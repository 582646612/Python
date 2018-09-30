#coding:utf-8
from appium import webdriver
from Function import Z_unlock,L_unlock
import time
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.0'
desired_caps['deviceName'] = '127.0.0.1:4555'
desired_caps['appPackage'] = 'com.asiainfo.wcs'
desired_caps['appActivity'] = '.ui.splash.SplashActivity'
desired_caps['unicodeKeyboard'] = 'true'
desired_caps['resetKeyboard'] = 'True'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(2)
print(driver.get_window_size())  # 获取屏幕的高
Z_unlock(driver)
L_unlock(driver)
time.sleep(4)
driver.quit()