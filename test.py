import unittest

class Calc:
    def sum(self, a, b):
        return a+b
    def divide(self, a, b):
        return a/b
    def sub(self, a, b): 
        return a - b
    def multi(self, a, b):
        return a * b

class TestStringMethods(unittest.TestCase):
    def test_sum(self):
        c = Calc()
        self.assertEqual(c.sum(7,8), 15)
    def test_sub(self):
        c = Calc()
        self.assertEqual(c.sub(7,8), -1)

if __name__ == '__main__':
    unittest.main()
