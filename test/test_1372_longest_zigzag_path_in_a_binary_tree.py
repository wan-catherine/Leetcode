from unittest import TestCase
from problems.N1372_Longest_Zigzag_Path_In_A_Binary_Tree import Solution
from problems.Utility_Tree import list_to_tree_node, null

class TestSolution(TestCase):
    def test_longestZigZag(self):
        self.assertEqual(3, Solution().longestZigZag(list_to_tree_node([1,null,1,1,1,null,null,1,1,null,1,null,null,null,1,null,1])))

    def test_longestZigZag_1(self):
        self.assertEqual(4, Solution().longestZigZag(list_to_tree_node([1,1,1,null,1,null,null,1,1,null,1])))

    def test_longestZigZag_2(self):
        self.assertEqual(0, Solution().longestZigZag(list_to_tree_node([1])))

    def test_longestZigZag_3(self):
        self.assertEqual(5, Solution().longestZigZag(list_to_tree_node([6,9,7,3,null,2,8,5,8,9,7,3,9,9,4,2,10,null,5,4,3,10,10,9,4,1,2,null,null,6,5,null,null,null,null,9,null,9,6,5,null,5,null,null,7,7,4,null,1,null,null,3,7,null,9,null,null,null,null,null,null,null,null,9,9,null,null,null,7,null,null,null,null,null,null,null,null,null,6,8,7,null,null,null,3,10,null,null,null,null,null,1,null,1,2])))
