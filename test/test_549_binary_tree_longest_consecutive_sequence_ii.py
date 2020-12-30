from unittest import TestCase
from problems.N549_Binary_Tree_Longest_Consecutive_Sequence_II import Solution
from problems.Utility_Tree import TreeNode, list_to_tree_node, null

class TestSolution(TestCase):
    def test_longestConsecutive(self):
        self.assertEqual(3, Solution().longestConsecutive(list_to_tree_node([2,null,3,4,null,1])))

    def test_longestConsecutive_1(self):
        self.assertEqual(3, Solution().longestConsecutive(list_to_tree_node([2,1,3])))

    def test_longestConsecutive_2(self):
        self.assertEqual(3, Solution().longestConsecutive(list_to_tree_node([1,null,4,3,null,null,2])))
