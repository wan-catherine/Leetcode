from unittest import TestCase
from problems.FindMinimumRotatedSortedArray import Solution

class TestSolution(TestCase):
    def test_findMin(self):
        solution = Solution()
        res = solution.findMin([3,4,5,1,2])
        self.assertEqual(1, res)

    def test_findMin_one(self):
        solution = Solution()
        res = solution.findMin([4,5,6,7,0,1,2])
        self.assertEqual(0, res)