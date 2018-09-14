from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.get("http://www.51zxw.net")
#driver.maximize_window()

#driver.find_element_by_xpath("//input[@id='kw']").send_keys("51zxw")
#driver.find_element_by_xpath("//input[@name='wd']").send_keys("51zxw")

#driver.find_element_by_xpath("//form[@id='loginForm']/ul/input[1]").send_keys("csc825096095")
driver.find_element_by_xpath("//input[@type='text' and @name='username']").send_keys("csc825096095")
sleep(3)
driver.find_element_by_xpath("//form[@id='loginForm']/ul/input[2]").send_keys("cs774411")
sleep(3)
driver.find_element_by_class_name("lobtn").click()
sleep(5)
driver.quit()
