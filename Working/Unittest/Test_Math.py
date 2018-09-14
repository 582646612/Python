# -*- coding: utf-8 -*-
from calculator import *
import unittest
import HTMLTestRunner
from Email import *
class TestMath(unittest.TestCase):
    def setUp(self):
        print("start")

    def test_add(self):
        a=add(2,4)
        self.assertEqual(a,6)

    def test_minus(self):
        self.assertEqual(minus(15,3), 12)

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
    filename = 'D:\\python\\Working\\Unittest\\HtmlReport.html'
    with open(filename, 'wb') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行详情：')
        runner.run(suite)
    send_email()
    # unittest.runner()