from unittest import TestCase
from problems.N776_Split_BST import Solution
from problems.Utility_Tree import list_to_tree_node, treenode_to_list, null

class TestSolution(TestCase):
    def test_splitBST(self):
        root = list_to_tree_node([4,2,6,1,3,5,7])
        res = Solution().splitBST(root, 2)
        ans = [[2,1],[4,3,6,null,null,5,7]]
        for node in res:
            li = treenode_to_list(node)
            self.assertTrue(li in ans)

    def test_splitBST_1(self):
        root = list_to_tree_node([10, 5, 20, 3, 9, 15, 25, null, null, 8, null, null, null, null, null, 6, null, null, 7])
        res = Solution().splitBST(root, 6)
        ans = [[5,3,6],[10,9,20,8,null,15,25,7]]
        for node in res:
            li = treenode_to_list(node)
            self.assertTrue(li in ans)
