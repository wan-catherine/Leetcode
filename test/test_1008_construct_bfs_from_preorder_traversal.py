from unittest import TestCase
from problems.Utility_Tree import treenode_to_list, null
from problems.N1008_Construct_BST_From_Preorder_Traversal import Solution

class TestSolution(TestCase):
    def test_bstFromPreorder(self):
        self.assertListEqual([8,5,10,1,7,null,12], treenode_to_list(Solution().bstFromPreorder([8,5,1,7,10,12])))

    def test_bstFromPreorder_1(self):
        self.assertListEqual([4,2], treenode_to_list(Solution().bstFromPreorder([4,2])))
