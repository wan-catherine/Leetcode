from unittest import TestCase
from problems.N2412_Minimum_Money_Required_Before_Transactions import Solution

class TestSolution(TestCase):
    def test_minimum_money(self):
        self.assertEqual(10, Solution().minimumMoney([[2,1],[5,0],[4,2]]))

    def test_minimum_money_1(self):
        self.assertEqual(3, Solution().minimumMoney([[3,0],[0,3]]))

    def test_minimum_money_2(self):
        self.assertEqual(18, Solution().minimumMoney([[7,2],[0,10],[5,0],[4,1],[5,8],[5,9]]))