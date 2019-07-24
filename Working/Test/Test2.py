from selenium import webdriver
from PIL import Image
from time import sleep
driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://10.123.0.126:18010/CIS-SSF/login")
driver.implicitly_wait(5)
sleep(5)
driver.save_screenshot(r'D:\Project\python\Working\qudao_system\photo\1.png')
rangle = (975,538,975+90,538+30)  #计算验证码整体坐标
login = Image.open(r'D:\Project\python\Working\qudao_system\photo\1.png')
frame4=login.crop(rangle)   #截取验证码图片
frame4.save(r'D:\Project\python\Working\qudao_system\photo\1.jpg')
driver.quit()
# #
