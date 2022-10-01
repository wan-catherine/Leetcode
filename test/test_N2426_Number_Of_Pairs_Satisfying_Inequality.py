from unittest import TestCase
from problems.N2426_Number_Of_Pairs_Satisfying_Inequality import Solution

class TestSolution(TestCase):
    def test_number_of_pairs(self):
        self.assertEqual(3, Solution().numberOfPairs(nums1 = [3,2,5], nums2 = [2,2,1], diff = 1))

    def test_number_of_pairs_1(self):
        self.assertEqual(0, Solution().numberOfPairs(nums1 = [3,-1], nums2 = [-2,2], diff = -1))
