from unittest import TestCase
from problems.N948_Bag_Of_Tokens import Solution

class TestSolution(TestCase):
    def test_bagOfTokensScore(self):
        self.assertEqual(0, Solution().bagOfTokensScore(tokens = [100], P = 50))

    def test_bagOfTokensScore_1(self):
        self.assertEqual(1, Solution().bagOfTokensScore(tokens = [100,200], P = 150))

    def test_bagOfTokensScore_2(self):
        self.assertEqual(2, Solution().bagOfTokensScore(tokens = [100,200,300,400], P = 200))
