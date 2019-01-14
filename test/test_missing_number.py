from unittest import TestCase
from problems.MissingNumber import Solution

class TestSolution(TestCase):
    def test_missingNumber(self):
        solution = Solution()
        res = solution.missingNumber([3,0,1])
        self.assertEqual(res, 2)

    def test_missingNumber_one(self):
        solution = Solution()
        res = solution.missingNumber([9,6,4,2,3,5,7,0,1])
        self.assertEqual(res, 8)

    def test_missingNumber_two(self):
        solution = Solution()
        res = solution.missingNumber([0])
        self.assertEqual(res, 1)