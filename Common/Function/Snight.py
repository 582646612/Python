#coding:utf-8
import os
from Function.Now_time import get_time
def snight(driver):
    curpath = os.path.dirname(os.path.realpath(__file__))
    path = curpath + "\Picture\\"+get_time()+".jpg"
    driver.get_screenshot_as_file(path)

if __name__ == '__main__':
    snight()

