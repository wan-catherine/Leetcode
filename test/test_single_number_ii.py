from unittest import TestCase
from problems.SingleNumberII import Solution

class TestSolution(TestCase):
    def test_singleNumber(self):
        solution = Solution()
        res = solution.singleNumber([2,2,3,2])
        self.assertEqual(3, res)


    def test_singleNumber_one(self):
        solution = Solution()
        res = solution.singleNumber([0,1,0,1,0,1,99])
        self.assertEqual(99, res)

