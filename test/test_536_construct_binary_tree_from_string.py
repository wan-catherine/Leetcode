from unittest import TestCase
from problems.N536_Construct_Binary_Tree_From_String import Solution
from problems.Utility_Tree import TreeNode, treenode_to_list

class TestSolution(TestCase):
    def test_str2tree(self):
        res = Solution().str2tree("4(2(3)(1))(6(5))")
        self.assertListEqual([4,2,6,3,1,5], treenode_to_list(res))

    def test_str2tree_1(self):
        res = Solution().str2tree("4(2(3)(1))(6(5)(7))")
        self.assertListEqual([4,2,6,3,1,5,7], treenode_to_list(res))

    def test_str2tree_2(self):
        res = Solution().str2tree("-4(2(3)(1))(6(5)(7))")
        self.assertListEqual([-4,2,6,3,1,5,7], treenode_to_list(res))
