from unittest import TestCase
from problems.N958_Check_Completeness_Of_A_Binary_Tree import Solution
from problems.Utility_Tree import list_to_tree_node, null

class TestSolution(TestCase):
    def test_isCompleteTree(self):
        self.assertTrue(Solution().isCompleteTree(list_to_tree_node([1,2,3,4,5,6])))

    def test_isCompleteTree_1(self):
        self.assertFalse(Solution().isCompleteTree(list_to_tree_node([1,2,3,4,5,null,7])))
