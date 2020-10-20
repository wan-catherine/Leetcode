from unittest import TestCase
from problems.N754_Reach_A_Number import Solution

class TestSolution(TestCase):
    def test_reachNumber(self):
        self.assertEqual(2, Solution().reachNumber(3))

    def test_reachNumber_1(self):
        self.assertEqual(3, Solution().reachNumber(2))

    def test_reachNumber_2(self):
        self.assertEqual(2, Solution().reachNumber(-3))
