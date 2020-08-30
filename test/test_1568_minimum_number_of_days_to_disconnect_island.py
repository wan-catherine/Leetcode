from unittest import TestCase
from problems.N1568_Minimum_Number_Of_Days_To_Disconnect_Island import Solution

class TestSolution(TestCase):
    def test_minDays(self):
        grid = [[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
        self.assertEqual(2, Solution().minDays(grid))

    def test_minDays_1(self):
        grid = [[1,1]]
        self.assertEqual(2, Solution().minDays(grid))

    def test_minDays_2(self):
        grid = [[1,0,1,0]]
        self.assertEqual(0, Solution().minDays(grid))

    def test_minDays_3(self):
        grid = [[1,1,0,1,1],
               [1,1,1,1,1],
               [1,1,0,1,1],
               [1,1,0,1,1]]
        self.assertEqual(1, Solution().minDays(grid))

    def test_minDays_4(self):
        grid = [[1,1,0,1,1],
               [1,1,1,1,1],
               [1,1,0,1,1],
               [1,1,1,1,1]]
        self.assertEqual(2, Solution().minDays(grid))
