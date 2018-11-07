#coding:utf-8
from selenium import webdriver
from LoginPage import LoginPage
from time import sleep

def test_user_login(driver, username, password):
    """测试用户名/密码是否可以登录"""
    login_page = LoginPage(driver)
    login_page.open()
    login_page.type_username(username)
    login_page.type_password(password)
    login_page.type_login()
    login_page.close()

#创建main()函数
def main():
    driver = webdriver.Edge()
    username = '3494xxxxx'    #qq号码
    password = 'kemixxxx'    #qq密码
    test_user_login(driver, username, password)
    sleep(3)

    driver.quit()

if __name__ == '__main__':
    main()