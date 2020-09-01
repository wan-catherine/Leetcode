from unittest import TestCase
from problems.N513_Find_Bottom_Left_Tree_Value import Solution
from problems.Utility_Tree import list_to_tree_node, null

class TestSolution(TestCase):
    def test_findBottomLeftValue(self):
        root = list_to_tree_node([2,1,3])
        self.assertEqual(1, Solution().findBottomLeftValue(root))

    def test_findBottomLeftValue_1(self):
        root = list_to_tree_node([1,2,3,4,null,5,6,null,null,7])
        self.assertEqual(7, Solution().findBottomLeftValue(root))
