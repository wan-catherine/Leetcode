from unittest import TestCase
from problems.N2817_Minimum_Absolute_Difference_Between_Elements_With_Constraint import Solution

class TestSolution(TestCase):
    def test_min_absolute_difference(self):
        self.assertEquals(0, Solution().minAbsoluteDifference(nums = [4,3,2,4], x = 2))

    def test_min_absolute_difference_1(self):
        self.assertEquals(1, Solution().minAbsoluteDifference(nums = [5,3,2,10,15], x = 1))

    def test_min_absolute_difference_2(self):
        self.assertEquals(3, Solution().minAbsoluteDifference(nums = [1,2,3,4], x = 3))
