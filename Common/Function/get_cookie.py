#coding=utf-8
from  selenium import webdriver
import time
def get_cookie(driver):
    cookie=driver.get_cookies()
    return cookie
