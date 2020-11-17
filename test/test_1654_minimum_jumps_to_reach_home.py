from unittest import TestCase
from problems.N1654_Minimum_Jumps_To_Reach_Home import Solution

class TestSolution(TestCase):
    def test_minimumJumps(self):
        self.assertEqual(3, Solution().minimumJumps(forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9))

    def test_minimumJumps_1(self):
        self.assertEqual(-1, Solution().minimumJumps(forbidden = [8,3,16,6,12,20], a = 15, b = 13, x = 11))

    def test_minimumJumps_2(self):
        self.assertEqual(2, Solution().minimumJumps(forbidden = [1,6,2,14,5,17,4], a = 16, b = 9, x = 7))

    def test_minimumJumps_3(self):
        self.assertEqual(121, Solution().minimumJumps([162,118,178,152,167,100,40,74,199,186,26,73,200,127,30,124,193,84,184,36,103,149,153,9,54,154,133,95,45,198,79,157,64,122,59,71,48,177,82,35,14,176,16,108,111,6,168,31,134,164,136,72,98], 29, 98, 80))

