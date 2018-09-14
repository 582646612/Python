#coding=utf-8
from selenium import webdriver
import os,time

driver = webdriver.Chrome()

driver.get("https://yun.baidu.com/")
driver.implicitly_wait(10)
driver.maximize_window()
#登陆
driver.find_element_by_xpath("//div/div[6]/div[2]/a").click()
driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("825096095@qq.com")
driver.find_element_by_id("TANGRAM__PSP_4__password").send_keys("cs774411")
driver.find_element_by_id("TANGRAM__PSP_4__submit").click()
time.sleep(6)
#driver.switch_to_alert().accept()
driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[2]/p[2]").click()
time.sleep(2)

#进入139网盘模块

#driver.find_element_by_id("h5Input0").click()
time.sleep(2)

#上传文件
driver.find_element_by_id("h5Input0").send_keys('E:\python\est.txt')

time.sleep(5)

#driver.quit()