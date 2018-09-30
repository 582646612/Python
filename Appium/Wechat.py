#coding:utf-8
from appium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from  Weixin import send_message
desired_caps = {}

desired_caps['platformName'] ='Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = '127.0.0.1:4555'
desired_caps['appPackage'] = 'com.tencent.mm'
desired_caps['appActivity'] = '.ui.LauncherUI'
# desired_caps['app'] ='C:\\Users\\cs\\Desktop\\app-release.apk'
# desired_caps["unicodeKeyboard"] ="True"
# desired_caps["resetKeyboard"] ="True"

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
sleep(3)
WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.ID,"com.tencent.mm:id/cdh")))

print(driver.get_window_size())  # 获取屏幕的高
sleep(2)
# send_message(driver)
sleep(2)
driver.tap([(450,943),(600,1024)],100)
print "我的"
sleep(2)
driver.tap([(462,36),(498,108)],200)
print "搜索"
sleep(2)
driver.hide_keyboard()#隐藏输入法
driver.back()
driver.tap([(498,36),(600,108)],200)
print "扫一扫"
sleep(2)
driver.get_screenshot_as_file("C:\\Users\\cs\\Desktop\\123.png")#截图保存

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
# driver.swipe(75, 0, 75, 500, 200);

sleep(3)
driver.close_app()
driver.quit()