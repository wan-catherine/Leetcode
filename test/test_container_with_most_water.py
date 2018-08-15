from unittest import TestCase
from problems.ContainerWithMostWater import Solution

class TestSolution(TestCase):
    def test_maxArea_with_sample(self):
        solution = Solution()
        res = solution.maxArea([1,8,6,2,5,4,8,3,7])
        self.assertEqual(49, res)

    def test_maxArea_with_sample_two(self):
        solution = Solution()
        res = solution.maxArea([1,1])
        self.assertEqual(1, res)

    def test_maxArea_with_sample_three(self):
        solution = Solution()
        res = solution.maxArea([1,1,1])
        self.assertEqual(2, res)

    def test_maxArea_with_sample_16(self):
        solution = Solution()
        res = solution.maxArea([2,3,4,5,18,17,6])
        self.assertEqual(17, res)