from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
driver = webdriver.Chrome()
driver.get("http://www.51zxw.net")
sleep(3)
select=Select(driver.find_element_by_css_selector("[name='CookieDate']"))
# select.select_by_index(1)
select.select_by_visible_text("留一年")
select.deselect_by_value("1")
sleep(3)
driver.quit()