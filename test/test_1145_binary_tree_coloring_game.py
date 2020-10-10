from unittest import TestCase
from problems.N1145_Binary_Tree_Coloring_Game import Solution
from problems.Utility_Tree import list_to_tree_node, null

class TestSolution(TestCase):
    def test_btreeGameWinningMove(self):
        self.assertTrue(Solution().btreeGameWinningMove(list_to_tree_node([1,2,3,4,5,6,7,8,9,10,11]), 11, 3))
