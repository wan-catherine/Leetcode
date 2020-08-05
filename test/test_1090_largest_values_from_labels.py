from unittest import TestCase
from problems.N1090_Largest_Values_From_Labels import Solution

class TestSolution(TestCase):
    def test_largestValsFromLabels(self):
        self.assertEqual(9, Solution().largestValsFromLabels(values = [5,4,3,2,1], labels = [1,1,2,2,3], num_wanted = 3, use_limit = 1))

    def test_largestValsFromLabels_1(self):
        self.assertEqual(12, Solution().largestValsFromLabels(values = [5,4,3,2,1], labels = [1,3,3,3,2], num_wanted = 3, use_limit = 2))

    def test_largestValsFromLabels_2(self):
        self.assertEqual(16, Solution().largestValsFromLabels(values = [9,8,8,7,6], labels = [0,0,0,1,1], num_wanted = 3, use_limit = 1))

    def test_largestValsFromLabels_3(self):
        self.assertEqual(24, Solution().largestValsFromLabels(values = [9,8,8,7,6], labels = [0,0,0,1,1], num_wanted = 3, use_limit = 2))
