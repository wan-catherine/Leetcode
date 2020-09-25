from unittest import TestCase
from problems.N1262_Greatest_Sum_Divisible_By_Three import Solution

class TestSolution(TestCase):
    def test_maxSumDivThree(self):
        self.assertEqual(18, Solution().maxSumDivThree([3,6,5,1,8]))

    def test_maxSumDivThree_1(self):
        self.assertEqual(0, Solution().maxSumDivThree([4]))

    def test_maxSumDivThree_2(self):
        self.assertEqual(12, Solution().maxSumDivThree([1,2,3,4,4]))
