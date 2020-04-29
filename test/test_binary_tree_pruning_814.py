from unittest import TestCase
from problems.Utility_Tree import TreeNode,stringToTreeNode,treeNodeToString, treenode_to_list
from problems.BinaryTreePruning_814 import Solution

class TestSolution(TestCase):
    def test_pruneTree(self):
        input = "[1,null, 0, 0, 1]"
        root = stringToTreeNode(input)
        solution = Solution().pruneTree(root)
        self.assertEqual([1, None, 0, None, 1], treenode_to_list(solution))

    def test_pruneTree_two(self):
        input = "[1,0,1,0,0,0,1]"
        root = stringToTreeNode(input)
        solution = Solution().pruneTree(root)
        self.assertEqual([1,None,1,None,1], treenode_to_list(solution))
