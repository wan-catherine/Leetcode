from unittest import TestCase
from .Xor_Operation_In_An_Array import Solution

class TestSolution(TestCase):
    def test_xorOperation(self):
        self.assertEqual(8, Solution().xorOperation(5,0))

    def test_xorOperation_1(self):
        self.assertEqual(8, Solution().xorOperation(4,3))

    def test_xorOperation_2(self):
        self.assertEqual(7, Solution().xorOperation(1,7))

    def test_xorOperation_3(self):
        self.assertEqual(2, Solution().xorOperation(10,5))

