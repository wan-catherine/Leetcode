from unittest import TestCase
from problems.Utility_Tree import list_to_tree_node, null
from problems.N337_House_Robber_III import Solution

class TestSolution(TestCase):
    def test_rob(self):
        root = list_to_tree_node([3,2,3,null,3,null,1])
        self.assertEqual(7, Solution().rob(root))

    def test_rob_1(self):
        root = list_to_tree_node([3,4,5,1,3,null,1])
        self.assertEqual(9, Solution().rob(root))

    def test_rob_2(self):
        root = list_to_tree_node([2,1,3,null,4])
        self.assertEqual(7, Solution().rob(root))
