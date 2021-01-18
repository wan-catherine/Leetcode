from unittest import TestCase
from problems.N1245_Tree_Diameter import Solution

class TestSolution(TestCase):
    def test_treeDiameter(self):
        self.assertEqual(2, Solution().treeDiameter([[0,1],[0,2]]))

    def test_treeDiameter_1(self):
        self.assertEqual(4, Solution().treeDiameter([[0,1],[1,2],[2,3],[1,4],[4,5]]))
