from unittest import TestCase
from problems.N1049_Last_Stone_Weight_II import Solution

class TestSolution(TestCase):
    def test_lastStoneWeightII(self):
        self.assertEqual(1, Solution().lastStoneWeightII([2,7,4,1,8,1]))

    def test_lastStoneWeightII_1(self):
        self.assertEqual(5, Solution().lastStoneWeightII([31,26,33,21,40]))
