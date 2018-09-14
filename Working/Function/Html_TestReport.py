#coding=utf-8
import unittest
from HTMLTestRunner import HTMLTestRunner
import time
test_dir='./test'
discover=unittest.defaultTestLoader.discover(test_dir,pattern="test.py")

if __name__=='__main__':
    report_dir='./Report'
    now=time.strftime("%Y-%m-%d %H_%M_%S")
    report_name=report_dir='/'+now+'result.html'

    with open(report_name,'wb') as f:
        runner=HTMLTestRunner(stream=f,title='Test Report',description='Test case Result')
        runner.run(discover)
    f.close()