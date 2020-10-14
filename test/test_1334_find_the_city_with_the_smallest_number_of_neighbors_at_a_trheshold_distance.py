from unittest import TestCase
from problems.N1334_Find_The_City_With_The_Smallest_Number_Of_Neighbors_At_A_Threshold_Distance import Solution

class TestSolution(TestCase):
    def test_findTheCity(self):
        self.assertEqual(3, Solution().findTheCity(n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4))

    def test_findTheCity_1(self):
        self.assertEqual(0, Solution().findTheCity(n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2))

    def test_findTheCity_2(self):
        self.assertEqual(7, Solution().findTheCity(8,
[[3,5,9558],[1,2,1079],[1,3,8040],[0,1,9258],[4,7,7558],[5,6,8196],[3,4,7284],[1,5,6327],[0,4,5966],[3,6,8575],[2,5,8604],[1,7,7782],[4,6,2857],[3,7,2336],[0,6,6],[5,7,2870],[4,5,5055],[0,7,2904],[1,6,2458],[0,5,3399],[6,7,2202],[0,2,3996],[0,3,7495],[1,4,2262],[2,6,1390]], 7937))

    def test_findTheCity_3(self):
        self.assertEqual(5, Solution().findTheCity(6, [[0,1,10],[0,2,1],[2,3,1],[1,3,1],[1,4,1],[4,5,10]], 20))

    def test_findTheCity_4(self):
        self.assertEqual(3, Solution().findTheCity(4, [[0,1,3977],[2,3,8807],[0,2,2142],[1,3,1201]], 8174))