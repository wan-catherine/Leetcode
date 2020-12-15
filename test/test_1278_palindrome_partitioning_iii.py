from unittest import TestCase
from problems.N1278_Palindrome_Partitioning_III import Solution

class TestSolution(TestCase):
    def test_palindromePartition(self):
        self.assertEqual(1, Solution().palindromePartition(s = "abc", k = 2))

    def test_palindromePartition_1(self):
        self.assertEqual(0, Solution().palindromePartition(s = "aabbc", k = 3))

    def test_palindromePartition_2(self):
        self.assertEqual(0, Solution().palindromePartition(s = "leetcode", k = 8))

