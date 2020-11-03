from unittest import TestCase
from problems.N968_Binary_Tree_Cameras import Solution
from problems.Utility_Tree import list_to_tree_node, null

class TestSolution(TestCase):
    def test_minCameraCover(self):
        self.assertEqual(1, Solution().minCameraCover(list_to_tree_node([0,0,null,0,0])))

    def test_minCameraCover_1(self):
        self.assertEqual(2, Solution().minCameraCover(list_to_tree_node([0,0,null,0,null,0,null,null,0])))
