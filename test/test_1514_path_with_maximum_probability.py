from unittest import TestCase
from problems.N1514_Path_With_Maximum_Probability import Solution

class TestSolution(TestCase):
    def test_maxProbability(self):
        self.assertEqual(0.25000, Solution().maxProbability(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2))

    def test_maxProbability_1(self):
        self.assertEqual(0.30000, Solution().maxProbability(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2))

    def test_maxProbability_2(self):
        self.assertEqual(0.00000, Solution().maxProbability(n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2))
