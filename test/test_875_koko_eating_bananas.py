from unittest import TestCase
from problems.N875_Koko_Eating_Bananas import Solution

class TestSolution(TestCase):
    def test_minEatingSpeed(self):
        self.assertEqual(4, Solution().minEatingSpeed(piles = [3,6,7,11], H = 8))

    def test_minEatingSpeed_1(self):
        self.assertEqual(30, Solution().minEatingSpeed(piles = [30,11,23,4,20], H = 5))

    def test_minEatingSpeed_2(self):
        self.assertEqual(1, Solution().minEatingSpeed(piles = [30,11,23,4,20], H = 6))

    def test_minEatingSpeed_3(self):
        self.assertEqual(23, Solution().minEatingSpeed([312884470], 968709470))