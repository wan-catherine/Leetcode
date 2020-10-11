from unittest import TestCase
from problems.N1325_Delete_Leaves_With_A_Given_Value import Solution
from problems.Utility_Tree import list_to_tree_node, treenode_to_list, null

class TestSolution(TestCase):
    def test_removeLeafNodes(self):
        root = list_to_tree_node([1,2,3,2,null,2,4])
        res = treenode_to_list(Solution().removeLeafNodes(root, 2))
        self.assertListEqual([1,null,3,null,4], res)

    def test_removeLeafNodes_1(self):
        root = list_to_tree_node([1,3,3,3,2])
        res = treenode_to_list(Solution().removeLeafNodes(root, 3))
        self.assertListEqual([1,3,null,null,2], res)

    def test_removeLeafNodes_2(self):
        root = list_to_tree_node([1,2,null,2,null,2])
        res = treenode_to_list(Solution().removeLeafNodes(root, 2))
        self.assertListEqual([1], res)

    def test_removeLeafNodes_3(self):
        root = list_to_tree_node([1,1,1])
        res = treenode_to_list(Solution().removeLeafNodes(root, 1))
        self.assertListEqual([], res)

    def test_removeLeafNodes_4(self):
        root = list_to_tree_node([1,2,3])
        res = treenode_to_list(Solution().removeLeafNodes(root, 1))
        self.assertListEqual([1,2,3], res)
