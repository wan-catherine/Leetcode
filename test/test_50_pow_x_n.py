from unittest import TestCase
from problems.N50_Pow_X_N import Solution

class TestSolution(TestCase):
    def test_myPow(self):
        self.assertEqual(1024.00000, Solution().myPow(2.00000, 10))

    def test_myPow_1(self):
        self.assertEqual(9.26100, Solution().myPow(2.1, 3))

    def test_myPow_2(self):
        self.assertEqual(0.25000, Solution().myPow(2.00000, -2))

