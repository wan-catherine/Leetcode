from unittest import TestCase
from .The_Kth_Factor_Of_N import Solution

class TestSolution(TestCase):
    def test_kthFactor(self):
        self.assertEqual(3, Solution().kthFactor(12,3))

    def test_kthFactor_1(self):
        self.assertEqual(7, Solution().kthFactor(7,2))

    def test_kthFactor(self):
        self.assertEqual(3, Solution().kthFactor(12,3))

    def test_kthFactor_2(self):
        self.assertEqual(-1, Solution().kthFactor(4,4))

    def test_kthFactor_3(self):
        self.assertEqual(4, Solution().kthFactor(1000,3))
