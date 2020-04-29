from unittest import TestCase
from problems.Utility_Tree import TreeNode, list_to_tree_node, treenode_to_list, null
from problems.N124_Binary_Tree_Maximum_Path_Sum import Solution


class TestSolution(TestCase):
    def test_maxPathSum(self):
        input = [1,2,3]
        root = list_to_tree_node(input)
        soluton = Solution()
        res = soluton.maxPathSum(root)
        self.assertEqual(6, res)

    def test_maxPathSum_two(self):
        input = [-10,9,20,null,null,15,7]
        root = list_to_tree_node(input)
        soluton = Solution()
        res = soluton.maxPathSum(root)
        self.assertEqual(42, res)

    def test_maxPathSum_three(self):
        input = [-3]
        root = list_to_tree_node(input)
        soluton = Solution()
        res = soluton.maxPathSum(root)
        self.assertEqual(-3, res)

    def test_maxPathSum_four(self):
        input = [1,2]
        root = list_to_tree_node(input)
        soluton = Solution()
        res = soluton.maxPathSum(root)
        self.assertEqual(3, res)

    def test_maxPathSum_five(self):
        input = [1,-2, 3]
        root = list_to_tree_node(input)
        soluton = Solution()
        res = soluton.maxPathSum(root)
        self.assertEqual(4, res)

    def test_maxPathSum_six(self):
        input = [1,null,2,null,3,null,4,null,5]
        root = list_to_tree_node(input)
        soluton = Solution()
        res = soluton.maxPathSum(root)
        self.assertEqual(15, res)

    def test_maxPathSum_seven(self):
        input = [5,4,8,11,null,13,4,7,2,null,null,null,1]
        root = list_to_tree_node(input)
        soluton = Solution()
        res = soluton.maxPathSum(root)
        self.assertEqual(48, res)

