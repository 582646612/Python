#coding=utf-8
from appium import webdriver
import time
import os

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub')

def dingwei():
    driver.find_element_by_xpath("//*[@class='android.widget.FrameLayout'][5]").click()
    driver.find_element_by_xpath("//android.widget.Button[contains(@text,'7')]").click();
    driver.find_element_by_xpath("//android.widget.Button[contains(@content-desc,'times')]").click();
    driver.find_element_by_xpath("//android.widget.Button[contains(@text,'7')]").click();
    driver.find_element_by_xpath("//android.widget.Button[contains(@content-desc,'equals')]").click()
def huadong():
    print(driver.get_window_size())
    x = driver.get_window_size()['width']   # 获取屏幕的高
    y = driver.get_window_size()['height'] # 获取屏幕宽
    driver.swipe(5/ 7 * x, 1 / 2 * y, 3/ 7 * x, 1 / 2 * y, 100)# 滑屏，大概从屏幕右边2分之一高度，往左侧滑动,滑动后显示的是 热点
    time.sleep(4)

    driver.swipe(2/ 7 * x, 1 / 2 * y, 5 / 7 * x, 1 / 2 * y, 200)# 向右滑动，显示推荐tab 内容，第五个参数，时间设置大一点
    time.sleep(4)
    driver.swipe(1 / 2 * x, 1 / 2 * y, 1 / 2 * x, 1 / 7 * y, 200)# 向下滑
    time.sleep(4)
    driver.swipe(1 / 2 * x, 1 / 7 * y, 1 / 2 * x, 6 / 7 * y, 200)# 向上滑动

def caozuo():
    driver.tap([(918, 413), (1026, 521)], 100)

def sign():
    img_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '//screenshots//'
    times =time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    screen_save_path = img_folder + time + '.png'
    driver.get_screenshot_as_file(screen_save_path)

