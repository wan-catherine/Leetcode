from unittest import TestCase
from problems.Utility_Tree import list_to_tree_node, null
from problems.N230_Kth_Smallest_Element_In_A_BST import Solution

class TestSolution(TestCase):
    def test_kthSmallest(self):
        self.assertEqual(1, Solution().kthSmallest(list_to_tree_node([3,1,4,null,2]), 1))

    def test_kthSmallest_1(self):
        self.assertEqual(3, Solution().kthSmallest(list_to_tree_node([5,3,6,2,4,null,null,1]), 3))

    def test_kthSmallest_2(self):
        self.assertEqual(2, Solution().kthSmallest(list_to_tree_node([1,null,2]), 2))

    def test_kthSmallest_3(self):
        self.assertEqual(3, Solution().kthSmallest(list_to_tree_node([3,1,4,null,2]), 3))

