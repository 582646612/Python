# coding=utf-8
import time
import unittest
class DemoTest(unittest.TestCase):

    def setUp(self):
        print("start")
    def a(self):
        print("a")
    def b(self):
        print("b")
    @unittest.skip('暂时跳过用例3的测试')
    def c(self):
          print("c")
    def d(self):
         print("d")
    # def test_demo(self):
    #      a()
    #      b()
    #      c()
    #      d()
    def tearDown(self):
        print("ending")
if __name__ == '__main__':
    # suite = unittest.TestLoader().loadTestsFromTestCase(DemoTest)
    # unittest.TextTestRunner(verbosity=2).run(suite)
    unittest.main()
