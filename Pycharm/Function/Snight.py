#coding:utf-8
import time
from selenium import webdriver

driver = webdriver.Firefox()
# driver.maximize_window()
# driver.implicitly_wait(6)
driver.get("https://www.baidu.com/?tn=10018800_hao_pg")
time.sleep(1)

# driver.get_screenshot_as_file("C:\\Users\\sw\\Desktop\\baidu.png")
driver.quit()