from unittest import TestCase
from problems.N2616_Minimize_The_Maximum_Difference_Of_Pairs import Solution

class TestSolution(TestCase):
    def test_minimize_max(self):
        self.assertEqual(1, Solution().minimizeMax(nums = [10,1,2,7,1,3], p = 2))

    def test_minimize_max_1(self):
        self.assertEqual(0, Solution().minimizeMax(nums = [4,2,1,2], p = 1))
