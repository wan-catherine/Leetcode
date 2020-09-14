from unittest import TestCase
from problems.N486_Predict_The_Winner import Solution

class TestSolution(TestCase):
    def test_PredictTheWinner(self):
        self.assertFalse(Solution().PredictTheWinner([1, 5, 2]))

    def test_PredictTheWinner_1(self):
        self.assertTrue(Solution().PredictTheWinner([1, 5, 233, 7]))

    def test_PredictTheWinner_2(self):
        self.assertTrue(Solution().PredictTheWinner([1, 1, 1]))

    def test_PredictTheWinner_3(self):
        self.assertTrue(Solution().PredictTheWinner([1,567,1,1]))

    def test_PredictTheWinner_4(self):
        self.assertTrue(Solution().PredictTheWinner([3,9,1,2]))

