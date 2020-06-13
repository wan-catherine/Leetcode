from unittest import TestCase
from problems.N368_Largest_Divisible_Subset import Solution

class TestSolution(TestCase):
    def test_largestDivisibleSubset(self):
        self.assertEqual(set([1,3]), Solution().largestDivisibleSubset([1,2,3]))


    def test_largestDivisibleSubset_1(self):
        self.assertEqual(set([1,2,4,8]), Solution().largestDivisibleSubset([1,2,4,8]))

    def test_largestDivisibleSubset_2(self):
        self.assertEqual(set([4,8,240]), Solution().largestDivisibleSubset([4,8,10,240]))