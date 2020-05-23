from unittest import TestCase
from problems.N986_Interval_List_Intersections import Solution

class TestSolution(TestCase):
    def test_intervalIntersection(self):
        A = [[0, 2], [5, 10], [13, 23], [24, 25]]
        B = [[1, 5], [8, 12], [15, 24], [25, 26]]
        res = Solution().intervalIntersection(A, B)
        output = [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
        self.assertListEqual(output, res)

    def test_intervalIntersection_1(self):
        A = [[8,15]]
        B = [[2,6],[8,10],[12,20]]
        res = Solution().intervalIntersection(A, B)
        output = [[8,10],[12,15]]
        self.assertListEqual(output, res)

    def test_intervalIntersection_2(self):
        A = [[3,10]]
        B = [[5,10]]
        res = Solution().intervalIntersection(A, B)
        output = [[5,10]]
        self.assertListEqual(output, res)

    def test_intervalIntersection_3(self):
        A = [[17,20]]
        B = [[2,3],[6,8],[12,14],[19,20]]
        res = Solution().intervalIntersection(A, B)
        output = [[19,20]]
        self.assertListEqual(output, res)








