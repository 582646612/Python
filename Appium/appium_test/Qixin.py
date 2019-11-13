#coding:utf-8
import yaml
import random
import warnings
from appium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from Function import Open_app
warnings.filterwarnings("ignore", category=Warning)#警告不显示
def login(x):
    try:
        desired_caps=Open_app("qixin")
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.ID, "com.bonc.mobile.jlmhim.tt:id/login_user")))
        driver.find_element_by_id("com.bonc.mobile.jlmhim.tt:id/login_user").send_keys(x)
        driver.find_element_by_id("com.bonc.mobile.jlmhim.tt:id/login_password").send_keys('123@@456')
        for x in range(1,4):
            driver.find_element_by_id("com.bonc.mobile.jlmhim.tt:id/login_login").click()
        driver.close_app()
        driver.quit()
    except Exception as e:
        print(e)
def remain(min):
    count = 0
    while (count < min):
        count += 1
        n = min - count
        sleep(1)
        print(n)
if __name__ == '__main__':
    for j in range(1,100):
        x = random.randint(100, 999)
        name = '0111' + str(x)
        print("工号：",name)
        for i in range(1,6):
            print("第",i,"次")
            login(name)
            remain(60)