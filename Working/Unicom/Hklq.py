#coding:utf-8
import time
from selenium import webdriver

driver = webdriver.Firefox()
# driver.maximize_window()
# driver.implicitly_wait(6)
driver.get("http://10.86.36.43:8000/resourceManageIndex?staffNo=KMKGZC0030&staffName=%E5%94%90%E8%B0%A6&phone=13294954625&channelCode=86b1wlu&role=100")
driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[3]/a").click()
def hklb(x):
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div[1]/a").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div/div/div/div/div[2]").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div/div[2]/div/div/div/div/label/input").send_keys(x)
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div/div[3]/div/a[2]").click()
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/a").click()
    time.sleep(4)

a=["8986011780155659655","8986011780155659656","8986011780155659657","8986011780155659658","8986011780155659660","8986011780155659661","8986011780155659662","8986011780155659663","8986011780155659664","8986011780155659665","8986011780155659666","8986011780155659667","8986011780155659668","8986011780155659669","8986011780155659670","8986011780155659671","8986011780155659672","8986011780155659673","8986011780155659674","8986011780155659675","8986011780155659676","8986011780155659677","8986011780155659678","8986011780155659679","8986011780155659680","8986011780155659681","8986011780155659682","8986011780155659683","8986011780155659684","8986011780155659685","8986011780155659686","8986011780155659687","8986011780155659688","8986011780155659689","8986011780155659690","8986011780155659691","8986011780155659692","8986011780155659693","8986011780155659694","8986011780155659695","8986011780155659696"]
for i in range(0,30):
   dt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
   print(dt,i,a[i])
   hklb(a[i])