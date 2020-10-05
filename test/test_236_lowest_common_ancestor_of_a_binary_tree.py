from unittest import TestCase
from problems.N236_Lowest_Common_Ancestor_Of_A_Binary_Tree import Solution
from problems.Utility_Tree import list_to_tree_node, null

class TestSolution(TestCase):
    def test_lowestCommonAncestor(self):
        self.assertEqual(3, Solution().lowestCommonAncestor(root = list_to_tree_node([3,5,1,6,2,0,8,null,null,7,4]), p = 5, q = 1))

    def test_lowestCommonAncestor_(self):
        self.assertEqual(5, Solution().lowestCommonAncestor(root = list_to_tree_node([3,5,1,6,2,0,8,null,null,7,4]), p = 5, q = 4))
