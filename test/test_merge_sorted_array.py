from unittest import TestCase
from problems.MergeSortedArray import Solution

class TestSolution(TestCase):
    def test_merge(self):
        solution = Solution()
        res = solution.merge([1,2,3,0,0,0], 3, [2,5,6], 3)
        self.assertEqual([1,2,2,3,5,6], res)
