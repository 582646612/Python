# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest, time


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://135.64.22.33:18082/ordercenter/loginController/login")
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id("usernameInput").send_keys("admin")
        self.driver.find_element_by_id("passwordInput").send_keys("1qaz2wsx")
        self.driver.find_element_by_id("loginButton").click()
    def test_untitled_test_case(self):
        driver = self.driver
        driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div[1]/div[1]").click()
        driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div[2]/ul/li[8]/a").click()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/table/thead/tr/th[2]/a[5]").click()


    # def tearDown(self):
    #     self.driver.quit()


if __name__ == "__main__":
    unittest.main()
