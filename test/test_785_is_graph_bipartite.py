from unittest import TestCase
from problems.N785_Is_Graph_Bipartite import Solution

class TestSolution(TestCase):
    def test_isBipartite(self):
        self.assertTrue(Solution().isBipartite([[1,3], [0,2], [1,3], [0,2]]))

    def test_isBipartite_1(self):
        self.assertFalse(Solution().isBipartite([[1,2,3], [0,2], [0,1,3], [0,2]]))
