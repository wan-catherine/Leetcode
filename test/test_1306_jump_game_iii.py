from unittest import TestCase
from problems.N1306_Jump_Game_III import Solution

class TestSolution(TestCase):
    def test_canReach(self):
        self.assertTrue(Solution().canReach(arr = [4,2,3,0,3,1,2], start = 5))

    def test_canReach_1(self):
        self.assertTrue(Solution().canReach(arr = [4,2,3,0,3,1,2], start = 0))

    def test_canReach_2(self):
        self.assertFalse(Solution().canReach(arr = [3,0,2,1,2], start = 2))
