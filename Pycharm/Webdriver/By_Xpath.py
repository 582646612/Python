from selenium import webdriver
from time import sleep
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

#driver.find_element_by_xpath("//input[@id='kw']").send_keys("51zxw")
#driver.find_element_by_xpath("//input[@name='wd']").send_keys("51zxw")
driver.find_element_by_xpath("//*[@class='s_ipt']").send_keys("51zxw")
sleep(2)
driver.find_element_by_id("su").click()
sleep(2)

driver.quit()
