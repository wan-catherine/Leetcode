from unittest import TestCase
from problems.N2597_The_Number_Of_Beautiful_Subsets import Solution

class TestSolution(TestCase):
    def test_beautiful_subsets(self):
        self.assertEqual(4, Solution().beautifulSubsets(nums = [2,4,6], k = 2))

    def test_beautiful_subsets_1(self):
        self.assertEqual(1, Solution().beautifulSubsets(nums = [1], k = 1))
