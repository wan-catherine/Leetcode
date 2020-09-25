from unittest import TestCase
from problems.N179_LargestNumber import Solution

class TestSolution(TestCase):
    def test_largestNumber(self):
        self.assertEqual("210", Solution().largestNumber([10,2]))

    def test_largestNumber_1(self):
        self.assertEqual("9534330", Solution().largestNumber([3,30,34,5,9]))

    def test_largestNumber_2(self):
        self.assertEqual("0", Solution().largestNumber([0,0]))
