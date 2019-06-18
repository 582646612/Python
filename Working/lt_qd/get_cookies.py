from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
def get_cookie():
    driver = webdriver.Ie()
    driver.implicitly_wait(5)
    driver.get("http://10.123.0.126:18010/CIS-SSF/login")
    driver.implicitly_wait(5)
    driver.find_element_by_id("username").send_keys("yn-pangq3")
    driver.find_element_by_id("password").send_keys("123@zyzx")
    driver.find_element_by_id("B1").send_keys(Keys.ENTER)
    try:
        driver.find_element_by_xpath("//*[@id='keepOnForm']/div[2]/div/div[2]/div[2]/ul/li[1]/a").send_keys(Keys.ENTER)
    except:
        print()
    time.sleep(2)
    result=driver.get_cookies()
    # driver.quit()
    return result#[0]['value']
def write_file(x):
    conten =x
    with open("The_cookies.txt", "w") as f:
        f.write(conten)
        f.close()
if __name__ == '__main__':
    the_token=get_cookie()
    print(the_token)
    # write_file(the_cookies)