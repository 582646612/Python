from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import  sleep
driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.find_element_by_css_selector("#kw").send_keys("python")
sleep(3)
element=driver.find_element_by_css_selector("#kw")
#双击
ActionChains(driver).double_click(element).perform()
sleep(2)
#右键
ActionChains(driver).context_click(element).perform()
sleep(3)
#悬停
above=driver.find_element_by_css_selector(".pf")
ActionChains(driver).move_to_element(above).perform()
sleep(3)
driver.find_element_by_link_text("高级搜索").click()
sleep(3)
#driver.quit()