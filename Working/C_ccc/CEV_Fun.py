from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.get("http://www.c-ccc.net")
driver.maximize_window()
driver.find_element_by_id("username").send_keys("123")
driver.find_element_by_id("password").send_keys("123")
driver.find_element_by_id("btnSubmit").click()
sleep(5)
driver.find_element_by_xpath("//*[@id='chkbox']").click()
driver.find_element_by_xpath("//*[@id='btn']").click()
sleep(5)
driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div[1]/div[5]/div/a/div").click()
sleep(2)
#互转
# driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div[1]/div/h2/a[1]").click()
# sleep(3)
# driver.find_element_by_xpath("//*[@id='out_s_price']").send_keys("10")
# driver.find_element_by_xpath("//*[@id='username']").send_keys("751751")
# driver.find_element_by_xpath("//*[@id='paypass']").send_keys("123789Qm")
# driver.find_element_by_xpath("//*[@id='btnSubmit']").click()
#To CRP
#driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div[1]/div/h2/a[2]").click()
# sleep(3)
#To CMV
driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div[1]/div/h2/a[3]").click()
sleep(3)
driver.find_element_by_xpath("//*[@id='out_b_price']").clear()
driver.find_element_by_xpath("//*[@id='out_b_price']").send_keys("50")
driver.find_element_by_xpath("//*[@id='paypass']").send_keys("132")
driver.find_element_by_xpath("//*[@id='btnSubmit']").click()
print(driver.find_element_by_id("layui-layer3").text)
# #To GVe
# driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div[1]/div/h2/a[4]").click()
#
# #To 小3
# driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div[1]/div/h2/a[5]").click()
#
# #To ACDP
# driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div[1]/div/h2/a[6]").click()

sleep(3)

# driver.close()
