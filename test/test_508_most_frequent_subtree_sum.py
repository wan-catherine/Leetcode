from unittest import TestCase
from problems.N508_Most_Frequent_Subtree_Sum import Solution
from problems.Utility_Tree import list_to_tree_node, null

class TestSolution(TestCase):
    def test_findFrequentTreeSum(self):
        self.assertListEqual([2, -3, 4], Solution().findFrequentTreeSum(list_to_tree_node([5,2,-3])))

    def test_findFrequentTreeSum_1(self):
        self.assertListEqual([], Solution().findFrequentTreeSum(list_to_tree_node([])))

    def test_findFrequentTreeSum_2(self):
        self.assertListEqual([1,2], Solution().findFrequentTreeSum(list_to_tree_node([1,1])))

    def test_findFrequentTreeSum_3(self):
        self.assertListEqual([15,20,1], Solution().findFrequentTreeSum(list_to_tree_node([5,14,null,1])))
