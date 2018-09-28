#coding=utf-8
from appium import webdriver
import time
import os
desired_caps = {}

desired_caps['platformName'] ='Android'
desired_caps['platformVersion'] = '4.4'
desired_caps['deviceName'] = 'emulator-5554'
# desired_caps['appPackage'] = 'com.android.calculator2'
# desired_caps['appActivity'] = '.Calculator'
desired_caps['app'] ='C:\\Users\\cs\\Desktop\\app-release.apk'
desired_caps["unicodeKeyboard"] ="True"
desired_caps["resetKeyboard"] ="True"

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(6)
def dingwei():
    driver.findElement(By.name("9"))
    driver.findElement(By.id("com.android.calculator2:id/formula"))
    driver.findElement(By.className("android.widget.Button"))
    driver.findElement(By.xpath("//android.view.ViewGroup/android.widget.Button"))
    driver.find_element_by_xpath("//*[@class='android.widget.FrameLayout'][5]").click()
def huadong():
    print(driver.get_window_size())  # 获取屏幕的高
    x = driver.get_window_size()['width']  # 获取屏幕宽
    y = driver.get_window_size()['height']  # 滑屏，大概从屏幕右边2分之一高度，往左侧滑动,滑动后显示的是 热点
    driver.swipe(6 / 7 * x, 1 / 2 * y, 1 / 7 * x, 1 / 2 * y, 100)
    time.sleep(4)
    # 向右滑动，显示推荐tab 内容，第五个参数，时间设置大一点，否则容易看不到滑动效果
    driver.swipe(1 / 7 * x, 1 / 2 * y, 5 / 7 * x, 1 / 2 * y, 200)
    time.sleep(4)  # 向上滑
    driver.swipe(1 / 2 * x, 1 / 2 * y, 1 / 2 * x, 1 / 7 * y, 200)
    time.sleep(4)  # 向下滑动
    driver.swipe(1 / 2 * x, 1 / 7 * y, 1 / 2 * x, 6 / 7 * y, 200)

def caozuo():
    driver.tap([(918, 413), (1026, 521)], 100)

def sign():
    img_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '//screenshots//'
    time = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    screen_save_path = img_folder + time + '.png'
    driver.get_screenshot_as_file(screen_save_path)

time.sleep(6)
driver.quit()
