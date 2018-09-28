#coding:utf-8
from appium import webdriver
import time
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4'
desired_caps['deviceName'] = '127.0.0.1:62001'
desired_caps['appPackage'] = 'com.zhihu.android'
desired_caps['appActivity'] = '.app.ui.activity.MainActivity'
desired_caps['unicodeKeyboard'] = 'true'
desired_caps['resetKeyboard'] = 'True'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(5)
print(driver.get_window_size())  # 获取屏幕的高
# driver.find_element_by_id("com.zhihu.android:id/input").click()
# driver.find_element_by_class_name("android.widget.EditText").send_keys("tester")
# driver.tap([(0,737),(720,942)],100)
time.sleep(3)
driver.find_element_by_xpath("//*[@class='android.support.v7.app.a$c'][2]").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@class='android.support.v7.app.a$c'][3]").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@class='android.support.v7.app.a$c'][4]").click()
time.sleep(3)
driver.back()
driver.tap([(576,1208),(720,1280)],100)
# x = driver.get_window_size()['width']  # 获取屏幕宽
# y = driver.get_window_size()['height']
# time.sleep(3)
# driver.swipe(75, 0, 75, 500, 800);
# driver.swipe(1 / 2 * x, 1 / 7 * y, 1 / 2 * x, 6 / 7 * y, 200)
# time.sleep(3)
# driver.swipe(1 / 2 * x, 1 / 7 * y, 1 / 2 * x, 6 / 7 * y, 200)
# time.sleep(3)
# driver.swipe(1 / 2 * x, 1 / 2 * y, 1 / 2 * x, 1 / 7 * y, 200)
time.sleep(3)
driver.close_app()
# time.sleep(3)
driver.quit()