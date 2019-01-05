from unittest import TestCase
from problems.IntersectionTwoArrays import Solution

class TestSolution(TestCase):
    def test_intersection(self):
        solution = Solution()
        res = solution.intersection([1,2,2,1], [2,2])
        self.assertEqual([2], res)

    def test_intersection_two(self):
        solution = Solution()
        res = solution.intersection([4,9,5], [9,4,9,8,4])
        self.assertEqual([4, 9], res)
