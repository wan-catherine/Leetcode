from unittest import TestCase
from problems.N1026_Maximum_Difference_Between_Node_And_Ancestor import Solution
from problems.Utility_Tree import list_to_tree_node, null

class TestSolution(TestCase):
    def test_maxAncestorDiff(self):
        self.assertEqual(7, Solution().maxAncestorDiff(list_to_tree_node([8,3,10,1,6,null,14,null,null,4,7,13])))
