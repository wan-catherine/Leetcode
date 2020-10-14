from unittest import TestCase
from problems.N1361_Validate_Binary_Tree_Nodes import Solution

class TestSolution(TestCase):
    def test_validateBinaryTreeNodes(self):
        self.assertTrue(Solution().validateBinaryTreeNodes(n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]))

    def test_validateBinaryTreeNodes_1(self):
        self.assertFalse(Solution().validateBinaryTreeNodes(n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]))

    def test_validateBinaryTreeNodes_2(self):
        self.assertFalse(Solution().validateBinaryTreeNodes(n = 2, leftChild = [1,0], rightChild = [-1,-1]))

    def test_validateBinaryTreeNodes_3(self):
        self.assertFalse(Solution().validateBinaryTreeNodes(n = 6, leftChild = [1,-1,-1,4,-1,-1], rightChild = [2,-1,-1,5,-1,-1]))

    def test_validateBinaryTreeNodes_4(self):
        self.assertFalse(Solution().validateBinaryTreeNodes(4, [1,0,3,-1], [-1,-1,-1,-1]))

    def test_validateBinaryTreeNodes_5(self):
        self.assertFalse(Solution().validateBinaryTreeNodes(4, [1,2,0,-1], [-1,-1,-1,-1]))

