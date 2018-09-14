#encoding:utf-8
from selenium import webdriver
from time import sleep
import time
driver=webdriver.Firefox()
driver.implicitly_wait(6)
driver.get("http://www.360doc.com/content/14/0917/15/597197_410194555.shtml")
js = "var q=document.documentElement.scrollTop=1000"
driver.execute_script(js)
driver.get_screenshot_as_file("C:\\Users\\sw\\Desktop\\Screenshots.png")
print(time.strftime("%Y%m%d.%H.%M.%S"))

