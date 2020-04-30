from unittest import TestCase
from problems.N322_Coin_Change import Solution

class TestSolution(TestCase):
    def test_coinChange(self):
        res = Solution().coin_change([1,2,5], 11)
        self.assertEqual(3, res)

    def test_coinChange_2(self):
        res = Solution().coin_change([2], 3)
        self.assertEqual(-1, res)

    def test_coinChange_3(self):
        res = Solution().coin_change([1], 0)
        self.assertEqual(0, res)

    def test_coinChange_4(self):
        res = Solution().coin_change([186,419,83,408], 6249)
        self.assertEqual(20, res)
