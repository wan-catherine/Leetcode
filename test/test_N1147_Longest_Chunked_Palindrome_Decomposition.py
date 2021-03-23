from unittest import TestCase
from problems.N1147_Longest_Chunked_Palindrome_Decomposition import Solution

class TestSolution(TestCase):
    def test_longest_decomposition(self):
        self.assertEqual(7, Solution().longestDecomposition("ghiabcdefhelloadamhelloabcdefghi"))

    def test_longest_decomposition_1(self):
        self.assertEqual(1, Solution().longestDecomposition("merchant"))

    def test_longest_decomposition_2(self):
        self.assertEqual(11, Solution().longestDecomposition("antaprezatepzapreanta"))

    def test_longest_decomposition_3(self):
        self.assertEqual(3, Solution().longestDecomposition("aaa"))

    def test_longest_decomposition_4(self):
        self.assertEqual(5, Solution().longestDecomposition("qjetgzetgqj"))
