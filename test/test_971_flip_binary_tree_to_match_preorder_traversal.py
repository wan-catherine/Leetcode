from unittest import TestCase
from problems.N971_Flip_Binary_Tree_To_Match_Preorder_Traversal import Solution
from problems.Utility_Tree import list_to_tree_node, null

class TestSolution(TestCase):
    def test_flipMatchVoyage(self):
        root = list_to_tree_node([1,2])
        self.assertListEqual([-1], Solution().flipMatchVoyage(root, [2, 1]))

    def test_flipMatchVoyage_1(self):
        root = list_to_tree_node([1,2,3])
        self.assertListEqual([1], Solution().flipMatchVoyage(root, [1, 3, 2]))

    def test_flipMatchVoyage_2(self):
        root = list_to_tree_node([1,2,3])
        self.assertListEqual([], Solution().flipMatchVoyage(root, [1,2,3]))
