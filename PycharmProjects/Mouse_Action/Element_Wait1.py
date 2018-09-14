from selenium import webdriver
from  selenium.common.exceptions import NoSuchAttributeException
from  time import sleep,ctime

from time import sleep
driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
sleep(2)
driver.implicitly_wait(5)

try:
    print(ctime())
    driver.find_element_by_css_selector("#kw").send_keys("51zxw")
    driver.find_element_by_css_selector("#su").click()
except NoSuchAttributeException as msg:
    print(msg)
finally:
    print(ctime())
sleep(3)
driver.quit()
