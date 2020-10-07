from unittest import TestCase
from problems.N654_Maximum_Binary_Tree import Solution
from problems.Utility_Tree import treenode_to_list,null

class TestSolution(TestCase):
    def test_constructMaximumBinaryTree(self):
        res = Solution().constructMaximumBinaryTree([3,2,1,6,0,5])
        self.assertListEqual([6,3,5,null,2,0,null,null,1], treenode_to_list(res))
