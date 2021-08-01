from unittest import TestCase
from problems.N1932_Merge_BSTs_To_Create_Single_BST import Solution
from problems.Utility_Tree import list_to_tree_node, treenode_to_list, null


class TestSolution(TestCase):
    def test_can_merge(self):
        trees = [list_to_tree_node([2,1]), list_to_tree_node([3,2,5]), list_to_tree_node([5,4])]
        res = Solution().canMerge(trees)
        self.assertListEqual([3,2,5,1,null,4], treenode_to_list(res))

    def test_can_merge_1(self):
        trees = [list_to_tree_node([5, 3, 8]), list_to_tree_node([3, 2, 6])]
        res = Solution().canMerge(trees)
        self.assertListEqual([], treenode_to_list(res))

    def test_can_merge_2(self):
        trees = [list_to_tree_node([7])]
        res = Solution().canMerge(trees)
        self.assertListEqual([7], treenode_to_list(res))
