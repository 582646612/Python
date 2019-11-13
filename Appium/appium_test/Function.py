#coding:utf-8
from time import sleep
import yaml
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction

def Open_app(name):
    files = open("date.yaml", 'r').read()
    desired_caps = yaml.load(files)[name]
    return desired_caps

def Z_unlock(driver):
    jiu = 'com.asiainfo.wcs:id/lockPatternView'
    local = driver.find_element_by_id(jiu).location
    size = driver.find_element_by_id(jiu).size
    x = local["x"]
    y = local["y"]  # 元素的宽和高
    width = size["width"]
    height = size["height"]
    print (x, y, width, height)
    num1x = x + width / 6
    num1y = y + height / 6
    unlock2 = TouchAction(driver).press(None, num1x, num1y).wait(200).move_to(None, num1x+width / 3, num1y).wait(200).move_to(None,num1x+width*2 / 3,num1y).wait(200).move_to(None,num1x+width / 3, num1y+height / 3).wait(200).move_to(None,num1x, num1y+height *2/ 3).wait(200).move_to(None,num1x+width / 3,num1y+height *2/ 3).wait(200).move_to(None,num1x+width *2/ 3,num1y+height *2/ 3)
    unlock2.release()
    unlock2.wait(100).perform()

def L_unlock(driver):
    jiu = 'com.asiainfo.wcs:id/lockPatternView'
    local = driver.find_element_by_id(jiu).location
    size = driver.find_element_by_id(jiu).size
    x = local["x"]
    y = local["y"]  # 元素的宽和高
    width = size["width"]
    height = size["height"]
    print (x, y, width/3, height/3)
    num1x = x + width / 6
    num1y = y + height / 6
    unlock1 = TouchAction(driver).press(None, num1x, num1y).wait(200).move_to(None, num1x, num1y+width/3).wait(200).move_to(None, num1x, num1y+width*2/3).wait(200).move_to(None, num1x+height/3, num1y+width*2/3).wait(200).move_to(None, num1x+height*2/3, num1y+width*2/3).wait(200).release()
    unlock1.wait(200).perform()



def location(driver,locat): #by.name
    def boolss():
        try:
            driver.find_element_by_name(locat)
            return 0
        except Exception as e:
            print (e)
            return 1
    size = driver.get_window_size()
    width = size["width"]
    height = size["height"]
    print (width, height)
    while (boolss() != 0):
        driver.swipe(width / 2, height / 7 * 6, width / 2, height / 7 * 4, 200)
        sleep(1)
    # WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.NAME,"日期和时间")))
    driver.find_element_by_name(locat).click()
def Zoom(driver):#放大
    screen= driver.get_window_size()
    x=screen["width"]
    y = screen["height"]
    action1=TouchAction(driver)#第一个手势
    action2=TouchAction(driver)#第二个手势
    zoom_action=MultiAction(driver) #放大手势
    action1.press(x=x * 0.5, y=y * 0.5).wait(1000).move_to(x=x * 0.1, y=y * 0.1).release()
    action2.press(x=x * 0.6, y=y * 0.6).wait(1000).move_to(x=x * 0.9, y=y * 0.9).release()
    zoom_action.add(action1,action2)#加载
    zoom_action.perform()#执行


def Pinch(driver):  # 定义缩小函数
    screen = driver.get_window_size()
    x = screen["width"]
    y = screen["height"]
    print (screen,x,y)
    action1 = TouchAction(driver)
    action2 = TouchAction(driver)
    add_action = MultiAction(driver)
    # 指定操作
    action1.press(x=x * 0.1, y=y * 0.1).wait(1000).move_to(x=x * 0.5, y=y * 0.5).wait(1000).release()
    action2.press(x=x * 0.9, y=y * 0.9).wait(1000).move_to(x=x * 0.6, y=y * 0.6).wait(1000).release()
    add_action.add(action1, action2)
    # 执行操作
    add_action.perform()


def Scroll_down(driver):
    screen = driver.get_window_size()
    width = screen["width"]
    height = screen["height"]
    driver.swipe(width / 2, height / 7 * 4, width / 2, height / 7 * 6, 200)


def Scroll_up(driver):
    screen = driver.get_window_size()
    width = screen["width"]
    height = screen["height"]
    driver.swipe(width / 2, height / 7 * 6, width / 2, height / 7 * 4, 200)

def send_message(driver):
    sleep(1)
    driver.find_element_by_name("…").click()
    sleep(1)
    driver.find_element_by_name("发消息").click()
    sleep(1)
    driver.find_element_by_id("com.tencent.mm:id/aie").send_keys("hello word")
    driver.find_element_by_name("发送").click()
    driver.back()