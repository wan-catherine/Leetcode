from unittest import TestCase
from problems.N128_Longest_Consecutive_Sequence import Solution

class TestSolution(TestCase):
    def test_longestConsecutive(self):
        self.assertEqual(4, Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))
