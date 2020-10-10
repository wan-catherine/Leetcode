from unittest import TestCase
from problems.N1161_Maximum_Level_Sum_Of_A_Binary_Tree import Solution
from problems.Utility_Tree import list_to_tree_node, null

class TestSolution(TestCase):
    def test_maxLevelSum(self):
        self.assertEqual(2, Solution().maxLevelSum(list_to_tree_node([1,7,0,7,-8,null,null])))

    def test_maxLevelSum_1(self):
        self.assertEqual(2, Solution().maxLevelSum(list_to_tree_node([989,null,10250,98693,-89388,null,null,null,-32127])))