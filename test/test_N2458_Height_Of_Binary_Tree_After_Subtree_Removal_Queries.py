from unittest import TestCase
from problems.N2458_Height_Of_Binary_Tree_After_Subtree_Removal_Queries import Solution
from problems.Utility_Tree import list_to_tree_node, null


class TestSolution(TestCase):
    def test_tree_queries(self):
        root = list_to_tree_node([1,3,4,2,null,6,5,null,null,null,null,null,7])
        self.assertListEqual([2], Solution().treeQueries(root, [4]))

    def test_tree_queries_1(self):
        root = list_to_tree_node([5,8,9,2,1,3,7,4,6])
        self.assertListEqual([3,2,3,2], Solution().treeQueries(root, [3,2,4,8]))

    def test_tree_queries_2(self):
        root = list_to_tree_node([1,null,5,3,null,2,4])
        self.assertListEqual([1,0,3,3,3], Solution().treeQueries(root, [3,5,4,2,4]))

