from unittest import TestCase
from problems.N518_Coin_Change_2 import Solution

class TestSolution(TestCase):
    def test_change(self):
        res = Solution().change(5, [1,2,5])
        self.assertEqual(4, res)

    def test_change_2(self):
        res = Solution().change(3, [2])
        self.assertEqual(0, res)

    def test_change_3(self):
        res = Solution().change(10, [10])
        self.assertEqual(1, res)

    def test_change_4(self):
        res = Solution().change(0, [])
        self.assertEqual(1, res)