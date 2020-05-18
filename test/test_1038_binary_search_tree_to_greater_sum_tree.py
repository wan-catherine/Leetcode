from unittest import TestCase
from problems.Utility_Tree import TreeNode, list_to_tree_node, treenode_to_list, null, treeNodeToString
from problems.N1038_Binary_Search_Tree_To_Greater_Sum_Tree import Solution

class TestSolution(TestCase):
    def test_bstToGst(self):
        input = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
        output = [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
        res = Solution().bstToGst(list_to_tree_node(input))
        self.assertListEqual(output, treenode_to_list(res))

    def test_bstToGst_1(self):
        input = [5,2,13]
        output = [18,20,13]
        self.assertListEqual(output, treenode_to_list(Solution().bstToGst(list_to_tree_node(input))))
