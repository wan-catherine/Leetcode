from unittest import TestCase
from problems.ReverseString import Solution

class TestSolution(TestCase):
    def test_reverseString(self):
        solution = Solution()
        res = solution.reverseString("hello")
        self.assertEqual(res, "olleh")
