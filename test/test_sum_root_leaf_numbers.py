from unittest import TestCase
from problems.SumRootLeafNumbers import TreeNode, Solution

class TestSolution(TestCase):
    def test_sumNumbers(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        solution = Solution()
        res = solution.sumNumbers(root)
        self.assertEqual(25, res)

    def test_sumNumbers_one(self):
        root = TreeNode(4)
        root.left = TreeNode(9)
        root.right = TreeNode(0)
        root.left.left = TreeNode(5)
        root.left.right = TreeNode(1)
        solution = Solution()
        res = solution.sumNumbers(root)
        self.assertEqual(1026, res)

    def test_sumNumbers_two(self):
        root = TreeNode(1)
        root.left = TreeNode(0)
        solution = Solution()
        res = solution.sumNumbers(root)
        self.assertEqual(10, res)