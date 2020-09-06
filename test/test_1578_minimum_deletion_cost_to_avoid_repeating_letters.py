from unittest import TestCase
from problems.N1578_Minimum_Deletion_Cost_To_Avoid_Repeating_Letters import Solution

class TestSolution(TestCase):
    def test_minCost(self):
        self.assertEqual(3, Solution().minCost(s = "abaac", cost = [1,2,3,4,5]))

    def test_minCost_1(self):
        self.assertEqual(0, Solution().minCost(s = "abc", cost = [1,2,3]))

    def test_minCost_2(self):
        self.assertEqual(2, Solution().minCost(s = "aabaa", cost = [1,2,3,4,1]))

