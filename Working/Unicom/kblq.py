#coding:utf-8
import time
from selenium import webdriver

driver = webdriver.Firefox()
# driver.maximize_window()
# driver.implicitly_wait(6)
driver.get("http://10.86.36.43:8000/resourceManageIndex?staffNo=KMWHZXY00913&staffName=%E5%AE%98%E6%A2%85&phone=13294954625&channelCode=86b1wlu&role=100")
driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[3]/a").click()
def hklb(x):
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div[2]/a").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div/div/div/div/div[2]").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div/div[2]/div/div/div/div/label/input").send_keys(x)
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div/div[3]/div/a[2]").click()
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/a").click()
    time.sleep(3)

a=["card180829112431975903","card180829112651678922"]
for i in range(0,40):
   dt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
   print(dt,i,a[i])
   hklb(a[i])