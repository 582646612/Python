from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.get("http://www.global-asset-exchange.com")
driver.maximize_window()
driver.find_element_by_id("username").send_keys("123")
driver.find_element_by_id("password").send_keys("123")
driver.find_element_by_id("btnSubmit").click()
sleep(6)
driver.find_element_by_xpath("//*[@id='chkbox']").click()
driver.find_element_by_xpath("//*[@id='btn']").click()
sleep(5)
driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div[3]/div[1]/div/div/a/div").click()
sleep(2)
driver.find_element_by_xpath("//*[@id='lotteryBtn']").click()
sleep(3)
if driver.find_element_by_xpath("//*[@id='errortitle']").text=='':
    print("成功抢到奖品")
    print(driver.find_element_by_xpath("//*[@id='successtitle']").text)
else:
    print(driver.find_element_by_xpath("//*[@id='errortitle']").text)
# driver.close()
