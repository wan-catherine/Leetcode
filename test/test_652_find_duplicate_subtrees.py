from unittest import TestCase
from problems.N652_Find_Duplicate_Subtrees import Solution
from problems.Utility_Tree import list_to_tree_node,treenode_to_list,null

class TestSolution(TestCase):
    def test_findDuplicateSubtrees_1(self):
        root = list_to_tree_node([2,1,1])
        self.assertListEqual([1], treenode_to_list(Solution().findDuplicateSubtrees(root)[0]))

    def test_findDuplicateSubtrees_2(self):
        root = list_to_tree_node([1,2,3,4,null,2,4,null,null,4])
        self.assertListEqual([2,4], treenode_to_list(Solution().findDuplicateSubtrees(root)[1]))
        self.assertListEqual([4], treenode_to_list(Solution().findDuplicateSubtrees(root)[0]))

