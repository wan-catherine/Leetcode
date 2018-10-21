from unittest import TestCase
from problems.UniqueBinarySearchTreesII import TreeNode,Solution

class TestSolution(TestCase):
    def test_generateTrees(self):
        solution = Solution()
        res = solution.generateTrees(2)
        root1 = TreeNode(2)
        root1.left = TreeNode(1)
        root2 = TreeNode(1)
        root2.right = TreeNode(2)
        expected = [root1, root2]
