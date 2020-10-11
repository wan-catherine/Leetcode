from unittest import TestCase
from problems.N1530_Number_Of_Good_Leaf_Nodes_Pairs import Solution
from problems.Utility_Tree import list_to_tree_node, null

class TestSolution(TestCase):
    def test_countPairs(self):
        self.assertEqual(1, Solution().countPairs(list_to_tree_node([1,2,3,null,4]), 3))

    def test_countPairs_1(self):
        self.assertEqual(2, Solution().countPairs(list_to_tree_node([1,2,3,4,5,6,7]), 3))

    def test_countPairs_2(self):
        self.assertEqual(1, Solution().countPairs(list_to_tree_node([7,1,4,6,null,5,3,null,null,null,null,null,2]), 3))

    def test_countPairs_3(self):
        self.assertEqual(0, Solution().countPairs(list_to_tree_node([100]), 1))

    def test_countPairs_4(self):
        self.assertEqual(1, Solution().countPairs(list_to_tree_node([1,1,1]), 2))

