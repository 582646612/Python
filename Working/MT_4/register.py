from selenium import webdriver
from time import sleep
import time
def Shoping(x):
    driver = webdriver.Firefox()
    driver.get("http://192.168.0.186:9090/#/auth/login")
    driver.find_element_by_id("mat-input-0").send_keys(x)
    driver.find_element_by_id("mat-input-1").send_keys("Aa123456")
    driver.find_element_by_xpath("/html/body/app-root/app-auth/app-login/div/main/div/mat-card/form/mat-card-content/div/button").click()
    sleep(4)
    try:
        driver.find_element_by_id("mat-expansion-panel-header-3")
    except Exception   as e:
        driver.close()
        print(e)
    else:
        driver.find_element_by_id("mat-expansion-panel-header-3").click()
        driver.find_element_by_id("cdk-accordion-child-3").click()
        sleep(3)
        driver.find_element_by_xpath("/html/body/app-root/app-base/mat-sidenav-container/mat-sidenav-content/main/app-products/div/mat-card/div/div/mat-table/mat-row[1]/mat-cell[7]/a").click()
        sleep(2)
        try:
            driver.find_element_by_id("mat-select-0")
        except Exception   as e:
             print(e)
        else:
            driver.find_element_by_id("mat-select-0").click()
            driver.find_element_by_id("mat-option-0").click()
        # driver.find_element_by_id("mat-input-3").send_keys("1000")
        driver.find_element_by_id("mat-checkbox-1").click()
        driver.find_element_by_xpath("/html/body/app-root/app-base/mat-sidenav-container/mat-sidenav-content/main/app-investment/div/mat-card/div[3]/div/form/button").click()
        sleep(1)
        driver.close()
def Register(x,y):
    driver = webdriver.Chrome()
    driver.get("http://192.168.0.186:9090/#/auth/register")
    driver.find_element_by_id("mat-select-0").click()
    driver.find_element_by_id("mat-option-0").click()
    driver.find_element_by_id("mat-input-0").send_keys(x)
    driver.find_element_by_id("mat-input-1").send_keys(y)
    driver.find_element_by_id("mat-input-2").send_keys("Aa123456")
    driver.find_element_by_id("mat-input-3").send_keys("Aa123456")
    driver.find_element_by_id("mat-input-4").send_keys("111111")
    driver.find_element_by_id("mat-input-5").send_keys("111111")
    # driver.find_elements_by_id("mat-input-6").send_keys("111111")
    driver.find_element_by_xpath("/html/body/app-root/app-auth/app-register/div/main/div/mat-card/mat-card-content/form/div/button").click()
    sleep(6)
    try:
        driver.find_element_by_id("mat-input-7")
    except Exception:
        print("fail")
        driver.close()
    else:
        driver.find_element_by_id("mat-input-7").send_keys("jack")
        driver.find_element_by_id("mat-input-8").send_keys("mary")
        driver.find_element_by_id("mat-input-9").send_keys("530381199001012222")
        driver.find_element_by_id("mat-input-10").send_keys("6/4/1993")
        driver.find_element_by_id("mat-input-11").send_keys("America")
        driver.find_element_by_id("mat-input-12").send_keys("kunming")
        driver.find_element_by_id("mat-input-13").send_keys("123456")
        driver.find_element_by_id("mat-checkbox-1").click()
        driver.find_element_by_xpath("/html/body/app-root/app-auth/app-register-info/div/main/div/mat-card/mat-card-content/form/div[3]/button").click()
        sleep(2)
        driver.quit()
        print("success")

a=[15974500711,15974500712,15974500713,15974500714,15974500715,15974500716,15974500717,15974500718,15974500719,15974500720,15974500721,15974500722,15974500723,15974500724,15974500725,15974500726,15974500727,15974500728,15974500729,15974500730,15974500731,15974500732,15974500733,15974500734,15974500735,15974500736,15974500737,15974500738,15974500739,15974500740,15974500741,15974500742,15974500743,15974500744,15974500745,15974500746,15974500747,15974500748,15974500749,15974500750,15974500751,15974500752,15974500753,15974500754,15974500755,15974500756,15974500757,15974500758,15974500759,15974500760,15974500761,15974500762,15974500763,15974500764,15974500765,15974500766,15974500767,15974500768,15974500769,15974500770,15974500771,15974500772,15974500773,15974500774,15974500775,15974500776,15974500777,15974500778,15974500779,15974500780,15974500781,15974500782,15974500783,15974500784,15974500785,15974500786,15974500787,15974500788,15974500789,15974500790,15974500791,15974500792,15974500793,15974500794,15974500795,15974500796,15974500797,15974500798,15974500799,15974500800,15974500801,15974500802,15974500803,15974500804,15974500805,15974500806,15974500807,15974500808,15974500809]
b=["582645511@qq.com","582645512@qq.com","582645513@qq.com","582645514@qq.com","582645515@qq.com","582645516@qq.com","582645517@qq.com","582645518@qq.com","582645519@qq.com","582645520@qq.com","582645521@qq.com","582645522@qq.com","582645523@qq.com","582645524@qq.com","582645525@qq.com","582645526@qq.com","582645527@qq.com","582645528@qq.com","582645529@qq.com","582645530@qq.com","582645531@qq.com","582645532@qq.com","582645533@qq.com","582645534@qq.com","582645535@qq.com","582645536@qq.com","582645537@qq.com","582645538@qq.com","582645539@qq.com","582645540@qq.com","582645541@qq.com","582645542@qq.com","582645543@qq.com","582645544@qq.com","582645545@qq.com","582645546@qq.com","582645547@qq.com","582645548@qq.com","582645549@qq.com","582645550@qq.com","582645551@qq.com","582645552@qq.com","582645553@qq.com","582645554@qq.com","582645555@qq.com","582645556@qq.com","582645557@qq.com","582645558@qq.com","582645559@qq.com","582645560@qq.com","582645561@qq.com","582645562@qq.com","582645563@qq.com","582645564@qq.com","582645565@qq.com","582645566@qq.com","582645567@qq.com","582645568@qq.com","582645569@qq.com","582645570@qq.com","582645571@qq.com","582645572@qq.com","582645573@qq.com","582645574@qq.com","582645575@qq.com","582645576@qq.com","582645577@qq.com","582645578@qq.com","582645579@qq.com","582645580@qq.com","582645581@qq.com","582645582@qq.com","582645583@qq.com","582645584@qq.com","582645585@qq.com","582645586@qq.com","582645587@qq.com","582645588@qq.com","582645589@qq.com","582645590@qq.com","582645591@qq.com","582645592@qq.com","582645593@qq.com","582645594@qq.com","582645595@qq.com","582645596@qq.com","582645597@qq.com","582645598@qq.com","582645599@qq.com","582645600@qq.com","582645601@qq.com","582645602@qq.com","582645603@qq.com","582645604@qq.com","582645605@qq.com","582645606@qq.com","582645607@qq.com","582645608@qq.com","582645609@qq.com"]
c=[29853236]
for i in range(0,1):
   dt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
   print(dt)
   # print(i, a[i], b[i])
   # Register(a[i],b[i])
   print(i,c[i])
   Shoping(c[i])