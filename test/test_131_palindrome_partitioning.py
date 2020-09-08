from unittest import TestCase
from problems.N131_Palindrome_Partitioning import Solution

class TestSolution(TestCase):
    def test_partition(self):
        output = [
  ["aa","b"],
  ["a","a","b"]
]
        self.assertListEqual(output, Solution().partition("aab"))
