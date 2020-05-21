from unittest import TestCase
from problems.Utility_Tree import list_to_tree_node,null
from problems.N437_Path_Sum_III import Solution

class TestSolution(TestCase):
    def test_pathSum(self):
        self.assertEqual(3, Solution().pathSum(list_to_tree_node([10,5,-3,3,2,null,11,3,-2,null,1]), 8))

    def test_pathSum_1(self):
        self.assertEqual(2, Solution().pathSum(list_to_tree_node([1,null,2,null,3,null,4,null,5]), 3))
