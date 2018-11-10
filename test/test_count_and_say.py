from unittest import TestCase
from problems.CountAndSay import Solution

class TestSolution(TestCase):
    def test_countAndSay(self):
        solution = Solution()
        res = solution.countAndSay(1)
        self.assertEqual("1", res)

    def test_countAndSay_one(self):
        solution = Solution()
        res = solution.countAndSay(4)
        self.assertEqual("1211", res)