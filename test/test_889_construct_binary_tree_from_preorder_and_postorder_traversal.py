from unittest import TestCase
from problems.N889_Construct_Binary_Tree_From_Preorder_And_Postorder_Traversal import Solution
from problems.Utility_Tree import treenode_to_list, null

class TestSolution(TestCase):
    def test_constructFromPrePost(self):
        self.assertListEqual([1,2,3,4,5,6,7], treenode_to_list(Solution().constructFromPrePost(pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1])))

    def test_constructFromPrePost_1(self):
        self.assertListEqual([2,1,null,3], treenode_to_list(Solution().constructFromPrePost([2,1,3], [3,1,2])))
