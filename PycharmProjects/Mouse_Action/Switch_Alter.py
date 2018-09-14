#encoding:utf-8
from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.get("file:///E:/new.html")
'''driver.find_element_by_xpath("/html/body/div/input[2]").click()
sleep(3)
alert=driver.switch_to_alert()
print(alert.text)
sleep(2)
alert.accept()'''
# driver.find_element_by_xpath("/html/body/div/input[3]").click()
# dialog_box=driver.switch_to_alert()
# sleep(2)
# print(dialog_box.text)
# #dialog_box.accept()
# dialog_box.dismiss()
driver.find_element_by_xpath("/html/body/div/input[1]").click()
dialog_box = driver.switch_to_alert()
sleep(2)
print(dialog_box.text)
dialog_box.send_keys("1")
sleep(3)
dialog_box.accept()
