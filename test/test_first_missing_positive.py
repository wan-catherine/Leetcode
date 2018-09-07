from unittest import TestCase
from problems.FirstMissingPositive import Solution

class TestSolution(TestCase):
    def test_firstMissingPositive(self):
        solution = Solution()
        res = solution.firstMissingPositive([3,4,-1,1])
        self.assertEqual(2, res)

    def test_firstMissingPositive_empty(self):
        solution = Solution()
        res = solution.firstMissingPositive([])
        self.assertEqual(1, res)

    def test_firstMissingPositive_one(self):
        solution = Solution()
        res = solution.firstMissingPositive([1])
        self.assertEqual(2, res)

    def test_firstMissingPositive_one_one(self):
        solution = Solution()
        res = solution.firstMissingPositive([1,1])
        self.assertEqual(2, res)

    def test_firstMissingPositive_one_one(self):
        solution = Solution()
        res = solution.firstMissingPositive([2,2])
        self.assertEqual(1, res)

    def test_firstMissingPositive_1(self):
        solution = Solution()
        res = solution.firstMissingPositive([7,8,9,11,12])
        self.assertEqual(1, res)
