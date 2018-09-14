from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
sleep(3)
# driver.find_element_by_css_selector("#kw").send_keys("我要自学网")
# driver.find_element_by_css_selector(".s_ipt").send_keys("51zxw")
driver.find_element_by_css_selector("[autocomplete='off]").send_keys("51zxw")

sleep(3)
driver.find_element_by_id("su").click()
sleep(3)
driver.quit()

# driver.find_element_by_css_selector("form#loginForm>ul>input").send_keys("123456")