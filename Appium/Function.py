#coding:utf-8
from time import sleep
from appium.webdriver.common.touch_action import TouchAction

def Z_unlock(driver):
    jiu = 'com.asiainfo.wcs:id/lockPatternView'
    local = driver.find_element_by_id(jiu).location
    size = driver.find_element_by_id(jiu).size
    x = local["x"]
    y = local["y"]  # 元素的宽和高
    width = size["width"]
    height = size["height"]
    print x, y, width, height
    num1x = x + width / 4
    num1y = y + height / 4
    unlock2 = TouchAction(driver).press(None, num1x, num1y).wait(500).move_to(None, width / 4, 0).move_to(None,width / 4,0).move_to(None,-width / 4, height / 4).move_to(None,-width / 4, height / 4).move_to(None,width / 4,0).move_to(None,width / 4,0)
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
    print x, y, width, height
    num1x = x + width / 4
    num1y = y + height / 4
    unlock1 = TouchAction(driver).press(None, num1x, num1y).wait(500).move_to(None, width / 4, 0).move_to(None,width / 4,0).move_to(None, 0, height / 4).move_to(None, 0, height / 4).release()
    unlock1.perform()



def location(driver,locat): #by.name
    def boolss():
        try:
            driver.find_element_by_name(locat)
            return 0
        except Exception as e:
            print e
            return 1
    size = driver.get_window_size()
    width = size["width"]
    height = size["height"]
    print width, height
    while (boolss() != 0):
        driver.swipe(width / 2, height / 7 * 6, width / 2, height / 7 * 4, 200)
        sleep(1)
    # WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.NAME,"日期和时间")))
    driver.find_element_by_name(locat).click()
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
    driver.tap([(150, 943), (300, 1024)], 100)
    sleep(1)
    driver.find_element_by_xpath("//*[@class='android.widget.LinearLayout'][5]").click()
    sleep(1)
    driver.find_element_by_id("com.tencent.mm:id/ap1").click()
    sleep(1)
    driver.find_element_by_id("com.tencent.mm:id/ac7").send_keys("helloword")
    driver.find_element_by_id("com.tencent.mm:id/acd").click()
    driver.back()