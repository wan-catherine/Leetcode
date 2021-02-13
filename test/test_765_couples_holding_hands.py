from unittest import TestCase
from problems.N765_Couples_Holding_Hands import Solution

class TestSolution(TestCase):
    def test_minSwapsCouples(self):
        self.assertEqual(1, Solution().minSwapsCouples([0, 2, 1, 3]))

    def test_minSwapsCouples_1(self):
        self.assertEqual(0, Solution().minSwapsCouples([3, 2, 0, 1]))
