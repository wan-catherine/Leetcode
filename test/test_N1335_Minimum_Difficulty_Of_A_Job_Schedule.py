from unittest import TestCase
from problems.N1335_Minimum_Difficulty_Of_A_Job_Schedule import Solution

class TestSolution(TestCase):
    def test_min_difficulty(self):
        self.assertEqual(7, Solution().minDifficulty(jobDifficulty = [6,5,4,3,2,1], d = 2))

    def test_min_difficulty_1(self):
        self.assertEqual(-1, Solution().minDifficulty(jobDifficulty = [9,9,9], d = 4))

    def test_min_difficulty_2(self):
        self.assertEqual(3, Solution().minDifficulty(jobDifficulty = [1,1,1], d = 3))

    def test_min_difficulty_3(self):
        self.assertEqual(15, Solution().minDifficulty(jobDifficulty = [7,1,7,1,7,1], d = 3))

    def test_min_difficulty_4(self):
        self.assertEqual(843, Solution().minDifficulty(jobDifficulty = [11,111,22,222,33,333,44,444], d = 6))
