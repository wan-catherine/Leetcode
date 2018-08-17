from unittest import TestCase
from problems.ThreeSumClosest import Solution

class TestSolution(TestCase):
    def test_threeSumClosest_one(self):
        solution = Solution()
        res = solution.threeSumClosest([-1, 2, 1, -4], 1)
        self.assertEqual(2, res)

    def test_threeSumClosest_81(self):
        solution = Solution()
        res = solution.threeSumClosest([1,6,9,14,16,70], 81)
        self.assertEqual(80, res)
