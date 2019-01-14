from unittest import TestCase
from problems.SingleNumberIII import Solution

class TestSolution(TestCase):
    def test_singleNumber(self):
        solution = Solution()
        res = solution.singleNumber([1,2,1,3,2,5])
        self.assertEqual(res, [3,5])
