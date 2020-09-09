from unittest import TestCase
from problems.N1219_Path_With_Maximum_Gold import Solution

class TestSolution(TestCase):
    def test_getMaximumGold(self):
        self.assertEqual(24, Solution().getMaximumGold([[0,6,0],[5,8,7],[0,9,0]]))

    def test_getMaximumGold_1(self):
        self.assertEqual(28, Solution().getMaximumGold([[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]))