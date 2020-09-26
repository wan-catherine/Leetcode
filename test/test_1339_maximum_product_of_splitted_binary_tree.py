from unittest import TestCase
from problems.N1339_Maximum_Product_Of_Splitted_Binary_Tree import Solution
from problems.Utility_Tree import list_to_tree_node, null

class TestSolution(TestCase):
    def test_maxProduct(self):
        self.assertEqual(110, Solution().maxProduct(list_to_tree_node([1,2,3,4,5,6])))

    def test_maxProduct_1(self):
        self.assertEqual(90, Solution().maxProduct(list_to_tree_node([1,null,2,3,4,null,null,5,6])))

    def test_maxProduct_2(self):
        self.assertEqual(1025, Solution().maxProduct(list_to_tree_node([2,3,9,10,7,8,6,5,4,11,1])))

    def test_maxProduct_3(self):
        self.assertEqual(1, Solution().maxProduct(list_to_tree_node([1,1])))
