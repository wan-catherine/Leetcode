from unittest import TestCase
from problems.N652_Find_Duplicate_Subtrees import Solution
from problems.Utility_Tree import list_to_tree_node,treenode_to_list,null

class TestSolution(TestCase):
    def test_findDuplicateSubtrees_1(self):
        root = list_to_tree_node([2,1,1])
        self.assertListEqual([1], treenode_to_list(Solution().findDuplicateSubtrees(root)[0]))

