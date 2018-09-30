import unittest
from  appium import webdriver
from time import sleep
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