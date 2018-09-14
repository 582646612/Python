from calculator import Math
import unittest
class TestMath(unittest.TestCase):
    def setUp(self):
        print("start")

    def test_add(self):
        j=Math(5,8)
        self.assertEqual(j.add(),13)

    def tearDown(self):
        print("end")


if __name__ == "__main__":
     unittest.main()