from unittest import TestCase
from problems.FindPeakElement import Solution

class TestSolution(TestCase):
    def test_findPeakElement(self):
        solution = Solution()
        res = solution.findPeakElement([1,2,3,1])
        self.assertEqual(2, res)

    def test_findPeakElement_one(self):
        solution = Solution()
        res = solution.findPeakElement( [1,2,1,3,5,6,4])
        self.assertEqual(1, res)

    def test_findPeakElement_two(self):
        solution = Solution()
        res = solution.findPeakElement([1,2])
        self.assertEqual(1, res)

