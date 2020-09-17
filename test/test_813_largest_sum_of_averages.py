from unittest import TestCase
from problems.N813_Largest_Sum_Of_Averages import Solution

class TestSolution(TestCase):
    def test_largestSumOfAverages(self):
        self.assertEqual(20, Solution().largestSumOfAverages([9,1,2,3,9], 3))

    def test_largestSumOfAverages_1(self):
        self.assertEqual(20.5, Solution().largestSumOfAverages([1,2,3,4,5,6,7], 4))
