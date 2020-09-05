from unittest import TestCase
from problems.N1305_All_Elements_In_Two_Binary_Search_Trees import Solution
from problems.Utility_Tree import null, list_to_tree_node

class TestSolution(TestCase):
    def test_getAllElements(self):
        self.assertListEqual([0,1,1,2,3,4], Solution().getAllElements(list_to_tree_node([2,1,4]), list_to_tree_node([1,0,3])))

    def test_getAllElements_1(self):
        self.assertListEqual([-10,0,0,1,2,5,7,10], Solution().getAllElements(list_to_tree_node([0,-10,10]), list_to_tree_node([5,1,7,0,2])))

    def test_getAllElements_2(self):
        self.assertListEqual([0,1,2,5,7], Solution().getAllElements(list_to_tree_node([]), list_to_tree_node([5,1,7,0,2])))

    def test_getAllElements_3(self):
        self.assertListEqual([-10,0,10], Solution().getAllElements(list_to_tree_node([0,-10,10]), list_to_tree_node([])))

    def test_getAllElements_4(self):
        self.assertListEqual([1,1,8,8], Solution().getAllElements(list_to_tree_node([1,null,8]), list_to_tree_node([8,1])))
