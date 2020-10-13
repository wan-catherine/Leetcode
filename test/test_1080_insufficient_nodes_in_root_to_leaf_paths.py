from unittest import TestCase
from problems.N1080_Insufficient_Nodes_In_Root_To_Leaf_Paths import Solution
from problems.Utility_Tree import list_to_tree_node, null, treenode_to_list

class TestSolution(TestCase):
    def test_sufficientSubset(self):
        root = list_to_tree_node([1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14])
        self.assertListEqual([1,2,3,4,null,null,7,8,9,null,14], treenode_to_list(Solution().sufficientSubset(root, 1)))

    def test_sufficientSubset_1(self):
        root = list_to_tree_node([5,4,8,11,null,17,4,7,1,null,null,5,3])
        self.assertListEqual([5,4,8,11,null,17,4,7,null,null,null,5], treenode_to_list(Solution().sufficientSubset(root, 22)))

    def test_sufficientSubset_2(self):
        root = list_to_tree_node([1,2,-3,-5,null,4,null])
        self.assertListEqual([1,null,-3,4], treenode_to_list(Solution().sufficientSubset(root, -1)))

    def test_sufficientSubset_3(self):
        root = list_to_tree_node([10,5,10])
        self.assertListEqual([], treenode_to_list(Solution().sufficientSubset(root, 21)))
