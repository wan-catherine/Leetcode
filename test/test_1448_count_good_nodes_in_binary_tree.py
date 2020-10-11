from unittest import TestCase
from problems.N1448_Count_Good_Nodes_In_Binary_Tree import Solution
from problems.Utility_Tree import list_to_tree_node, null

class TestSolution(TestCase):
    def test_goodNodes(self):
        self.assertEqual(4, Solution().goodNodes(list_to_tree_node([3,1,4,3,null,1,5])))

    def test_goodNodes_1(self):
        self.assertEqual(3, Solution().goodNodes(list_to_tree_node([3,3,null,4,2])))

    def test_goodNodes_2(self):
        self.assertEqual(1, Solution().goodNodes(list_to_tree_node([1])))
