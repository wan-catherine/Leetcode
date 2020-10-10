from unittest import TestCase
from problems.N1302_Deepest_Leaves_Sum import Solution
from problems.Utility_Tree import list_to_tree_node, null

class TestSolution(TestCase):
    def test_deepestLeavesSum(self):
        self.assertEqual(15, Solution().deepestLeavesSum(list_to_tree_node([1,2,3,4,5,null,6,7,null,null,null,null,8])))