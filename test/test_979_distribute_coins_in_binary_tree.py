from unittest import TestCase
from problems.N979_Distribute_Coins_In_Binary_Tree import Solution
from problems.Utility_Tree import list_to_tree_node, null

class TestSolution(TestCase):
    def test_distributeCoins(self):
        self.assertEqual(2, Solution().distributeCoins(list_to_tree_node([3,0,0])))

    def test_distributeCoins_1(self):
        self.assertEqual(3, Solution().distributeCoins(list_to_tree_node([0,3,0])))

    def test_distributeCoins_2(self):
        self.assertEqual(2, Solution().distributeCoins(list_to_tree_node([1,0,2])))

    def test_distributeCoins_3(self):
        self.assertEqual(4, Solution().distributeCoins(list_to_tree_node([1,0,0,null,3])))

