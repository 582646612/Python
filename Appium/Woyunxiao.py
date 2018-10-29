#coding:utf-8
from appium import webdriver
from Function import Z_unlock,L_unlock,Open_app
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time

# os.system("adb connect 127.0.0.1:7555")
desired_caps=Open_app('woyunxiao')
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

try:
    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.ID,"com.asiainfo.wcs:id/lockPatternView")))
    # Z_unlock(driver)
    L_unlock(driver)
except:
    driver.find_element_by_id("com.asiainfo.wcs:id/iv_cbss_login").click()
    time.sleep(1)
    driver.find_element_by_id("com.asiainfo.wcs:id/login_account_input_edit").send_keys("KMCSGH000051")
    driver.find_element_by_id("com.asiainfo.wcs:id/login_psw_input_edit").send_keys("Yy198623..")
    driver.find_element_by_id("com.asiainfo.wcs:id/login_vercode_input_edit").send_keys("123")
    driver.find_element_by_id("com.asiainfo.wcs:id/login_btn").click()
WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.NAME,"kaihu")))
driver.find_element_by_name("kaihu").click()
time.sleep(3)
print driver.get_window_size()

driver.quit()

# if not self.driver.find_element_by_name("登录"):
# #滑动界面
# else:
# try:
#     if(xxxx.isDisplay);
#
# catch:
#     xxxxx