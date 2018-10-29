from unittest import TestCase
from problems.ConvertSortedArrayBinarySearchTree import TreeNode, Solution

class TestSolution(TestCase):
    def test_sortedArrayToBST(self):
        solution = Solution()
        res = solution.sortedArrayToBST([-10,-3,0,5,9])
        
