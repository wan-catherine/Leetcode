from unittest import TestCase
from problems.N1643_Kth_Smallest_Instructions import Solution

class TestSolution(TestCase):
    def test_kthSmallestPath(self):
        self.assertEqual("HHHVV", Solution().kthSmallestPath(destination = [2,3], k = 1))

    def test_kthSmallestPath_1(self):
        self.assertEqual("HHVHV", Solution().kthSmallestPath(destination = [2,3], k = 2))

    def test_kthSmallestPath_2(self):
        self.assertEqual("HHVVH", Solution().kthSmallestPath(destination = [2,3], k = 3))
