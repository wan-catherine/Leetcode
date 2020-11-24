from unittest import TestCase
from problems.N862_Shortest_Subarray_With_Sum_At_Least_K import Solution

class TestSolution(TestCase):
    def test_shortestSubarray(self):
        self.assertEqual(1, Solution().shortestSubarray(A = [1], K = 1))

    def test_shortestSubarray_1(self):
        self.assertEqual(-1, Solution().shortestSubarray(A = [1,2], K = 4))

    def test_shortestSubarray_2(self):
        self.assertEqual(3, Solution().shortestSubarray(A = [2,-1,2], K = 3))

