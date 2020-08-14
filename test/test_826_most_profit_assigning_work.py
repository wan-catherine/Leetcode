from unittest import TestCase
from problems.N826_Most_Profit_Assigning_Work import Solution

class TestSolution(TestCase):
    def test_maxProfitAssignment(self):
        self.assertEqual(100, Solution().maxProfitAssignment(difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]))

    def test_maxProfitAssignment_1(self):
        difficulty = [85, 47, 57]
        profit = [24, 66, 99]
        worker = [40, 25, 25]
        self.assertEqual(0, Solution().maxProfitAssignment(difficulty, profit, worker))

    def test_maxProfitAssignment_2(self):
        difficulty = [68, 35, 52, 47, 86]
        profit = [67, 17, 1, 81, 3]
        worker = [92, 10, 85, 84, 82]
        self.assertEqual(324, Solution().maxProfitAssignment(difficulty, profit, worker))

    def test_maxProfitAssignment_3(self):
        difficulty = [66, 1, 28, 73, 53, 35, 45, 60, 100, 44, 59, 94, 27, 88, 7, 18, 83, 18, 72, 63]
        profit = [66, 20, 84, 81, 56, 40, 37, 82, 53, 45, 43, 96, 67, 27, 12, 54, 98, 19, 47, 77]
        worker = [61, 33, 68, 38, 63, 45, 1, 10, 53, 23, 66, 70, 14, 51, 94, 18, 28, 78, 100, 16]
        self.assertEqual(1392, Solution().maxProfitAssignment(difficulty, profit, worker))
