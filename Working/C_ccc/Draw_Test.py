from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.get("https://3c-ccc-3c.com/#/share/login")
# driver.maximize_window()
driver.find_element_by_xpath("//form/div[2]/div/input").send_keys("188188")
driver.find_element_by_xpath("//form/div[3]/div/input").send_keys("789789Qm")
driver.find_element_by_id("loginsubmit").click()
sleep(6)
driver.find_element_by_id("chkbox").click()
driver.find_element_by_xpath("/html/body/modal-container/div/div/app-major/div/div/div[4]/div/button").click()
driver.get("https://3c-ccc-3c.com/#/base/wallet/cdv")


# driver.find_element_by_xpath("/html/body/app-root/app-base/div/div/app-home/div/app-assetmenu/div/div[9]/div/a/div").click()

# driver.find_element_by_xpath("/html/body/modal-container/div/div/div/form/div[1]/div[2]/div/input").send_keys("100")
# driver.find_element_by_xpath("/html/body/modal-container/div/div/div/form/div[1]/div[4]/div/input").send_keys("123789Qm")
# driver.find_element_by_xpath("/html/body/modal-container/div/div/div/form/div[2]/button[1]").click()
sleep(3)
# driver.close()
