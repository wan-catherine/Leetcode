from unittest import TestCase
from problems.N973_K_Closest_Points_To_Origin import Solution

class TestSolution(TestCase):
    def test_kClosest(self):
        self.assertEqual([[-2,2]], Solution().kClosest([[1,3],[-2,2]], 1))

    def test_kClosest_1(self):
        self.assertEqual([[3,3],[-2,4]], Solution().kClosest([[3,3],[5,-1],[-2,4]], 2))
