from unittest import TestCase
from problems.BurstBalloons import Solution

class TestSolution(TestCase):
    def test_maxCoins(self):
        solution = Solution()
        res = solution.maxCoins([3,1,5,8])
        self.assertEqual(167, res)
