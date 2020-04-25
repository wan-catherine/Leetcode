from unittest import TestCase
from problems.KthSmallestElementSortedMatrix import Solution

class TestSolution(TestCase):
    def test_kthSmallest(self):
        matrix = [
                     [1, 5, 9],
                     [10, 11, 13],
                     [12, 13, 15]
                 ]
        k = 8
        solution = Solution()
        res = solution.kthSmallest(matrix, k)
        self.assertEqual(res, 13)
