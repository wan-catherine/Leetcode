from unittest import TestCase
from problems.MinimumWindowSubstring import Solution

class TestSolution(TestCase):
    def test_minWindow(self):
        solution = Solution()
        res = solution.minWindow("ADOBECODEBANC", "ABC")
        self.assertEqual(res, "BANC")
