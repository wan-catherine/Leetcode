from unittest import TestCase
from problems.N998_Maximum_Binary_Tree_II import Solution
from problems.Utility_Tree import list_to_tree_node, null, treenode_to_list

class TestSolution(TestCase):
    def test_insertIntoMaxTree(self):
        root = list_to_tree_node([4,1,3,null,null,2])
        self.assertListEqual([5,4,null,1,3,null,null,2], treenode_to_list(Solution().insertIntoMaxTree(root, 5)))

    def test_insertIntoMaxTree_1(self):
        root = list_to_tree_node([5,2,4,null,1])
        self.assertListEqual([5,2,4,null,1,null,3], treenode_to_list(Solution().insertIntoMaxTree(root, 3)))

    def test_insertIntoMaxTree_2(self):
        root = list_to_tree_node([5,2,3,null,1])
        self.assertListEqual([5,2,4,null,1,3], treenode_to_list(Solution().insertIntoMaxTree(root, 4)))

