from unittest import TestCase
from problems.N1938_Maximum_Genetic_Difference_Query import Solution

class TestSolution(TestCase):
    def test_max_genetic_difference(self):
        self.assertListEqual([2,3,7], Solution().maxGeneticDifference(parents = [-1,0,1,1], queries = [[0,2],[3,2],[2,5]]))

    def test_max_genetic_difference_1(self):
        self.assertListEqual([6,14,7], Solution().maxGeneticDifference(parents = [3,7,-1,2,0,7,0,2], queries = [[4,6],[1,15],[0,5]]))
