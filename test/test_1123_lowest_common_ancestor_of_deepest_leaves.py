from unittest import TestCase
from problems.N1123_Lowest_Common_Ancestor_Of_Deepest_Leaves import Solution
from problems.Utility_Tree import list_to_tree_node,null,treenode_to_list

class TestSolution(TestCase):
    def test_lcaDeepestLeaves(self):
        self.assertListEqual([1,2,3], treenode_to_list(Solution().lcaDeepestLeaves(list_to_tree_node([1,2,3]))))

    def test_lcaDeepestLeaves_1(self):
        self.assertListEqual([4], treenode_to_list(Solution().lcaDeepestLeaves(list_to_tree_node([1,2,3,4]))))

    def test_lcaDeepestLeaves_2(self):
        self.assertListEqual([2,4,5], treenode_to_list(Solution().lcaDeepestLeaves(list_to_tree_node([1,2,3,4,5]))))
