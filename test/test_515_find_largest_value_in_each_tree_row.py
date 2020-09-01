from unittest import TestCase
from problems.N515_Find_Largest_Value_In_Each_Tree_Row import Solution
from problems.Utility_Tree import list_to_tree_node, null

class TestSolution(TestCase):
    def test_largestValues(self):
        root = list_to_tree_node([1,3,2,5,3,null,9])
        self.assertListEqual([1,3,9], Solution().largestValues(root))

    def test_largestValues_1(self):
        root = list_to_tree_node([1,2,3])
        self.assertListEqual([1,3], Solution().largestValues(root))

    def test_largestValues_2(self):
        root = list_to_tree_node([1])
        self.assertListEqual([1], Solution().largestValues(root))

    def test_largestValues_3(self):
        root = list_to_tree_node([1,null,2])
        self.assertListEqual([1,2], Solution().largestValues(root))

    def test_largestValues_4(self):
        root = list_to_tree_node([])
        self.assertListEqual([], Solution().largestValues(root))
