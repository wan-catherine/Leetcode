from unittest import TestCase
from problems.N1326_Minimum_Number_Of_Taps_To_Open_To_Water_A_Garden import Solution

class TestSolution(TestCase):
    def test_min_taps(self):
        self.assertEqual(1, Solution().minTaps(n = 5, ranges = [3,4,1,1,0,0]))

    def test_min_taps_1(self):
        self.assertEqual(-1, Solution().minTaps(n = 3, ranges = [0,0,0,0]))

    def test_min_taps_2(self):
        self.assertEqual(3, Solution().minTaps(n = 7, ranges = [1,2,1,0,2,1,0,1]))

    def test_min_taps_3(self):
        self.assertEqual(2, Solution().minTaps(n = 8, ranges = [4,0,0,0,0,0,0,0,4]))

    def test_min_taps_4(self):
        self.assertEqual(1, Solution().minTaps(n = 8, ranges = [4,0,0,0,4,0,0,0,4]))

    def test_min_taps_5(self):
        self.assertEqual(2, Solution().minTaps(9, [0,5,0,3,3,3,1,4,0,4]))
