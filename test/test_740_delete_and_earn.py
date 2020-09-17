from unittest import TestCase
from problems.N740_Delete_And_Earn import Solution

class TestSolution(TestCase):
    def test_deleteAndEarn(self):
        self.assertEqual(6, Solution().deleteAndEarn([3, 4, 2]))

    def test_deleteAndEarn_1(self):
        self.assertEqual(9, Solution().deleteAndEarn([2, 2, 3, 3, 3, 4]))

    def test_deleteAndEarn_2(self):
        self.assertEqual(4, Solution().deleteAndEarn([3,1]))