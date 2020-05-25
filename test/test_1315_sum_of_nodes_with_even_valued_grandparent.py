from unittest import TestCase
from problems.Utility_Tree import list_to_tree_node, null
from problems.N1315_Sum_Of_Nodes_With_Even_Valued_Grandparent import Solution

class TestSolution(TestCase):
    def test_sumEvenGrandparent(self):
        root = list_to_tree_node([6,7,8,2,7,1,3,9,null,1,4,null,null,null,5])
        self.assertEqual(18, Solution().sumEvenGrandparent(root))
