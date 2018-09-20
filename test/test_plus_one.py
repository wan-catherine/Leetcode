from unittest import TestCase
from problems.PlusOne import Solution

class TestSolution(TestCase):
    def test_plusOne(self):
        solution = Solution()
        res = solution.plusOne([1,2,3])
        self.assertEqual(res, [1,2,4])
