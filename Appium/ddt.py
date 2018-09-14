import unittest
from ddt import ddt,data,unpack
@ddt
class MyTestCase(unittest.TestCase):
    def setup(self):
        print("this is the setup")
    @data(["sd","ad"],["aa","aa"])
    @unpack
    def test_something(self,value,value2):
      print('value',value2)
      print("this is test b")
    def tearDown(self):
        print("this is the down")

if __name__ == '__main__':
    unittest.main()
