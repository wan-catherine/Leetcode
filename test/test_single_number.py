from unittest import TestCase
from problems.SingleNumber import Solution

class TestSolution(TestCase):
    def test_singleNumber(self):
        solution = Solution()
        res = solution.singleNumber([2,2,1])
        self.assertEqual(1,res)

    def test_singleNumber_one(self):
        solution = Solution()
        res = solution.singleNumber([4,1,2,1,2])
        self.assertEqual(4,res)