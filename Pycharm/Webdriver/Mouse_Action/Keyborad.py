from selenium import  webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.find_element_by_css_selector("#kw").send_keys("python")
sleep(2)
driver.find_element_by_css_selector("#kw").send_keys(Keys.CONTROL,'a')
sleep(2)
driver.find_element_by_css_selector("#kw").send_keys(Keys.CONTROL,'c')
sleep(2)
driver.get("https://www.yahoo.com/")
sleep(2)
driver.find_element_by_css_selector("#uh-search-box").send_keys(Keys.CONTROL,'v')
sleep(2)
driver.find_element_by_id("uh-search-button").click()
sleep(2)
driver.quit()



