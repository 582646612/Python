import unittest
from  appium import webdriver


class MyTestCase(unittest.TestCase):
    def setUp(self):
        desired_caps={}
        desired_caps['platformName']='Android'
        desired_caps['platformVersion']='4.4'
        desired_caps['deviceName']='MPIFC25N3H01999'
        desired_caps['appPackage']='com.android.calculator2'
        desired_caps['appActivity']='.Calculator'
        desired_caps['unicodeKeyboard']='true'
        desired_caps['resetKeyboard']='True'
        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
    def test(self):
        self.assertEqual(True, False)
    # com.android.calculator2 /.Calculator
    # def test_something(self):
    #     self.assertEqual(True, False)
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
