#coding=utf-8
from selenium import webdriver
import os,time

driver = webdriver.Chrome()

#脚本要与upload_file.html同一目录
driver.get("file:///E:/JavaScript/upload_file.html")

#定位上传按钮，添加本地文件
driver.find_element_by_name("file").send_keys('E:\python\est.txt')
time.sleep(2)

#driver.quit()