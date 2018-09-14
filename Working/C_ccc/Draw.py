from selenium import webdriver
from time import sleep
import time
def login(x):
 driver=webdriver.Chrome()
 driver.get("http://www.member.com")
 driver.maximize_window()
 driver.find_element_by_id("username").send_keys(x)
 driver.find_element_by_id("password").send_keys("Sw496723")
 driver.find_element_by_id("btnSubmit").click()
 sleep(6)
 driver.find_element_by_xpath("//input[@id='chkbox']").click()
 driver.find_element_by_xpath("//*[@id='btn']").click()
 sleep(4)
 driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div[4]/div[2]/div/div/a/div").click()
 sleep(4)
 driver.find_element_by_xpath("//*[@id='lotteryBtn']").click()
 sleep(5)
 print("成功抢到奖品")
 print(driver.find_element_by_xpath("//*[@id='errortitle']").text)
 driver.close()

a = [1065917,1066145,930656,703001,479948,511323,915849,109634,119319,129319,666110,666111,666112,666113,666114,666115,666116,666117,666118,666119,666120,666121,666122,666123,666126,888300,888301,888302,888303,888304,888305,888306,888307,888308,888309,888310,888311,888312,888313,888314,333338,337788,1688888,1688889,1688890,333778,333779,139319,159319,619319,295578,919391,919392,919393,919395,559515,559516,559517,919396]
for i in range(0,600):
   print(i,a[i])
   dt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
   print(dt)
   login(a[i])




