from unittest import TestCase
from problems.N2065_Maximum_Path_Quality_Of_A_Graph import Solution

class TestSolution(TestCase):
    def test_maximal_path_quality(self):
        self.assertEqual(75, Solution().maximalPathQuality(values = [0,32,10,43], edges = [[0,1,10],[1,2,15],[0,3,10]], maxTime = 49))

    def test_maximal_path_quality_1(self):
        self.assertEqual(25, Solution().maximalPathQuality(values = [5,10,15,20], edges = [[0,1,10],[1,2,10],[0,3,10]], maxTime = 30))

    def test_maximal_path_quality_2(self):
        self.assertEqual(7, Solution().maximalPathQuality(values = [1,2,3,4], edges = [[0,1,10],[1,2,11],[2,3,12],[1,3,13]], maxTime = 50))

    def test_maximal_path_quality_3(self):
        self.assertEqual(0, Solution().maximalPathQuality(values = [0,1,2], edges = [[1,2,10]], maxTime = 10))