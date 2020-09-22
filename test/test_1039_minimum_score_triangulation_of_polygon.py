from unittest import TestCase
from problems.N1039_Minimum_Score_Triangulation_Of_Polygon import Solution

class TestSolution(TestCase):
    def test_minScoreTriangulation(self):
        self.assertEqual(6, Solution().minScoreTriangulation([1,2,3]))

    def test_minScoreTriangulation_1(self):
        self.assertEqual(144, Solution().minScoreTriangulation([3,7,4,5]))

    def test_minScoreTriangulation_2(self):
        self.assertEqual(13, Solution().minScoreTriangulation([1,3,1,4,1,5]))