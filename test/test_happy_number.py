from unittest import TestCase
from problems.HappyNumber import Solution

class TestSolution(TestCase):
    def test_isHappy(self):
        solution = Solution()
        res = solution.isHappy(19)
        self.assertEqual(True, res)
