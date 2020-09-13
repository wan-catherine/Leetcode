from unittest import TestCase
from problems.N464_Can_I_Win import Solution

class TestSolution(TestCase):
    def test_canIWin(self):
        self.assertFalse(Solution().canIWin(10, 11))

    def test_canIWin_1(self):
        self.assertTrue(Solution().canIWin(10, 0))

    def test_canIWin_2(self):
        self.assertTrue(Solution().canIWin(10, 1))

    def test_canIWin_3(self):
        self.assertTrue(Solution().canIWin(4, 6))

    def test_canIWin_4(self):
        self.assertFalse(Solution().canIWin(10, 40))