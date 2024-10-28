from unittest import TestCase
from problems.N2501_Longest_Square_Streak_In_An_Array import Solution

class TestSolution(TestCase):
    def test_longest_square_streak(self):
        self.assertEquals(3, Solution().longestSquareStreak([4,3,6,16,8,2]))

    def test_longest_square_streak_1(self):
        self.assertEquals(-1, Solution().longestSquareStreak([2,3,5,6,7]))
