from unittest import TestCase
from problems.N1547_Minimum_Cost_To_Cut_A_Stick import Solution

class TestSolution(TestCase):
    def test_minCost(self):
        self.assertEqual(16, Solution().minCost(n = 7, cuts = [1,3,4,5]))

    def test_minCost_1(self):
        self.assertEqual(22, Solution().minCost(n = 9, cuts = [5,6,1,4,2]))
