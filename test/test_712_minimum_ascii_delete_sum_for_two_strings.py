from unittest import TestCase
from problems.N712_Minimum_ASCII_Delete_Sum_For_Two_Strings import Solution

class TestSolution(TestCase):
    def test_minimumDeleteSum(self):
        self.assertEqual(231, Solution().minimumDeleteSum(s1 = "sea", s2 = "eat"))

    def test_minimumDeleteSum_1(self):
        self.assertEqual(403, Solution().minimumDeleteSum(s2 = "delete", s1 = "leet"))