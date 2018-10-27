from unittest import TestCase
from problems.PathSumII import TreeNode, Solution

class TestSolution(TestCase):
    def test_pathSum(self):
        solution = Solution()
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.right = TreeNode(8)
        root.left.left = TreeNode(11)
        root.left.left.left = TreeNode(7)
        root.left.left.right = TreeNode(2)
        root.right.left = TreeNode(13)
        root.right.right = TreeNode(4)
        root.right.right.right = TreeNode(1)
        root.right.right.left=TreeNode(5)
        res = solution.pathSum(root, 22)
        expected =[
   [5,4,11,2],
   [5,8,4,5]
]
        self.assertEqual(expected, res)

