from unittest import TestCase
from problems.N1423_Maximum_Points_You_Can_Obtain_From_Cards import Solution

class TestSolution(TestCase):
    def test_maxScore(self):
        cardPoints = [1, 2, 3, 4, 5, 6, 1]
        k = 3
        self.assertEqual(12, Solution().maxScore(cardPoints, k))

    def test_maxScore_1(self):
        cardPoints = [2,2,2]
        k = 2
        self.assertEqual(4, Solution().maxScore(cardPoints, k))

    def test_maxScore_2(self):
        cardPoints = [9,7,7,9,7,7,9]
        k = 7
        self.assertEqual(55, Solution().maxScore(cardPoints, k))

    def test_maxScore_3(self):
        cardPoints = [1,1000,1]
        k = 1
        self.assertEqual(1, Solution().maxScore(cardPoints, k))

    def test_maxScore_4(self):
        cardPoints = [1,79,80,1,1,1,200,1]
        k = 3
        self.assertEqual(202, Solution().maxScore(cardPoints, k))

    def test_maxScore_5(self):
        cardPoints = [100,40,17,9,73,75]
        k = 3
        self.assertEqual(248, Solution().maxScore(cardPoints, k))

    def test_maxScore_6(self):
        cardPoints = [96,90,41,82,39,74,64,50,30]
        k = 8
        self.assertEqual(536, Solution().maxScore(cardPoints, k))
