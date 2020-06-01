from unittest import TestCase
from problems.N226_Invert_Binary_Tree import Solution
from problems.Utility_Tree import list_to_tree_node,treenode_to_list

class TestSolution(TestCase):
    def test_invertTree(self):
        root = list_to_tree_node([4,2,7,1,3,6,9])
        self.assertListEqual([4,7,2,9,6,3,1], treenode_to_list(Solution().invertTree(root)))
