#coding:utf-8
import yaml
from appium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from  Function import send_message,Open_app
# desired_caps=Open_app("wechat")
desired_caps={'platformName': 'Android', 'platformVersion': 6.0, 'dunicodeKeyboard': False, 'resetKeyboard': False, 'deviceName': '127.0.0.1:6555', 'appPackage': 'com.tencent.mm', 'appActivity': '.ui.LauncherUI'}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
sleep(3)
try:
    WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.NAME,"微信")))
    print("success")  # 获取屏幕的高
    # driver.tap([(450,943),(600,1024)],100)
    # driver.find_element_by_name("通讯录").click()
    # print "通讯录"
    # send_message(driver)
    # sleep(1)
    # driver.find_element_by_name("发现").click()
    # print "发现"
    # sleep(1)
    # driver.find_element_by_name("我").click()
    # sleep(1)
    driver.find_element_by_name("搜索").click()
    print ("搜索")
    sleep(2)
    # driver.hide_keyboard()#隐藏输入法
    print ("keyboard")
    sleep(1)
    driver.keyevent('4')
    print ("back")
    sleep(1)
    driver.keyevent('4')
    print ("back")


    sleep(2)
    # driver.find_element_by_name("扫一扫").click()
    # print "扫一扫"
    driver.back()
    print ("back")
    sleep(2)
    # driver.get_screenshot_as_file("C:\\Users\\cs\\Desktop\\123.png")#截图保存
except Exception as e:
    print (e)

driver.close_app()
sleep(1)
driver.quit()