from selenium import webdriver
from time import sleep
driver=webdriver.Firefox()
driver.get("http://www.51zxw.net")
#driver.find_element_by_tag_name("input").send_keys("csc")
driver.find_element_by_tag_name("input").send_keys("123456")
sleep(3)
driver.quit()