from unittest import TestCase
from problems.N842_Split_Array_Into_Fibonacci_Sequence import Solution

class TestSolution(TestCase):
    def test_splitIntoFibonacci(self):
        self.assertListEqual([123,456,579], Solution().splitIntoFibonacci("123456579"))

    def test_splitIntoFibonacci_1(self):
        self.assertListEqual([1,1,2,3,5,8,13], Solution().splitIntoFibonacci("11235813"))

    def test_splitIntoFibonacci(self):
        self.assertListEqual([], Solution().splitIntoFibonacci("112358130"))

    def test_splitIntoFibonacci(self):
        self.assertListEqual([], Solution().splitIntoFibonacci("0123"))
