from unittest import TestCase
from problems.FindMinimumRotatedSortedArrayII import Solution

class TestSolution(TestCase):
    def test_findMin(self):
        solution = Solution()
        res = solution.findMin([1,3,5])
        self.assertEqual(1, res)

    def test_findMin_one(self):
        solution = Solution()
        res = solution.findMin([2,2,2,0,1])
        self.assertEqual(0, res)

    def test_findMin_two(self):
        solution = Solution()
        res = solution.findMin([2,2,2,2,2])
        self.assertEqual(2, res)

    def test_findMin_three(self):
        solution = Solution()
        res = solution.findMin([1])
        self.assertEqual(1, res)

    def test_findMin_four(self):
        solution = Solution()
        res = solution.findMin([3,3,3,3,3,3,3,3,1,3])
        self.assertEqual(1, res)

    def test_findMin_1(self):
        solution = Solution()
        res = solution.findMin([1, 3, 3])
        self.assertEqual(1, res)
