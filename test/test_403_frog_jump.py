from unittest import TestCase
from problems.N403_Frog_Jump import Solution

class TestSolution(TestCase):
    def test_canCross(self):
        self.assertTrue(Solution().canCross([0,1,3,5,6,8,12,17]))

    def test_canCross_1(self):
        self.assertFalse(Solution().canCross([0,1,2,3,4,8,9,11]))

    def test_canCross_2(self):
        self.assertFalse(Solution().canCross([0,2]))
