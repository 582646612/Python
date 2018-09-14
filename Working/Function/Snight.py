import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)
driver.get("https://www.baidu.com")
time.sleep(1)

driver.get_screenshot_as_file("C:\\Users\\sw\\Desktop\\baidu.png")
driver.quit()