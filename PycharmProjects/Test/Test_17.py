from selenium import webdriver
from time import sleep
import time
def login(x):
 driver=webdriver.Chrome()
 driver.get("https://www.icloud.com/")
 driver.maximize_window()
 sleep(6)
 driver.find_element_by_id("appleId").send_keys("825096095@qq.com")
 driver.find_element_by_id("pwd").send_keys("Cs&774411")
 driver.find_element_by_id("btnSubmit").click()
 # sleep(6)
 # driver.find_element_by_xpath("//input[@id='chkbox']").click()
 # driver.find_element_by_xpath("//*[@id='btn']").click()
 # sleep(4)
 # driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div[4]/div[2]/div/div/a/div").click()
 # sleep(4)
 # driver.find_element_by_xpath("//*[@id='lotteryBtn']").click()
 # sleep(5)
 # print("成功抢到奖品")
 # print(driver.find_element_by_xpath("//*[@id='errortitle']").text)
 driver.close()

  # a = [919396]
  # for i in range(0, 600):
  #    print(i, a[i])
  #    dt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
  #    print(dt)
