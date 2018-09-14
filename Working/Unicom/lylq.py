#coding:utf-8
import time
from selenium import webdriver

driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(6)
driver.get("http://10.86.36.43:8000/resourceManageIndex?staffNo=KMKGZC0030&staffName=%E5%94%90%E8%B0%A6&phone=18608710428&channelCode=86b1wlu&role=100")
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[3]/a").click()
def hklb(x):
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div/a").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div/div/div/div/div[2]").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div/div[2]/div/div/div/div/label/input").send_keys(x)
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div/div[3]/div/a[2]").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/a").click()
    time.sleep(3)



a=["bluetooth80155659647","bluetooth80117945172","bluetooth80155659712","bluetooth80155659693","bluetooth80155659603","bluetooth80155659206","bluetooth80155659768","bluetooth80155659769","bluetooth80155659770","bluetooth80155659771","bluetooth80155659772","bluetooth80155659773","bluetooth80155659774","bluetooth80155659775","bluetooth80155659776","bluetooth80155659777","bluetooth80155659778","bluetooth80155659779","bluetooth80155659780","bluetooth80155659781","bluetooth80155659782","bluetooth80155659783","bluetooth80155659784","bluetooth80155659785","bluetooth80155659786","bluetooth80155659787","bluetooth80155659788","bluetooth80155659789","bluetooth80155659790","bluetooth80155659791","bluetooth80155659792","bluetooth80155659793","bluetooth80155659794","bluetooth80155659795","bluetooth80155659796","bluetooth80155659797","bluetooth80155659798","bluetooth80155659799","bluetooth80155659800","bluetooth80155659801","bluetooth80155659802","bluetooth80155659803","bluetooth80155659804","bluetooth80155659805","bluetooth80155659806","bluetooth80155659807","bluetooth80155659808","bluetooth80155659809","bluetooth80155659810","bluetooth80155659811","bluetooth80155659812","bluetooth80155659813","bluetooth80155659814","bluetooth80155659815","bluetooth80155659816","bluetooth80155659817","bluetooth80155659818","bluetooth80155659819","bluetooth80155659820","bluetooth80155659821","bluetooth80155659822","bluetooth80155659823","bluetooth80155659824","bluetooth80155659825","bluetooth80155659826","bluetooth80155659827","bluetooth80155659828","bluetooth80155659829","bluetooth80155659830","bluetooth80155659831","bluetooth80155659832","bluetooth80155659833","bluetooth80155659834","bluetooth80155659835","bluetooth80155659696","bluetooth80155659697","bluetooth80155659698","bluetooth80155659699","bluetooth80155659700","bluetooth80155659701","bluetooth80155659702","bluetooth80155659703","bluetooth80155659704","bluetooth80155659705","bluetooth80155659706","bluetooth80155659707","bluetooth80155659708","bluetooth80155659709","bluetooth80155659710","bluetooth80155659711","bluetooth80155659712","bluetooth80155659713","bluetooth80155659714","bluetooth80155659715","bluetooth80155659716","bluetooth80155659717","bluetooth80155659718","bluetooth80155659719","bluetooth80155659720","bluetooth80155659721","bluetooth80155659722","bluetooth80155659723","bluetooth80155659724","bluetooth80155659725","bluetooth80155659726","bluetooth80155659727","bluetooth80155659728","bluetooth80155659729","bluetooth80155659730","bluetooth80155659731","bluetooth80155659732","bluetooth80155659733","bluetooth80155659734","bluetooth80155659735","bluetooth80155659736","bluetooth80155659737","bluetooth80155659738","bluetooth80155659739","bluetooth80155659740","bluetooth80155659741","bluetooth80155659742","bluetooth80155659743","bluetooth80155659744","bluetooth80155659745","bluetooth80155659746","bluetooth80155659747","bluetooth80155659748","bluetooth80155659749","bluetooth80155659750","bluetooth80155659751","bluetooth80155659752","bluetooth80155659753","bluetooth80155659754","bluetooth80155659755","bluetooth80155659756","bluetooth80155659757","bluetooth80155659758","bluetooth80155659759","bluetooth80155659760","bluetooth80155659761","bluetooth80155659762","bluetooth80155659763","bluetooth80155659764","bluetooth80155659765","bluetooth80155659766","bluetooth80155659767","bluetooth80155659768","bluetooth80155659769","bluetooth80155659770","bluetooth80155659771"]
for i in range(0,10):
   dt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
   print(dt,i,a[i])
   hklb(a[i])