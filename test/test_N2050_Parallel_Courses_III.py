from unittest import TestCase
from problems.N2050_Parallel_Courses_III import Solution

class TestSolution(TestCase):
    def test_minimum_time(self):
        self.assertEqual(8, Solution().minimumTime(n = 3, relations = [[1,3],[2,3]], time = [3,2,5]))

    def test_minimum_time_1(self):
        self.assertEqual(12, Solution().minimumTime(n = 5, relations = [[1,5],[2,5],[3,5],[3,4],[4,5]], time = [1,2,3,4,5]))

    def test_minimum_time_2(self):
        self.assertEqual(32, Solution().minimumTime(9,
[[2,7],[2,6],[3,6],[4,6],[7,6],[2,1],[3,1],[4,1],[6,1],[7,1],[3,8],[5,8],[7,8],[1,9],[2,9],[6,9],[7,9]], [9,5,9,5,8,7,7,8,4]))
