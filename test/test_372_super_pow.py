from unittest import TestCase
from problems.N372_Super_Pow import Solution

class TestSolution(TestCase):
    def test_superPow(self):
        self.assertEqual(8, Solution().superPow(a = 2, b = [3]))

    def test_superPow_1(self):
        self.assertEqual(1024, Solution().superPow(a = 2, b = [1,0]))

    def test_superPow_2(self):
        self.assertEqual(1, Solution().superPow(a = 1, b = [4,3,3,8,5,2]))

    def test_superPow_3(self):
        self.assertEqual(1198, Solution().superPow(a = 2147483647, b = [2,0,0]))