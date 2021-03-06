# -*- coding: utf-8 -*-
from calculator import *
import unittest
import HTMLTestRunner

class TestMath(unittest.TestCase):
    def setUp(self):
        print("start")

    def test_add(self):
        a=add(2,4)
        self.assertEqual(a,6)

    def test_minus(self):
        self.assertEqual(minus(15,3), 12)

    # @unittest.skip("直接跳过测试")
    # @unittest.skipIf(4 > 3, "当条件为True时跳过测试")
    # @unittest.skipUnless(3 > 2, "当条件为True时执行测试")
    def test_multi(self):
        self.assertEqual(multi(2, 3), 6)

    def test_divide(self):
        self.assertEqual(divide(12, 3), 2)
        print("end")


if __name__ == "Test_Math":
    # suite = unittest.TestSuite()
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    suite = unittest.TestSuite()
    suite.addTest(TestMath('test_add'))
    suite.addTest(TestMath('test_minus'))
    suite.addTest(TestMath( 'test_multi'))
    suite.addTest(TestMath('test_divide'))
    filename = 'D:\\python\\Working\\Webdriver\\HtmlReport.html'
    with open(filename, 'wb') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行详情：')
        runner.run(suite)

    # unittest.runner()