# -*- coding:cp936 -*-
__author__ = 'Administrator'

import unittest,time
from selenium import webdriver

class Untitled(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def test_Untitled (self):
        driver = self.driver
        self.driver.get("http://www.baidu.com")
        now_handle = driver.current_window_handle #��ȡ��ǰ���ھ��
        print (now_handle)   #�����ǰ��ȡ�Ĵ��ھ��
        driver.find_element_by_id("kw1").send_keys("selenium")
        driver.find_element_by_id("su1").click()
        driver.find_element_by_xpath("//*[@id='1']/h3/a[1]").click()
        time.sleep(2)
        all_handles = driver.window_handles #��ȡ���д��ھ��

        for handle in all_handles:

            if handle != now_handle:
                print (handle )   #�����ѡ��Ĵ��ھ��
                driver.switch_to_window(handle)
                driver.find_element_by_xpath("//*[@id='menu_projects']/a").click()
                time.sleep(5)
                driver.close() #�رյ�ǰ����
        time.sleep(3)
        print (now_handle )  #��������ھ��
        driver.switch_to_window(now_handle) #����������
        time.sleep(2)
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("abc")
        driver.find_element_by_id("su").click()

        time.sleep(10)

    def tearDown(self):
        self.driver.quit()
        #pass


if __name__ == "__main__":
    unittest.main()
